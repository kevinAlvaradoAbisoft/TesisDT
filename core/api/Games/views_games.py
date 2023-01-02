from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.user.models import User
from core.erp.models import *
from core.homepage.models import *
from core.api.User.serializers_user import UserSerializer,UserTokenSerializerJWT,CustomUserSerializer
from core.api.Games.serializers_games import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class GameViewSet(generics.ListAPIView):
    model = GameFootball
    serializer_class = GameSerializer
    queryset = GameFootball.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['referee_id','refereeAssistantOne_id','refereeAssistantTwo_id','teamLocal','teamVisitor','stadium']