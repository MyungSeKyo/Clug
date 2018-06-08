from django.urls import path
from .views import LoginView, LogoutView, SignupView, PasswordChangeView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]
