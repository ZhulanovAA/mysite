from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ExtendedUserCreationForm


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            default_group = Group.objects.get(name='комментатор')
            user.groups.add(default_group)
            user.save()
            return HttpResponseRedirect("/")
    else:
        form = ExtendedUserCreationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


def about(request):
    return render(request, 'about.html')
