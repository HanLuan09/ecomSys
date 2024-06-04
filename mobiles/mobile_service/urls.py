from django.urls import path
from mobile_service.views import CreateCategoryView, CreateProducerView, AddMobileView, CategoryListView, MobileListView, MobileListofCategoryView, SearchMobileListView, UpdateMobileView, DeleteMobile, DeleteCategory, MobileDetailView

urlpatterns = [
    path('category/add/', CreateCategoryView.as_view()),
    path('producer/add/', CreateProducerView.as_view()),
    path('mobile/add/', AddMobileView.as_view()),
    path('category/all/', CategoryListView.as_view()),
    path('mobile/all/', MobileListView.as_view()),
    path('mobile/detail/<str:mobile_id>/', MobileDetailView.as_view()),
    path('mobile/category/<str:category_id>/', MobileListofCategoryView.as_view()),
    path('mobile/search/<str:key>/', SearchMobileListView.as_view()),
    path('mobile/edit/<str:mobile_id>/', UpdateMobileView.as_view()),
    path('mobile/delete/<str:mobile_id>/', DeleteMobile.as_view()),
    path('category/delete/<str:category_id>/', DeleteCategory.as_view()),
]