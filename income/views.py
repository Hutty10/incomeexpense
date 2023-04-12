from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOwnerOrAdmin

from .models import Income
from .serializers import IncomeSerializer

# Create your views here.


class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    # queryset = Income.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
    # queryset = Income.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)
