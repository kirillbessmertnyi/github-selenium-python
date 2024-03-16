import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFieldValueDateTime")


@attr.s(auto_attribs=True)
class ApiFieldValueDateTime:
    """
    Attributes:
        field_value_type (str):
        text (Union[Unset, None, str]): A human-readable representation of the field value.
        value (Union[Unset, None, datetime.datetime]):
    """

    field_value_type: str
    text: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_value_type = self.field_value_type
        text = self.text
        value: Union[Unset, None, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat() if self.value else None

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

        _value = d.pop("Value", UNSET)
        value: Union[Unset, None, datetime.datetime]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value)

        api_field_value_date_time = cls(
            field_value_type=field_value_type,
            text=text,
            value=value,
        )

        api_field_value_date_time.additional_properties = d
        return api_field_value_date_time

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
