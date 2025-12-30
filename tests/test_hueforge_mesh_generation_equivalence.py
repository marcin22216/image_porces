import numpy as np

from hueforge.geometry.mesh_generation import Mesh as NewMesh
from hueforge.geometry.mesh_generation import height_map_to_mesh as new_height_map_to_mesh
from src.geom.mesh_generation import Mesh as LegacyMesh
from src.geom.mesh_generation import height_map_to_mesh as legacy_height_map_to_mesh


def test_mesh_generation_equivalence() -> None:
    height_map = np.array(
        [
            [0.32, 0.40],
            [0.48, 0.56],
        ],
        dtype=np.float32,
    )
    mm_per_pixel = 0.5

    legacy = legacy_height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
    new = new_height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)

    assert isinstance(legacy, LegacyMesh)
    assert isinstance(new, NewMesh)
    assert legacy.vertices.dtype == np.float32
    assert new.vertices.dtype == np.float32
    assert legacy.faces.dtype == np.int32
    assert new.faces.dtype == np.int32
    assert legacy.vertices.shape == new.vertices.shape
    assert legacy.faces.shape == new.faces.shape
    np.testing.assert_allclose(legacy.vertices, new.vertices)
    np.testing.assert_array_equal(legacy.faces, new.faces)

    legacy2 = legacy_height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
    new2 = new_height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)

    np.testing.assert_allclose(legacy.vertices, legacy2.vertices)
    np.testing.assert_array_equal(legacy.faces, legacy2.faces)
    np.testing.assert_allclose(new.vertices, new2.vertices)
    np.testing.assert_array_equal(new.faces, new2.faces)
