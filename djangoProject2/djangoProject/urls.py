from django.urls import path
from bookstore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add_book, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('catalog/', views.catalog, name='catalog'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






