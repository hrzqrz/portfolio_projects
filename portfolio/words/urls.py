from django.urls import path
from . import views
urlpatterns = [
    path('', views.word_home, name='word_home'),
    path('count/', views.count, name='count'),
]
