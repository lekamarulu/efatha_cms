from rest_framework import serializers
from .models import (
    Region, Branch, BranchCell, DefaultInfo, Denomination, Department,
    EducationLevel, HousingStatus, Institution, LeadershipRole, MaritalStatus,
    MembershipLevel, Ministry, OccupationType, Position, Religion, Skill
)

from .models import (
    Member,
    MemberBranch,
    MemberBranchChurchPosition,
    MemberBranchDepartmentLeadership,
    MemberBranchMinistry,
    MemberEducation,
    MemberOccupation
)

from .models import (
    Location,
    AssetCategory,
    AssetSubcategory,
    AssetIndex,
    Asset,
    AssetLocation,
    AssetMovement,
)

from .models import (
    FinancialYear, PaymentMethod, AccountCategory, AccountSubcategory,
    ProfitCostCenter, Account, AccountBalance, AccountJournalDetail,
    AccountJournalHeader, AccountingDonor, AccountingProject, AccountingPledge,
    CenterAnnualForecast, IncomeAccountShares, JournalHeader, JournalDetail,
    Receipt, ReceiptAttachment
)


class RefResolverMixin:
    """
    Resolves *_ref fields for models with UUID-based foreign keys,
    even when the model itself doesn’t physically store the *_ref field.
    """
    ref_map = {}

    def resolve_refs(self, validated_data):
        for ref_field, (model, lookup_field, target_field) in self.ref_map.items():
            ref_value = validated_data.pop(ref_field, None)
            if not ref_value:
                continue

            instance = model.objects.filter(**{lookup_field: ref_value}).first()
            if not instance:
                raise serializers.ValidationError({
                    ref_field: f"{model.__name__} with {lookup_field}='{ref_value}' not found."
                })
            validated_data[target_field] = instance
        return validated_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for ref_field, (model, lookup_field, target_field) in self.ref_map.items():
            related_obj = getattr(instance, target_field, None)
            if related_obj:
                data[ref_field] = getattr(related_obj, lookup_field, None)
        return data

    def create(self, validated_data):
        validated_data = self.resolve_refs(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.resolve_refs(validated_data)
        return super().update(instance, validated_data)


# ----------------------------------------------------------------------
# FUNCTION: Create serializer based on UUID FK presence
# ----------------------------------------------------------------------
def create_serializer(model, ref_map=None):
    ref_map = ref_map or {}

    has_uuid_fk = any(
        isinstance(f, models.ForeignKey) and isinstance(f.target_field, models.UUIDField)
        for f in model._meta.fields if isinstance(f, models.ForeignKey)
    )

    base_classes = (serializers.ModelSerializer,)
    if has_uuid_fk:
        base_classes = (RefResolverMixin, serializers.ModelSerializer)

    class AutoSerializer(*base_classes):
        class Meta:
            model = model
            exclude = tuple(
                f.name for f in model._meta.fields
                if f.name in ('created_at', 'updated_at', 'posted_at', 'uploaded_at')
            )

        if has_uuid_fk:
            ref_map = ref_map

    return AutoSerializer


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_ref', 'name_lang1', 'name_lang2')


class BranchSerializer(RefResolverMixin, serializers.ModelSerializer):
    # Use the mapping to automatically link region_ref → region
    ref_map = {
        'region_ref': (Region, 'region_ref', 'region'),
    }

    class Meta:
        model = Branch
        fields = (
            'branch_ref',
            'name_lang1',
            'region_ref',  # user provides this
            'latitude',
            'longitude',
            'photo',
            'photo_date_updated',
            'is_collection',
            # 'date_created',
        )


class BranchCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchCell
        fields = ('branch_ref', 'cell_id', 'name_lang1')


class DefaultInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultInfo
        fields = (
            'collection_branch_id',
            'branch_ref',
            'church_abbr',
            'church_name',
            'logo',
            'vision',
            'mission',
            'initial_voucher_no',
            'initial_pcv',
            'initial_receipt_no',
            'petty_cash_account',
            'main_cash_account_local',
            'main_cash_account_usd',
            'zaka_label',
            'zaka_code',
            'system_currency',
            'default_year',
            'language_id',
            'show_details',
        )


class DenominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denomination
        fields = ('denomination_ref', 'name_lang1', 'name_lang2', 'is_christian')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_ref', 'name_lang1', 'name_lang2', 'leadership_type')


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('level_ref', 'name_lang1', 'name_lang2')


class HousingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingStatus
        fields = ('name_lang1', 'name_lang2')


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('institution_ref', 'name_lang1', 'name_lang2')


class LeadershipRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipRole
        fields = ('name_lang1', 'name_lang2')


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ('name_lang1', 'name_lang2')


class MembershipLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipLevel
        fields = ('name_lang1', 'name_lang2')


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('name_lang1', 'name_lang2')


class OccupationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OccupationType
        fields = ('name_lang1', 'name_lang2')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('name_lang1', 'name_lang2')


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ('religion_ref', 'name_lang1', 'name_lang2')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name_lang1', 'name_lang2')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'member_ref', 'system_reg_no', 'full_name', 'gender',
            'date_of_birth', 'country_of_birth', 'region_of_birth', 'district_of_birth',
            'marital_status_id', 'num_child', 'num_dependant',
            'email', 'phone_number', 'date_of_salvation', 'completed_growth_class',
            'growth_class_level', 'water_baptised', 'date_of_water_baptism',
            'holy_spirit_baptised'
        )


class MemberBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberBranch
        fields = (
            'member_ref', 'branch_ref', 'start_date', 'end_date',
            'church_zone', 'church_cell', 'street_residence', 'house_number',
            'residence_detail', 'housing_status_id', 'postal_address'
        )


class MemberBranchChurchPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberBranchChurchPosition
        fields = (
            'member_ref', 'branch_ref', 'position', 'start_date', 'end_date', 'is_active'
        )


class MemberBranchDepartmentLeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberBranchDepartmentLeadership
        fields = (
            'member_ref', 'branch_ref', 'department', 'department_ref',
            'leadership_role', 'start_date', 'end_date', 'is_active',
            'vote_count', 'appointed_by', 'created_at', 'updated_at'
        )


class MemberBranchMinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberBranchMinistry
        fields = (
            'member_ref', 'branch_ref', 'ministry', 'start_date', 'end_date',
            'created_at', 'updated_at'
        )


class MemberEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberEducation
        fields = (
            'member_ref', 'level_ref', 'institution_ref', 'certificate',
            'status', 'created_at', 'updated_at'
        )


class MemberOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberOccupation
        fields = (
            'member_ref', 'occupation_type', 'company_name', 'specialisation',
            'type_of_work', 'type_of_business', 'created_at', 'updated_at'
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'location_ref',
            'name_lang1',
            'name_lang2',
            'created_at',
            'updated_at',
        )


class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = (
            'category_code',
            'name_lang1',
            'name_lang2',
        )


class AssetSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSubcategory
        fields = (
            'asset_category',  # FK UUID reference
            'category_code',
            'subcategory_code',
            'name_lang1',
            'name_lang2',
        )


class AssetIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetIndex
        fields = (
            'category_code',
            'asset_subcategory',  # FK UUID reference
            'subcategory_code',
            'code',
            'name_lang1',
            'name_lang2',
            'has_serial_no',
        )


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = (
            'branch',  # FK UUID reference
            'branch_ref',
            'asset_index',  # FK UUID reference
            'asset_index_code',
            'asset_code',
            'description',
            'serial_no',
            'model',
            'oem',
            'purchase_date',
            'purchase_amount',
            'in_service_date',
            'status',
            'created_at',
            'updated_at',
        )


class AssetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLocation
        fields = (
            'asset',  # FK UUID reference
            'asset_index_code',
            'location_ref',  # FK to Location via ref
            'assigned_date',
            'released_date',
            'created_at',
            'updated_at',
        )


class AssetMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMovement
        fields = (
            'asset',  # FK UUID reference
            'from_location_ref',
            'to_location_ref',
            'movement_date',
            'movement_type',
            'remarks',
            'created_at',
            'updated_at',
        )


## FINANCES

from rest_framework import serializers
from .models import (
    FinancialYear,
    PaymentMethod,
    AccountCategory,
    AccountSubcategory,
    ProfitCostCenter,
    Account,
    AccountBalance,
    AccountJournalDetail,
    AccountJournalHeader,
    AccountingDonor,
    AccountingProject,
    AccountingPledge,
    CenterAnnualForecast,
    IncomeAccountShares,
    JournalHeader,
    JournalDetail,
    Receipt,
    ReceiptAttachment,
    Branch,
    Department,
    Member,
)

# ------------------------
# RefResolverMixin
# ------------------------
class RefResolverMixin:
    """
    Resolves reference fields (like 'branch_ref') into actual FK objects.
    Only used for models whose foreign key parent uses a unique key
    instead of an ID.
    """

    ref_map = {}

    def resolve_refs(self, validated_data):
        for ref_field, (model, lookup_field, target_field) in self.ref_map.items():
            ref_value = validated_data.pop(ref_field, None)
            if not ref_value:
                continue

            instance = model.objects.filter(**{lookup_field: ref_value}).first()
            if not instance:
                raise serializers.ValidationError({
                    ref_field: f"{model.__name__} with {lookup_field} '{ref_value}' not found."
                })
            validated_data[target_field] = instance

        return validated_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for ref_field, (_, lookup_field, target_field) in self.ref_map.items():
            related = getattr(instance, target_field, None)
            if related:
                data[ref_field] = getattr(related, lookup_field)
        return data

    def create(self, validated_data):
        validated_data = self.resolve_refs(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.resolve_refs(validated_data)
        return super().update(instance, validated_data)


# =========================================================
# Simple serializers
# =========================================================
class FinancialYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialYear
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class AccountCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCategory
        fields = "__all__"


class AccountSubcategorySerializer(RefResolverMixin, serializers.ModelSerializer):
    class Meta:
        model = AccountSubcategory
        fields = "__all__"


class ProfitCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitCostCenter
        fields = "__all__"


class AccountSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "category_code": (AccountCategory, "code", "category_code"),
        "account_subcategory_code": (AccountSubcategory, "code", "account_subcategory_code"),
        "center_code": (ProfitCostCenter, "center_code", "center_code"),
    }

    category_code = serializers.IntegerField(required=False)
    account_subcategory_code = serializers.IntegerField(required=False)
    center_code = serializers.CharField(required=False)

    class Meta:
        model = Account
        exclude = ("id",)  # ignore UUID


class AccountBalanceSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "branch_ref": (Branch, "branch_ref", "branch"),
        "account_ref": (Account, "account_code", "account"),
    }

    branch_ref = serializers.CharField(required=False)
    account_ref = serializers.CharField(required=False)

    class Meta:
        model = AccountBalance
        exclude = ("id",)


class AccountJournalDetailSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "branch_ref": (Branch, "branch_ref", "branch"),
        "account_ref": (Account, "account_code", "account"),
    }

    branch_ref = serializers.CharField(required=False)
    account_ref = serializers.CharField(required=False)

    class Meta:
        model = AccountJournalDetail
        exclude = ("id",)


class AccountJournalHeaderSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "branch_ref": (Branch, "branch_ref", "branch"),
    }

    branch_ref = serializers.CharField(required=False)

    class Meta:
        model = AccountJournalHeader
        exclude = ("id",)


class AccountingDonorSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "member": (Member, "member_ref", "member"),
    }

    member = serializers.CharField(required=False)

    class Meta:
        model = AccountingDonor
        exclude = ("id",)


class AccountingProjectSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "branch_ref": (Branch, "branch_ref", "branch"),
        "center": (ProfitCostCenter, "center_code", "center"),
        "income_account": (Account, "account_code", "income_account"),
    }

    branch_ref = serializers.CharField(required=False)
    center = serializers.CharField(required=False)
    income_account = serializers.CharField(required=False)

    class Meta:
        model = AccountingProject
        exclude = ("id",)


class AccountingPledgeSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "project": (AccountingProject, "project_code", "project"),
        "donor": (AccountingDonor, "id", "donor"),
        "income_account": (Account, "account_code", "income_account"),
    }

    project = serializers.CharField(required=False)
    donor = serializers.CharField(required=False)
    income_account = serializers.CharField(required=False)

    class Meta:
        model = AccountingPledge
        exclude = ("id",)


class CenterAnnualForecastSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "branch_ref": (Branch, "branch_ref", "branch"),
        "center": (ProfitCostCenter, "center_code", "center"),
    }

    branch_ref = serializers.CharField(required=False)
    center = serializers.CharField(required=False)

    class Meta:
        model = CenterAnnualForecast
        exclude = ("id",)


class IncomeAccountSharesSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "center_code": (ProfitCostCenter, "center_code", "center_code"),
    }

    center_code = serializers.CharField(required=False)

    class Meta:
        model = IncomeAccountShares
        exclude = ("id",)


class JournalHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalHeader
        exclude = ("id",)


class JournalDetailSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "journal": (JournalHeader, "journal_no", "journal"),
        "account": (Account, "account_code", "account"),
    }

    journal = serializers.CharField(required=False)
    account = serializers.CharField(required=False)

    class Meta:
        model = JournalDetail
        exclude = ("id",)


class ReceiptSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "member": (Member, "member_ref", "member"),
        "donor": (AccountingDonor, "id", "donor"),
        "project": (AccountingProject, "project_code", "project"),
        "pledge": (AccountingPledge, "id", "pledge"),
        "asset_account": (Account, "account_code", "asset_account"),
        "income_account": (Account, "account_code", "income_account"),
        "branch": (Branch, "branch_ref", "branch"),
    }

    member = serializers.CharField(required=False)
    donor = serializers.CharField(required=False)
    project = serializers.CharField(required=False)
    pledge = serializers.CharField(required=False)
    asset_account = serializers.CharField(required=False)
    income_account = serializers.CharField(required=False)
    branch = serializers.CharField(required=False)

    class Meta:
        model = Receipt
        exclude = ("id",)


class ReceiptAttachmentSerializer(RefResolverMixin, serializers.ModelSerializer):
    ref_map = {
        "receipt": (Receipt, "receipt_no", "receipt"),
    }

    receipt = serializers.CharField(required=False)

    class Meta:
        model = ReceiptAttachment
        exclude = ("id",)


# class FinancialYearSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FinancialYear
#         fields = ['fin_year', 'start_date', 'end_date', 'is_current', 'is_closed']
#
#
# class PaymentMethodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentMethod
#         fields = ['pay_method', 'name_lang1', 'name_lang2', 'description',
#                   'is_cash', 'is_bank', 'is_mobile', 'is_electronic', 'active']
#
#
# class AccountCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountCategory
#         fields = ['code', 'name', 'description', 'crdr', 'display_order']
#
#
# class AccountSubcategorySerializer(serializers.ModelSerializer):
#     ref_map = {
#         'category_code_ref': (AccountCategory, 'code', 'category_code')
#     }
#
#     class Meta:
#         model = AccountSubcategory
#         fields = ['code', 'category_code_ref', 'name', 'description', 'display_order']
#
#
# class ProfitCostCenterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProfitCostCenter
#         fields = [
#             'center_code', 'name_lang1', 'name_lang2', 'description1', 'description2',
#             'center_type', 'include_in_overall', 'distribute', 'has_envelop',
#             'is_tithe', 'is_transfer', 'revenue_expenditure_type'
#         ]
#
#
# # ==============================================================
# # Account / Balance / Journal Serializers
# # ==============================================================
#
# # serializers/accounting_serializers.py
#
# # -------------------------------
# # Account Serializer
# # -------------------------------
# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = (
#             "account_code",
#             "account_name",
#             "category",
#             "subcategory",
#             "is_active",
#             "is_control",
#             "is_posting",
#         )
#
#
# # -------------------------------
# # Account Balance Serializer
# # -------------------------------
# class AccountBalanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountBalance
#         fields = (
#             "branch_ref",
#             "account_ref",
#             "fin_year",
#             "opening_balance",
#             "running_balance",
#             "closing_balance",
#             "remarks",
#         )
#
#     def create(self, validated_data):
#         branch_ref = validated_data.pop("branch_ref", None)
#         account_ref = validated_data.pop("account_ref", None)
#         # fin_year_ref = validated_data.pop("fin_year", None)
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         if account_ref and isinstance(account_ref, str):
#             validated_data["account_ref"] = Account.objects.filter(account_code=account_ref).first()
#
#         # if fin_year_ref and isinstance(fin_year_ref, str):
#         #     validated_data["fin_year"] = FinancialYear.objects.filter(fin_year=fin_year_ref).first()
#
#         return super().create(validated_data)
#
#     def update(self, instance, validated_data):
#         return self.create(validated_data)
#
#
# # -------------------------------
# # Account Journal Header Serializer
# # -------------------------------
# class AccountJournalHeaderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountJournalHeader
#         fields = (
#             "journal_no",
#             "journal_date",
#             "journal_type",
#             "branch_ref",
#             "fin_year",
#             "description",
#             "posted_by",
#         )
#
#     def create(self, validated_data):
#         branch_ref = validated_data.pop("branch_ref", None)
#         fin_year_ref = validated_data.pop("fin_year", None)
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         if fin_year_ref and isinstance(fin_year_ref, str):
#             validated_data["fin_year"] = FinancialYear.objects.filter(fin_year=fin_year_ref).first()
#
#         return super().create(validated_data)
#
#
# # -------------------------------
# # Account Journal Detail Serializer
# # -------------------------------
# class AccountJournalDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountJournalDetail
#         fields = (
#             "journal_id",
#             "line_no",
#             "branch_ref",
#             "account_ref",
#             "fin_year",
#             "dr_amount",
#             "cr_amount",
#             "currency_ref",
#             "remarks",
#         )
#
#     def create(self, validated_data):
#         journal_ref = validated_data.pop("journal_id", None)
#         account_ref = validated_data.pop("account_ref", None)
#         branch_ref = validated_data.pop("branch_ref", None)
#         fin_year_ref = validated_data.pop("fin_year", None)
#
#         if journal_ref and isinstance(journal_ref, str):
#             validated_data["journal_id"] = AccountJournalHeader.objects.filter(journal_no=journal_ref).first()
#
#         if account_ref and isinstance(account_ref, str):
#             validated_data["account_ref"] = Account.objects.filter(account_code=account_ref).first()
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         if fin_year_ref and isinstance(fin_year_ref, str):
#             validated_data["fin_year"] = FinancialYear.objects.filter(fin_year=fin_year_ref).first()
#
#         return super().create(validated_data)
#
#
# # -------------------------------
# # Accounting Project Serializer
# # -------------------------------
# class AccountingProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountingProject
#         fields = (
#             "branch_ref",
#             "project_code",
#             "project_name",
#             "project_description",
#             "center",
#             "income_account",
#             "department",
#             "start_date",
#             "end_date",
#             "target_amount",
#             "total_pledged",
#             "total_collected",
#             "is_open",
#         )
#
#     def create(self, validated_data):
#         branch_ref = validated_data.pop("branch_ref", None)
#         center_ref = validated_data.pop("center", None)
#         income_account_ref = validated_data.pop("income_account", None)
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         if center_ref and isinstance(center_ref, str):
#             validated_data["center"] = ProfitCostCenter.objects.filter(center_code=center_ref).first()
#
#         if income_account_ref and isinstance(income_account_ref, str):
#             validated_data["income_account"] = Account.objects.filter(account_code=income_account_ref).first()
#
#         return super().create(validated_data)
#
#
# # -------------------------------
# # Accounting Pledge Serializer
# # -------------------------------
# class AccountingPledgeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountingPledge
#         fields = (
#             "project",
#             "donor",
#             "income_account",
#             "pledge_code",
#             "pledge_description",
#             "pledge_amount",
#             "paid_amount",
#             "balance",
#             "pledge_date",
#             "currency_ref",
#             "branch_ref",
#         )
#
#     def create(self, validated_data):
#         project_ref = validated_data.pop("project", None)
#         donor_ref = validated_data.pop("donor", None)
#         income_account_ref = validated_data.pop("income_account", None)
#         branch_ref = validated_data.pop("branch_ref", None)
#
#         if project_ref and isinstance(project_ref, str):
#             validated_data["project"] = AccountingProject.objects.filter(project_code=project_ref).first()
#
#         if donor_ref and isinstance(donor_ref, str):
#             validated_data["donor"] = AccountingDonor.objects.filter(full_name=donor_ref).first()
#
#         if income_account_ref and isinstance(income_account_ref, str):
#             validated_data["income_account"] = Account.objects.filter(account_code=income_account_ref).first()
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         return super().create(validated_data)
#
#
# # -------------------------------
# # Receipt Serializer
# # -------------------------------
# class ReceiptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Receipt
#         fields = (
#             "receipt_no",
#             "receipt_date",
#             "receipt_type",
#             "service_id",
#             "member",
#             "donor",
#             "project",
#             "pledge",
#             "department",
#             "asset_account",
#             "income_account",
#             "amount",
#             "currency_ref",
#             "exchange_rate",
#             "description",
#             "payment_method",
#             "pay_reference",
#             "sender_number",
#             "bank_id",
#             "bank_account",
#             "branch_ref",
#             "posted_by",
#         )
#
#     def create(self, validated_data):
#         donor_ref = validated_data.pop("donor", None)
#         project_ref = validated_data.pop("project", None)
#         pledge_ref = validated_data.pop("pledge", None)
#         asset_account_ref = validated_data.pop("asset_account", None)
#         income_account_ref = validated_data.pop("income_account", None)
#         # pay_method_ref = validated_data.pop("payment_method", None)
#         branch_ref = validated_data.pop("branch_ref", None)
#
#         if donor_ref and isinstance(donor_ref, str):
#             validated_data["donor"] = AccountingDonor.objects.filter(full_name=donor_ref).first()
#
#         if project_ref and isinstance(project_ref, str):
#             validated_data["project"] = AccountingProject.objects.filter(project_code=project_ref).first()
#
#         if pledge_ref and isinstance(pledge_ref, str):
#             validated_data["pledge"] = AccountingPledge.objects.filter(pledge_code=pledge_ref).first()
#
#         if asset_account_ref and isinstance(asset_account_ref, str):
#             validated_data["asset_account"] = Account.objects.filter(account_code=asset_account_ref).first()
#
#         if income_account_ref and isinstance(income_account_ref, str):
#             validated_data["income_account"] = Account.objects.filter(account_code=income_account_ref).first()
#
#         # if pay_method_ref and isinstance(pay_method_ref, str):
#         #     validated_data["payment_method"] = PaymentMethod.objects.filter(pay_method=pay_method_ref).first()
#
#         if branch_ref and isinstance(branch_ref, str):
#             validated_data["branch_ref"] = Branch.objects.filter(branch_ref=branch_ref).first()
#
#         return super().create(validated_data)
#
#
# # -------------------------------
# # Receipt Attachment Serializer
# # -------------------------------
# class ReceiptAttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReceiptAttachment
#         fields = (
#             "receipt_no",
#             "file_name",
#             "file_path",
#             "upload_date",
#             "uploaded_by",
#         )
#
