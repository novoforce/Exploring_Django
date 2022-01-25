from django.urls import path
from . import views #import all the views(function/class) from the current app(directory)

urlpatterns = [
    path('',views.home, name='home'),
    path('room/',views.room,name='room'),
]
