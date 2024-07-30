from django.urls import include, path
app_name='accounts'
from . import views

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('profile/',views.profile, name = 'profile'),
    path('profile/edit',views.profile_edit, name = 'profile_edit'),
]