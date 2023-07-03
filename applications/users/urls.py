from django.urls import path
from . import views

urlpatterns = [
    path('api/create/', views.CreateUserView.as_view()),
    path('api/token/', views.CreateTokenView.as_view()),
    path('api/user/', views.RetrieveUpdateUserView.as_view()),
]
