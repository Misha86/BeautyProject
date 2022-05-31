from django.urls import path
from .views import *


app_name = "api"

urlpatterns = [
    path('user/', CustomUserListCreateView.as_view(), name='user-list'),
    path('user/<int:pk>/', CustomUserDetailRUDView.as_view(), name='user-detail'),
    path('user/specialist/<int:pk>/',
         SpecialistInformationView.as_view(),
         name='specialist-detail'),
    path('user/<int:user>/order/<int:id>/',
         CustomUserOrderDetailRUDView.as_view(),
         name='specialist-order-detail'),
]
