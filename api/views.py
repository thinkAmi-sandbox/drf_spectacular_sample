from rest_framework import viewsets

from api.serializers import ShopSerializer
from shop.models import Shop


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
