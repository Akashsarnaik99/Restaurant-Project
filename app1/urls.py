from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('lunch/',views.lunch, name='lunch'),
    path('dinner/',views.dinner,name='dinner'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('starter/',views.starter, name='starter'),
    path('userdetails',views.userdetails, name='userdetails'),
    path('delete_data/<int:id>/',views.delete_data, name='delete_data'),
    path('delete_order/<int:id>/',views.delete_order, name='delete_order'),
    path('update/<int:id>',views.update, name='update'),
    path('do_update/<int:id>/',views.do_update, name='do_update'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout' ),
    path('password_reset',views.password_reset,name='password_reset'),
    path('breakfast',views.breakfast,name='breakfast'),
    path('checkout',views.checkout,name='checkout'),
    path('',views.home,name='home'),
    path('makelist',views.makelist,name='makelist'),
    path('order_details',views.order_details, name='order_details'),
    path('order_data',views.order_data, name='order_data'),
    path('feedback',views.feedback,name='feedback'),
    path('signup',views.signup,name='signup'),


    


]
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
