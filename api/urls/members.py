from rest_framework.routers import DefaultRouter
from api.views import (
    MemberViewSet, MemberBranchViewSet, MemberBranchChurchPositionViewSet,
    MemberBranchDepartmentLeadershipViewSet, MemberBranchMinistryViewSet,
    MemberEducationViewSet, MemberOccupationViewSet
)

router = DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'member-branch', MemberBranchViewSet)
router.register(r'member-position', MemberBranchChurchPositionViewSet)
router.register(r'member-department-leadership', MemberBranchDepartmentLeadershipViewSet)
router.register(r'member-ministry', MemberBranchMinistryViewSet)
router.register(r'member-education', MemberEducationViewSet)
router.register(r'member-occupation', MemberOccupationViewSet)

urlpatterns = router.urls
