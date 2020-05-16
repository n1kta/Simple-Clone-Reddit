from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import User, ArticlesModel, LinkModel, CommentsModel
from .forms import ArticlesForm, LinkForm, CommentsForm

# Home view

def home(request):
    links = LinkModel.objects.all()
    if request.method == 'GET':
        articles = ArticlesModel.objects.all()
        return render(request, 'home.html', {'articles': articles, 'links': links})
    else:
        if request.POST.get('articles_sort') == 'top':
            articles = ArticlesModel.objects.order_by('-likes')
        elif request.POST.get('articles_sort') == 'new':
            articles = ArticlesModel.objects.order_by('-created')
        elif request.POST.get('articles_sort') == 'old':
            articles = ArticlesModel.objects.order_by('created')
        return render(request, 'home.html', {'articles': articles, 'links': links})
            
def search(request):
    if request.method == 'POST':
        search_article = request.POST.get('search_article')
        if search_article:
            articles = ArticlesModel.objects.filter(title__icontains=search_article)
            return render(request, 'search.html', {'articles': articles, 'search_article': search_article})

# Articles view

def article_view(request, article_id):
    current_article = get_object_or_404(ArticlesModel, pk=article_id)
    new_comment = CommentsForm()
    if request.method == 'GET':
        current_comments = CommentsModel.objects.filter(article_id=article_id)
        return render(request, 'article_detail.html', {'current_article': current_article, 'current_comments': current_comments, 'comment': new_comment})
    else:
        if request.POST.get('comments_sort'):
            if request.POST.get('comments_sort') == 'top':
                current_comments = CommentsModel.objects.order_by('-likes')
            elif request.POST.get('comments_sort') == 'new':
                current_comments = CommentsModel.objects.order_by('-created')
            elif request.POST.get('comments_sort') == 'old':
                current_comments = CommentsModel.objects.order_by('created')
            return render(request, 'article_detail.html', {'current_article': current_article, 'current_comments': current_comments, 'comment': new_comment})
        else:
            form = CommentsForm(request.POST)
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.article_id = article_id
            new_comment.save()
            return redirect('article_view', article_id)

def new_article(request):
    if request.method == 'GET':
        return render(request, 'new_post.html', {'form': ArticlesForm()})
    else:
        form = ArticlesForm(request.POST)
        new_article = form.save(commit=False)
        new_article.user = request.user
        new_article.save()
        return redirect('home')

def edit_article(request, article_id):
    current_article = get_object_or_404(ArticlesModel, pk=article_id)
    current_comments = CommentsModel.objects.filter(article_id=article_id)
    article = ArticlesModel.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=article) # instance - берет текущие данные с формы под aritcle_id
        if form.is_valid():
            form.save()
            return redirect('article_view', article_id)
    else:
        form = ArticlesForm(instance=article)
    return render(request, 'edit_post.html', {'form': form, 'current_article': current_article, 'current_comments': current_comments})
    
def delete_article(request, article_id):
    article = ArticlesModel.objects.get(id=article_id)
    comment = CommentsModel.objects.get(article_id=article_id)
    article.delete()
    comment.delete()
    return redirect('home')

# Link view

def links(request, link_name):
    links = LinkModel.objects.all()
    link_id = LinkModel.objects.get(subbeddit=link_name)
    articles = ArticlesModel.objects.filter(group=link_id.id)
    return render(request, 'link.html', {'articles': articles, 'link_name': link_name, 'links': links})

def new_link(request):
    if request.method == 'GET':
        return render(request, 'new_link.html', {'form': LinkForm()})
    else:
        form = LinkForm(request.POST)
        new_link = form.save(commit=False)
        new_link.save()
        return redirect('home')

# Like view

def like(request, article_id):
    like = ArticlesModel.objects.get(id=article_id)
    like.likes.add(request.user)
    return redirect('article_view', article_id)

def dislike(request, article_id):
    like = ArticlesModel.objects.get(id=article_id)
    like.likes.remove(request.user)
    return redirect('article_view', article_id)

def comments_like(request, article_id, comment_id):
    like = CommentsModel.objects.get(id=comment_id)
    like.likes.add(request.user)
    return redirect('article_view', article_id)

def comments_dislike(request, article_id, comment_id):
    like = CommentsModel.objects.get(id=comment_id)
    like.likes.remove(request.user)
    return redirect('article_view', article_id)

# Profile view

def profile_view(request, profile_name):
    profile_user = User.objects.get(username=profile_name)
    return render(request, 'profile.html', {'user': profile_user})

def profile_post(request, profile_name):
    articles = ArticlesModel.objects.filter(user=User.objects.get(username=profile_name))
    return render(request, 'profile_post.html', {'articles': articles})

def profile_comments(request, profile_name):
    current_comments = CommentsModel.objects.filter(user=User.objects.get(username=profile_name))
    return render(request, 'profile_comments.html', {'current_comments': current_comments})

# Comments view

def edit_comment(request, article_id, comment_id):
    current_article = get_object_or_404(ArticlesModel, pk=article_id)
    current_comments = CommentsModel.objects.filter(article_id=article_id)
    comment = CommentsModel.objects.get(id=comment_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=comment) # instance - берет текущие данные с формы под aritcle_id
        if form.is_valid():
            form.save()
            return redirect('article_view', article_id)
    else:
        form = CommentsForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'current_article': current_article, 'current_comments': current_comments})
    
def delete_comment(request, article_id, comment_id):
    comment = CommentsModel.objects.get(id=comment_id)
    comment.delete()
    return redirect('article_view', article_id)