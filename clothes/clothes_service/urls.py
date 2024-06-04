from django.urls import path
from clothes_service.views import CreateCategoryView, CreateStyleView, CreateProducerView, AddClothesView, CategoryListView, ClothesListView, ClothesListofCategoryView, SearchClothesListView, UpdateClothesView, DeleteClothes, DeleteCategory, ClothesDetailView

urlpatterns = [
    path('category/add/', CreateCategoryView.as_view()),
    path('clothes/add/', AddClothesView.as_view()),
    path('style/add/', CreateStyleView.as_view()),
    path('producer/add/', CreateProducerView.as_view()),
    path('clothes/add/', AddClothesView.as_view()),
    path('category/all/', CategoryListView.as_view()),
    path('clothes/all/', ClothesListView.as_view()),
    path('clothes/detail/<str:clothes_id>/', ClothesDetailView.as_view()),
    path('clothes/category/<str:category_id>/', ClothesListofCategoryView.as_view()),
    path('clothes/search/<str:key>/', SearchClothesListView.as_view()),
    path('clothes/edit/<str:clothes_id>/', UpdateClothesView.as_view()),
    path('clothes/delete/<str:clothes_id>/', DeleteClothes.as_view()),
    path('category/delete/<str:category_id>/', DeleteCategory.as_view()),
]