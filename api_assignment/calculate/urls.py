from django.urls import path
from calculate import views

urlpatterns = [
    path('numbers/', views.number_list),  # for testing the basic setup
]