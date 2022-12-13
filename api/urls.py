from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nest_routers

from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('shops', viewset=views.ShopViewSet)
router.register('exceptions', viewset=views.ExceptionViewSet)

parent_router = nest_routers.SimpleRouter()
parent_router.register(r'companies', views.CompanyViewSet)

nest_shop_router = nest_routers.NestedSimpleRouter(parent_router, r'companies', lookup='company')
nest_shop_router.register(r'shops', views.NestedShopViewSet, basename='company-shops')

m2m_router = nest_routers.NestedSimpleRouter(nest_shop_router, r'shops', lookup='shop')
m2m_router.register(r'apples', views.M2MAppleViewSet, basename='company-shops-apples')

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(nest_shop_router.urls)),
    path(r'', include(m2m_router.urls)),
]
