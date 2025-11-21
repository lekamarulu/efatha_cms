# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models

from api.models.lookup import Branch


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_ref = models.CharField(unique=True, max_length=50)
    name_lang1 = models.CharField(max_length=200, blank=True, null=True)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'

class AssetCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_code = models.CharField(unique=True, max_length=4)
    name_lang1 = models.CharField(max_length=200)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_category'


class AssetSubcategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_category = models.ForeignKey(AssetCategory, models.DO_NOTHING, db_column='asset_category_id')
    # asset_category = models.ForeignKey(AssetCategory, models.DO_NOTHING, db_column='category_code', to_field='category_code')
    category_code = models.CharField(max_length=4)
    subcategory_code = models.CharField(max_length=4)
    name_lang1 = models.CharField(max_length=200)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_subcategory'
        unique_together = (('asset_category', 'subcategory_code'),)


class AssetIndex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_code = models.CharField(max_length=4)
    asset_subcategory = models.ForeignKey(AssetSubcategory, models.DO_NOTHING, db_column='asset_subcategory_id')
    subcategory_code = models.CharField(max_length=4)
    code = models.CharField(unique=True, max_length=8)
    name_lang1 = models.CharField(max_length=200)
    name_lang2 = models.CharField(max_length=200, blank=True, null=True)
    has_serial_no = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_index'
        unique_together = (('asset_subcategory','code'),)


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, models.DO_NOTHING,db_column='branch_id')
    branch_ref = models.CharField(max_length=30)
    asset_index = models.ForeignKey(AssetIndex, models.DO_NOTHING, db_column='asset_index_id')
    asset_index_code = models.CharField(max_length=8)
    asset_code = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=80, blank=True, null=True)
    oem = models.CharField(max_length=30, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    in_service_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'


class AssetLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # asset_code = models.ForeignKey(Asset, models.DO_NOTHING, db_column='asset_code', to_field='asset_code')
    asset = models.ForeignKey(Asset, models.DO_NOTHING,db_column='asset_id')
    asset_index_code = models.CharField(max_length=8)
    location_ref = models.ForeignKey(Location, models.DO_NOTHING, db_column='location_ref', to_field='location_ref')
    assigned_date = models.DateField(blank=True, null=True)
    released_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_location'


class AssetMovement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, models.DO_NOTHING, db_column='asset_id')
    # asset_code = models.ForeignKey(Asset, models.DO_NOTHING, db_column='asset_code', to_field='asset_code')
    from_location_ref = models.CharField(max_length=50, blank=True, null=True)
    to_location_ref = models.CharField(max_length=50, blank=True, null=True)
    movement_date = models.DateField()
    movement_type = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_movement'
        unique_together = (('asset','from_location_ref','movement_date'),)
