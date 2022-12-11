from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from shop.models import Shop


@extend_schema_field({
    'type': 'integer',
    'title': Shop._meta.get_field('size').verbose_name,
    'enum': Shop.Size.values,
    'x-enum-varnames': Shop.Size.names,
})
class SizeField(serializers.IntegerField):
    pass


class ShopSerializer(serializers.ModelSerializer):
    size = SizeField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'size', 'established_at', 'updated_at']
