from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:resenha_id>/', views.detail_resenha, name='detail'), 
    path('update/<int:resenha_id>/', views.update_resenha, name='update'), 
    path('delete/<int:resenha_id>/', views.delete_resenha, name='delete'), 
    path('search/', views.search_resenha, name='search'), 
    path('create/', views.create_resenha, name='create'), 
    path('<int:resenha_id>/createcomments/', views.create_comment, name='create_comment'), 
    path('<int:resenha_id>/comments/', views.view_comments, name='view_comments'), 
    
# Listagem de todas as categorias
    path('categories/', views.CategoryListView.as_view(), name='category_list'), 
    
    # Detalhe da categoria (lista posts da categoria)
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

