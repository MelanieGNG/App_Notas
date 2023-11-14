from django.test import TestCase
from .models import Note
from django.utils import timezone

class NoteModelTests(TestCase):  
    
    def setUp(self):
        self.nota_original = Note.objects.create(
            title="Nota Original",
            creation_date=timezone.now(),
            content="Contexto original"
        )
        self.nota_eliminar = Note.objects.create(
            title="Nota a Eliminar",
            creation_date=timezone.now(),
            content="Contexto de prueba"
        )

    def test_create_note(self):

        nueva_nota = Note.objects.create(
            title="Nota Try",
            creation_date=timezone.now(),
            content="Contexto de prueba"
        )
        
        self.assertEqual(nueva_nota.title, "Nota Try")
        self.assertEqual(nueva_nota.creation_date, timezone.now())
        self.assertEqual(nueva_nota.content, "Contexto de prueba")
        
        
    def test_update_note(self):
        self.nota_original.title = "Nota Actualizada"
        self.nota_original.save()
        nota_actualizada = Note.objects.get(pk=self.nota_original.pk)
        
        self.assertEqual(nota_actualizada.title, "Nota Actualizada")
        
        
    def test_delete_note(self):
        self.nota_eliminar.delete()
        
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=self.nota_eliminar.pk)
            
    def test_show_notes(self):
        Note.objects.create(
            title="Nota 1",
            creation_date=timezone.now(),
            content="Contexto 1"
        )
        Note.objects.create(
            title="Nota 2",
            creation_date=timezone.now(),
            content="Contexto 2"
        )
        notas = Note.objects.all()
        
        self.assertEqual(len(notas), 4) 
        
        
    def test_show_note_details(self):
        nota = Note.objects.create(
            title="Nota de prueba",
            content="Contexto de prueba"
        )
        response = self.client.get(f'/{nota.pk}/')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nota de prueba")

        
