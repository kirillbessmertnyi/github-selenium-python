from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_test_execution_status import ApiTestExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_value_date_time import ApiFieldValueDateTime
    from ..models.api_field_value_user import ApiFieldValueUser
    from ..models.api_test_scenario_execution_statistics import ApiTestScenarioExecutionStatistics


T = TypeVar("T", bound="ApiTestExecutionStatistics")


@attr.s(auto_attribs=True)
class ApiTestExecutionStatistics:
    """The statistics for the test scenario execution

    Attributes:
        test_scenario_execution_id (Union[Unset, int]): The test scenario execution that these statistics are for
        last_tester (Union[Unset, None, ApiFieldValueUser]):
        last_execution_date (Union[Unset, None, ApiFieldValueDateTime]):
        last_execution_status (Union[Unset, ApiTestExecutionStatus]): Identifies the status of an execution.
            This enum has the following values:
              - `Aborted` Execution has been aborted.
              - `Blocked` At least one executed step was blocked, and there were no failures (only considered for manual
            tests)
              - `Failed` At least one executed step marked as failed.
              - `Incomplete` Some steps executed, but at least one step was not executed (and no failures or blocked yet).
              - `InProgress` Execution is in progress.
              - `NotApplicable` All steps were not applicable to the execution
              - `NotRun` No steps executed yet.
              - `Pass` All steps executed and passed.
              - `Queued` The step is queued for automated execution.
              - `Waiting` An execution was started and a step is waiting for pickup by agent
        last_execution_id (Union[Unset, int]): The execution id of the most recent execution
        statistics (Union[Unset, None, ApiTestScenarioExecutionStatistics]):
    """

    test_scenario_execution_id: Union[Unset, int] = UNSET
    last_tester: Union[Unset, None, "ApiFieldValueUser"] = UNSET
    last_execution_date: Union[Unset, None, "ApiFieldValueDateTime"] = UNSET
    last_execution_status: Union[Unset, ApiTestExecutionStatus] = UNSET
    last_execution_id: Union[Unset, int] = UNSET
    statistics: Union[Unset, None, "ApiTestScenarioExecutionStatistics"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_scenario_execution_id = self.test_scenario_execution_id
        last_tester: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_tester, Unset):
            last_tester = self.last_tester.to_dict() if self.last_tester else None

        last_execution_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_execution_date, Unset):
            last_execution_date = self.last_execution_date.to_dict() if self.last_execution_date else None

        last_execution_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_execution_status, Unset):
            last_execution_status = self.last_execution_status.value

        last_execution_id = self.last_execution_id
        statistics: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict() if self.statistics else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_scenario_execution_id is not UNSET:
            field_dict["TestScenarioExecutionId"] = test_scenario_execution_id
        if last_tester is not UNSET:
            field_dict["LastTester"] = last_tester
        if last_execution_date is not UNSET:
            field_dict["LastExecutionDate"] = last_execution_date
        if last_execution_status is not UNSET:
            field_dict["LastExecutionStatus"] = last_execution_status
        if last_execution_id is not UNSET:
            field_dict["LastExecutionId"] = last_execution_id
        if statistics is not UNSET:
            field_dict["Statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_value_date_time import ApiFieldValueDateTime
        from ..models.api_field_value_user import ApiFieldValueUser
        from ..models.api_test_scenario_execution_statistics import ApiTestScenarioExecutionStatistics

        d = src_dict.copy()
        test_scenario_execution_id = d.pop("TestScenarioExecutionId", UNSET)

        _last_tester = d.pop("LastTester", UNSET)
        last_tester: Union[Unset, None, ApiFieldValueUser]
        if _last_tester is None:
            last_tester = None
        elif isinstance(_last_tester, Unset):
            last_tester = UNSET
        else:
            last_tester = ApiFieldValueUser.from_dict(_last_tester)

        _last_execution_date = d.pop("LastExecutionDate", UNSET)
        last_execution_date: Union[Unset, None, ApiFieldValueDateTime]
        if _last_execution_date is None:
            last_execution_date = None
        elif isinstance(_last_execution_date, Unset):
            last_execution_date = UNSET
        else:
            last_execution_date = ApiFieldValueDateTime.from_dict(_last_execution_date)

        _last_execution_status = d.pop("LastExecutionStatus", UNSET)
        last_execution_status: Union[Unset, ApiTestExecutionStatus]
        if isinstance(_last_execution_status, Unset):
            last_execution_status = UNSET
        else:
            last_execution_status = ApiTestExecutionStatus(_last_execution_status)

        last_execution_id = d.pop("LastExecutionId", UNSET)

        _statistics = d.pop("Statistics", UNSET)
        statistics: Union[Unset, None, ApiTestScenarioExecutionStatistics]
        if _statistics is None:
            statistics = None
        elif isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = ApiTestScenarioExecutionStatistics.from_dict(_statistics)

        api_test_execution_statistics = cls(
            test_scenario_execution_id=test_scenario_execution_id,
            last_tester=last_tester,
            last_execution_date=last_execution_date,
            last_execution_status=last_execution_status,
            last_execution_id=last_execution_id,
            statistics=statistics,
        )

        return api_test_execution_statistics
