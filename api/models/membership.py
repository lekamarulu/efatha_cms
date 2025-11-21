# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models

from api.models.lookup import Branch, Position, Department, LeadershipRole, Ministry, EducationLevel, Institution, \
    OccupationType


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_ref = models.CharField(unique=True, max_length=30)
    system_reg_no = models.CharField(unique=True, max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    # middle_name = models.CharField(max_length=100, blank=True, null=True)
    # last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    country_of_birth = models.CharField(max_length=100, blank=True, null=True)
    region_of_birth = models.CharField(max_length=100, blank=True, null=True)
    district_of_birth = models.CharField(max_length=100, blank=True, null=True)
    marital_status_id = models.UUIDField(blank=True, null=True)
    num_child = models.IntegerField(blank=True, null=True)
    num_dependant = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_salvation = models.DateField(blank=True, null=True)
    completed_growth_class = models.BooleanField(blank=True, null=True)
    growth_class_level = models.CharField(max_length=100, blank=True, null=True)
    water_baptised = models.BooleanField(blank=True, null=True)
    date_of_water_baptism = models.DateField(blank=True, null=True)
    holy_spirit_baptised = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member'


class MemberBranch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # member_ref = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_ref', to_field='member_ref', related_name='memberbranch_member_ref_set')
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, models.DO_NOTHING,db_column='branch_id')
    branch_ref = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    church_zone = models.CharField(max_length=50, blank=True, null=True)
    church_cell = models.CharField(max_length=50, blank=True, null=True)
    street_residence = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    residence_detail = models.TextField(blank=True, null=True)
    housing_status_id = models.UUIDField(blank=True, null=True)
    postal_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_branch'
        unique_together = (('member', 'branch'),)


class MemberBranchChurchPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, models.DO_NOTHING,db_column='branch_id')
    branch_ref = models.CharField(max_length=30)
    position = models.ForeignKey(Position, models.DO_NOTHING,db_column='position_id')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_branch_church_position'
        unique_together = (('member', 'branch', 'position', 'start_date'),)


class MemberBranchDepartmentLeadership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, models.DO_NOTHING,db_column='branch_id')
    branch_ref = models.CharField(max_length=30)
    # member_ref = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_ref', to_field='member_ref', related_name='memberbranchdepartmentleadership_member_ref_set')
    department = models.ForeignKey(Department, models.DO_NOTHING,db_column='department_id')
    department_ref = models.CharField(max_length=30)
    leadership_role = models.ForeignKey(LeadershipRole, models.DO_NOTHING,db_column='leadership_role_id')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    appointed_by = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_branch_department_leadership'
        unique_together = (('branch', 'member', 'department', 'leadership_role', 'start_date'),)


class MemberBranchMinistry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, models.DO_NOTHING,db_column='branch_id')
    branch_ref = models.CharField(max_length=30)
    ministry = models.ForeignKey(Ministry, models.DO_NOTHING,db_column='ministry_id')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_branch_ministry'
        unique_together = (('member', 'branch', 'ministry', 'start_date'),)


class MemberEducation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    education_level= models.ForeignKey(EducationLevel, models.DO_NOTHING,db_column='level_id')
    level_ref = models.CharField(max_length=20)
    institution= models.ForeignKey(Institution, models.DO_NOTHING,db_column='institution_id')
    institution_ref = models.CharField(max_length=30, blank=True, null=True)
    certificate = models.BinaryField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_education'
        unique_together = (('member', 'education_level'),)


class MemberOccupation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, models.DO_NOTHING,db_column='member_id')
    member_ref = models.CharField(max_length=30)
    occupation_type = models.ForeignKey(OccupationType, models.DO_NOTHING,db_column='occupation_type_id')
    company_name = models.CharField(max_length=150, blank=True, null=True)
    specialisation = models.CharField(max_length=100, blank=True, null=True)
    type_of_work = models.CharField(max_length=100, blank=True, null=True)
    type_of_business = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"membership".member_occupation'
        unique_together = (('member', 'occupation_type'),)
