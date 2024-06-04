"""payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from payment_service.views import PaymentMethodView, PaymentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/payment/payment-method', PaymentMethodView.as_view()),
    path('api/payment/payment-method/<int:id>', PaymentMethodView.as_view()),
    path('api/payment', PaymentView.as_view()),
    path('api/payment/<int:id>', PaymentView.as_view()),
]
