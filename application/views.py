from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


current_page = dict()

navbar = list()
navbar.append({'link': 'index', 'title': 'Home'})


def get_base_context(title):
    context = dict()
    context['navbar'] = navbar
    context['title'] = title
    return context


def get_page(data):
    return render(data['request'], data['url'], data['context'])


def index_page(request):
    global current_page
    context = get_base_context('Home')
    current_page = {
        'request': request,
        'url': 'pages/index.html',
        'context': context
    }
    return get_page(current_page)


def login_view(request):
    global current_page
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user:
            login(request, user)
            current_page['context']['auth_success'] = True
            context = get_base_context('Home')
            current_page = {
                'request': request,
                'url': 'pages/index.html',
                'context': context
            }
        else:
            current_page['context']['auth_success'] = False
    elif request.method == 'GET':
        context = get_base_context('Login')
        current_page = {
            'request': request,
            'url': 'pages/login.html',
            'context': context
        }
    return get_page(current_page)


def logout_view(request):
    global current_page
    logout(request)
    context = get_base_context('Home')
    current_page = {
        'request': request,
        'url': 'pages/index.html',
        'context': context
    }
    return get_page(current_page)


def registration_view(request):
    global current_page
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user is None:
            current_page['context']['reg_success'] = True
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            context = get_base_context('Home')
            current_page = {
                'request': request,
                'url': 'pages/index.html',
                'context': context
            }
        else:
            current_page['context']['reg_success'] = False
    elif request.method == 'GET':
        context = get_base_context('Registration')
        current_page = {
            'request': request,
            'url': 'pages/registration.html',
            'context': context
        }
    return get_page(current_page)