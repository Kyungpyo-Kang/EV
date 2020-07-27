from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'login.html')

def join(request):
    return render(request, 'join.html')

def join_pro(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['member_id'], password= request.POST['password1']
            )
            member = Member()
            member.user = user
            member.member_name = request.POST['member_name']
            member.member_email = request.POST['member_email']
            member.save()
            auth.login(request, user)         
            return redirect('index')
    return render(request, 'join.html')

def login_pro(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        userPw = request.POST['userPw']
        user = auth.authenticate(request, username=userId, password=userPw)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
    

    

