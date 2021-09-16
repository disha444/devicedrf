from django.urls import path
from . import views

urlpatterns = [
    path('dev1/', views.find_price)

    ]
