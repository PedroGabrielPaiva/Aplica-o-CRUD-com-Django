from django.db import models
from django.conf import settings
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    description = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.name
    
    # Adiciona a URL absoluta para a view de detalhes de categoria
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('livros:category_detail', kwargs={'pk': self.pk}) 
    
    class Meta:
        verbose_name_plural = "Categorias" # Correção gramatical para Admin
    


class Resenha(models.Model):
    title = models.CharField(max_length=200)
    data_postagem = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    autor_nome = models.TextField(max_length=500, null=True) 
    resenha = models.TextField() 
    
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    categories = models.ManyToManyField(Category, related_name='resenhas')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Resenha, on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} - {self.text}'

