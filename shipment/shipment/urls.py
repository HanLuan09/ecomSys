"""shipment URL Configuration

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

from shipment_service.views import CarriersView, ShipmentInfoView, ShipmentView, TransactionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shipment/shipment-info', ShipmentInfoView.as_view()),
    path('api/shipment/shipment-info/<int:id>', ShipmentInfoView.as_view()),
    path('api/shipment/transaction', TransactionView.as_view()),
    path('api/shipment/transaction/<int:id>', TransactionView.as_view()),
    path('api/shipment/carrier', CarriersView.as_view()),
    path('api/shipment/carrier/<int:id>', CarriersView.as_view()),
    path('api/shipment/', ShipmentView.as_view()),
    path('api/shipment/<int:id>', ShipmentView.as_view()),
]
