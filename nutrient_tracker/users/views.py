from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Goal
from .serializers import UserSerializer, GoalSerializer
from rest_framework.decorators import action

#create viewsets for users

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'


    def get_object(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(self.request, user)
        return user

    def create(self, request, *args, **kwargs):
        """Creates A New User Object In The Database"""
        
        #deserialize data: i.e convert incoming JSON to a python dictionary
        serializer = UserSerializer(data=request.data)

        #validate the data
        if serializer.is_valid():
            try:
                user = serializer.save()
            except IntegrityError:
                return Response(status=409)
            else:
                login(request, user)
                #serialize data to JSON
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def goal(self, request, format=None, pk=""):
        """Returns The Most Recently Used Address (If Any) Of The Given User"""
        user = self.get_object()
        goal = get_object_or_404(Goal, user=user)
        serializer = GoalSerializer(goal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer