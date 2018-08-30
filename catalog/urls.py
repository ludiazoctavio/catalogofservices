from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.service_list, name='service_list'),
    path('areas', views.area_list, name='area_list'),
    path('items', views.item_list, name='item_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('area/<int:area_id>/', views.area_detail, name='area_detail'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]