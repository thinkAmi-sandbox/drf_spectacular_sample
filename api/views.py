from rest_framework import viewsets

from api.serializers import ShopSerializer
from shop.models import Shop

from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        operation_id='shops',
        extensions={
            'x-amazon-apigateway-integration': {
                'type': 'AWS_PROXY',
                'httpMethod': 'POST',
                'uri': 'arn:aws:lambda:***:***:function:HelloWorld',
                'payloadFormatVersion': '1.0'
            }
        }
    )
)
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
