from random import randint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Avg
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework import permissions

from .models import Module, ModuleInstance, Professor, Rating, User
from . serializers import ModuleInstanceSerializer, RatingSerializer, UserSerializer
import json
from django.contrib.auth import authenticate


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print (serializer)
                serializer.save()
                response = json.dumps([{ 'Success':'Registration Successful'}])
            except:
                response = json.dumps([{'Error': 'Registration unsuccessful!'}])
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
    response = json.dumps([{'Error': 'Invalid request'}])
    return HttpResponse(response, content_type='text/json')

@api_view(['POST'])
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        response = json.dumps([{'Success':'Logged in'}])
    else:
        response = json.dumps([{'Error':'Login failed'}])
    return JsonResponse(response, safe=False)

@api_view(['POST'])
def logout_(request):
    request.user.auth_token.delete()
    response = json.dumps([{'Success':'You are logged out'}])
    return JsonResponse(response, safe=False)

@api_view(['GET'])
def list(request):
    if request.method == 'GET':
        try:
            list = ModuleInstance.objects.all()
            serializer = ModuleInstanceSerializer(list, many=True)
            response = serializer.data
        except:
            response = json.dumps([{'Error':'No Records Found'}])
        return JsonResponse(response, safe=False)

@api_view(['GET'])
def view(request):
    if request.method == 'GET':
        try:
            response = []
            view = Professor.objects.all()
            for prof in view:
                avg = Rating.objects.filter(professor=Professor.objects.get(code=prof.code).id).aggregate(Avg('rating'))
                prof_rate = {"code": prof.code, "name": prof.name, "avg": avg.get('rating__avg')}
                response.append( prof_rate )
        except Exception as e:
            response = json.dumps([{'Error':'No Records Found'}])
            raise e
        return JsonResponse(response, safe=False)

@api_view(['GET'])
def avg(request):
    # prevent failure from onvalid codes/module

    try:
        profCode = request.query_params.get('code')
        modCode = request.query_params.get('module')
        modCode = ModuleInstance.objects.get(code=modCode)
        professor =  Professor.objects.get(code=profCode)
        avg = Rating.objects.filter(professor=Professor.objects.get(code=profCode).id, module=modCode).aggregate(Avg('rating'))
        prof_rate = {"code": professor.code, "name": professor.name, "avg": avg.get('rating__avg')}
        response=( prof_rate )
    except Exception as e:
        response = json.dumps([{'Error':'No Records Found'}])
        raise e
    return JsonResponse(response, safe=False)       


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate(request):
    if request.method =='POST':
        try:
            data = request.data
            year = request.data.get('year') #not exact year
            year = year + "-01-01"

            semester = request.data.get('semester')
            profCode = request.data.get('professor')
            professor =  Professor.objects.get(code=profCode).pk
            moduleCode = request.data.get('module')
            module =  Module.objects.get(code=moduleCode).pk
            rating = request.data.get('rating')
            moduleInstance = ModuleInstance.objects.filter(module=module, year=year, semester = semester)[0]
            user = User.objects.get(username=request.user.username)
            if ((Rating.objects.filter(username=user, module=moduleInstance).count()) != 0):
                response = json.dumps([{'Error':'Module rating previously submitted.'}])
                return JsonResponse(response, safe=False)

            data = {
                "username":user.pk, 
                "professor":professor,
                "module":moduleInstance.pk,
                "rating":rating
            }
        except Exception as e:
            response = json.dumps([{'Error':'Invalid rating data'}])
            raise e

        serializer = RatingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                response = json.dumps([{ 'Success':'Rating added successfully!'}])
            except:
                response = json.dumps([{'Error': 'Rating unsuccessful!'}])
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
    response = json.dumps([{'Error': 'Invalid request'}])
    return HttpResponse(response, content_type='text/json')