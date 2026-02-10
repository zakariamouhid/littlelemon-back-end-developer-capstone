from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def book(request):
    # Handle POST requests for token management
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')
            
            if action == 'store_token':
                token = data.get('token')
                if token:
                    request.session['auth_token'] = token
                    return JsonResponse({'status': 'success'})
            
            elif action == 'clear_token':
                if 'auth_token' in request.session:
                    del request.session['auth_token']
                return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    # Check if user has auth token in session
    auth_token = request.session.get('auth_token')
    context = {
        'is_authenticated': bool(auth_token),
        'auth_token': auth_token if auth_token else None
    }
    return render(request, 'book.html', context)