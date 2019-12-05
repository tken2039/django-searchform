# board/urls.py

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # 記事の一覧表示ページ
    path('', views.IndexView.as_view(), name='index'),

    # 記事作成ページ
    path('post/create/', views.CreateView.as_view(), name='create'),

    # 記事の詳細ページ
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # path('post/<int:pk>/update/', views.update, name='update'),

    # path('post/<int:pk>/delete/', views.delete, name='delete'),
]