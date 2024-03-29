from enum import Enum


class ApiPermission(str, Enum):
    RQVIEWCONTENTALL = "RQViewContentAll"
    RQVIEWDISCUSSIONSALL = "RQViewDiscussionsAll"
    RQVIEWWORDEXPORTALL = "RQViewWordExportAll"
    RQVIEWWORDEXPORTASSIGNED = "RQViewWordExportAssigned"
    RQVIEWWORDEXPORTOWN = "RQViewWordExportOwn"
    RQCREATEEDITFIELDSDESCRIPTIONALL = "RQCreateEditFieldsDescriptionAll"
    RQCREATEEDITCOMMENTSALL = "RQCreateEditCommentsAll"
    RQCREATEWORDIMPORTALL = "RQCreateWordImportAll"
    RQEDITSTATUSALL = "RQEditStatusAll"
    RQEDITSTATUSASSIGNED = "RQEditStatusAssigned"
    RQEDITSTATUSOWN = "RQEditStatusOwn"
    RQEDITFIELDSALL = "RQEditFieldsAll"
    RQEDITFIELDSASSIGNED = "RQEditFieldsAssigned"
    RQEDITFIELDSOWN = "RQEditFieldsOwn"
    RQEDITDESCRIPTIONALL = "RQEditDescriptionAll"
    RQEDITDESCRIPTIONASSIGNED = "RQEditDescriptionAssigned"
    RQEDITDESCRIPTIONOWN = "RQEditDescriptionOwn"
    RQEDITCOMMENTSALL = "RQEditCommentsAll"
    RQEDITCOMMENTSASSIGNED = "RQEditCommentsAssigned"
    RQEDITCOMMENTSOWN = "RQEditCommentsOwn"
    RQEDITWORDIMPORTALL = "RQEditWordImportAll"
    RQEDITWORDIMPORTASSIGNED = "RQEditWordImportAssigned"
    RQEDITWORDIMPORTOWN = "RQEditWordImportOwn"
    RQEDITBATCHALL = "RQEditBatchAll"
    RQDELETEALL = "RQDeleteAll"
    RQDELETEASSIGNED = "RQDeleteAssigned"
    RQDELETEOWN = "RQDeleteOwn"
    RQMOVEINPROJECTALL = "RQMoveInProjectAll"
    RQMOVEINPROJECTASSIGNED = "RQMoveInProjectAssigned"
    RQMOVEINPROJECTOWN = "RQMoveInProjectOwn"
    RQMOVEBETWEENPROJECTSALL = "RQMoveBetweenProjectsAll"
    RQMOVEBETWEENPROJECTSASSIGNED = "RQMoveBetweenProjectsAssigned"
    RQMOVEBETWEENPROJECTSOWN = "RQMoveBetweenProjectsOwn"
    RQCREATEDEPENDENCYALL = "RQCreateDependencyAll"
    RQDELETEDEPENDENCYALL = "RQDeleteDependencyAll"
    DFVIEWCONTENTALL = "DFViewContentAll"
    DFCREATEALL = "DFCreateAll"
    DFEDITALL = "DFEditAll"
    DFEDITASSIGNED = "DFEditAssigned"
    DFEDITOWN = "DFEditOwn"
    DFEDITENCLOSURESALL = "DFEditEnclosuresAll"
    DFEDITENCLOSURESOWN = "DFEditEnclosuresOwn"
    DFEDITBATCHALL = "DFEditBatchAll"
    DFDELETEALL = "DFDeleteAll"
    DFDELETEASSIGNED = "DFDeleteAssigned"
    DFDELETEOWN = "DFDeleteOwn"
    DFDELETEENCLOSURESALL = "DFDeleteEnclosuresAll"
    DFDELETEENCLOSURESOWN = "DFDeleteEnclosuresOwn"
    DFMOVEINPROJECTALL = "DFMoveInProjectAll"
    DFMOVEINPROJECTASSIGNED = "DFMoveInProjectAssigned"
    DFMOVEINPROJECTOWN = "DFMoveInProjectOwn"
    DFMOVEBETWEENPROJECTSALL = "DFMoveBetweenProjectsAll"
    DFMOVEBETWEENPROJECTSASSIGNED = "DFMoveBetweenProjectsAssigned"
    DFMOVEBETWEENPROJECTSOWN = "DFMoveBetweenProjectsOwn"
    DFCREATEDEPENDENCYALL = "DFCreateDependencyAll"
    DFDELETEDEPENDENCYALL = "DFDeleteDependencyAll"
    TCVIEWCONTENTALL = "TCViewContentAll"
    TCCREATEEDITFIELDSDESCRIPTIONALL = "TCCreateEditFieldsDescriptionAll"
    TCCREATEEDITVARIABLESALL = "TCCreateEditVariablesAll"
    TCCREATEEDITNESTINGALL = "TCCreateEditNestingAll"
    TCCREATEEDITTESTAUTOMATIONALL = "TCCreateEditTestAutomationAll"
    TCEDITSTATUSALL = "TCEditStatusAll"
    TCEDITSTATUSASSIGNED = "TCEditStatusAssigned"
    TCEDITSTATUSOWN = "TCEditStatusOwn"
    TCEDITFIELDDESCRIPTIONALL = "TCEditFieldDescriptionAll"
    TCEDITFIELDDESCRIPTIONASSIGNED = "TCEditFieldDescriptionAssigned"
    TCEDITFIELDDESCRIPTIONOWN = "TCEditFieldDescriptionOwn"
    TCEDITSTEPSALL = "TCEditStepsAll"
    TCEDITSTEPSASSIGNED = "TCEditStepsAssigned"
    TCEDITSTEPSOWN = "TCEditStepsOwn"
    TCEDITVARIABLESALL = "TCEditVariablesAll"
    TCEDITVARIABLESASSIGNED = "TCEditVariablesAssigned"
    TCEDITVARIABLESOWN = "TCEditVariablesOwn"
    TCEDITNESTINGALL = "TCEditNestingAll"
    TCEDITNESTINGASSIGNED = "TCEditNestingAssigned"
    TCEDITNESTINGOWN = "TCEditNestingOwn"
    TCEDITTESTAUTOMATIONALL = "TCEditTestAutomationAll"
    TCEDITTESTAUTOMATIONASSIGNED = "TCEditTestAutomationAssigned"
    TCEDITTESTAUTOMATIONOWN = "TCEditTestAutomationOwn"
    TCEDITBATCHALL = "TCEditBatchAll"
    TCDELETEALL = "TCDeleteAll"
    TCDELETEASSIGNED = "TCDeleteAssigned"
    TCDELETEOWN = "TCDeleteOwn"
    TCMOVEINPROJECTALL = "TCMoveInProjectAll"
    TCMOVEINPROJECTASSIGNED = "TCMoveInProjectAssigned"
    TCMOVEINPROJECTOWN = "TCMoveInProjectOwn"
    TCMOVEBETWEENPROJECTSALL = "TCMoveBetweenProjectsAll"
    TCMOVEBETWEENPROJECTSASSIGNED = "TCMoveBetweenProjectsAssigned"
    TCMOVEBETWEENPROJECTSOWN = "TCMoveBetweenProjectsOwn"
    TCCREATEDEPENDENCYALL = "TCCreateDependencyAll"
    TCDELETEDEPENDENCYALL = "TCDeleteDependencyAll"
    TSVIEWCONTENTALL = "TSViewContentAll"
    TSCREATEALL = "TSCreateAll"
    TSEDITALL = "TSEditAll"
    TSEDITASSIGNED = "TSEditAssigned"
    TSEDITOWN = "TSEditOwn"
    TSEDITBATCHALL = "TSEditBatchAll"
    TSDELETEALL = "TSDeleteAll"
    TSDELETEASSIGNED = "TSDeleteAssigned"
    TSDELETEOWN = "TSDeleteOwn"
    TSMOVEINPROJECTALL = "TSMoveInProjectAll"
    TSMOVEINPROJECTASSIGNED = "TSMoveInProjectAssigned"
    TSMOVEINPROJECTOWN = "TSMoveInProjectOwn"
    TSMOVEBETWEENPROJECTSALL = "TSMoveBetweenProjectsAll"
    TSMOVEBETWEENPROJECTSASSIGNED = "TSMoveBetweenProjectsAssigned"
    TSMOVEBETWEENPROJECTSOWN = "TSMoveBetweenProjectsOwn"
    TSCREATEDEPENDENCYALL = "TSCreateDependencyAll"
    TSDELETEDEPENDENCYALL = "TSDeleteDependencyAll"
    EXTCMANUALALL = "EXTCManualAll"
    EXTCAUTOMATEDALL = "EXTCAutomatedAll"
    EXTSMANUALALL = "EXTSManualAll"
    EXTSAUTOMATEDALL = "EXTSAutomatedAll"
    EXSCHEDULINGALL = "EXSchedulingAll"
    EXSCHEDULINGASSIGNED = "EXSchedulingAssigned"
    EXSCHEDULINGOWN = "EXSchedulingOwn"
    EXFINALIZEALL = "EXFinalizeAll"
    EXSETRELEVANCEALL = "EXSetRelevanceAll"
    SCVIEWCONTENTALL = "SCViewContentAll"
    SCCREATEALL = "SCCreateAll"
    SCEDITALL = "SCEditAll"
    SCEDITASSIGNED = "SCEditAssigned"
    SCEDITOWN = "SCEditOwn"
    SCEDITBATCHALL = "SCEditBatchAll"
    SCDELETEALL = "SCDeleteAll"
    SCDELETEASSIGNED = "SCDeleteAssigned"
    SCDELETEOWN = "SCDeleteOwn"
    SCMOVEINPROJECTALL = "SCMoveInProjectAll"
    SCMOVEINPROJECTASSIGNED = "SCMoveInProjectAssigned"
    SCMOVEINPROJECTOWN = "SCMoveInProjectOwn"
    SCMOVEBETWEENPROJECTSALL = "SCMoveBetweenProjectsAll"
    SCMOVEBETWEENPROJECTSASSIGNED = "SCMoveBetweenProjectsAssigned"
    SCMOVEBETWEENPROJECTSOWN = "SCMoveBetweenProjectsOwn"
    SCCREATEDEPENDENCYALL = "SCCreateDependencyAll"
    SCDELETEDEPENDENCYALL = "SCDeleteDependencyAll"
    GEVIEWSPUBLISHALL = "GEViewsPublishAll"
    GEVIEWSEDITPUBLICALL = "GEViewsEditPublicAll"
    GEPROJECTEDITTREEALL = "GEProjectEditTreeAll"
    GEPROJECTCONFIGUREALL = "GEProjectConfigureAll"
    GEPROJECTCONFIGUREUSERSALL = "GEProjectConfigureUsersAll"
    GEPROJECTCONFIGURESUBTEMPLATEALL = "GEProjectConfigureSubtemplateAll"
    GEPROJECTVIEWALLUSERSALL = "GEProjectViewAllUsersAll"
    GENOTIFICATIONSALL = "GENotificationsAll"
    GEMINDMAPVIEWALL = "GEMindMapViewAll"
    GEMINDMAPCREATEEDITALL = "GEMindMapCreateEditAll"
    GEATTACHMENTSVIEWOPENALL = "GEAttachmentsViewOpenAll"
    GEATTACHMENTSADDALL = "GEAttachmentsAddAll"
    GEATTACHMENTSDELETEALL = "GEAttachmentsDeleteAll"
    GEEXPORTITEMALL = "GEExportItemAll"
    GEIMPORTITEMALL = "GEImportItemAll"
    PPVIEWCONTENTALL = "PPViewContentAll"
    PPREPORTWORKALL = "PPReportWorkAll"
    PPCREATEEDITDELETEITEMSALL = "PPCreateEditDeleteItemsAll"
    PPSHOWEARNEDVALUEANALYSISALL = "PPShowEarnedValueAnalysisAll"
    DAVIEWALL = "DAViewAll"
    DAEDITALL = "DAEditAll"
    DACHARTPUBLISHALL = "DAChartPublishAll"
    DACHARTEDITPUBLICALL = "DAChartEditPublicAll"
    AGVIEWALL = "AGViewAll"
    AGSPRINTCREATEEDITALL = "AGSprintCreateEditAll"
    AGSPRINTDELETEALL = "AGSprintDeleteAll"
    AGSPRINTPLANNINGALL = "AGSprintPlanningAll"
    RPUSEALL = "RPUseAll"
    RPMANAGETEMPLATESALL = "RPManageTemplatesAll"
    RPCREATETEMPLATEEDITLAYOUTALL = "RPCreateTemplateEditLayoutAll"
    RPEXPORTPDFALL = "RPExportPDFAll"
    RPEXPORTHTMLALL = "RPExportHTMLAll"
    RPEXPORTMHTALL = "RPExportMHTAll"
    RPEXPORTRTFALL = "RPExportRTFAll"
    RPEXPORTXLSALL = "RPExportXLSAll"
    RPEXPORTXLSXALL = "RPExportXLSXAll"
    RPEXPORTCSVALL = "RPExportCSVAll"
    RPEXPORTTEXTFILEALL = "RPExportTextFileAll"
    RPEXPORTIMAGEFILEALL = "RPExportImageFileAll"
    RPEXPORTDOCALL = "RPExportDOCAll"
    RPEXPORTDOCXALL = "RPExportDOCXAll"
    RPEXPORTODTALL = "RPExportODTAll"
    RPSIGNPDFALL = "RPSignPDFAll"

    def __str__(self) -> str:
        return str(self.value)
