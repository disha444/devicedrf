import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Devicinfo
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import requests

from rest_framework import status

from .serializers import devserializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@csrf_exempt
@api_view(['POST', 'GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated],)
def find_price(request):
    if request.method == 'GET':
        name1 = request.query_params.get('device_name')
        # response = requests.get('https://testodsy.wrtual.in/api/v2/dem/testing_init/')
        # print(response)
        # response.json()

        data = Devicinfo.objects.filter(device_name=name1).order_by('device_price')
        print(data,"data")

        serializer = devserializer(data[0])

        return Response(serializer.data)



    if request.method == 'POST':

        name = request.data.get('device_name')
        price = request.data.get('device_price')
        data = {"d_name": name,"d_price":price}
        r = requests.post('https://testodsy.wrtual.in/api/v2/dem/testing_init/',json = data)
        print(r.content)

        user = Devicinfo.objects.create(device_name=name, device_price=price)

        return Response({"message":"record has been created!!"}, status=status.HTTP_201_CREATED)


# response = requests.get('https://testodsy.wrtual.in/api/v2/dem/testing_init/')
# print(response)
# response.json()


data  = {"device_name" : "OPPO A92" , "device_price": 17500}
r = requests.post('https://testodsy.wrtual.in/api/v2/dem/testing_init/',json = data)

print(r.content)
