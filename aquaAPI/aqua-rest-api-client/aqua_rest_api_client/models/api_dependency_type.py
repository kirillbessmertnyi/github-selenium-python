from enum import Enum


class ApiDependencyType(str, Enum):
    RELATEDTO = "RelatedTo"
    DUPLICATES = "Duplicates"
    DETAILS = "Details"
    ISDETAILEDBY = "IsDetailedBy"
    ISNEWERVERSIONOF = "IsNewerVersionOf"
    HASNEWERVERSION = "HasNewerVersion"
    DEPENDSON = "DependsOn"
    HASDEPENDENTITEM = "HasDependentItem"
    CONFLICTSWITH = "ConflictsWith"
    ALTERNATIVETO = "AlternativeTo"
    VERIFIES = "Verifies"
    ISVERIFIEDBY = "IsVerifiedBy"
    ISPRECONDITIONOF = "IsPreconditionOf"
    HASPRECONDITION = "HasPrecondition"
    ISCOPYOF = "IsCopyOf"
    WASCOPIEDTO = "WasCopiedTo"
    ISUTILITYSCRIPTOF = "IsUtilityScriptOf"
    USESUTILITYSCRIPT = "UsesUtilityScript"
    NESTS = "Nests"
    ISNESTEDIN = "IsNestedIn"
    REFERENCESTESTCASETESTDATA = "ReferencesTestCaseTestData"
    SHARESTESTDATAWITH = "SharesTestDataWith"

    def __str__(self) -> str:
        return str(self.value)
