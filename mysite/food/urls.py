from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # /food/1
    path('<int:pk>', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    # /food/add item
    path('add', views.CreateItem.as_view(), name='create_item'),
    # /food/update/id item
    path('update/<int:item_id>', views.update_item, name='update_item'),
    # /food/delete/id
    path('delete/<int:item_id>', views.delete_item, name='delete_item')
]
