from django.urls import path

from . import views


app_name = 'authenticator'
urlpatterns = [
    path('auth/register-request', views.RegisterRequestView.as_view(), name='register_request'),
    path('auth/register-response', views.RegisterResponseView.as_view(), name='register_response'),
    path('auth/login-request', views.LoginRequestView.as_view(), name='login_request'),
    path('auth/login-response', views.LoginResponseView.as_view(), name='login_response'),
    path('auth/session-completed', views.PollingView.as_view(), name='session_completed'),
]
