from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import CommentForm
from django.urls import reverse

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    params = {'posts': posts}
    return render(request, 'blog/post/list.html', params)


def post_details(request,	year,	month,	day,	post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    #	List	of	active	comments	for	this	post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        #	A	comment	was	posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #	Create	Comment	object	but	don't	save	to	database	yet
            new_comment = comment_form.save(commit=False)
            #	Assign	the	current	post	to	the	comment
            new_comment.post = post
            #	Save	the	comment	to	the	database
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/details.html',
                  {'post':	post,
                   'comments':	comments,
                   'new_comment':	new_comment,
                   'comment_form':	comment_form})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,  'posts': posts})


def About(request):
    return render(request, 'blog/about.html')


def Contact(request):
    return render(request, 'blog/contact.html')


def aboutWargs(request,year,month,day,post):
    return render(request, 'blog/about.html')


def contactWargs(request,year,month,day,post):
    return render(request, 'blog/contact.html')
