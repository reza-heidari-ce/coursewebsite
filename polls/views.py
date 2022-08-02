from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import RegisterForm, ContactUsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            template = loader.get_template('register.html')
            return HttpResponse(template.render({'form': form}, request=request))
    template = loader.get_template('register.html')
    return HttpResponse(template.render({'form': RegisterForm()}, request=request))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request=request, user=user)
                return redirect('polls:index')
        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({'form': form}, request=request))
    template = loader.get_template('login.html')
    return HttpResponse(template.render({'form': AuthenticationForm()}, request=request))


def logout_view(request):
    logout(request=request)
    return redirect('polls:index')


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            #TODO send mail
            template = loader.get_template('contact.html')
            return HttpResponse(template.render({'form': form, 'done': True}, request=request))
        else:
            template = loader.get_template('contact.html')
            return HttpResponse(template.render({'form': form, 'done': False}, request=request))
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({'form': ContactUsForm(), 'done': False}, request=request))


@login_required(login_url='polls:login')
def profile(request):
    template = loader.get_template('profile.html')
    user = get_object_or_404(User, id=request.user.id)
    return HttpResponse(template.render({'user': user}, request=request))