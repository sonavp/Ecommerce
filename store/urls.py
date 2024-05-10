from django.urls import path
from store import views

urlpatterns = [
    path("home/", views.Home.as_view(), name="home"),
    # path("collection/", views.Collections.as_view(), name="collection")
    path("Category/<int:pk>",views.Category_detail.as_view(),name="category_detail"),
    path("product_detail/<int:pk>",views.Product_detail.as_view(),name="p_detail"),
    path('register/',views.Registerview.as_view(),name="reg"),
    path('addtocart/<int:pk>',views.Addtocartview.as_view(),name="cart"),
    path('login/',views.signinview.as_view(),name="login"),
    path('logout/',views.signout.as_view(),name="signout"),
    path('delete/<int:pk>',views.Cart_deleteview.as_view(),name="delete"),
    path('cartview/',views.Cart_detailview.as_view(),name="detail_cart"),
    path("order/<int:pk>",views.Orderview.as_view(),name="order"),
    path('order_view/',views.Vieworder.as_view(),name="view_order")
]
