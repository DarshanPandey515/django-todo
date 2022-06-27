from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.add, name='add'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('signup',views.signup_user, name='signup'),
    path('remove/<int:id>',views.removelist, name='remove'),
    path('edit/<int:id>',views.edit, name='edit'),
]

