import utils.constants as constants

from os import environ
from pytest import fixture
from reqflow import given
from time import sleep


@fixture(scope="session")
def get_token():
    """
    Request to get token
    :return: token from response
    """
    dsis_user = environ["OEC_USERNAME"]
    dsis_pass = environ["OEC_PASS"]
    token_data = f"username={dsis_user}&password={dsis_pass}&grant_type=password&client_id=dsis-data"
    token_headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = (given(url=constants.TOKEN_URL).headers(token_headers)
                .body(data=token_data)
                .when("POST", constants.TOKEN_ENDPOINT)
                .then()
                .get_response())
    return response.body["access_token"]


@fixture(scope="session")
def test_microservice():
    response = given(url=constants.BASE_URL).when("GET", constants.HEALTHCHECK_ENDPOINT).then().get_response()
    return response.body


def pytest_addoption(parser):
    parser.addoption("--delay", action="store", default=0, type=int, help="delay between tests in seconds")


@fixture(scope="function", autouse=True)
def delay_between_tests(request):
    delay = request.config.getoption("--delay")
    yield
    if delay > 0:
        print(f"Delay for {delay} sec")
    sleep(delay)
