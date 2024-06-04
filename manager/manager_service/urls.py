from django.urls import path
from manager_service.views import LoginView, AddManagerView, ManagerInfoView, ChangePasswordView, UpdateProfileView, VerifyTokenView

urlpatterns = [
    path('add/', AddManagerView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('info/', ManagerInfoView.as_view(), name='manager-detail'),
    path('change/', ChangePasswordView.as_view(), name='change'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
]
