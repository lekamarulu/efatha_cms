from rest_framework.routers import DefaultRouter
from api.views import (
    RegionViewSet, BranchViewSet, BranchCellViewSet, DefaultInfoViewSet,
    DenominationViewSet, DepartmentViewSet, EducationLevelViewSet, HousingStatusViewSet,
    InstitutionViewSet, LeadershipRoleViewSet, MaritalStatusViewSet, MembershipLevelViewSet,
    MinistryViewSet, OccupationTypeViewSet, PositionViewSet, ReligionViewSet, SkillViewSet
)

router = DefaultRouter()
router.register(r'region', RegionViewSet)
router.register(r'branch', BranchViewSet)
router.register(r'branch-cell', BranchCellViewSet)
router.register(r'default-info', DefaultInfoViewSet)
router.register(r'denomination', DenominationViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'education-level', EducationLevelViewSet)
router.register(r'housing-status', HousingStatusViewSet)
router.register(r'institution', InstitutionViewSet)
router.register(r'leadership-role', LeadershipRoleViewSet)
router.register(r'marital-status', MaritalStatusViewSet)
router.register(r'membership-level', MembershipLevelViewSet)
router.register(r'ministry', MinistryViewSet)
router.register(r'occupation-type', OccupationTypeViewSet)
router.register(r'position', PositionViewSet)
router.register(r'religion', ReligionViewSet)
router.register(r'skill', SkillViewSet)

urlpatterns = router.urls
