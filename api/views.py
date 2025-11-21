from rest_framework import viewsets
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


from .serializers import (
    RegionSerializer, BranchSerializer, BranchCellSerializer, DefaultInfoSerializer,
    DenominationSerializer, DepartmentSerializer, EducationLevelSerializer,
    HousingStatusSerializer, InstitutionSerializer, LeadershipRoleSerializer,
    MaritalStatusSerializer, MembershipLevelSerializer, MinistrySerializer,
    OccupationTypeSerializer, PositionSerializer, ReligionSerializer, SkillSerializer
)

from .serializers import (
    MemberSerializer,
    MemberBranchSerializer,
    MemberBranchChurchPositionSerializer,
    MemberBranchDepartmentLeadershipSerializer,
    MemberBranchMinistrySerializer,
    MemberEducationSerializer,
    MemberOccupationSerializer
)

from .serializers import (
    LocationSerializer,
    AssetCategorySerializer,
    AssetSubcategorySerializer,
    AssetIndexSerializer,
    AssetSerializer,
    AssetLocationSerializer,
    AssetMovementSerializer,
)


from .models import (
    FinancialYear, PaymentMethod, AccountCategory, AccountSubcategory,
    ProfitCostCenter, Account, AccountBalance, AccountJournalHeader,
    AccountJournalDetail, AccountingDonor, AccountingProject,
    AccountingPledge, CenterAnnualForecast, IncomeAccountShares,
    JournalHeader, JournalDetail, Receipt, ReceiptAttachment
)


from .serializers import (
    FinancialYearSerializer, PaymentMethodSerializer, AccountCategorySerializer,
    AccountSubcategorySerializer, ProfitCostCenterSerializer, AccountSerializer,
    AccountBalanceSerializer, AccountJournalHeaderSerializer, AccountJournalDetailSerializer,
    AccountingDonorSerializer, AccountingProjectSerializer, AccountingPledgeSerializer,
    CenterAnnualForecastSerializer, IncomeAccountSharesSerializer, JournalHeaderSerializer,
    JournalDetailSerializer, ReceiptSerializer, ReceiptAttachmentSerializer
)


# Lookup info
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.select_related('region').all()
    serializer_class = BranchSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class BranchCellViewSet(viewsets.ModelViewSet):
    queryset = BranchCell.objects.all()
    serializer_class = BranchCellSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class DefaultInfoViewSet(viewsets.ModelViewSet):
    queryset = DefaultInfo.objects.all()
    serializer_class = DefaultInfoSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class DenominationViewSet(viewsets.ModelViewSet):
    queryset = Denomination.objects.all()
    serializer_class = DenominationSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class EducationLevelViewSet(viewsets.ModelViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class HousingStatusViewSet(viewsets.ModelViewSet):
    queryset = HousingStatus.objects.all()
    serializer_class = HousingStatusSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class LeadershipRoleViewSet(viewsets.ModelViewSet):
    queryset = LeadershipRole.objects.all()
    serializer_class = LeadershipRoleSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class MembershipLevelViewSet(viewsets.ModelViewSet):
    queryset = MembershipLevel.objects.all()
    serializer_class = MembershipLevelSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class OccupationTypeViewSet(viewsets.ModelViewSet):
    queryset = OccupationType.objects.all()
    serializer_class = OccupationTypeSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    swagger_tags = ['1. Lookup']  # Group in Swagger UI



# MEMBERSHIP MANAGEMENT

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberBranchViewSet(viewsets.ModelViewSet):
    queryset = MemberBranch.objects.all()
    serializer_class = MemberBranchSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberBranchChurchPositionViewSet(viewsets.ModelViewSet):
    queryset = MemberBranchChurchPosition.objects.all()
    serializer_class = MemberBranchChurchPositionSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberBranchDepartmentLeadershipViewSet(viewsets.ModelViewSet):
    queryset = MemberBranchDepartmentLeadership.objects.all()
    serializer_class = MemberBranchDepartmentLeadershipSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberBranchMinistryViewSet(viewsets.ModelViewSet):
    queryset = MemberBranchMinistry.objects.all()
    serializer_class = MemberBranchMinistrySerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberEducationViewSet(viewsets.ModelViewSet):
    queryset = MemberEducation.objects.all()
    serializer_class = MemberEducationSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI


class MemberOccupationViewSet(viewsets.ModelViewSet):
    queryset = MemberOccupation.objects.all()
    serializer_class = MemberOccupationSerializer
    swagger_tags = ['2. Membership']  # Group in Swagger UI

# ASSET MANAGEMENT
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetSubcategory.objects.all()
    serializer_class = AssetSubcategorySerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetIndexViewSet(viewsets.ModelViewSet):
    queryset = AssetIndex.objects.all()
    serializer_class = AssetIndexSerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetLocationViewSet(viewsets.ModelViewSet):
    queryset = AssetLocation.objects.all()
    serializer_class = AssetLocationSerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


class AssetMovementViewSet(viewsets.ModelViewSet):
    queryset = AssetMovement.objects.all()
    serializer_class = AssetMovementSerializer
    swagger_tags = ['3. Assets']  # Group in Swagger UI


# FINANCES


# -------------------------------------------------------------
# Simple ViewSets
# -------------------------------------------------------------

class FinancialYearViewSet(viewsets.ModelViewSet):
    queryset = FinancialYear.objects.all()
    serializer_class = FinancialYearSerializer
    # permission_classes = [IsAuthenticated]
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountCategoryViewSet(viewsets.ModelViewSet):
    queryset = AccountCategory.objects.all()
    serializer_class = AccountCategorySerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = AccountSubcategory.objects.all()
    serializer_class = AccountSubcategorySerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class ProfitCostCenterViewSet(viewsets.ModelViewSet):
    queryset = ProfitCostCenter.objects.all()
    serializer_class = ProfitCostCenterSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


# -------------------------------------------------------------
# Accounting Core
# -------------------------------------------------------------

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountJournalHeaderViewSet(viewsets.ModelViewSet):
    queryset = AccountJournalHeader.objects.all()
    serializer_class = AccountJournalHeaderSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountJournalDetailViewSet(viewsets.ModelViewSet):
    queryset = AccountJournalDetail.objects.all()
    serializer_class = AccountJournalDetailSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


# -------------------------------------------------------------
# Donor / Project / Pledge
# -------------------------------------------------------------

class AccountingDonorViewSet(viewsets.ModelViewSet):
    queryset = AccountingDonor.objects.all()
    serializer_class = AccountingDonorSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountingProjectViewSet(viewsets.ModelViewSet):
    queryset = AccountingProject.objects.all()
    serializer_class = AccountingProjectSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class AccountingPledgeViewSet(viewsets.ModelViewSet):
    queryset = AccountingPledge.objects.all()
    serializer_class = AccountingPledgeSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


# -------------------------------------------------------------
# Forecast / Shares
# -------------------------------------------------------------

class CenterAnnualForecastViewSet(viewsets.ModelViewSet):
    queryset = CenterAnnualForecast.objects.all()
    serializer_class = CenterAnnualForecastSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class IncomeAccountSharesViewSet(viewsets.ModelViewSet):
    queryset = IncomeAccountShares.objects.all()
    serializer_class = IncomeAccountSharesSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


# -------------------------------------------------------------
# Journal Header / Detail
# -------------------------------------------------------------

class JournalHeaderViewSet(viewsets.ModelViewSet):
    queryset = JournalHeader.objects.all()
    serializer_class = JournalHeaderSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class JournalDetailViewSet(viewsets.ModelViewSet):
    queryset = JournalDetail.objects.all()
    serializer_class = JournalDetailSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


# -------------------------------------------------------------
# Receipt / Attachment
# -------------------------------------------------------------

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI


class ReceiptAttachmentViewSet(viewsets.ModelViewSet):
    queryset = ReceiptAttachment.objects.all()
    serializer_class = ReceiptAttachmentSerializer
    swagger_tags = ['4. Finance']  # Group in Swagger UI
