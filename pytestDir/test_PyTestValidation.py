import pytest

@pytest.fixture(scope="module")
def pre_work():
    print("I setup module instance")
    return "fail"

@pytest.fixture(scope="function")
def second_work():
    print("I setup second_work instance")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initial_check(pre_work, second_work):
    print("this is first test")
    assert pre_work == "fail"

@pytest.mark.skip
def test_second_check(pre_setup_work, second_work):
    print("this is second test")