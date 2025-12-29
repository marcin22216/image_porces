import numpy as np

from ops.merge_small_regions import merge


def test_merge_small_regions_contract_and_size():
    image = np.zeros((6, 6, 3), dtype=np.uint8)
    image[:, :3, :] = 20
    image[:, 3:, :] = 200

    labels = np.zeros((6, 6), dtype=np.int32)
    labels[:, 3:] = 1
    labels[0, 0] = 2  # tiny region on left
    labels[5, 5] = 3  # tiny region on right

    merged = merge(labels, image, min_area=4)

    assert merged.shape == labels.shape
    assert merged.dtype == np.int32

    unique, counts = np.unique(merged, return_counts=True)
    assert np.all(counts >= 4)
    assert unique.size <= np.unique(labels).size
