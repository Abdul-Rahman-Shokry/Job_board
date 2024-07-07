from django.db import models

# Create your models here.

'''
django model field:
    - validation
    - HTML widgit
    - DB size
'''
class Job(models.Model): #Table
    title = models.CharField(max_length=100) #column