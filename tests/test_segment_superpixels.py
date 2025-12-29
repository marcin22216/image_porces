import numpy as np

from ops.segment_superpixels import segment


def test_segment_contract_and_labels():
    image = np.zeros((12, 12, 3), dtype=np.uint8)
    image[:, :6, :] = 40
    image[:, 6:, :] = 200

    labels = segment(
        image,
        n_segments=9,
        compactness=10.0,
        max_iter=3,
        method="slic",
    )

    assert labels.shape == (12, 12)
    assert labels.dtype == np.int32
    assert labels.min() >= 0

    unique = np.unique(labels)
    assert 4 <= unique.size <= 18
