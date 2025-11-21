# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )
#
# from .views import (
#     RegionViewSet, BranchViewSet, BranchCellViewSet, DefaultInfoViewSet,
#     DenominationViewSet, DepartmentViewSet, EducationLevelViewSet, HousingStatusViewSet,
#     InstitutionViewSet, LeadershipRoleViewSet, MaritalStatusViewSet, MembershipLevelViewSet,
#     MinistryViewSet, OccupationTypeViewSet, PositionViewSet, ReligionViewSet, SkillViewSet
# )
#
# # 1. Initialize DefaultRouter for REST API endpoints
# router = DefaultRouter()
# router.register(r'regions', RegionViewSet)
# router.register(r'branches', BranchViewSet)
# router.register(r'branch-cells', BranchCellViewSet)
# router.register(r'default-info', DefaultInfoViewSet)
# router.register(r'denominations', DenominationViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'education-levels', EducationLevelViewSet)
# router.register(r'housing-statuses', HousingStatusViewSet)
# router.register(r'institutions', InstitutionViewSet)
# router.register(r'leadership-roles', LeadershipRoleViewSet)
# router.register(r'marital-statuses', MaritalStatusViewSet)
# router.register(r'membership-levels', MembershipLevelViewSet)
# router.register(r'ministries', MinistryViewSet)
# router.register(r'occupation-types', OccupationTypeViewSet)
# router.register(r'positions', PositionViewSet)
# router.register(r'religions', ReligionViewSet)
# router.register(r'skills', SkillViewSet)
#
# # 2. Define urlpatterns including the router and the documentation paths
# urlpatterns = [
#     # API endpoints handled by DefaultRouter
#     path('api/', include(router.urls)),
#
#     # ----------------------------------------------------
#     # DRF-Spectacular (OpenAPI/Swagger) Documentation Paths
#     # ----------------------------------------------------
#
#     # Serves the OpenAPI schema file (YAML/JSON)
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#
#     # Serves the Swagger UI - uses the 'schema' path above as its source
#     path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#
#     # Serves the ReDoc UI (alternative documentation view)
#     path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]