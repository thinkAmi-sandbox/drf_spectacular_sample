from rest_framework import viewsets

from api.serializers import ShopSerializer
from shop.models import Shop

from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        operation_id='shops'
    )
)
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
