from django.urls import path

from .views import ( homeview, signupview, signup_completeview, loginview, logoutview, user_informationview, user_updateview, 
PasswordChange, PasswordChangeDone, 
)

urlpatterns = [
    path('home/', homeview, name='home'),
    path('signup/', signupview, name='signup'),
    path('signup-complete/', signup_completeview, name='signup_complete'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('user-information/<int:pk>/', user_informationview, name='user_information'),
    path('user-update/<int:pk>/', user_updateview, name='user_update'),
    path('password-change/<int:pk>/', PasswordChange.as_view(), name='password_change'),
    path('password-change-complete/', PasswordChangeDone.as_view(), name='password_change_complete'),
]