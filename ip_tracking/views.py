from django.http import HttpResponse
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def login_view(request):
    if getattr(request, 'limited', False):
        return HttpResponse("Rate limit exceeded. Try again later.", status=429)
    # ...your login logic here...
    return HttpResponse("Login page or login successful.")
