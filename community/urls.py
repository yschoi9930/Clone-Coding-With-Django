from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'community'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:review_id>/', views.detail, name='detail'),
    path('review/create/', views.review_create, name='review_create'),
    path('comment/create/<int:review_id>/', views.comment_create, name='comment_create'),
]