(() => {
  const form = document.getElementById("previewForm");
  const fileInput = document.getElementById("imageFile");
  const nColorsInput = document.getElementById("nColors");
  const blendDepthInput = document.getElementById("blendDepth");
  const statusEl = document.getElementById("status");
  const previewImage = document.getElementById("previewImage");
  const submitButton = form.querySelector("button[type=\"submit\"]");
  const statusFile = document.getElementById("statusFile");
  const statusColors = document.getElementById("statusColors");
  const statusBlend = document.getElementById("statusBlend");
  const statusState = document.getElementById("statusState");

  let currentPreviewUrl = null;
  let debounceTimer = null;
  let activeController = null;
  let activeRequestId = 0;

  const formatBytes = (bytes) => {
    if (!Number.isFinite(bytes) || bytes <= 0) {
      return "0 KB";
    }
    const kb = bytes / 1024;
    if (kb < 1024) {
      return `${kb.toFixed(1)} KB`;
    }
    const mb = kb / 1024;
    return `${mb.toFixed(1)} MB`;
  };

  const setStatusState = (state) => {
    statusState.textContent = state;
  };

  const setStatus = (message, isError = false) => {
    statusEl.textContent = message;
    statusEl.classList.toggle("error", isError);
  };

  const updateStatusPanel = () => {
    const file = fileInput.files[0];
    if (file) {
      statusFile.textContent = `${file.name} (${formatBytes(file.size)})`;
    } else {
      statusFile.textContent = "None";
    }
    statusColors.textContent = nColorsInput.value || "default";
    statusBlend.textContent = blendDepthInput.value || "default";
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
        setStatusState("Error");
      }
      return;
    }

    cancelActiveRequest();
    const controller = new AbortController();
    activeController = controller;
    const requestId = activeRequestId + 1;
    activeRequestId = requestId;
    setBusy(true);
    setStatusState("Rendering...");
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
        setStatus(`Preview failed: ${response.status}`, true);
        setStatusState("Error");
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
      setStatusState("Done");
      setStatus("Preview ready.");
    } catch (error) {
      if (error.name === "AbortError") {
        return;
      }
      setStatus("Network error", true);
      setStatusState("Error");
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
    updateStatusPanel();
    await runPreview(true);
  });

  fileInput.addEventListener("change", updateStatusPanel);
  nColorsInput.addEventListener("input", () => {
    updateStatusPanel();
    scheduleLivePreview();
  });
  blendDepthInput.addEventListener("input", () => {
    updateStatusPanel();
    scheduleLivePreview();
  });

  setStatusState("Idle");
  updateStatusPanel();
})();
