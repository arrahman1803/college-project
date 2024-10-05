from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from userauths.forms import UserRegistrationForm
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL

# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} Your Account Successfully Created")
            new_user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect("/")
    else:
        form = UserRegistrationForm()

    context = {'form' : form}
    return render(request, "auth/signup.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email = email)
        except:
            messages.warning(request, f"User with {email} does not exist.")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You are Logged In")
            return redirect("/")
        else:
            messages.warning(request, "User Does Not Exist, Create An Account")

    context = {}
    return render(request, "auth/login.html", context)

def logout(request):
    logout(request)
    return redirect("/login")


