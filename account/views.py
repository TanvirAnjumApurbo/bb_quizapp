from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Profile
from quiz.models import QuizSubmission

# View for user registration
def register(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.username)
  
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already used. Try to login.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('profile', username)
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    
    return render(request, 'reg.html')
  
# View for user profile
@login_required(login_url='login')
def profile(request, username):
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)
  
    user_object2 = User.objects.get(username=request.user)
    user_profile2 = Profile.objects.get(user=user_object2)
  
    submissions = QuizSubmission.objects.filter(user=user_object)
    
    context = {"user_profile": user_profile, "user_profile2": user_profile2, "submissions": submissions}
    return render(request, 'profile.html', context)

# View to edit user profile
@login_required(login_url='login')
def editProfile(request):
    user_object2 = User.objects.get(username=request.user)
    user_profile2 = Profile.objects.get(user=user_object2)

    if request.method == 'POST':
        new_email = request.POST['email']
        new_username = request.POST['username']

        if User.objects.filter(email=new_email).exclude(username=request.user.username).exists():
            messages.error(request, 'Email is already used by another account.')
            return redirect('edit_profile')

        if User.objects.filter(username=new_username).exclude(username=request.user.username).exists():
            messages.error(request, 'Username is already taken by another account.')
            return redirect('edit_profile')

        user_object2.first_name = request.POST['first_name']
        user_object2.last_name = request.POST['last_name']
        user_object2.email = new_email
        user_object2.username = new_username
        user_profile2.location = request.POST['location']
        user_profile2.gender = request.POST['gender']
        user_profile2.bio = request.POST['bio']
        
        if 'profile_img' in request.FILES:
            user_profile2.profile_img = request.FILES['profile_img']
        
        user_object2.save()
        user_profile2.save()
        
        messages.success(request, 'Profile updated successfully')
        return redirect('profile', user_object2.username)

    context = {"user_profile2": user_profile2}
    return render(request, 'profile-edit.html', context)

# View to delete user profile
@login_required(login_url='login')
def deleteProfile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('logout')
    return render(request, 'confirm.html')

# View for user login
def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid!')
            return redirect('login')

    return render(request, "login1.html")

# View for user logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')