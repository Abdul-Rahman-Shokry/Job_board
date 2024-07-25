from django.urls import include, path
app_name='accounts'
from . import views

urlpatterns = [
    path('signup',views.signup, name = 'signup'),
]