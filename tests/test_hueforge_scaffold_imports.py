def test_hueforge_scaffold_imports() -> None:
    import hueforge
    from hueforge.preprocessing.scale import scale_image_to_canvas
    from hueforge.geometry.mesh import Mesh, height_map_to_mesh
    from hueforge.export.colorplan import export_colorplan_txt

    assert hueforge is not None
    assert scale_image_to_canvas is not None
    assert height_map_to_mesh is not None
    assert Mesh is not None
    assert export_colorplan_txt is not None
