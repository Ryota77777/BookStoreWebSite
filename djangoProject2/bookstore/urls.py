from django.urls import path, include
from . import views
from .views import edit_book

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('catalog/', views.catalog, name='catalog'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
]
