# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models

class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    region_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=150, blank=True, null=True)
    name_lang2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'region'
        ordering = ['-id']
        

class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=150)
    region = models.ForeignKey(Region, models.DO_NOTHING)
    region_ref = models.CharField(max_length=30)
    # region_ref = models.ForeignKey(Region, models.DO_NOTHING, db_column='region_ref', to_field='region_ref', related_name='branch_region_ref_set')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    photo_date_updated = models.DateTimeField(blank=True, null=True)
    is_collection = models.BooleanField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'branch'
        ordering = ['-id']


class BranchCell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    branch_ref = models.CharField(max_length=30)
    # branch_ref = models.ForeignKey(Branch, models.DO_NOTHING, db_column='branch_ref', to_field='branch_ref', related_name='branchcell_branch_ref_set')
    cell_id = models.CharField(max_length=50)
    name_lang1 = models.CharField(max_length=150)

    class Meta:
        # managed = False
        db_table = 'branch_cell'
        unique_together = (('branch', 'cell_id'),)
        ordering = ['-id']


    def save(self, *args, **kwargs):
        # Auto-update branch from project if not manually set
        if self.branch_ref:
            branch = Branch.objects.get(branch_ref=self.branch_ref)
            self.branch = branch
        super().save(*args, **kwargs)

class DefaultInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    church_abbr = models.CharField(max_length=15, blank=True, null=True)
    church_name = models.CharField(max_length=200, blank=True, null=True)
    collection_branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    branch_ref = models.CharField(max_length=30)
    # collection_branch_ref = models.ForeignKey(Branch, models.DO_NOTHING, db_column='collection_branch_ref', to_field='branch_ref', related_name='defaultinfo_collection_branch_ref_set', blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    vision = models.CharField(max_length=1000, blank=True, null=True)
    mission = models.CharField(max_length=1000, blank=True, null=True)
    initial_voucher_no = models.IntegerField(blank=True, null=True)
    initial_pcv = models.IntegerField(blank=True, null=True)
    initial_receipt_no = models.IntegerField(blank=True, null=True)
    petty_cash_account = models.CharField(max_length=10, blank=True, null=True)
    main_cash_account_local = models.CharField(max_length=10, blank=True, null=True)
    main_cash_account_usd = models.CharField(max_length=15, blank=True, null=True)
    zaka_label = models.CharField(max_length=255, blank=True, null=True)
    zaka_code = models.CharField(max_length=10, blank=True, null=True)
    system_currency = models.CharField(max_length=3, blank=True, null=True)
    default_year = models.CharField(max_length=4, blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    show_details = models.BooleanField()

    class Meta:
        # managed = False
        db_table = 'default_info'
        ordering = ['-id']


class Denomination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    denomination_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=150, blank=True, null=True)
    name_lang2 = models.CharField(max_length=150, blank=True, null=True)
    is_christian = models.BooleanField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'denomination'
        ordering = ['-id']


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=150, blank=True, null=True)
    name_lang2 = models.CharField(max_length=150, blank=True, null=True)
    leadership_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'department'
        ordering = ['-id']


class EducationLevel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level_ref = models.CharField(unique=True, max_length=20)
    name_lang1 = models.CharField(max_length=50)
    name_lang2 = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'education_level'
        ordering = ['-id']


class HousingStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=50)
    name_lang2 = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'housing_status'
        ordering = ['-id']


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=200)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'institution'
        ordering = ['-id']


class LeadershipRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=50)
    name_lang2 = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'leadership_role'
        ordering = ['-id']


class MaritalStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=50)
    name_lang2 = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'marital_status'
        ordering = ['-id']


class MembershipLevel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=30)
    name_lang2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'membership_level'
        ordering = ['-id']


class Ministry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=30)
    name_lang2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ministry'
        ordering = ['-id']


class OccupationType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=50)
    name_lang2 = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'occupation_type'
        ordering = ['-id']


class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=200)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'position'
        ordering = ['-id']


class Religion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    religion_ref = models.CharField(unique=True, max_length=30)
    name_lang1 = models.CharField(max_length=150, blank=True, null=True)
    name_lang2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'religion'
        ordering = ['-id']


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_lang1 = models.CharField(unique=True, max_length=100)
    name_lang2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'skill'
        ordering = ['-id']



class Currency(models.Model):
    currency_ref = models.CharField(primary_key=True, max_length=3)
    name_lang1 = models.CharField(max_length=100, blank=True, null=True)
    name_lang2 = models.CharField(max_length=100, blank=True, null=True)
    is_local = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'currency'
        ordering = ['-currency_ref']
