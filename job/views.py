from django.shortcuts import render
from .models import Job
"""
The dot . represents the current directory or
package. So, in this case, from .models import
Job is importing the Job class from the models
module that is in the same directory as the
module where this import statement is written.
"""

def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs':job_list}
    return render(request, 'job\job_list.html', context)


def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    context = {'job' : job_detail}
    return render(request, 'job\job_detail.html', context)