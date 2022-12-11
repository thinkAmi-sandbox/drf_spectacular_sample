from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer, OpenApiExample, OpenApiResponse
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ShopSerializer
from shop.models import Shop


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
    ),
    message=extend_schema(
        operation_id='shop_status',
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    name='MessageResponse',
                    fields={
                        'message': serializers.CharField(),
                    },
                ),
                description='レスポンス型'
            )
        },
        examples=[OpenApiExample(
            name='例',
            value=[
                {'message': 'open'},
                {'message': 'close'}
            ]
        )],
        description='actionデコレータ分'
    )
)
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @action(detail=False, methods=['get'])
    def message(self, request, pk=None):
        return Response({'message': 'open'})
