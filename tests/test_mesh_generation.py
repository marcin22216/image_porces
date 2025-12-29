import numpy as np

from geom.mesh_generation import height_map_to_mesh


def test_mesh_generation_contract_and_counts():
    height_map = np.array(
        [
            [0.0, 1.0],
            [2.0, 0.0],
        ],
        dtype=np.float32,
    )

    mesh = height_map_to_mesh(height_map, mm_per_pixel=2.0)

    assert mesh.vertices.shape == (68, 3)
    assert mesh.vertices.dtype == np.float32
    assert mesh.faces.shape == (34, 3)
    assert mesh.faces.dtype == np.int32
    assert np.isfinite(mesh.vertices).all()
    assert np.isfinite(mesh.faces).all()
    assert mesh.faces.max() < mesh.vertices.shape[0]
    assert mesh.vertices[:, 0].max() == 4.0
    assert mesh.vertices[:, 1].max() == 4.0
