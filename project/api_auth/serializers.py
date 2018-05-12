from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import environ
from datetime import datetime, timedelta

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=32,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all())]
                                     )

    password = serializers.CharField(min_length=8, write_only=True, required=True)

    wallet = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='address')

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            is_active=validated_data['is_active'])

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'wallet', 'password','is_active')
        required_fields = ('username','password','email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        print(token)
        # Add custom claims
        
        print(token)
        
        return token

    def validate(self,attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)

        env = environ.Env()
        expired_token = env('ACCESS_TOKEN_LIFETIME', default=5)
        nextTime = datetime.now() + timedelta(minutes = expired_token)
        time_stamp = str(int(nextTime.timestamp()))
        print('time stamp ' + time_stamp)
        
        data['expires_on'] = time_stamp

        return data

