from django.urls import path
from . import views

urlpatterns = [
        path('',views.superuser,name="superuser"),
]
