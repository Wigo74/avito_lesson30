import json

from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import IsOwnerSelection, IsOwnerAdOrStaff
from ads.serialazers import AdSerializer, AdDetailSerializer, AdListSerializer, AdCreateSerializer


def root(request):
    return JsonResponse({
        "status": "ok"
    })


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.order_by('-price')
    default_serializer = AdSerializer

    default_permission = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'partial_update': [IsAuthenticated(), IsOwnerAdOrStaff()],
        'destroy': [IsAuthenticated(), IsOwnerAdOrStaff()]
    }

    serializer_class = {
        'list': AdListSerializer,
        'create': AdCreateSerializer,
        'retrieve': AdDetailSerializer,
        }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImage(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "author": self.object.author.username,
                             "price": self.object.price,
                             "description": self.object.description,
                             "category": self.object.category.name,
                             "is_published": self.object.is_published,
                             "image": self.object.image.url if self.object.image else None
                             }, safe=False)


