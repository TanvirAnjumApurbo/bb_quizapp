from django.urls import path
from . import views

urlpatterns = [
  path('all-quiz/', views.all_quiz_view, name='all-quiz'),
  path('search/<str:category>/', views.search_view, name='search'),
  path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz'),
]