from django.urls import path
from . import views



urlpatterns = [
    path('vegetables/', views.vegetables_ingredients, name='vegetables'),
    path('meat/', views.meat_ingredients, name='vegetables'),
    path('other/', views.other_ingredients, name='vegetables')
]
