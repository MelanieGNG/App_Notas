from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.views import generic
from django.urls import reverse_lazy

class NoteListView(generic.ListView):
    model = Note
    template_name = "mynotes/note_list.html"
    context_object_name = "note"
    success_url = reverse_lazy('mynotes:create')


class NoteDetailView(generic.DetailView):
    model = Note
    fields = ["title", "content"]
    template_name = "mynotes/note_detail.html"

class NoteCreateView(generic.CreateView):
    model = Note
    fields = ["title", "content"]
    template_name = "mynotes/note_edit.html"
    success_url = reverse_lazy('mynotes:index')

class NoteUpdateView(generic.UpdateView):
    model = Note
    fields = ["title", "content"]
    template_name = "mynotes/note_edit.html"
    success_url = reverse_lazy('mynotes:index')

class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('mynotes:index')
