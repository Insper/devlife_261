import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mega_hello_world.settings'

import django
django.setup()


def test_comida(client):
    response = client.get('/comida')
    assert 'baião de dois' in response.content.decode('utf-8').lower()


def test_filme(client):
    response = client.get('/filme')
    assert 'estrelas além do tempo' in response.content.decode('utf-8').lower()


def test_livro(client):
    response = client.get('/livro')
    assert 'o design do dia a dia' in response.content.decode('utf-8').lower()
