from django.forms import ModelForm
from .models import Resenha, Comment

class ResenhaForm(ModelForm):
    class Meta:
        model = Resenha
        fields = ['title', 'autor_nome', 'resenha', 'image']

        labels = {
            'title': 'Título do livro Resenhado',
            'autor_nome': 'Nome do Autor do livro',
            'resenha': 'Corpo da Resenha',
            'image': 'Capa/Imagem',
        }
        
class ReviewForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
        labels = {
            'text': 'Comentário',
        }