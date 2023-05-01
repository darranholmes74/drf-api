from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Snacks
from .serializer import SnacksSerializer


class SnacksList(ListAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer


class SnacksDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer
