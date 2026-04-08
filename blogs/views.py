from django.shortcuts import redirect
from blogs.models import Category
from blogs.models import Blog
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_by_categ(request, category_id) :
    posts = Blog.objects.filter(status='Published', category=category_id)
    try: 
        category = Category.objects.get(pk=category_id)
    except: 
        return redirect('home')
    #use get_object_or_404 when we want to show 404 error page

    context= {
        'posts': posts,
        'category' : category,
    }
    return render(request, 'posts_by_categ.html', context)
    # print(posts)
    # return HttpResponse('Posts by category')