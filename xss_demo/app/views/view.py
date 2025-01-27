from django.shortcuts import render, redirect
from django.http import JsonResponse
from ..models.message import Message

def message_list(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        Message.objects.create(content=content)
        return redirect('message_list')
    
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'message_list.html', {'messages': messages})

def search_messages(request):
    query = request.GET.get('q', '')
    # Vulnerable! The query parameter is reflected directly in the template
    return render(request, 'search.html', {'query': query})

def api_messages(request):
    # This endpoint will be used for DOM-based XSS
    messages = list(Message.objects.all().order_by('-created_at').values('content'))
    return JsonResponse({'messages': messages})

def subtle_xss(request):
    context = {
        'message_id': request.GET.get('mid', '1'),
        'username': request.GET.get('user', 'guest'),
        'return_url': request.GET.get('return_url', '/'),
        'theme': request.GET.get('theme', 'light'),
        'last_login': request.GET.get('last_login', 'never')
    }
    return render(request, 'subtle_xss.html', context)
