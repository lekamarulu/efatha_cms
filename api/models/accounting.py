# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from api.models import Member
from api.models.lookup import Currency, Branch, Department


class FinancialYear(models.Model):
    fin_year = models.CharField(primary_key=True, max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField()
    is_closed = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_year'


class PaymentMethod(models.Model):
    pay_method = models.CharField(primary_key=True, max_length=20)
    name_lang1 = models.CharField(max_length=50)
    name_lang2 = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    is_cash = models.BooleanField()
    is_bank = models.BooleanField()
    is_mobile = models.BooleanField()
    is_electronic = models.BooleanField()
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method'

class AccountCategory(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    crdr = models.CharField(max_length=2, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_category'



class AccountSubcategory(models.Model):
    code = models.IntegerField(primary_key=True)
    category_code = models.ForeignKey(AccountCategory, models.DO_NOTHING, db_column='category_code',to_field='code')
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_subcategory'



class ProfitCostCenter(models.Model):
    id = models.UUIDField(primary_key=True)
    center_code = models.CharField(unique=True, max_length=15, blank=True, null=True)
    name_lang1 = models.CharField(max_length=100, blank=True, null=True)
    name_lang2 = models.CharField(max_length=100, blank=True, null=True)
    description1 = models.CharField(max_length=200, blank=True, null=True)
    description2 = models.CharField(max_length=200, blank=True, null=True)
    center_type = models.CharField(max_length=10, blank=True, null=True)
    include_in_overall = models.BooleanField()
    distribute = models.BooleanField()
    has_envelop = models.BooleanField()
    is_tithe = models.BooleanField()
    is_transfer = models.BooleanField()
    revenue_expenditure_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profit_cost_center'


class Account(models.Model):
    id = models.UUIDField(primary_key=True)
    account_code = models.CharField(unique=True, max_length=15)
    account_name = models.CharField(max_length=100)
    parent_account = models.CharField(max_length=15, blank=True, null=True)
    account_level = models.IntegerField(blank=True, null=True)
    category_code = models.ForeignKey(AccountCategory, models.DO_NOTHING, db_column='category_code', blank=True, null=True)
    account_subcategory_code = models.ForeignKey(AccountSubcategory, models.DO_NOTHING, db_column='account_subcategory_code', blank=True, null=True)
    crdr = models.CharField(max_length=2)
    currency_ref = models.CharField(max_length=3, blank=True, null=True)
    # currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='currency_ref', blank=True, null=True)
    center_code = models.ForeignKey(ProfitCostCenter, models.DO_NOTHING, db_column='center_code', to_field='center_code', blank=True, null=True)
    opening_balance = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    is_cash_bank = models.BooleanField()
    show_in_chart_of_accounts = models.BooleanField()
    blocked = models.BooleanField()
    has_transactions = models.BooleanField()
    description = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class AccountBalance(models.Model):
    id = models.UUIDField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    account_ref = models.CharField(db_column='account_code',max_length=15)
    fin_year = models.CharField(max_length=10)
    # financialyear = models.ForeignKey(FinancialYear, models.DO_NOTHING, db_column='fin_year', blank=True, null=True)
    opening_balance = models.FloatField()
    running_balance = models.FloatField()
    closing_balance = models.FloatField()
    last_updated = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_balance'
        unique_together = (('branch', 'account', 'fin_year'),)

class AccountJournalDetail(models.Model):
    id = models.UUIDField(primary_key=True)
    journal_id = models.UUIDField(blank=True, null=True)
    line_no = models.IntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    account_ref = models.CharField(db_column='account_code',max_length=15)
    fin_year = models.CharField(max_length=10)
    # fin_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='fin_year', blank=True, null=True)
    dr_amount = models.FloatField()
    cr_amount = models.FloatField()
    currency_ref = models.CharField(max_length=3, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_detail'
        unique_together = (('journal_id', 'line_no'),)


class AccountJournalHeader(models.Model):
    id = models.UUIDField(primary_key=True)
    journal_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    journal_date = models.DateField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    fin_year = models.CharField(max_length=10)
    # fin_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='fin_year', blank=True, null=True)
    journal_type = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_header'

class AccountingDonor(models.Model):
    id = models.UUIDField(primary_key=True)
    # branch = models.ForeignKey(Branch, models.DO_NOTHING)
    donor_type = models.CharField(max_length=15, blank=False, null=False)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_donor'


class AccountingProject(models.Model):
    id = models.UUIDField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    project_code = models.CharField(unique=True, max_length=15, blank=True, null=True)
    project_name = models.CharField(max_length=150, blank=True, null=True)
    project_description = models.CharField(max_length=255, blank=True, null=True)
    center = models.ForeignKey(ProfitCostCenter, models.DO_NOTHING, blank=True, null=True)
    income_account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    target_amount = models.FloatField(blank=True, null=True)
    total_pledged = models.FloatField(blank=True, null=True)
    total_collected = models.FloatField(blank=True, null=True)
    is_open = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_project'


class AccountingPledge(models.Model):
    id = models.UUIDField(primary_key=True)
    project = models.ForeignKey(AccountingProject, models.DO_NOTHING, blank=True, null=True)
    donor = models.ForeignKey(AccountingDonor, models.DO_NOTHING, blank=True, null=True)
    income_account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    pledge_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    pledge_description = models.CharField(max_length=255, blank=True, null=True)
    pledge_amount = models.FloatField()
    paid_amount = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    pledge_date = models.DateField(blank=True, null=True)
    currency_ref = models.CharField(max_length=3, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_pledge'
        unique_together = (('donor', 'project'),)

    def save(self, *args, **kwargs):
        # Auto-update branch from project if not manually set
        if self.project and self.project.branch:
            self.branch = self.project.branch
        super().save(*args, **kwargs)


class CenterAnnualForecast(models.Model):
    id = models.UUIDField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    center = models.ForeignKey(ProfitCostCenter, models.DO_NOTHING, blank=True, null=True)
    center_type = models.CharField(max_length=10, blank=True, null=True)
    fin_year = models.CharField(max_length=10)
    # fin_year = models.ForeignKey('FinancialYear', models.DO_NOTHING, db_column='fin_year', blank=True, null=True)
    forecast_amount = models.FloatField()
    remarks = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'center_annual_forecast'
        unique_together = (('branch', 'center', 'fin_year'),)


class IncomeAccountShares(models.Model):
    id = models.UUIDField(primary_key=True)
    center_code = models.ForeignKey(ProfitCostCenter, models.DO_NOTHING, db_column='center_code', to_field='center_code', blank=True, null=True)
    account_code = models.CharField(max_length=25, blank=True, null=True)
    share_percent = models.FloatField()
    description = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income_account_shares'
        unique_together = (('center_code', 'account_code'),)


class JournalHeader(models.Model):
    id = models.UUIDField(primary_key=True)
    journal_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    journal_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_header'

class JournalDetail(models.Model):
    id = models.UUIDField(primary_key=True)
    journal = models.ForeignKey(JournalHeader, models.DO_NOTHING, db_column='journal_id',blank=True, null=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    dr_amount = models.FloatField(blank=True, null=True)
    cr_amount = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_detail'


class Receipt(models.Model):
    id = models.UUIDField(primary_key=True)
    receipt_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    receipt_date = models.DateField(blank=True, null=True)
    receipt_type = models.CharField(max_length=25, blank=True, null=True)
    service_id = models.SmallIntegerField(blank=True, null=True)
    # member_id = models.UUIDField(blank=True, null=True)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    donor = models.ForeignKey(AccountingDonor, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(AccountingProject, models.DO_NOTHING, blank=True, null=True)
    pledge = models.ForeignKey(AccountingPledge, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department_id',blank=True, null=True)
    asset_account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    income_account = models.ForeignKey(Account, models.DO_NOTHING, related_name='receipt_income_account_set', blank=True, null=True)
    amount = models.FloatField()
    currency_ref = models.CharField(max_length=3, blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # pay_method = models.CharField(max_length=20, blank=True, null=True)
    # payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, db_column='pay_method',blank=True, null=True)
    payment_method = models.CharField(db_column='pay_method',blank=True, null=True, max_length=20)
    pay_reference = models.CharField(max_length=50, blank=True, null=True)
    sender_number = models.CharField(max_length=25, blank=True, null=True)
    bank_id = models.CharField(max_length=10, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt'


class ReceiptAttachment(models.Model):
    id = models.UUIDField(primary_key=True)
    receipt = models.ForeignKey(Receipt, models.DO_NOTHING)
    file_data = models.BinaryField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    mime_type = models.CharField(max_length=100, blank=True, null=True)
    uploaded_by = models.CharField(max_length=50, blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt_attachment'
