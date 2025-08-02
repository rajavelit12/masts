from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_and_show_student),
]
