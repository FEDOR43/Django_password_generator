from django.shortcuts import render
from random import *


def index(request):
    return render(request, 'generator/index.html')


def password(request):

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_(){}[]`~'

    chars = lowercase_letters
    # print('Введите количество паролей, которое требуется сгенерировать.')
    # count_pass = int(input())
    # print('Введите требуемую длину пароля.')
    password_length = int(request.GET.get('password_length', 12))
    if request.GET.get('numbers'):
        chars += digits
    if request.GET.get('uppercase'):
        chars += uppercase_letters
    if request.GET.get('special'):
        chars += punctuation
    if request.GET.get('similar'):
        for char in chars:
            if char in 'il1Lo0O':
                chars = chars.replace(char, '')

    def generate_password(len_pass, chars):
        password = ''
        for _ in range(len_pass):
            password += choice(chars)
        return password

    return render(request, 'generator/password.html', {'password': generate_password(password_length, chars)})


def about(request):
    return render(request, 'generator/about.html')
