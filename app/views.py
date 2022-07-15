from django.shortcuts import render


def index(request):
    '''Loads the Home page'''
    return render(request, 'index.html')

def pricing(request):
    '''Loads the Prcing page
    Here the user can decide on what package they can purchase'''
    return render(request, 'pricing.html')

def user_research(request):
    #Edit this doc string and state exactly what is going on in the page
    '''Loads the user research related page'''
    return render(request, 'user-research.html')

def web_development(request):
    #Edit this doc string too. 
    '''loads courses'''
    return render(request, 'web-development.html')


