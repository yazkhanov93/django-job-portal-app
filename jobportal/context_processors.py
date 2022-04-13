from .models import *


def categories(request):
    return{
        'categories': Category.objects.all()
    }

def jobtypes(request):
    return {
        'jobtypes': JobType.objects.all()
    }

