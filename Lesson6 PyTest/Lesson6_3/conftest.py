import pytest
from tools import Calculator


# scope = module means that object Calculator will be create only once and then used
@pytest.fixture(scope='module')  # by each method with this fixture
def calc():
    # return Calculator()
    # run some code before yield (e.g. code to perform  authentication)
    yield Calculator()
    # run some code after yield - this is an advantage of yield usage, cause after return nothing can be run


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="select option: type1 or type2"
    )


@pytest.fixture  # by default scope = function
def cmdopt(request):
    return request.config.getoption("--cmdopt")
