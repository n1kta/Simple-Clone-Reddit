from django.urls import path

from .views import loginuser, signupuser, logooutuser

urlpatterns = [
    path('signup', signupuser, name='signupuser'),
    path('login', loginuser, name='loginuser'),
    path('logout', logooutuser, name='logooutuser'),
]