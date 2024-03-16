from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValueTestScenarios")


@attr.s(auto_attribs=True)
class ApiFieldValueTestScenarios:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        value (Union[Unset, None, List[int]]):
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        value: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.value, Unset):
            if self.value is None:
                value = None
            else:
                value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldValueType": field_value_type,
            }
        )
        if text is not UNSET:
            field_dict["Text"] = text
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_value_type = d.pop("FieldValueType")

        text = d.pop("Text", UNSET)

        value = cast(List[int], d.pop("Value", UNSET))

        api_field_value_test_scenarios = cls(
            field_value_type=field_value_type,
            text=text,
            value=value,
        )

        api_field_value_test_scenarios.additional_properties = d
        return api_field_value_test_scenarios

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
