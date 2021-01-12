from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]

