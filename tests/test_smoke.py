def test_smoke():
    from lambdawalker.reflection.load import load_submodules
    assert load_submodules is not None
    print("reflection OK")
