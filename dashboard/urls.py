from django.urls import path

from dashboard import views

urlpatterns = [
    path('dash/', views.dashboard, name='dash'),
]