from django.shortcuts import render


def say_hello(request, person_name):
    return render(request, 'app_principal/hello.html', {'nome': person_name})