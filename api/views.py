from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer, OpenApiExample, OpenApiResponse, \
    OpenApiParameter
from rest_framework import viewsets, serializers, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ShopSerializer, CompanySerializer, NestedShopSerializer
from shop.models import Shop, Company


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


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@extend_schema_view(
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter(name='company_pk', location=OpenApiParameter.PATH, type=int),
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, type=int)
        ]
    ),
)
class NestedShopViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = NestedShopSerializer

    def get_queryset(self):
        return Shop.objects.filter(company=self.kwargs['company_pk'])
