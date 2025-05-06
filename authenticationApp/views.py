from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import CustomUser
# Create your views here.


def signup_function(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password')  # Note: In your form both fields are named 'password'
        
        # Check if passwords match (though in your form both fields are named the same)
        # You should fix your form to have 'password' and 'password_confirm'
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authenticationApp/signup.html', {
                'username': username,
                'email': email
            })
        
        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'authenticationApp/signup.html', {
                'username': '',
                'email': email
            })
            
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'authenticationApp/signup.html', {
                'username': username,
                'email': ''
            })
        
        # Create the user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Account Created Successfully!")
        return redirect('login_function')
        
        # Log the user in
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('dashboard')  
    return render(request, "authenticationApp/signup.html")

def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "authenticationApp/login.html")



def logout_function(request):
    logout(request)
    return redirect('login_function')