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
    path('',views.job_list),
    path('<int:id>',views.job_detail, name = 'job_detail')
]