from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from users.models import User
from users.serializers import UserAdSerializer


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


def check_not_published(value):
    if not value:
        raise ValidationError("Нельзя создавать опубликованные объявления")


class AdCreateSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    is_published = BooleanField(validators=[check_not_published], required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserAdSerializer()
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class SelectionListSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = ["owner", "name"]


class SelectionSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
