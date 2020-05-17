from django.urls import path

from .views import (
    loginuser,
    signupuser,
    logooutuser,
    changepassworduser,
    deleteuser,
)

urlpatterns = [
    path('signup', signupuser, name='signupuser'),
    path('login', loginuser, name='loginuser'),
    path('logout', logooutuser, name='logooutuser'),
    path('changepassword/<str:user_username>/', changepassworduser, name='changepassworduser'),
    path('deleteuser/<str:user_username>/', deleteuser, name='deleteuser'),
]