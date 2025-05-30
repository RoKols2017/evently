from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('verify/email/<uidb64>/<token>/', views.email_verify_view, name='email_verify'),
    path('verify/email/sent/', views.verify_email_sent, name='verify_email_sent'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('telegram/qr/', views.telegram_verification_qr, name='telegram_qr'),
    path('profile/', views.profile_view, name='profile'),
]
