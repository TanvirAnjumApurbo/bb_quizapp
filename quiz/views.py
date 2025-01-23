from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
from .models import Quiz, Category, QuizSubmission
from django.db.models import Q
from django.contrib import messages

# View to display all quizzes
@login_required(login_url='login')
def all_quiz_view(request):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'all-quiz.html', context)

# View to search quizzes by category or query
@login_required(login_url='login')
def search_view(request, category):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    
    if request.GET.get('q'):
        q = request.GET.get('q')
        query = Q(title__icontains=q) | Q(description__icontains=q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at').distinct()
    elif category != " ":
        quizzes = Quiz.objects.filter(category__name=category).order_by('-created_at')
    else:
        quizzes = Quiz.objects.order_by('-created_at')
    
    categories = Category.objects.all()
    context = {"user_profile": user_profile, "quizzes": quizzes, "categories": categories}
    return render(request, 'all-quiz.html', context)

# View to display a specific quiz and handle quiz submission
@login_required(login_url='login')
def quiz_view(request, quiz_id):
    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    total_questions = quiz.question_set.count()
    
    if request.method == 'POST':
        score = int(request.POST.get('score', 0))
        
        if QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists():
            messages.success(request, f"This time you got {score} out of {total_questions}")
            return redirect('quiz', quiz_id=quiz_id)
        
        QuizSubmission.objects.create(user=request.user, quiz=quiz, score=score)
        messages.success(request, f"Quiz submitted successfully. Your score is {score} out of {total_questions}")
        return redirect('quiz', quiz_id=quiz_id)
    
    context = {"user_profile": user_profile, "quiz": quiz}
    return render(request, 'quiz.html', context)