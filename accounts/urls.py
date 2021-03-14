from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from project_main import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='../templates/login.html'), name='login'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name='../templates/change_password.html'),
         name='password_change'),
    path('settings/change_password/done', auth_views.PasswordChangeDoneView.as_view(template_name='../templates/change_password_done.html'),
         name='password_change_done'),
    path('account/', views.UserUpdateView.as_view(), name='my_account'),

]


