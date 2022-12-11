from django.urls import path, include
from rest_framework import routers

from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('shops', viewset=views.ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]