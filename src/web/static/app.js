(() => {
  const form = document.getElementById("previewForm");
  const fileInput = document.getElementById("imageFile");
  const nColorsInput = document.getElementById("nColors");
  const blendDepthInput = document.getElementById("blendDepth");
  const statusEl = document.getElementById("status");
  const previewImage = document.getElementById("previewImage");
  const submitButton = form.querySelector("button[type=\"submit\"]");

  let currentPreviewUrl = null;
  let debounceTimer = null;
  let activeController = null;
  let activeRequestId = 0;

  const setStatus = (message, isError = false) => {
    statusEl.textContent = message;
    statusEl.classList.toggle("error", isError);
  };

  const clearPreview = () => {
    if (currentPreviewUrl) {
      URL.revokeObjectURL(currentPreviewUrl);
      currentPreviewUrl = null;
    }
    previewImage.style.display = "none";
    previewImage.removeAttribute("src");
  };

  const setBusy = (isBusy) => {
    submitButton.disabled = isBusy;
  };

  const cancelActiveRequest = () => {
    if (activeController) {
      activeController.abort();
      activeController = null;
    }
  };

  const buildFormData = () => {
    const file = fileInput.files[0];
    if (!file) {
      return null;
    }
    const formData = new FormData();
    formData.append("file", file);
    if (nColorsInput.value) {
      formData.append("n_colors", nColorsInput.value);
    }
    if (blendDepthInput.value) {
      formData.append("blend_depth", blendDepthInput.value);
    }
    return formData;
  };

  const runPreview = async (showMissingFileError) => {
    const formData = buildFormData();
    if (!formData) {
      if (showMissingFileError) {
        clearPreview();
        setStatus("Select an image file to continue.", true);
      }
      return;
    }

    cancelActiveRequest();
    const controller = new AbortController();
    activeController = controller;
    const requestId = activeRequestId + 1;
    activeRequestId = requestId;
    setBusy(true);
    setStatus("Rendering...");
    try {
      const response = await fetch("/preview", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      });

      if (requestId !== activeRequestId) {
        return;
      }
      if (!response.ok) {
        const errorText = await response.text();
        setStatus(`Error: ${errorText}`, true);
        return;
      }

      const blob = await response.blob();
      if (requestId !== activeRequestId) {
        return;
      }
      if (currentPreviewUrl) {
        URL.revokeObjectURL(currentPreviewUrl);
      }
      currentPreviewUrl = URL.createObjectURL(blob);
      previewImage.src = currentPreviewUrl;
      previewImage.style.display = "block";
      setStatus("Preview ready.");
    } catch (error) {
      if (error.name === "AbortError") {
        return;
      }
      setStatus("Network error while calling /preview.", true);
    } finally {
      if (requestId === activeRequestId) {
        setBusy(false);
        activeController = null;
      }
    }
  };

  const scheduleLivePreview = () => {
    cancelActiveRequest();
    if (debounceTimer) {
      window.clearTimeout(debounceTimer);
    }
    debounceTimer = window.setTimeout(() => {
      debounceTimer = null;
      runPreview(false);
    }, 500);
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (debounceTimer) {
      window.clearTimeout(debounceTimer);
      debounceTimer = null;
    }
    await runPreview(true);
  });

  nColorsInput.addEventListener("input", scheduleLivePreview);
  blendDepthInput.addEventListener("input", scheduleLivePreview);
})();
