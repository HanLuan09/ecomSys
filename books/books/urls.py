"""books URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from book_service.views import CreateCategoryView, CreateAuthorView, CreatePublisherView, AddBookView, CategoryListView, BookListView, BookListofCategoryView, SearchBookListView, UpdateBookView, DeleteBook, DeleteCategory, BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/add/', CreateCategoryView.as_view()),
    path('api/author/add/', CreateAuthorView.as_view()),
    path('api/publisher/add/', CreatePublisherView.as_view()),
    path('api/book/add/', AddBookView.as_view()),
    path('api/category/all/', CategoryListView.as_view()),
    path('api/book/all/', BookListView.as_view()),
    path('api/book/detail/<str:book_id>/', BookDetailView.as_view()),
    path('api/book/category/<str:category_id>/', BookListofCategoryView.as_view()),
    path('api/book/search/<str:key>/', SearchBookListView.as_view()),
    path('api/book/edit/<str:book_id>/', UpdateBookView.as_view()),
    path('api/book/delete/<str:book_id>/', DeleteBook.as_view()),
    path('api/category/delete/<str:category_id>/', DeleteCategory.as_view()),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)