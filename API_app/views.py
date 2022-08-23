
from django.shortcuts import render
from .models import Student
from .serialzers import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def Student_detail(request,id=0):
    stu=Student.objects.get(id=id)
    serializer=Studentserializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')


                                                                          