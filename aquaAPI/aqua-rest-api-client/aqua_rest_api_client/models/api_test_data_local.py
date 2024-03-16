from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_placeholder import ApiFieldPlaceholder
    from ..models.api_test_data_value_set_info import ApiTestDataValueSetInfo
    from ..models.api_test_data_variable import ApiTestDataVariable


T = TypeVar("T", bound="ApiTestDataLocal")


@attr.s(auto_attribs=True)
class ApiTestDataLocal:
    """
    Attributes:
        variant (str):
        value_sets (Union[Unset, None, List['ApiTestDataValueSetInfo']]): The value sets which are part of the test
            data.
        variables (Union[Unset, None, List['ApiTestDataVariable']]): The variables which are part of the test data.
        values (Union[Unset, None, List[List[str]]]): The actual values contained in the test data. The table
            is a two-dimensional array which contains for each value
            set a list of values. The data is ordered according to
            the ValueSets and Variables list.
        fields (Union[Unset, None, List['ApiFieldPlaceholder']]): The list of fields that can be used as replacement
            placeholders in the TestCase
        is_referenced (Union[Unset, None, bool]): If not null, indicates whether this local test data is already
            referenced by other test cases.
            You need to provide 'IsReferenced' as an option to 'include' parameter in order to
            request initialization of this field.
    """

    variant: str
    value_sets: Union[Unset, None, List["ApiTestDataValueSetInfo"]] = UNSET
    variables: Union[Unset, None, List["ApiTestDataVariable"]] = UNSET
    values: Union[Unset, None, List[List[str]]] = UNSET
    fields: Union[Unset, None, List["ApiFieldPlaceholder"]] = UNSET
    is_referenced: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variant = self.variant
        value_sets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.value_sets, Unset):
            if self.value_sets is None:
                value_sets = None
            else:
                value_sets = []
                for value_sets_item_data in self.value_sets:
                    value_sets_item = value_sets_item_data.to_dict()

                    value_sets.append(value_sets_item)

        variables: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variables, Unset):
            if self.variables is None:
                variables = None
            else:
                variables = []
                for variables_item_data in self.variables:
                    variables_item = variables_item_data.to_dict()

                    variables.append(variables_item)

        values: Union[Unset, None, List[List[str]]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = []
                for values_item_data in self.values:
                    values_item = values_item_data

                    values.append(values_item)

        fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            if self.fields is None:
                fields = None
            else:
                fields = []
                for fields_item_data in self.fields:
                    fields_item = fields_item_data.to_dict()

                    fields.append(fields_item)

        is_referenced = self.is_referenced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Variant": variant,
            }
        )
        if value_sets is not UNSET:
            field_dict["ValueSets"] = value_sets
        if variables is not UNSET:
            field_dict["Variables"] = variables
        if values is not UNSET:
            field_dict["Values"] = values
        if fields is not UNSET:
            field_dict["Fields"] = fields
        if is_referenced is not UNSET:
            field_dict["IsReferenced"] = is_referenced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_placeholder import ApiFieldPlaceholder
        from ..models.api_test_data_value_set_info import ApiTestDataValueSetInfo
        from ..models.api_test_data_variable import ApiTestDataVariable

        d = src_dict.copy()
        variant = d.pop("Variant")

        value_sets = []
        _value_sets = d.pop("ValueSets", UNSET)
        for value_sets_item_data in _value_sets or []:
            value_sets_item = ApiTestDataValueSetInfo.from_dict(value_sets_item_data)

            value_sets.append(value_sets_item)

        variables = []
        _variables = d.pop("Variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = ApiTestDataVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        values = []
        _values = d.pop("Values", UNSET)
        for values_item_data in _values or []:
            values_item = cast(List[str], values_item_data)

            values.append(values_item)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiFieldPlaceholder.from_dict(fields_item_data)

            fields.append(fields_item)

        is_referenced = d.pop("IsReferenced", UNSET)

        api_test_data_local = cls(
            variant=variant,
            value_sets=value_sets,
            variables=variables,
            values=values,
            fields=fields,
            is_referenced=is_referenced,
        )

        api_test_data_local.additional_properties = d
        return api_test_data_local

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
