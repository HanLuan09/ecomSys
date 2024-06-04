from django.contrib import admin
from django.urls import path

from order_service.views import AddOrderView, AllOrderView, CancelOrderView, ConfirmOrderView, OrderDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/order/add/', AddOrderView.as_view()),
    path('api/order/all/', AllOrderView.as_view()),
    path('api/order/<str:user_id>/', OrderDetailView.as_view()),
    path('api/order/confirm/<str:order_id>/', ConfirmOrderView.as_view()),
    path('api/order/cancel/<str:order_id>/', CancelOrderView.as_view()),
]
