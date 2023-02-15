import json

from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDeleteSerializer, LocationListSerializer


def root(request):
    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if "first_name" in data:
            self.object.first_name = data["first_name"]
        if "last_name" in data:
            self.object.last_name = data["last_name"]
        if "age" in data:
            self.object.age = data["age"]
        if "role" in data:
            self.object.role = data["role"]
        if "locations" in data:
            for loc_name in data["locations"]:
                loc_, _ = Location.objects.get_or_create(name=loc_name)
                self.object.location.add(loc_)
        self.object.save()

        return JsonResponse(
            {"id": self.object.pk,
             # "username": self.object.username,
             "first_name": self.object.first_name,
             "last_name": self.object.last_name,
             "role": self.object.role,
             "age": self.object.age,
             "locations": list(map(str, self.object.location.all())),
             "total_ads": self.object.ads.filter(is_published=True).count()
             }, safe=False)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
