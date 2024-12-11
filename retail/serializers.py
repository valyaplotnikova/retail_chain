from rest_framework import serializers

from retail.models import Link, Product


class LinkSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Звено. """

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ['debt']


class ProductSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Продукт. """

    links = LinkSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
