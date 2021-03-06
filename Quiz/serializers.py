# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Mcq,Result

class McqSeriailizer(serializers.ModelSerializer):

    class Meta:
        model=Mcq
        fields='__all__'

class ResultSeriailizer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields='__all__'

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
