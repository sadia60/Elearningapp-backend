from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSeriailizer
from django.http import Http404

# Create your views here.
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSeriailizer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSeriailizer


# class CourseList(APIView):
#     """
#     List all course, or create a new course
#     """
#     def get(self, request, format=None):
#         courses = Course.objects.all()
#         serializer = CourseSeriailizer(courses, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CourseSeriailizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#