from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")

def login(request):
    # if request.user.is_anonymous:
        if request.method == "POST":
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                auth_login(request, login_form.get_user())
                return redirect("articles:main")
        else:
            login_form = AuthenticationForm()

        context = {
             "login_form": login_form,
        }
        return render(request, "accounts/login.html", context)
    # else:
    #     return HttpResponseRedirect("")