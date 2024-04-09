from django.urls import path
from . import views
app_name='shops'
urlpatterns =[
    path('',views.index,name="index"),
    path("shops/", views.shop_list, name="shop_list"),
    path('<int:id>/',views.details_of_shop,name='details_of_shop'),
    path('<int:id>/addtransaction/',views.add_transaction,name='add_transaction'),
    path('deleteshop/<int:id>',views.delete_shop,name='delete_shop'),
    path('addshop/',views.add_shop,name='add_shop'),
    path('editshop/<int:id>',views.edit_shop,name='edit_shop'),
]