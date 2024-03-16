from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_label_info import ApiLabelInfo


T = TypeVar("T", bound="ApiLabelNew")


@attr.s(auto_attribs=True)
class ApiLabelNew:
    """Represents a new label.

    Attributes:
        name (Union[Unset, None, str]): Name of this label. The name is unique in combination with the base object type.
        project_id (Union[Unset, int]): Project this label should belong to.
        description (Union[Unset, None, str]): Description of label.
        sub_labels (Union[Unset, None, List['ApiLabelInfo']]): Contains a list of lables this label includes, making it
            a super label.
    """

    name: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    description: Union[Unset, None, str] = UNSET
    sub_labels: Union[Unset, None, List["ApiLabelInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        project_id = self.project_id
        description = self.description
        sub_labels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_labels, Unset):
            if self.sub_labels is None:
                sub_labels = None
            else:
                sub_labels = []
                for sub_labels_item_data in self.sub_labels:
                    sub_labels_item = sub_labels_item_data.to_dict()

                    sub_labels.append(sub_labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if description is not UNSET:
            field_dict["Description"] = description
        if sub_labels is not UNSET:
            field_dict["SubLabels"] = sub_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_label_info import ApiLabelInfo

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        description = d.pop("Description", UNSET)

        sub_labels = []
        _sub_labels = d.pop("SubLabels", UNSET)
        for sub_labels_item_data in _sub_labels or []:
            sub_labels_item = ApiLabelInfo.from_dict(sub_labels_item_data)

            sub_labels.append(sub_labels_item)

        api_label_new = cls(
            name=name,
            project_id=project_id,
            description=description,
            sub_labels=sub_labels,
        )

        return api_label_new
