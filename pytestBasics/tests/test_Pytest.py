import pytest
# @pytest.mark.skip
@pytest.mark.regression
def testFirst_test(prework):
    print("this is my test")
    print(prework)

@pytest.mark.smoke
def testSecond_test1(prework, basic):
    print("this is my test1")
    name = "nitin"
    assert name == prework,"{} does not match with {}".format(name, prework)
