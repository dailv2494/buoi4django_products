from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('list_category',listCategory,name='category-list'),
    path('create_category',createCategory,name='category-create'),
    path('update_category/<int:id>',updateCategory,name='category-update'),
    path('delete_category/<int:id>',deleteCategory,name='category-delete'),
    path('list_category',listCategory,name='category-list'),
]