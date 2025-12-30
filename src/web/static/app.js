(() => {
  const form = document.getElementById("previewForm");
  const fileInput = document.getElementById("imageFile");
  const nColorsInput = document.getElementById("nColors");
  const blendDepthInput = document.getElementById("blendDepth");
  const statusEl = document.getElementById("status");
  const previewImage = document.getElementById("previewImage");

  let currentPreviewUrl = null;

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

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const file = fileInput.files[0];
    if (!file) {
      clearPreview();
      setStatus("Select an image file to continue.", true);
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    if (nColorsInput.value) {
      formData.append("n_colors", nColorsInput.value);
    }
    if (blendDepthInput.value) {
      formData.append("blend_depth", blendDepthInput.value);
    }

    clearPreview();
    setStatus("Generating preview...");

    try {
      const response = await fetch("/preview", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorText = await response.text();
        setStatus(`Error: ${errorText}`, true);
        return;
      }

      const blob = await response.blob();
      currentPreviewUrl = URL.createObjectURL(blob);
      previewImage.src = currentPreviewUrl;
      previewImage.style.display = "block";
      setStatus("Preview ready.");
    } catch (error) {
      setStatus("Network error while calling /preview.", true);
    }
  });
})();
