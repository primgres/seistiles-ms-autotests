import utils.constants as constants
import utils.patchgen_data_models as patchgen_models

from json import load
from pytest import mark, skip
from reqflow import given


@mark.parametrize("data", constants.PATCHGEN_DATA)
def test_patches_generation_positive(test_microservice, get_token, data):
    if test_microservice != "JobOrchestrator is healthy":
        skip("Microservice is not available")

    payload = load(open(data, "r"))
    response = (given(url=constants.BASE_URL).headers(constants.HEADERS).body(payload)
                .when("POST", constants.PATCH_GEN_ENDPOINT)
                .with_oauth2(get_token)
                .then(timeout=constants.MAX_GEN_TIMEOUT)
                .status_code(constants.SUCCESSFUL_STATUS_CODE)
                .assert_response_time(max_time=constants.MAX_GEN_TIMEOUT)
                .validate_data(patchgen_models.ResponsePatchGenModel)
                .get_response())

    print("\nPATCHGEN time: " + str(int(response.response_time)) + " sec")
