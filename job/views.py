from django.shortcuts import render
from django.core.paginator import Paginator
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

    paginator = Paginator(job_list, 1) # show 1 job per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj}
    return render(request, 'job\job_list.html', context)



def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    context = {'job' : job_detail}
    return render(request, 'job\job_detail.html', context)