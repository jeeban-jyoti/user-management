from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    first_name, last_name, profile_picture, username, email, password, confirm_password, address = "", "", "", "", "", "", "", ""
    if request.method == 'POST':
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        profile_picture = request.POST.get('profile_picture','')
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        address = request.POST.get('address','')
        print(first_name, last_name, profile_picture, username, email, password, confirm_password, address)

        if password != confirm_password:
            redirect('/playground/login')

    return render(request, 'signup.html')

@csrf_exempt
def login(request):
    email, password = "", ""
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        print(email, password)

    return render(request, 'login.html')
