from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import Ad, Category
from users.models import User
from users.serializers import UserAdSerializer


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserAdSerializer()
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'
