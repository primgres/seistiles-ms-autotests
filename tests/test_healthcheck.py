import utils.constants as constants

from pytest import mark
from reqflow import given


@mark.tryfirst
def test_microservice_is_available():
    expected_response_body = "JobOrchestrator is healthy"
    response = (given(url=constants.BASE_URL)
                .when("GET", constants.HEALTHCHECK_ENDPOINT)
                .then()
                .status_code(constants.SUCCESSFUL_STATUS_CODE)
                .assert_response_time(max_time=1.0)
                .assert_body_text(expected_response_body)
                .get_response())

    print("\nHEALTHCHECK time: " + str(int(response.response_time * 1000)) + " ms")
