from django.http import HttpResponse


def responde_comida(request):
    return HttpResponse("Baião de dois")


def responde_filme(request):
    return HttpResponse("Estrelas Além do Tempo")
