from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name = 'blog-home'),
    path('post/new', views.newPost, name='post-new'),
    path('post/<int:id>/delete', views.deletePost, name = "post-delete"),
    path('post/<int:id>/edit', views.editPost, name='post-edit'),
    path('like/', views.like, name = "like"),
    path('comment/<int:postId>/<int:commentId>/delete', views.deleteComment, name="comment-delete"),
    path(r'^exact_url/?$', views.search, name = "search"),
    path('about/', views.about, name='about'),
    


]