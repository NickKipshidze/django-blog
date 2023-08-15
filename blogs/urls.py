from django.urls import path
from . import views
 
urlpatterns = [
    path("newblog", views.CreateBlogPostView.as_view(), name="newblog")
]