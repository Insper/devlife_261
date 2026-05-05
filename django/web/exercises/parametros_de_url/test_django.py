import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto.settings'

import django
django.setup()


def test_Ana(client):
    response = client.get('/hello/Ana')
    assert 'Olá Ana!' in response.content.decode('utf-8')


def test_Bernardo(client):
    response = client.get('/hello/Bernardo')
    assert 'Olá Bernardo!' in response.content.decode('utf-8')


def test_Carla(client):
    response = client.get('/hello/Carla')
    assert 'Olá Carla!' in response.content.decode('utf-8')


def test_Daniel(client):
    response = client.get('/hello/Daniel')
    assert 'Olá Daniel!' in response.content.decode('utf-8')


def test_Eduardo(client):
    response = client.get('/hello/Eduardo')
    assert 'Olá Eduardo!' in response.content.decode('utf-8')


def test_Flavia(client):
    response = client.get('/hello/Flavia')
    assert 'Olá Flavia!' in response.content.decode('utf-8')
