from rest_framework import viewsets

from retail.models import Link, Product
from retail.serializers import LinkSerializer, ProductSerializer
from users.permissions import IsActive


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsActive,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)
