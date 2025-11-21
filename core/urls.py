# # """

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Grouped and ordered endpoints
    path('api/lookups/', include('api.urls.lookups')),      # 1. Lookups
    path('api/members/', include('api.urls.members')),      # 2. Members
    path('api/finance/', include('api.urls.finance')),      # 3. Finance
    path('api/assets/', include('api.urls.assets')),        # 4. Assets

    # DRF-Spectacular schema & docs
    path('api/schema/', include([
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ])),
]


#
#
#
#
# # URL configuration for core project.
# #
# # The `urlpatterns` list routes URLs to  For more information please see:
# #     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# # Examples:
# # Function views
# #     1. Add an import:  from my_app import views
# #     2. Add a URL to urlpatterns:  path('', home, name='home')
# # Class-based views
# #     1. Add an import:  from other_app.views import Home
# #     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# # Including another URLconf
# #     1. Import the include() function: from django.urls import include, path
# #     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# # """
#
# from django.contrib import admin
# from django.urls import path, include
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )
#
# urlpatterns = [
#
#     path('admin/', admin.site.urls),
#
#     # ---- Grouped API Routes ----
#     path('api/lookups/', include('api.urls.lookups')),
#     path('api/members/', include('api.urls.members')),
#     path('api/finance/', include('api.urls.finance')),
#     path('api/assets/', include('api.urls.assets')),
#
#
#     # ---- Swagger / OpenAPI ----
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]
#
#
# # from django.contrib import admin
# # from django.urls import path
# #
# #
# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter
# # from drf_spectacular.views import (
# #     SpectacularAPIView,
# #     SpectacularRedocView,
# #     SpectacularSwaggerView,
# # )
# #
# #
# #
# # from api.views import (
# #     RegionViewSet, BranchViewSet, BranchCellViewSet, DefaultInfoViewSet,
# #     DenominationViewSet, DepartmentViewSet, EducationLevelViewSet, HousingStatusViewSet,
# #     InstitutionViewSet, LeadershipRoleViewSet, MaritalStatusViewSet, MembershipLevelViewSet,
# #     MinistryViewSet, OccupationTypeViewSet, PositionViewSet, ReligionViewSet, SkillViewSet
# # )
# #
# # from api.views import (
# #     MemberViewSet,
# #     MemberBranchViewSet, MemberBranchChurchPositionViewSet, MemberBranchDepartmentLeadershipViewSet,
# #     MemberBranchMinistryViewSet, MemberEducationViewSet, MemberOccupationViewSet
# # )
# #
# # from api.views import (
# #     LocationViewSet,
# #     AssetCategoryViewSet,
# #     AssetSubcategoryViewSet,
# #     AssetIndexViewSet,
# #     AssetViewSet,
# #     AssetLocationViewSet,
# #     AssetMovementViewSet,
# # )
# #
# #
# # from api.views import (
# #     FinancialYearViewSet, PaymentMethodViewSet, AccountCategoryViewSet, AccountSubcategoryViewSet,
# #     ProfitCostCenterViewSet, AccountViewSet, AccountBalanceViewSet, AccountJournalHeaderViewSet,
# #     AccountJournalDetailViewSet
# # )
# #
# # # 1. Initialize DefaultRouter for REST API endpoints
# # router = DefaultRouter()
# # router.register(r'regions', RegionViewSet)
# # router.register(r'branches', BranchViewSet)
# # router.register(r'branch-cells', BranchCellViewSet)
# # router.register(r'default-info', DefaultInfoViewSet)
# # router.register(r'denominations', DenominationViewSet)
# # router.register(r'departments', DepartmentViewSet)
# # router.register(r'education-levels', EducationLevelViewSet)
# # router.register(r'housing-statuses', HousingStatusViewSet)
# # router.register(r'institutions', InstitutionViewSet)
# # router.register(r'leadership-roles', LeadershipRoleViewSet)
# # router.register(r'marital-statuses', MaritalStatusViewSet)
# # router.register(r'membership-levels', MembershipLevelViewSet)
# # router.register(r'ministries', MinistryViewSet)
# # router.register(r'occupation-types', OccupationTypeViewSet)
# # router.register(r'positions', PositionViewSet)
# # router.register(r'religions', ReligionViewSet)
# # router.register(r'skills', SkillViewSet)
# #
# # router.register(r'members', MemberViewSet)
# # router.register(r'member-branches', MemberBranchViewSet)
# # router.register(r'member-positions', MemberBranchChurchPositionViewSet)
# # router.register(r'member-department-leaderships', MemberBranchDepartmentLeadershipViewSet)
# # router.register(r'member-ministries', MemberBranchMinistryViewSet)
# # router.register(r'member-education', MemberEducationViewSet)
# # router.register(r'member-occupations', MemberOccupationViewSet)
# #
# # router.register(r'locations', LocationViewSet)
# # router.register(r'asset-categories', AssetCategoryViewSet)
# # router.register(r'asset-subcategories', AssetSubcategoryViewSet)
# # router.register(r'asset-indices', AssetIndexViewSet)
# # router.register(r'assets', AssetViewSet)
# # router.register(r'asset-locations', AssetLocationViewSet)
# # router.register(r'asset-movements', AssetMovementViewSet)
# # #
# # # #FINANCES
# # router.register(r'financial-years', FinancialYearViewSet)
# # router.register(r'payment-methods', PaymentMethodViewSet)
# # router.register(r'account-categories', AccountCategoryViewSet)
# # router.register(r'account-subcategories', AccountSubcategoryViewSet)
# # router.register(r'profit-cost-centers', ProfitCostCenterViewSet)
# # router.register(r'accounts', AccountViewSet)
# # router.register(r'account-balances', AccountBalanceViewSet)
# # router.register(r'account-journal-headers', AccountJournalHeaderViewSet)
# # router.register(r'account-journal-details', AccountJournalDetailViewSet)
# #
# # # 2. Define urlpatterns including the router and the documentation paths
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #
# #     # API endpoints handled by DefaultRouter
# #     path('api/', include(router.urls)),
# #
# #     # ----------------------------------------------------
# #     # DRF-Spectacular (OpenAPI/Swagger) Documentation Paths
# #     # ----------------------------------------------------
# #
# #     # Serves the OpenAPI schema file (YAML/JSON)
# #     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
# #
# #     # Serves the Swagger UI - uses the 'schema' path above as its source
# #     path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
# #
# #     # Serves the ReDoc UI (alternative documentation view)
# #     path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# # ]