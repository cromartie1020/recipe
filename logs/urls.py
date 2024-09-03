from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'logs_views'),
    path('index/', views.index, name = 'index'),
    path('topic_detail/<int:id>/', views.topic_detail, name = 'topic_detail' ),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_entry/', views.new_entry, name = 'new_entry'),
    path('list_entries/<int:id>/', views.list_entries, name = 'list_entries'),
    path('edit_topic/<int:id>/', views.edit_topic, name = 'edit_topic'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
    path('delete_entry/<int:entry_id>',views.delete_entry, name = 'delete_entry'),
    path('confirm_delete/<int:entry_id>/',views.confirm_delete, name = 'confirm_delete'),
]
