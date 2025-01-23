from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from account.models import Profile
from quiz.models import UserRank
from django.contrib.auth.decorators import login_required

# View for the home page
def home(request):
    leaderboard_users = UserRank.objects.order_by('rank')[:3]
    
    if request.user.is_authenticated:
        user_object2 = User.objects.get(username=request.user)
        user_profile2 = Profile.objects.get(user=user_object2)
        context = {"user_profile2": user_profile2, "leaderboard_users": leaderboard_users}
    else:
        context = {"leaderboard_users": leaderboard_users}
        
    return render(request, 'welcome.html', context)

# View for the leaderboard page
@login_required(login_url='login')
def leaderboard_view(request):
    leaderboard_users = UserRank.objects.order_by('rank')
    
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    
    context = { "leaderboard_users": leaderboard_users, user_profile: user_profile}
    return render(request, 'leaderboard.html', context)