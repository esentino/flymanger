from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render


def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponse("Udało się zaloguj się")
        return render(request, 'game/_partial/register.html', context=dict(register_form=register_form))


def home_page_view(request):
    if request.method == 'GET':
        return render(request, 'game/homepage.html')


def profile_view(request):
    if request.method == 'GET':
        auth_form = AuthenticationForm(request)
        register_form = UserCreationForm()
        return render(request, 'game/profile.html', context=dict(auth_form=auth_form,register_form=register_form))
