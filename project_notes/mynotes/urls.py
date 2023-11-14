from django.urls import path
from . import views

app_name = "mynotes"

urlpatterns = [
    path("notas/", views.NoteListView.as_view(), name="index"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="detail"),
    path("new/", views.NoteCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.NoteUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="delete"),
]