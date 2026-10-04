""" Smoke test: the package imports """


def test_import():
    import star_island
    assert star_island.__doc__
