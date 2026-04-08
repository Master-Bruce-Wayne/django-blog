from django.urls import path
from . import views

urlpatterns = [ 
    # parameter passing 
    path('<int:category_id>/', views.posts_by_categ, name='posts_by_category')
] 