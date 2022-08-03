from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import RegisterForm, ContactUsForm, ProfileChangeForm, CourseCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Course

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
    template = loader.get_template('contact.html')
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            #TODO send mail
            return HttpResponse(template.render({'form': form, 'done': True}, request=request))
        else:
            return HttpResponse(template.render({'form': form, 'done': False}, request=request))
    return HttpResponse(template.render({'form': ContactUsForm(), 'done': False}, request=request))


@login_required(login_url='polls:login')
def profile(request):
    template = loader.get_template('profile.html')
    user = get_object_or_404(User, id=request.user.id)
    return HttpResponse(template.render({'user': user}, request=request))


@login_required(login_url='polls:login')
def setting(request):
    template = loader.get_template('setting.html')
    if request.method == 'POST':
        form = ProfileChangeForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['first_name'] != '':
                request.user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name'] != '':
                request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            return redirect('polls:profile')
        else:
            return HttpResponse(template.render({'form': form}, request=request))
    return HttpResponse(template.render({'form': ProfileChangeForm()}, request=request))


@login_required(login_url='polls:login')
def panel(request):
    template = loader.get_template('panel.html')
    return HttpResponse(template.render(request=request))


@user_passes_test(lambda u: u.is_superuser, login_url='polls:panel')
def add_course(request):
    template = loader.get_template('add_course.html')
    if request.method == 'POST':
        form = CourseCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:panel')
        else:
            return HttpResponse(template.render({'form': form}, request=request))
    return HttpResponse(template.render({'form': CourseCreationForm()}, request=request))


class AllCoursesView(generic.ListView):
    model = Course
    template_name = 'all_courses.html'
