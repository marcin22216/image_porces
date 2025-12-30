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
  const statusUpdated = document.getElementById("statusUpdated");
  const statusFresh = document.getElementById("statusFresh");
  const requestFile = document.getElementById("requestFile");
  const requestColors = document.getElementById("requestColors");
  const requestBlend = document.getElementById("requestBlend");
  const statusFields = document.getElementById("statusFields");
  const statusOmitted = document.getElementById("statusOmitted");

  let currentPreviewUrl = null;
  let debounceTimer = null;
  let activeController = null;
  let requestSeq = 0;
  let lastCompletedSnapshot = null;

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

  const setStatusUpdated = () => {
    statusUpdated.textContent = new Date().toLocaleTimeString();
  };

  const setFreshness = (value) => {
    statusFresh.textContent = value;
  };

  const setStatus = (message, isError = false) => {
    statusEl.textContent = message;
    statusEl.classList.toggle("error", isError);
  };

  const captureSnapshot = () => {
    const file = fileInput.files[0];
    return {
      fileName: file ? file.name : null,
      fileSize: file ? file.size : null,
      nColors: nColorsInput.value || "",
      blendDepth: blendDepthInput.value || "",
    };
  };

  const snapshotsEqual = (left, right) => {
    if (!left || !right) {
      return false;
    }
    return (
      left.fileName === right.fileName
      && left.fileSize === right.fileSize
      && left.nColors === right.nColors
      && left.blendDepth === right.blendDepth
    );
  };

  const updateFreshness = () => {
    if (!lastCompletedSnapshot) {
      setFreshness("Unknown");
      return;
    }
    const current = captureSnapshot();
    setFreshness(snapshotsEqual(current, lastCompletedSnapshot) ? "Yes" : "No");
  };

  const updateStatusPanel = () => {
    const file = fileInput.files[0];
    let fileSummary = "None";
    const included = [];
    const omitted = [];
    if (file) {
      fileSummary = `${file.name} (${formatBytes(file.size)})`;
      included.push("file");
    } else {
      omitted.push("file");
    }
    statusFile.textContent = fileSummary;
    requestFile.textContent = fileSummary;
    const nColorsValue = nColorsInput.value.trim();
    const blendDepthValue = blendDepthInput.value.trim();
    statusColors.textContent = nColorsValue || "default";
    requestColors.textContent = nColorsValue || "default";
    statusBlend.textContent = blendDepthValue || "default";
    requestBlend.textContent = blendDepthValue || "default";
    if (nColorsValue) {
      included.push("n_colors");
    } else {
      omitted.push("n_colors");
    }
    if (blendDepthValue) {
      included.push("blend_depth");
    } else {
      omitted.push("blend_depth");
    }
    statusFields.textContent = included.length ? included.join(", ") : "none";
    statusOmitted.textContent = omitted.length ? omitted.join(", ") : "none";
    updateFreshness();
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
        setStatus("No file selected", true);
        setStatusState("Error");
      }
      return;
    }

    cancelActiveRequest();
    requestSeq += 1;
    const localSeq = requestSeq;
    const controller = new AbortController();
    activeController = controller;
    const requestSnapshot = captureSnapshot();
    setBusy(true);
    setStatusState("Rendering...");
    setStatus("Rendering...");
    try {
      const response = await fetch("/preview", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      });

      if (localSeq !== requestSeq) {
        return;
      }
      if (!response.ok) {
        if (response.status === 400) {
          setStatus("Preview failed (invalid input)", true);
        } else {
          setStatus(`Preview failed (status ${response.status})`, true);
        }
        setStatusState("Error");
        setStatusUpdated();
        updateFreshness();
        return;
      }

      const blob = await response.blob();
      if (localSeq !== requestSeq) {
        return;
      }
      if (currentPreviewUrl) {
        URL.revokeObjectURL(currentPreviewUrl);
      }
      currentPreviewUrl = URL.createObjectURL(blob);
      previewImage.src = currentPreviewUrl;
      previewImage.style.display = "block";
      lastCompletedSnapshot = requestSnapshot;
      setStatusState("Done");
      setStatusUpdated();
      setFreshness("Yes");
      setStatus("Preview ready.");
    } catch (error) {
      if (error.name === "AbortError") {
        if (localSeq === requestSeq) {
          setStatusState("Idle");
          setStatus("");
        }
        return;
      }
      if (localSeq !== requestSeq) {
        return;
      }
      setStatus("Network error", true);
      setStatusState("Error");
      setStatusUpdated();
      updateFreshness();
    } finally {
      if (localSeq === requestSeq) {
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
  setFreshness("Unknown");
  statusUpdated.textContent = "Never";
  updateStatusPanel();
})();
