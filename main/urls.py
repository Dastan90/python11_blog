from django.urls import  path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index-page'),
    path('posts/<slug:category>/', views.PostListView.as_view(), name='post-list'),
    path('posts/create/new/', views.CreateNewPostView.as_view(), name='create-post'),
    path('posts/update/<int:pk>/', views.EditPostView.as_view(), name='edit-post'),
    path('posts/delete/<int:pk>/', views.DeletePostView.as_view(), name='delete-post'),
    path('posts/details/<int:pk>/', views.PostDetailsView.as_view(), name='post-details'),
]