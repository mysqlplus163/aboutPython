from django.shortcuts import render
from app02 import modelforms
# Create your views here.


def host(request):
    form = modelforms.HostGroup
    return render(request, 'host.html', {'form': form})
