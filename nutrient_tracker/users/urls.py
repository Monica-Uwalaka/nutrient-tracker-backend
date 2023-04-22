from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


#for viewsets, the Router(DefaultRouter in this case)class designs URL conf automatically and connects them to the apporiate views
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
