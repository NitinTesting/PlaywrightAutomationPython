import pytest
@pytest.fixture
def prework():
    print("setup iniital test")
    name = "nitin"
    return name



@pytest.fixture
def basic():
    print("setup basic for test test")
    yield
    print("teardown")


