from rest_framework.routers import DefaultRouter
from api.views import (
    LocationViewSet, AssetCategoryViewSet, AssetSubcategoryViewSet,
    AssetIndexViewSet, AssetViewSet, AssetLocationViewSet, AssetMovementViewSet
)

router = DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'asset-category', AssetCategoryViewSet)
router.register(r'asset-subcategory', AssetSubcategoryViewSet)
router.register(r'asset-index', AssetIndexViewSet)
router.register(r'asset', AssetViewSet)
router.register(r'asset-location', AssetLocationViewSet)
router.register(r'asset-movement', AssetMovementViewSet)

urlpatterns = router.urls
