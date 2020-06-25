"""learnig_logs URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'), 
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('add_entry/<int:topic_id>', views.add_entry, name='add_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
