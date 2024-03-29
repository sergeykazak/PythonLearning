from tools import Calculator
import pytest


#                                 #scope = module means that object Calculator will be create only once and then used
# @pytest.fixture(scope='module')   # by each method with this fixture
# def calc():
#     # return Calculator()
#     # run some code before yield (e.g. code to perform  authentication)
#     yield Calculator()
#     #run some code after yield - this is an advantage of yield usage, cause after return nothing can be run


@pytest.mark.slow
def test_add(calc):
    result = calc.add(24, 24)
    assert result == 48


# to run in terminal test with custom fixture (in our case slow):
#  terminal -s -v -m 'slow'


@pytest.mark.slow
@pytest.mark.smoke
def test_extract(calc):
    result = calc.extract(245, 35)
    assert result == 210


def test_multiply(calc):
    result = calc.multiply(42, 2)
    assert result == 84


# @pytest.mark.skip(reason="will be fixed later")  # use this notation to skip this test from running, free text for reason
# def test_division_by_zero(calc):
#     result =calc.divide(5, 0)
#     assert result == 0

@pytest.mark.xfail  # use this notation when we know that this test faill, but it will be run anyway
def test_division_by_zero(calc):
    result = calc.divide(5, 0)
    assert result == None  # after we update divide methode with (if b == 0: return None) and modify assert here
    # from assert result == 0 to assert result == None test runs successfully and
    #  test_tools.py::test_division_by_zero XFAIL changes to test_tools.py::test_division_by_zero XPASS


def test_answer(cmdopt):
    if cmdopt == 'type1':
        print('first')
    elif cmdopt == 'type2':
        print('second')
    assert 0
