from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('allBlog/', allBlog, name="allBlog"),
    path('login/', login_view, name="login_view"),
    path('add_blog/', add_blog, name="add_blog"),
    path('view_blog/' , view_blog , name="view_blog"),
    path('delete/<id>' , delete , name="delete"),
    path('update/<slug>/' , update , name="update"),
    path('signup/', signup_view, name="signup_view"),
    path('details/<slug>', details, name="details"),
    path('logout/', logout_view, name="logout_view"),
    path('news/', news, name="news"),
]