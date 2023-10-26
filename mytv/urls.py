from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:title>/<str:vid>/', views.add, name="add"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('show/<int:id>/', views.show, name='show'),
    path('play/<int:id>/', views.play, name='play'),
    path('search/', views.search, name='search'),
    path('info/', views.info, name='info'),
    path('delete-list/<int:id>/', views.delete_list, name='delete_list'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
