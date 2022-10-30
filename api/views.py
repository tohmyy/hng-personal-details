
from django.shortcuts import render

import json
from urllib import response
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from yaml import serialize

from details.models import Details
from details.serializers import DetailSerializer

# Create your views here.
@api_view(['GET'])
def detail_api(request, *args, **kwargs):
    model_data = Details.objects.all()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['slackUsername', 'backend', 'age', 'bio'])

    return Response(data)

# Create your views here.
