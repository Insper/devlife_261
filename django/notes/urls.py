from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("anotacoes/<int:note_id>/apagar", views.delete_note, name="delete-note"),
]
