from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from . import views


urlpatterns=[
    path('admin/',admin.site.urls),
    path('clients/',views.Client.as_view()),
    path('clients/<int:pk>',views.Client.as_view()),
    path('clients/<int:pk>/projects',views.Client.as_view()),
    path('projects/',views.Project.as_view()),
    path('user/',views.User.as_view())
]