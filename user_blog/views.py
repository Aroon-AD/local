from .models import BlogModel,CommentModel
from .forms import CommentForm,SearchForm
from django.shortcuts import render,redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q


         
def BlogListView(request):
    dataset = BlogModel.objects.all()
    paginator = Paginator(dataset,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():         
            
            title = form.cleaned_data.title()
            blog = BlogModel.objects.get(blog_title=title)
               
            return redirect('/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset':dataset,
            'form':form,
            'posts':posts,
            
        }
    return render(request,'listview.html',context)
 
 
def BlogDetailView(request,_id):
    try:
        data =BlogModel.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
        nextblog = BlogModel.objects.filter(id__gt=data.id).order_by('id').first()
        prevblog = BlogModel.objects.filter(id__lt=data.id).order_by('id').last()
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name= form.cleaned_data['your_name'],
            comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect('/blog/{_id}')
    else:
        form = CommentForm()
        
    context = {
            'data':data,
            'form':form,
            'comments':comments,
            'nextblog' : nextblog,
            'prevblog' : prevblog
        }
    return render(request,'detailview.html',context)

def Searchview(request):
    if request.method =='GET':
     query = request.GET.get('q')
     submitbutton =  request.GET.get('submit')
     if query is not None:
          lookups = Q(blog_title__icontains=query)| Q(blog__icontains=query)
          results = BlogModel.objects.filter(lookups).distinct()
          context={
          'results':results,
          'submitbutton':submitbutton,
          }

          return render(request,'Search.html',context)