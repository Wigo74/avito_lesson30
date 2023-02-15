from rest_framework import serializers

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):

    location = serializers.SlugRelatedField(
        required=False,
        # queryset=Location.objects.all(),
        read_only=True,
        many=True,
        slug_field='name'
    )

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('location', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc_name in self._locations:
            location, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(location)
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    # def is_valid(self, *, raise_exception=False):
    #     self._location = self.initial_data.pop("location", [])
    #     return super().is_valid(raise_exception=raise_exception)

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        location = instance.location

        instance = validated_data.get("location", instance.location)
        instance.save()

        # user = User.objects.update(**validated_data)
        # for loc_name in self._locations:
        #     location, _ = Location.objects.get_or_create(name=loc_name)
        #     user.location.add(location)
        return instance

    class Meta:
        model = User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
