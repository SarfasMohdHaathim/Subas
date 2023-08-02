from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name="home"),
    path('signup/',signup,name="signup"),
    path('sign-in/',sign_in,name="sign_in"),
    path('userlogin/',userlogin,name="userlogin"),
    path('userlogout/',userlogout,name="userlogout"),
    path('shop/',shop,name="shop"),
    path('product/',product,name="product"),
    path('cart/',cart,name="cart"),
    path('wishlist/',wishlist,name="wishlist"),
    path('compare/',compare,name="compare"),
    path('checkout/',checkout,name="checkout"),
    path('account/',account,name="account"),
    path('send_otp/',send_otp,name="send_otp"),
    path('login_otp/',login_otp,name="login_otp"),
    path('addCart/<str:pk>/',addCart,name="addCart"),
    path('update_quantity/<str:pk>/',update_quantity,name="update_quantity"),
    path('delete_cart/<str:pk>/',delete_cart,name="delete_cart"),

]