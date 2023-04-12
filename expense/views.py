from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpensesSerializer
from .models import Expense
from rest_framework import permissions
from core.permissions import IsOwnerOrAdmin


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    # queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrAdmin)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)
    # queryset = Expense.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
