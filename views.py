
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def submit_quiz_ajax(request):
    if request.method == 'POST':
        score = request.POST.get('score', 0)
        # ...save or process score...
        return JsonResponse({'status': 'success', 'score': score})

# ...existing code...