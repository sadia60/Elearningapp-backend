# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Course

class CourseSeriailizer(serializers.ModelSerializer):

    class Meta:
        model=Course
        fields=(
            'auther_name','course_title','course_description','course_created_timestamp')



#__all__





#
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     username = serializers.CharField(
#             max_length=32,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     password = serializers.CharField(min_length=6, max_length=100,
#             write_only=True)
#
#     def create(self, validated_data):
#         user = User(email=validated_data['email'],
#                 username=validated_data['username'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')