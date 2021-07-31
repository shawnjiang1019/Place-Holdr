from django.db.models.base import Model
from .forms import NewPostForm
from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Comment
from django.db.models import Q  


def search(request):
    if request.method == GET:  
        search_text = request.GET.get(search_box, None)
        records=Table.objects.filter(columnn__contains=search_text)     
        from django.http import JsonResponse
        return JsonResponse({"result_records":records})

@login_required(login_url = 'register')
def home(request):


    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(event__icontains=search_query)
    else:
        posts = Post.objects.all()
    #try organizing by user in addition to date_posted
    context = {'posts': posts.order_by('-date_posted'),
    'post_form': NewPostForm(),}
    return render(request, 'blog/home.html', context)






# Create your views here.
@login_required(login_url = 'register')
def newPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        form.instance.user = request.user
        if (form.is_valid()):
            form.save()
            messages.success(request, f'Posted')
    return redirect('blog-home')

@login_required(login_url='register')
def editPost(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        # if user hits update, then update
        post.content = request.POST['content']
        post.save() # update post
        messages.success(request, f'Successfully updated post')
        return redirect('blog-home')
    # if user is still updating form, then show form with current content
    form = NewPostForm(instance=post) # empty form with post info


    return render(request, 'blog/update.html', {'form':form,'id':id})

@login_required(login_url='register')
def like(request):
    if request.method == "GET":
        post_id = request.GET['post_id']
        liked_post = get_object_or_404(Post, id = post_id)
        if liked_post.likes.filter(username = request.user.username).count() == 1:
            liked_post.likes.remove(request.user)
            liked_post.likes_count = liked_post.likes.count()
            liked_post.save()
            return HttpResponse('-1')
        else:
            liked_post.likes.add(request.user)
            liked_post.likes_count = liked_post.likes.count()
            liked_post.save()
            return  HttpResponse('1')
    return redirect('blog-home')

@login_required(login_url='register')
def deletePost(register, id):
    #get the post using it's id and delete it
    Post.objects.get(id=id).delete()
    #Bring us back to blog-home
    return redirect("blog-home")

@login_required(login_url='register')
def comment(request):
   if request.method == "GET":
         newComment = Comment.objects.create(
           user = request.user,
           text = request.GET.get('text')
         )
 
         commented_post = Post.objects.get(id=request.GET.get('post_id')) #get the post we want to comment on 
 
         commented_post.comments.add(newComment)
         commented_post.comments_count = commented_post.comments.count()
         commented_post.save()
         messages.success(request, f'Comment Added')
   return HttpResponse('Comment Added')

@login_required(login_url='register')
def deleteComment(request, postId, commentId):
     post = Post.objects.get(id=postId)
     comment = post.comments.get(id=commentId).delete()
     post.comments_count = post.comments.count()
     post.save()
     return redirect("blog-home")

@login_required(login_url='register')
def about(request):
    return render(request, 'blog/about.html')





