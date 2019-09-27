import uuid
from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords


class Document(models.Model):
    """
    Documentation Model
    """
    document_uuid = models.UUIDField(
        editable=False, verbose_name='Document UUID',
        default=uuid.uuid4, unique=True)
    name = models.CharField(
        'Name of Document', max_length=135, blank=True, null=True)
    url = models.CharField(
        'URL (Link to document or document repository)',
        blank=True, null=True, max_length=135)
    description = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', blank=True, null=True, editable=False)
    modified_date = models.DateTimeField(
        'Edit Date', blank=True, null=True, editable=False)
    created_by = models.ForeignKey(
        User, verbose_name='Created By', editable=False, null=True,
        related_name='document_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        User, verbose_name='Modified By', editable=False, null=True,
        related_name='document_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Documents'

    # displayed in admin templates
    def __str__(self):
        return self.name or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()

        self.edit_date = timezone.now()
        return super(Document, self).save(*args, **kwargs)

    @property
    def name_n_url(self):
        return "%s - %s" % (self.name, self.url)


class Workspace(models.Model):
    """
    Workspace is the top level model in the hierarchy for Activity
    """
    uuid = models.UUIDField(
        editable=False, verbose_name='Workspace UUID',
        default=uuid.uuid4, unique=True)
    name = models.CharField('Workspace Name', max_length=36)
    url = models.CharField('Workspace Url', max_length=100, blank=True)
    description = models.TextField(
        'Workspace Description', max_length=765, blank=True)
    workflow_level_1 = models.CharField(max_length=36, default='Project')
    workflow_level_2 = models.CharField(max_length=36, default='Activity')
    workflow_level_3 = models.CharField(max_length=36, default='Sub-Activity')
    workflow_level_4 = models.CharField('Organization/Account Label',
                                        max_length=36, default='Task')
    account_label = models.CharField(max_length=36, default='Account')
    indicator_label = models.CharField(max_length=36, default='Indicator')
    form_label = models.CharField(max_length=36, default='Forms')
    site_label = models.CharField(max_length=36, default='Sites')
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', blank=True, null=True, editable=False)
    modified_date = models.DateTimeField(
        'Edit Date', blank=True, null=True, editable=False)
    created_by = models.ForeignKey(
        User, verbose_name='Created By', editable=False, null=True,
        related_name='workspace_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        User, verbose_name='Modified By', editable=False, null=True,
        related_name='workspace_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Workspaces'

    # displayed in admin templates
    def __str__(self):
        return self.name or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()

        self.edit_date = timezone.now()
        return super(Workspace, self).save(*args, **kwargs)


class AccountType(models.Model):
    """
    Account Type Model
    """
    type_uuid = models.UUIDField(
        'Account Type UUID', editable=False, default=uuid.uuid4, unique=True)
    type = models.CharField('Account Type', max_length=100, unique=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True,
        related_name='account_type_workspace', on_delete=models.SET_NULL)
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', blank=True, null=True)
    modified_date = models.DateTimeField('Edit Date', blank=True, null=True)
    created_by = models.ForeignKey(
        User, verbose_name='Created By', editable=False, null=True,
        related_name='org_type_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        User, verbose_name='Modified By', editable=False, null=True,
        related_name='org_type_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Account Types'

    # displayed in admin templates
    def __str__(self):
        return self.type or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(AccountType, self).save(*args, **kwargs)


class AccountSubType(models.Model):
    """
    Account Sub-Type Model
    """
    sub_type_uuid = models.UUIDField(
        'Account Sub-Type UUID', editable=False,
        default=uuid.uuid4, unique=True)
    sub_type = models.CharField(
        'Account Sub-Type', max_length=100, unique=True)
    type = models.ForeignKey(
        AccountType, verbose_name='Account Type', null=True,
        on_delete=models.SET_NULL)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True,
        related_name='account_Sub_type_workspace',
        on_delete=models.SET_NULL)
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', blank=True, null=True, editable=False)
    modified_date = models.DateTimeField(
        'Edit Date', blank=True, null=True, editable=False)
    created_by = models.ForeignKey(
        User, verbose_name='Created By', editable=False, null=True,
        related_name='org_sub_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        User, verbose_name='Modified By', editable=False, null=True,
        related_name='org_sub_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Account Sub Types'

    # displayed in admin templates
    def __str__(self):
        return self.type or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(AccountSubType, self).save(*args, **kwargs)


class Account(models.Model):
    """
    Account Model
    """
    # define status choices
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'Inactive'))
    account_uuid = models.UUIDField(
        'Account UUID', editable=False, default=uuid.uuid4, unique=True)
    full_name = models.CharField(
        "Account's Full Name", max_length=135, blank=True,
        default='First Account')
    short_name = models.CharField('Account Short Name', max_length=100)
    url = models.CharField("Account's Website URL", max_length=165, blank=True)
    description = models.TextField(
        'Description/Notes', max_length=765, null=True, blank=True)
    organization_type = models.ForeignKey(
        AccountType, null=True, blank=True, on_delete=models.SET_NULL)
    parent_organization = models.ForeignKey(
        'self', null=True, blank=True, related_name='children',
        on_delete=models.SET_NULL)
    documentation = models.ForeignKey(
        Document, null=True, blank=True, on_delete=models.SET_NULL)
    link_to_description_relationship = models.CharField(
        'Link to Description of Relationship', blank=True, max_length=165)
    link_to_due_diligence = models.CharField(
        'Link to Due Diligence', blank=True, max_length=165)
    singular_label = models.CharField(
        'Account Singular Label', max_length=135, blank=True,
        default='Account')
    plural_label = models.CharField(
        'Account Plural Label', max_length=135, blank=True, default='Accounts')
    organization_identifier = models.CharField(
        'Account Identifier', max_length=100, blank=True)
    organization_status = models.CharField(
        'Account Status', max_length=100, choices=STATUS_CHOICES)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='account_workspace',
        on_delete=models.SET_NULL)
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        User, verbose_name='Created By', related_name='org_created_by',
        editable=False, null=True, on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        User, verbose_name='Modified By', related_name='org_modified_by',
        editable=False, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('full_name',)
        verbose_name_plural = "Accounts"

    # displayed in admin templates
    def __str__(self):
        return self.full_name or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Account, self).save(*args, **kwargs)


class HikayaUser(models.Model):
    """
    Hikaya Core User Model
    Has a one-to-one relation with the auth user model
    """
    TITLE_CHOICES = (('mr', 'Mr.'), ('mrs', 'Mrs.'), ('ms', 'Ms.'),)
    hikaya_user_uuid = models.UUIDField(
        'Hikaya User UUID', editable=False,
        default=uuid.uuid4, unique=True)
    title = models.CharField(blank=True, null=True,
                             max_length=3, choices=TITLE_CHOICES)
    name = models.CharField('Full Name', blank=True, null=True, max_length=100)
    employee_number = models.IntegerField(
        'Employee Number', blank=True, null=True)
    user = models.OneToOneField(
        User, unique=True, related_name='hikaya_user',
        on_delete=models.CASCADE)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='user_workspace',
        on_delete=models.SET_NULL)
    workspaces = models.ManyToManyField(
        Workspace, verbose_name='Accessible Workspaces',
        related_name='user_workspaces', blank=True)
    privacy_disclaimer_accepted = models.BooleanField(default=False)
    history = HistoricalRecords()
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name or ''

    @property
    def workspaces_list(self):
        return ', '.join([x.name for x in self.organizations.all()])

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date is None:
            self.create_date = timezone.now()
            self.name = '{} {}'.format(
                self.user.first_name, self.user.last_name)
        self.edit_date = timezone.now()
        super(HikayaUser, self).save()


class Office(models.Model):
    """
    Office Model
    """
    office_uuid = models.UUIDField(
        'Office UUID', editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField('Office Name', max_length=255, blank=True)
    code = models.CharField('Office Code', max_length=255, blank=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='office_workspace',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='office_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By',
        related_name='office_created_by', editable=False, null=True,
        on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By',
        related_name='office_modified_by', editable=False, null=True,
        on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date is None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Office, self).save(*args, **kwargs)

    # displayed in admin templates
    def __str__(self):
        new_name = '{} - {}'.format(self.name, self.code)
        return new_name


class Sector(models.Model):
    """
    Sector Model
    """
    sector_uuid = models.UUIDField(
        'Sector UUID', editable=False, default=uuid.uuid4, unique=True)
    sector = models.CharField('Sector Name', max_length=255)
    parent_sector = models.ForeignKey(
        'self', blank=True, null=True, related_name='sub_sectors',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='sector_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='sector_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='sector_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('sector',)
        verbose_name_plural = 'Location'

    # displayed in admin templates
    def __str__(self):
        return self.sector or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Sector, self).save(*args, **kwargs)


class Contact(models.Model):
    """
    Contact Model
    """
    contact_uuid = models.UUIDField(
        'Contact UUID', editable=False,
        default=uuid.uuid4, unique=True)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField(
        'Last Name', max_length=100, blank=True, null=True)
    singular_label = models.CharField(
        'Singular Label', max_length=100, default='Contact')
    plural_label = models.CharField(
        'Plural Label', max_length=100, default='Contacts')
    email = models.CharField(
        'Email Address', max_length=100, blank=True, null=True)
    phone = models.CharField(
        'Phone Number', max_length=25, blank=True, null=True)
    street = models.CharField('City', max_length=100, null=True, blank=True)
    city = models.CharField('City', max_length=100, null=True, blank=True)
    zip_code = models.CharField(
        'Zip/Postal Code', max_length=25, null=True, blank=True)
    state = models.CharField(
        'State/Province', max_length=100, null=True, blank=True)
    country = models.CharField(
        'Country', max_length=100, null=True, blank=True)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='contact_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='contact_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='contact_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('first_name',)
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def full_address(self):
        # html string
        return '{} <br> {} {} {} <br> {}'.format(
            self.street, self.city, self.zip_code,
            self.state, self.country
        )

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Contact, self).save(*args, **kwargs)


class LocationType(models.Model):
    """
    Location Type Model
    """
    location_type_uuid = models.UUIDField(
        'Workspace Sub-Type UUID', editable=False,
        default=uuid.uuid4, unique=True)
    type = models.CharField('Location Type', max_length=100, unique=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True,
        related_name='location_type_workspace',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='location_type_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', blank=True, null=True, editable=False)
    modified_date = models.DateTimeField(
        'Edit Date', blank=True, null=True, editable=False)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='location_type_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='location_type_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Location Types'

    # displayed in admin templates
    def __str__(self):
        return '{}'.format(self.type) or ''

    def save(self, *args, **kwargs):
        # get logged user
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(LocationType, self).save(*args, **kwargs)


class AdministrativeLevel(models.Model):
    """
    Administrative IndicatorLevel Model
    """
    admin_level_uuid = models.UUIDField(
        'Admin Level UUID', editable=False, default=uuid.uuid4, unique=True)
    level_1 = models.CharField(
        'Administrative IndicatorLevel 1', max_length=100, blank=True)
    level_2 = models.CharField(
        'Administrative IndicatorLevel 2', max_length=100, blank=True)
    level_3 = models.CharField(
        'Administrative IndicatorLevel 3', max_length=100, blank=True)
    level_4 = models.CharField(
        'Administrative IndicatorLevel 4', max_length=100, blank=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='admin_level_workspace',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='admin_level_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created by', editable=False, null=True,
        related_name='admin_level_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='admin_level_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('level_1',)
        verbose_name_plural = 'Administrative Levels'

    # displayed in admin templates
    def __str__(self):
        return '{}'.format(self.level_1) or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(AdministrativeLevel, self).save(*args, **kwargs)


class Country(models.Model):
    """
    Country Model
    """
    country_uuid = models.UUIDField(
        'Country UUID', editable=False,
        default=uuid.uuid4, unique=True)
    country = models.CharField('Country Name', max_length=255,
                               blank=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, on_delete=models.SET_NULL)
    code = models.CharField('2 Letter Country Code',
                            max_length=4, blank=True)
    description = models.TextField(
        'Description/Notes', max_length=765, blank=True)
    latitude = models.CharField(
        'Latitude', max_length=255, null=True, blank=True)
    longitude = models.CharField(
        'Longitude', max_length=255, null=True, blank=True)
    zoom = models.IntegerField('Zoom', default=5)
    history = HistoricalRecords()
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created by', blank=True, editable=False, null=True,
        related_name='country_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='country_modified_by', on_delete=models.SET_NULL)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('country',)
        verbose_name_plural = 'Countries'

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Country, self).save(*args, **kwargs)

    # displayed in admin templates
    def __str__(self):
        return '{}'.format(self.country) or ''


class Location(models.Model):
    """
    Location (Site) Model
    """
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'Inactive'))
    location_uuid = models.UUIDField(
        'Location UUID', editable=False,
        default=uuid.uuid4, unique=True)
    name = models.CharField('Site Name', max_length=100)
    parent_location = models.ForeignKey(
        'self', null=True, blank=True, related_name='sub_locations',
        on_delete=models.SET_NULL)
    contact = models.ForeignKey(
        Contact, null=True, blank=True, verbose_name='Location Contact',
        on_delete=models.SET_NULL)
    status = models.CharField(
        'Location Status', blank=True,
        max_length=100, choices=STATUS_CHOICES, default='active')
    country = models.ForeignKey(
        Country, verbose_name='Country of Location', null=True, blank=True,
        on_delete=models.CASCADE)
    office = models.ForeignKey(
        Office, null=True, blank=True, verbose_name='Location Office',
        on_delete=models.SET_NULL)
    type = models.ForeignKey(
        LocationType, null=True, blank=True, verbose_name='Location Type',
        on_delete=models.SET_NULL)
    admin_level = models.ForeignKey(
        AdministrativeLevel, verbose_name='Administrative Levels', null=True,
        blank=True, on_delete=models.SET_NULL)
    latitude = models.DecimalField(
        'Latitude Coordinates', decimal_places=16, max_digits=25,
        default=Decimal('0.00'))
    longitude = models.DecimalField(
        'Longitude Coordinates', decimal_places=16, max_digits=25,
        default=Decimal('0.00'))
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True,
        related_name='location_workspace', on_delete=models.SET_NULL)
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created by', blank=True, editable=False,
        null=True, related_name='location_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='location_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sites'

    # displayed in admin templates
    def __str__(self):
        return '{}'.format(self.name) or ''

    # on save add create date or update edit date
    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Location, self).save(*args, **kwargs)


class Portfolio(models.Model):
    """
    Portfolio Model
    This acts like a folder for user data
    """
    portfolio_uuid = models.UUIDField(
        'Portfolio UUID', editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField('Portfolio Name', max_length=100, unique=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='portfolio_workspace',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='portfolio_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', null=True, editable=False)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, editable=False)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created Vy', editable=False, null=True,
        related_name='portfolio_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='portfolio_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return '{}'.format(self.name) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Portfolio, self).save(*args, **kwargs)


class Currency(models.Model):
    """
    Currency Model
    """
    currency_uuid = models.UUIDField(
        'Currency UUID', editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField('Currency Name', max_length=255)
    symbol = models.CharField('Currency Symbol', max_length=10, blank=True)
    code = models.CharField('Currency Code', max_length=20, blank=True)
    workspace = models.ForeignKey(
        Workspace, blank=True, null=True, related_name='currency_workspace',
        on_delete=models.SET_NULL)
    account = models.ForeignKey(
        Account, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='currency_account')
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', null=True, editable=False)
    modified_date = models.DateTimeField(
        'Modified Date', null=True, editable=False)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created Vy', editable=False, null=True,
        related_name='currency_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='currency_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Currencies'

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name) or ''


class FundingStatus(models.Model):
    """
    Funding Status Model
    Tracking Workflow IndicatorLevel 1 funding status
    """
    funding_status_uuid = models.UUIDField(
        'Funding Status UUID', editable=False, default=uuid.uuid4, unique=True)
    status = models.CharField('Funding Status', max_length=165)
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', blank=True, null=True)
    modified_date = models.DateTimeField('Modified Date', blank=True, null=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='fund_status_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='fund_status_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Funding Statuses'

    def __str__(self):
        return '{}'.format(self.status) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(FundingStatus, self).save(*args, **kwargs)


class WorkflowStatus(models.Model):
    """
    Workflow Status Model
    TODO - create migrations to add the default values
    (Open, Awaiting approval, Tracking, Closed, Rejected)
    """
    status_uuid = models.UUIDField(
        'Workflow Status UUID', editable=False, default=uuid.uuid4, unique=True)
    status = models.CharField('Workflow Status', max_length=100)
    create_date = models.DateTimeField(
        'Create Date', null=True, blank=True, editable=False)
    history = HistoricalRecords()
    modified_date = models.DateTimeField(
        'Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='wfl_status_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='wfl_status_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Workflow Statuses'

    def __str__(self):
        return '{}'.format(self.status) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowStatus, self).save(*args, **kwargs)


class WorkflowLevel1Type(models.Model):
    """
    Workflow IndicatorLevel 1 Type Model
    These are Workflow IndicatorLevel 1 categories
    """
    type_uuid = models.UUIDField(
        'Workflow IndicatorLevel 1 Type UUID', editable=False,
        default=uuid.uuid4, unique=True)
    type = models.CharField(
        'Workflow IndicatorLevel 1 Type', max_length=100, unique=True)
    create_date = models.DateTimeField('Create Date', blank=True, null=True)
    history = HistoricalRecords()
    modified_date = models.DateTimeField('Modified Date', blank=True, null=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='wfl1_type_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='wfl1_type_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Workflow Level1 Types'

    def __str__(self):
        return '{}'.format(self.type) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowLevel1Type, self).save(*args, **kwargs)


class WorkflowLevel1(models.Model):
    """
    Workflow Level 1 model (top level workflow model)
    """
    workflow_level1_uuid = models.UUIDField(
        'Workflow Level 1 UUID', editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(
        'Workflow Level 1 Name', max_length=255,)
    workflow_level1_code = models.CharField(
        'Workflow Level 1 Code', max_length=100, blank=True, null=True)
    description = models.TextField(
        'Workflow Level 1 Description', max_length=765, blank=True, null=True)
    start_date = models.DateTimeField('Start Date', null=True, blank=True)
    end_date = models.DateTimeField('End Date', null=True, blank=True)
    workflow_level1_type = models.ForeignKey(
        WorkflowLevel1Type, verbose_name='Workflow Level 1 Type', blank=True, null=True,
        on_delete=models.SET_NULL)
    workflow_status = models.ForeignKey(
        WorkflowStatus, max_length=100, verbose_name='Workflow Status', null=True,
        blank=True,  on_delete=models.SET_NULL)
    sector = models.ManyToManyField(
        Sector, blank=True, help_text='Workflow Level 1 sectors')
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    portfolio = models.ForeignKey(
        Portfolio, blank=True, null=True, on_delete=models.CASCADE)
    funding_status = models.ForeignKey(
        FundingStatus, verbose_name='Funding Status', blank=True, null=True,
        on_delete=models.SET_NULL)
    history = HistoricalRecords()
    create_date = models.DateTimeField('Create Date', null=True, blank=True, editable=False)
    edit_date = models.DateTimeField('Edit Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True, blank=True,
        related_name='wfl1_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True, blank=True,
        related_name='wfl1_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'WorkflowLevel 1s'

    def __str__(self):
        return '{}'.format(self.name) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowLevel1, self).save(*args, **kwargs)


class Approval(models.Model):
    """
    Approval Model
    """
    approval_uuid = models.UUIDField(
        'Approval UUID', editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField('Approval Name', max_length=165)
    description = models.TextField(
        'Approval Description', blank=True, max_length=765)
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', null=True, blank=True, editable=False)
    modified_date = models.DateTimeField('Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='approval_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='approval_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Approvals'

    def __str__(self):
        return '{}'.format(self.name) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Approval, self).save(*args, **kwargs)


class WorkflowLevel2Type(models.Model):
    """
    Workflow IndicatorLevel 2 Type Model
    These are Workflow IndicatorLevel 2 categories
    """
    type_uuid = models.UUIDField(
        'Workflow IndicatorLevel 2 Type UUID', editable=False,
        default=uuid.uuid4, unique=True)
    type = models.CharField(
        'Workflow IndicatorLevel 2 Type', max_length=100, unique=True)
    create_date = models.DateTimeField('Create Date', blank=True, null=True)
    history = HistoricalRecords()
    modified_date = models.DateTimeField('Modified Date', blank=True, null=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='level2_type_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='level2_type_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('create_date',)
        verbose_name_plural = 'Workflow Level2 Types'

    def __str__(self):
        return '{}'.format(self.type) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowLevel2Type, self).save(*args, **kwargs)


class WorkflowLevel2(models.Model):
    """
    workflow Level2 or 3 or 4 model
    Workflow Level3s have self relationship with WFL2s
    """
    workflow_level2_uuid = models.UUIDField(
        'Workflow Level 2/3 UUID', editable=False, default=uuid.uuid4,
        unique=True)
    name = models.CharField('Workflow IndicatorLevel 2/3 Name', max_length=255)
    description = models.TextField(
        'Workflow Level 2/3 Description', max_length=765, null=True, blank=True)
    workflow_level2_code = models.CharField(
        'Workflow Level2 Code', blank=True, null=True, max_length=100)
    start_date = models.DateTimeField('Start Date', null=True, blank=True)
    end_date = models.DateTimeField('End Date', null=True, blank=True)
    workflow_status = models.ForeignKey(
        WorkflowStatus, max_length=100, verbose_name='Workflow Status', null=True,
        blank=True, on_delete=models.SET_NULL)
    workflow_level1 = models.ForeignKey(WorkflowLevel1, on_delete=models.CASCADE)
    workflow_level2_type = models.ForeignKey(
        WorkflowLevel2Type, verbose_name='Workflow Level 2 Type', null=True,
        blank=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='workflow_level3s',
        on_delete=models.SET_NULL)
    office_location = models.ForeignKey(
        Office, null=True, blank=True, verbose_name='Office Location Tag',
        on_delete=models.SET_NULL)
    implementation_location = models.ForeignKey(
        Location, verbose_name='Implementation Location Tag', null=True, blank=True,
        on_delete=models.SET_NULL)
    staff_responsible = models.ForeignKey(
        Contact, verbose_name='Staff Responsible', blank=True, null=True,
        on_delete=models.SET_NULL)
    workflow_sector = models.ManyToManyField(
        Sector, verbose_name='Workflow Sector Tag', related_name='workflow_sectors',
        blank=True)
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', null=True, blank=True, editable=False)
    modified_date = models.DateTimeField('Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='wfl2_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='wfl2_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Workflow Level 2/3s'

    def __str__(self):
        return '{}'.format(self.name) or ''

    def save(self, *args, **kwargs):
        # get logged user
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowLevel2, self).save(*args, **kwargs)


class WorkflowLevel2Plan(models.Model):
    """
    Workflow Level2 Plan Model
    A Junction Table for workflow Level1 and Level2
    """
    workflow_level2_plan_uuid = models.UUIDField(
        'Workflow Level2 Plan UUID', editable=False, default=uuid.uuid4,
        unique=True)
    name = models.CharField('Workflow Level2 Plan  Name', max_length=150)
    description = models.TextField(
        'Workflow Level2 Plan Description', max_length=765, null=True, blank=True)
    workflow_level1 = models.ForeignKey(
        WorkflowLevel1, verbose_name='Workflow Level 1',
        on_delete=models.CASCADE)
    workflow_level2 = models.ForeignKey(
        WorkflowLevel2, verbose_name='Workflow Level 2',
        on_delete=models.CASCADE)
    history = HistoricalRecords()
    create_date = models.DateTimeField(
        'Create Date', null=True, blank=True, editable=False)
    modified_date = models.DateTimeField('Modified Date', null=True, blank=True)
    created_by = models.ForeignKey(
        HikayaUser, verbose_name='Created By', editable=False, null=True,
        related_name='wfl2_plan_created_by', on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(
        HikayaUser, verbose_name='Modified By', editable=False, null=True,
        related_name='wfl2_plan_modified_by', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Workflow Level 2 Plans'

    def __str__(self):
        return '{}'.format(self.name) or ''

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified_date = timezone.now()
        return super(WorkflowLevel2Plan, self).save(*args, **kwargs)

