from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsOwnerSelection
from ads.serialazers import SelectionDetailSerializer, SelectionListSerializer, SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializer_class = {
        'list': SelectionListSerializer,
        'retrieve': SelectionDetailSerializer
    }

    default_permission = [AllowAny()]
    permissions = {
        'create': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsOwnerSelection()],
        'partial_update': [IsAuthenticated(), IsOwnerSelection()],
        'destroy': [IsAuthenticated(), IsOwnerSelection()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer)
