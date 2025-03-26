from django.urls import path
from . import views

urlpatterns = [
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api_auth_token'),
]
