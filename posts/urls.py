from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    path("", views.PostList.as_view(), name="post_list"),
    # user
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", views.UserDetial.as_view(), name="user_detail"),
]
