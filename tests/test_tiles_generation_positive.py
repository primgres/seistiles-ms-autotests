import utils.constants as constants
import utils.utilities as utils
import utils.tilegen_data_models as data_models

from pytest import mark, skip
from reqflow import given


@mark.parametrize("data", constants.TILEGEN_DATA)
def test_tiles_generation_positive(test_microservice, get_token, data):
    if test_microservice != "JobOrchestrator is healthy":
        skip("Microservice is not available")

    payload = utils.Utility().get_payload(data)
    response = (given(url=constants.BASE_URL).headers(constants.HEADERS).body(payload)
                .when("POST", constants.TILES_GEN_ENDPOINT)
                .with_oauth2(get_token)
                .then(timeout=constants.MAX_GEN_TIMEOUT)
                .status_code(constants.SUCCESSFUL_STATUS_CODE)
                .assert_response_time(max_time=constants.MAX_GEN_TIMEOUT)
                .validate_data(data_models.ResponseTileGenModel)
                .get_response())

    print("TILEGEN Response time: " + str(int(response.response_time)) + " s")
