from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_execution_statistics import ApiTestExecutionStatistics


T = TypeVar("T", bound="ApiTestScenarioExecutionStatisticsResponse")


@attr.s(auto_attribs=True)
class ApiTestScenarioExecutionStatisticsResponse:
    """
    Attributes:
        test_scenario_execution_statistics (Union[Unset, None, List['ApiTestExecutionStatistics']]): Contains the test
            scenario execution statistics
    """

    test_scenario_execution_statistics: Union[Unset, None, List["ApiTestExecutionStatistics"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_scenario_execution_statistics: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_scenario_execution_statistics, Unset):
            if self.test_scenario_execution_statistics is None:
                test_scenario_execution_statistics = None
            else:
                test_scenario_execution_statistics = []
                for test_scenario_execution_statistics_item_data in self.test_scenario_execution_statistics:
                    test_scenario_execution_statistics_item = test_scenario_execution_statistics_item_data.to_dict()

                    test_scenario_execution_statistics.append(test_scenario_execution_statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_scenario_execution_statistics is not UNSET:
            field_dict["TestScenarioExecutionStatistics"] = test_scenario_execution_statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_execution_statistics import ApiTestExecutionStatistics

        d = src_dict.copy()
        test_scenario_execution_statistics = []
        _test_scenario_execution_statistics = d.pop("TestScenarioExecutionStatistics", UNSET)
        for test_scenario_execution_statistics_item_data in _test_scenario_execution_statistics or []:
            test_scenario_execution_statistics_item = ApiTestExecutionStatistics.from_dict(
                test_scenario_execution_statistics_item_data
            )

            test_scenario_execution_statistics.append(test_scenario_execution_statistics_item)

        api_test_scenario_execution_statistics_response = cls(
            test_scenario_execution_statistics=test_scenario_execution_statistics,
        )

        return api_test_scenario_execution_statistics_response
