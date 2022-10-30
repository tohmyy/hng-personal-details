from django.shortcuts import render

from requests import request

from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import Http404

from django.shortcuts import get_object_or_404


from .models import Details

from .serializers import DetailSerializer
from details import serializers

class DetailMixinView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
    ):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

# Create your views here.
