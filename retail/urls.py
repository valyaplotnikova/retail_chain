from rest_framework import routers

from retail.apps import RetailConfig
from retail.views import LinkViewSet, ProductViewSet

app_name = RetailConfig.name

router = routers.DefaultRouter()
router.register('links', LinkViewSet, basename='links')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [

] + router.urls
