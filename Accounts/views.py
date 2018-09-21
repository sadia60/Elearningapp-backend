from django.shortcuts import render
from django.contrib.auth import(
authenticate,get_user_model,login,logout,
)
from .Forms import UserLoginForm
from .Forms import UserRegisterationForm

# Create your views here.
def loginview(request):
    title="Login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request,"Loginform.html",{"form":form,"title":title})

def register_view(request):
    title = "Register"
    form = UserRegisterationForm(request.POST or None)
    if form.is_valid():
        fullname = form.cleaned_data.get("fullname")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        confirmpassword = form.cleaned_data.get("Confirm password")
    return render(request,"Registerform.html",{"form": form, "title": title})

def logout_view(request):
    return render(request,"Logoutform.html",{})
