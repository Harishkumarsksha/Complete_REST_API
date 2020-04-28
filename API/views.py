from django.shortcuts import render
from django.http import JsonResponse, Http404
# Create your views here.
from API.models import Employee
from API.serializers import EmployeeSerializers, EmployeeSerializersfunc
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    #permission_classes = [au]


# @csrf_exempt
@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializersfunc(employee, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializersfunc(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializersfunc(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializersfunc(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Based views


class EmployeeList(APIView):

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializersfunc(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializersfunc(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeDetail(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializersfunc(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializersfunc(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
