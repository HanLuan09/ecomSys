
from django.urls import path

from .views import UserInfoView, UpdateProfileView, CreateUserProfile, CreateUserAddress, UserAddressInfoView, UpdateAddressView

urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user-detail'),
    path('profile/add/', CreateUserProfile.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
    path('address/add/', CreateUserAddress.as_view(), name='address_add'),
    path('address/update/', UpdateAddressView.as_view(), name='address_update'),
    path('address/', UserAddressInfoView.as_view(), name='address'),
]
