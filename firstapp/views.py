from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home_redirect(request):
    return redirect('login')  # or '/login/'


def dashboard(request):
  return render(request ,'dashboard.html')
  
from django.contrib.auth import get_user_model

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("🧪 Username:", username)
        print("🧪 Password:", password)

        User = get_user_model()
        try:
            user_obj = User.objects.get(username=username)
            print("👤 User found:", user_obj)

            if user_obj.check_password(password):
                print("🔑 Password is correct, but authenticate() failed.")
            else:
                print("❌ Password mismatch.")
        except User.DoesNotExist:
            print("⚠️ User with username does not exist.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("✅ Authentication successful for", user)
            login(request, user)
            return redirect('dashboard')
        else:
            print("❌ Authentication failed. Check user model config and password.")
            messages.error(request, "Invalid Username or Password")
            return render(request, 'login/login.html')

    return render(request, 'login/login.html')


def to_login(request):
  return render(request ,'login/login.html')