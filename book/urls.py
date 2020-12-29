from django.urls import path
from . import views

urlpatterns = [
    path('', views.listfunc, name='list'),
    path('form/', views.formfunc, name='form'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
]
