from rest_framework.routers import DefaultRouter
from api.views import (
    FinancialYearViewSet, PaymentMethodViewSet, AccountCategoryViewSet,
    AccountSubcategoryViewSet, ProfitCostCenterViewSet, AccountViewSet,
    AccountBalanceViewSet, AccountJournalHeaderViewSet, AccountJournalDetailViewSet
)

router = DefaultRouter()
router.register(r'financial-year',FinancialYearViewSet)
router.register(r'payment-method',PaymentMethodViewSet)
router.register(r'account-category', AccountCategoryViewSet)
router.register(r'account-subcategory', AccountSubcategoryViewSet)
router.register(r'profit-cost-center',ProfitCostCenterViewSet)
router.register(r'account',AccountViewSet)
router.register(r'account-balance',AccountBalanceViewSet)
router.register(r'account-journal-header',AccountJournalHeaderViewSet)
router.register(r'account-journal-detail',AccountJournalDetailViewSet)

urlpatterns = router.urls
