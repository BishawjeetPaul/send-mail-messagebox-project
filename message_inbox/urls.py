from django.contrib import admin
from django.urls import path, include
from message_inbox import settings
from django.conf.urls.static import static
from inbox import views

urlpatterns = [
    # path to admin page.
    path("admin/", admin.site.urls),
    # --------------- FRONTEND -------------- |
    # path to home page (front-end).
    path('', views.home, name='home'),
    # path to Login/Logout.
    path('login/', include('django.contrib.auth.urls')),
    # path to send a message.
    path('send_message', views.send_message, name='send_message'),
    # --------------- BACKEND --------------- |
    # path to inbox page (back-end).
    path('inbox/', views.inbox, name='inbox'),
    # path to delete the message.
    path('delete/message/<str:customer_id>', views.delete_message, name='delete_message'),
    # path to view the message individuals.
    path('customer/<str:customer_id>', views.customer, name='customer'),
    # path to mark the message as read.
    path('mark_message', views.mark_message, name="mark_message"), 
    # path to reply the message.
    path('email', views.email, name='email'),
    # path to auto logout.
    path('autologout/', views.AutoLogoutUser, name='autologout'),
    
    
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
