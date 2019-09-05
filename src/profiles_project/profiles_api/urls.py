from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
