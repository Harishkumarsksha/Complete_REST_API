from django.urls import path, include
from rest_framework import routers
from API.views import EmployeeViewset, employee_list, employee_detail, EmployeeList, EmployeeDetail
from rest_framework.urlpatterns import format_suffix_patterns
# for test frame work


# from rest_framework import viewsets, serializers, routers
# from django.contrib.auth.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email')


# class UserViewsets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# router = routers.DefaultRouter()
# router.register(r'users', UserViewsets)

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewset)

urlpatterns = [

    path('', include(router.urls)),

    # function based API Views
    path('employeelist/', employee_list, name='employeelist'),
    path('employeedetail/<str:pk>/', employee_detail, name='employeedetails'),

    path('Employee_List/', EmployeeList.as_view()),
    path('Employee_Detail/<str:pk>/', EmployeeDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
