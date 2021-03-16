from django.urls import path

from dashboard import views

urlpatterns = [
    path('dash/', views.dashboard, name='dash'),
    path('dash/<int:order>/', views.customers, name='customer'),
]