from django.contrib import admin

# Register your models here.

from circlescore.models import (
    Document, Workspace, LocationType, Location,
    AccountType, AccountSubType, Account, HikayaUser,
    Sector, Office, Contact, Country, Currency, FundingStatus,
    WorkflowStatus, WorkflowLevel1Type, WorkflowLevel1,
    WorkflowLevel2Type, WorkflowLevel2, WorkflowLevel2Plan ,Approval,
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'url', 'created_by', 'modified_by',
    )
    display = 'Documents'


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'url', 'created_by', 'modified_by',
    )
    display = 'Workspaces'


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'workspace', 'created_by', 'modified_by',
    )
    display = 'Account Types'
    list_filter = ('workspace',)


@admin.register(AccountSubType)
class AccountSubTypeAdmin(admin.ModelAdmin):
    list_display = (
        'sub_type', 'account_type', 'workspace', 'created_by',
        'modified_by',
    )
    display = 'Account Types'
    list_filter = ('workspace', 'account_type',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'url', 'parent_account', 'created_by', 'modified_by',
    )
    display = 'Accounts'
    list_filter = ('workspace', 'account_type',)


@admin.register(HikayaUser)
class HikayaUserAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'user', 'workspace',
    )
    display = 'Hikaya Users'
    list_filter = ('workspace',)


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'code', 'created_by', 'modified_by',
    )
    display = 'Offices'
    list_filter = ('workspace',)


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'sector', 'parent_sector', 'created_by',
        'modified_by',
    )
    display = 'Sectors'
    list_filter = ('parent_sector',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone',
        'created_by', 'modified_by',
    )
    display = 'Contacts'
    list_filter = ('account',)


@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'created_by', 'modified_by',
    )
    display = 'Location Types'
    list_filter = ('workspace', 'account',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'country', 'created_by', 'modified_by',
    )
    display = 'Countries'
    list_filter = ('workspace',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'parent_location', 'contact',
        'created_by', 'modified_by',
    )
    display = 'Locations'
    list_filter = ('workspace',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'symbol', 'code',
        'created_by', 'modified_by',
    )
    display = 'Currencies'
    list_filter = ('workspace',)


@admin.register(FundingStatus)
class FundingStatusAdmin(admin.ModelAdmin):
    list_display = (
        'status', 'created_by', 'modified_by',
    )
    display = 'Funding Statuses'


@admin.register(WorkflowStatus)
class WorkflowStatusAdmin(admin.ModelAdmin):
    list_display = (
        'status', 'created_by', 'modified_by',
    )
    display = 'Workflow Statuses'


@admin.register(WorkflowLevel1Type)
class WorkflowLevel1TypeAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'created_by', 'modified_by',
    )
    display = 'Workflow  Level1 Types'


@admin.register(WorkflowLevel1)
class WorkflowLevel1Admin(admin.ModelAdmin):
    list_display = (
        'name', 'start_date', 'end_date', 'created_by',
        'modified_by',
    )
    display = 'Workflow  Level1s'


@admin.register(WorkflowLevel2)
class WorkflowLevel2Admin(admin.ModelAdmin):
    list_display = (
        'name', 'parent', 'workflow_level1', 'created_by',
        'modified_by',
    )
    list_filter = ('workflow_level1', 'workflow_level2_type',
                   'created_by',)
    display = 'Workflow  Level2s'


@admin.register(WorkflowLevel2Type)
class WorkflowLevel2TypeAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'created_by', 'modified_by',
    )
    display = 'Workflow Level2 Types'


@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created_by', 'modified_by',
    )
    display = 'Approvals'


@admin.register(WorkflowLevel2Plan)
class WorkflowLevel2PlanAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'workflow_level1', 'workflow_level2',
        'created_by', 'modified_by',
    )
    display = 'Workflow Level2 Plans'
