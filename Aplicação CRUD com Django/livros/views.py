from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ResenhaForm, ReviewForm
from .models import Resenha, Comment, Category
from django.views import generic
from django.views.generic import ListView, DetailView


# CRUD
####################### READ ##################################

class IndexView(generic.ListView):
    model = Resenha
    # CORREÇÃO 1: Template path de 'resenhas/' para 'livros/'
    template_name = 'livros/index.html'


def detail_resenha(request, resenha_id):
    resenha = get_object_or_404(Resenha, pk=resenha_id)
    comments = Comment.objects.filter(post=resenha).order_by('-date')
    context = {'resenha': resenha,
               'comments': comments}
    # CORREÇÃO 1: Template path de 'resenhas/' para 'livros/'
    return render(request, 'livros/detail.html', context)
####################################################################

####################### SEARCH ##################################
def search_resenha(request):
    context = {"resenha_list": []}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Resenha.objects.filter(title__icontains=search_term)
        context = {
            'resenha_list': post_list
        }
    return render(request, 'livros/search.html', context)
#####################################################################

####################### CREATE ##################################
def create_resenha(request):
    if request.method == 'POST':
        post_form = ResenhaForm(request.POST)
        if post_form.is_valid():
            post = Resenha(**post_form.cleaned_data)
            post.save()
            return HttpResponseRedirect(reverse('livros:detail', args=(post.pk,)))
    else: 
        post_form = ResenhaForm() 
    context = {'form': post_form}
    return render(request, 'livros/create.html', context)
#####################################################################

####################### UPDATE ##################################
def update_resenha(request, resenha_id):
    resenha = get_object_or_404(Resenha, pk=resenha_id)
    if request.method == 'POST':
        form = ResenhaForm(request.POST, request.FILES, instance=resenha)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('livros:detail', args=(resenha_id,)))
    else: 
        form = ResenhaForm(instance=resenha)
    context = {'resenha': resenha, 'form': form}
    return render(request, 'livros/update.html', context)
#####################################################################

####################### DELETE ##################################
def delete_resenha(request, resenha_id):
    post = get_object_or_404(Resenha, pk=resenha_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('livros:index'))
    context = {'resenha': post}
    return render(request, 'livros/delete.html', context)
#####################################################################
def view_comments(request, resenha_id):
    resenha = get_object_or_404(Resenha, pk=resenha_id)
    comments = Comment.objects.filter(post=resenha).order_by('-date')
    context = {'resenha': resenha,
               'comments': comments}
    return render(request, 'livros/comments.html', context)

def create_comment(request, resenha_id):
    post = get_object_or_404(Resenha, pk=resenha_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            if request.user.is_authenticated:
                comment_autor = request.user
            else:
                comment_autor = None 
                
            comment_text = form.cleaned_data['text']
            
            comment = Comment(post=post, autor=comment_autor, text=comment_text)
            comment.save()
            
            return HttpResponseRedirect(reverse('livros:detail', args=(resenha_id,)))
    
    else:
        form = ReviewForm()
        
    context = {'form': form, 'resenha': post}
    return render(request, 'livros/create_comment.html', context)
#############################################################################

class CategoryListView(ListView):
    model = Category
    template_name = 'livros/category_list.html'
    context_object_name = 'categories'

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk) 

    resenha_list = category.resenhas.all().order_by('-data_postagem') 

    context = {
        'category': category,
        'resenha_list': resenha_list,
    }
    return render(request, 'livros/resenha_list.html', context)
