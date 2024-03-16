from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiIntegrationConfigVerifyOtrs")


@attr.s(auto_attribs=True)
class ApiIntegrationConfigVerifyOtrs:
    """
    Attributes:
        integration_type (str):
    """

    integration_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IntegrationType": integration_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_type = d.pop("IntegrationType")

        api_integration_config_verify_otrs = cls(
            integration_type=integration_type,
        )

        api_integration_config_verify_otrs.additional_properties = d
        return api_integration_config_verify_otrs

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
