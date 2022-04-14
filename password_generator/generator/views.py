from django.shortcuts import render


def index(requests):
    return render(requests, 'generator/index.html')


def password(requests):
    return render(requests, 'generator/password.html')
