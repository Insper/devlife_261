from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Note


@login_required
def index(request):
    if request.method == "POST":
        title = request.POST.get("titulo", "").strip()
        content = request.POST.get("detalhes", "").strip()

        if title and content:
            Note.objects.create(title=title, content=content, author=request.user)

        return redirect("index")

    notes = Note.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "notes/index.html", {"notes": notes})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    note.delete()
    return redirect("index")
