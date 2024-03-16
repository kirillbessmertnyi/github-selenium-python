import json
import pytest
from httpx import Client as HttpxClient
from aqua_rest_api_client import AuthenticatedClient
from aqua_rest_api_client.api.test_execution import test_execution_create
from aqua_rest_api_client.models.api_test_execution_new import ApiTestExecutionNew
from aqua_rest_api_client.models.api_test_step_execution_new import ApiTestStepExecutionNew
from aqua_rest_api_client.models.api_test_step_execution_step_type import ApiTestStepExecutionStepType
from aqua_rest_api_client.models.api_test_step_execution_update_status import ApiTestStepExecutionUpdateStatus

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        tokenAPI = get_access_token(aqua_base_url="https://app.aqua-cloud.io/aquawebng", 
                                 aqua_user="***PUT***AQUA***USERNAME***HERE***", 
                                 aqua_password="***PUT***AQUA***PASSWORD***HERE***")
        clientApi = AuthenticatedClient(base_url="https://app.aqua-cloud.io/aquawebng", token=tokenAPI)
        
        stepStatus = ApiTestStepExecutionUpdateStatus.PASS
        if (rep.outcome == 'failed'):
         stepStatus = ApiTestStepExecutionUpdateStatus.FAILED
        elif (rep.outcome != 'passed'):
         raise Exception("test execution has other status")
        
        testSteps = ApiTestStepExecutionNew(index=1,
                                            name="Step 1",
                                            step_type=ApiTestStepExecutionStepType.STEP,
                                            status=stepStatus)
        executionInfo = ApiTestExecutionNew(guid=None, 
                                            test_case_id=item.module.AQUA_TC_ID, 
                                            test_case_name=None,
                                            finalize=False,
                                            value_set_name=None,
                                            test_scenario_info=None,
                                            steps=[testSteps],
                                            tested_version=None,
                                            execution_duration=None,
                                            attached_labels=None,
                                            custom_fields=None,
                                            attachments=None)
        executionResponse = test_execution_create.sync(client=clientApi, json_body=[executionInfo])

def get_access_token(
    aqua_base_url: str, aqua_user: str, aqua_password: str
) -> str:
    # Authenticate against aqua server. The token is 15min valid, refresh_token can be used to generate a new token.
    auth_client = HttpxClient(base_url=aqua_base_url)
    response = auth_client.post(
        url="api/token",
        data={
            "grant_type": "password",
            "username": aqua_user,
            "password": aqua_password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    response = json.loads(response.content)

    return response["access_token"]
