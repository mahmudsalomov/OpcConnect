from datetime import datetime

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import time
import pywintypes
import OpenOPC


@api_view(["POST"])
def opc(data):
    try:
        pywintypes.datetime = pywintypes.TimeType
        k = json.load(data)
        server = k["server"]
        unit = k["unit"]
        opc = OpenOPC.client()
        opc.connect(server)
        result = opc.read(unit, timeout=1000)
        # height = json.loads(heightdata.body)
        # weight = str(height * 10)
        # return JsonResponse("Ideal weight should be:" + weight + " kg", safe=False)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        now = datetime.now()
        return Response(e.args["0", "error", now], status.HTTP_400_BAD_REQUEST)
