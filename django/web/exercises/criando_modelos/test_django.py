import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'superloja.settings'

import django
django.setup()


from django.db import models

from produtos import models as md


def assert_classe_definida():
    assert hasattr(md, 'Produto'), 'A classe Produto não foi definida no arquivo produtos/models.py'


def extrai_campos():
    return {campo.name: campo for campo in md.Produto._meta.get_fields()}


def test_classe_definida():
    assert_classe_definida()


def test_campo_nome():
    assert_classe_definida()

    campos = extrai_campos()
    assert 'nome' in campos, 'O campo nome não foi definido na classe Produto'

    nome = campos['nome']
    assert isinstance(nome, models.fields.CharField), 'O campo nome não é do tipo CharField'
    assert nome.max_length == 100, 'O campo nome deve ter o tamanho máximo de 100 caracteres'


def test_campo_descricao():
    assert_classe_definida()

    campos = extrai_campos()
    assert 'descricao' in campos, 'O campo descricao não foi definido na classe Produto'

    descricao = campos['descricao']
    assert isinstance(descricao, models.fields.TextField), 'O campo descricao não é do tipo TextField'
    assert descricao.blank, 'O campo descricao deve ser opcional (blank deve ser True)'
    assert descricao.null, 'O campo descricao deve ser opcional (null deve ser True)'


def test_campo_preco():
    assert_classe_definida()

    campos = extrai_campos()
    assert 'preco' in campos, 'O campo preco não foi definido na classe Produto'

    preco = campos['preco']
    assert isinstance(preco, models.fields.DecimalField), 'O campo preco não é do tipo DecimalField'
    assert preco.max_digits == 7, 'O campo preco deve ter no máximo 7 dígitos'
    assert preco.decimal_places == 2, 'O campo preco deve ter 2 casas decimais'


def test_campo_foto():
    assert_classe_definida()

    campos = extrai_campos()
    assert 'foto' in campos, 'O campo foto não foi definido na classe Produto'

    foto = campos['foto']
    assert isinstance(foto, models.fields.files.ImageField), 'O campo foto não é do tipo ImageField'
    assert foto.upload_to == 'uploads/imgs/', 'O campo foto deve ser salvo na pasta uploads/imgs/'


def test_campo_ultima_modificacao():
    assert_classe_definida()

    campos = extrai_campos()
    assert 'ultima_modificacao' in campos, 'O campo ultima_modificacao não foi definido na classe Produto'

    ultima_modificacao = campos['ultima_modificacao']
    assert isinstance(ultima_modificacao, models.fields.DateTimeField), 'O campo ultima_modificacao não é do tipo DateTimeField'
    assert ultima_modificacao.auto_now, 'O campo ultima_modificacao deve ser preenchido automaticamente (auto_now deve ser True)'
