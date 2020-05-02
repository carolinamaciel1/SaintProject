from django.shortcuts import render
from rest_framework import generics
from .models import Saints
from .serializers import SaintsSerializer


class ListSaintsView(generics.ListAPIView):
    queryset = Saints.objects.all()
    serializer_class = SaintsSerializer


