from django.urls import include, path
app_name='job'
from . import views
"""
This code means to import a module or
package named "something" from the current
directory or package. The dot (.) represents
the current directory or package within the directory.
"""

urlpatterns = [
    path('',views.job_list, name = 'job_list'),
    path('add',views.add_job, name = 'add_job'),
    path('<str:slug>',views.job_detail, name = 'job_detail')
]