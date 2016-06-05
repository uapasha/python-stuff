from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Post, Comment

class PublishedPostMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class PostListView(PublishedPostMixin, ListView):
    model = Post

class PostDetailView(PublishedPostMixin, DetailView):
    model = Post

# class CommentsView(ListView):
#     template_name = 'blog/comments.html'
#     model = Comment

#     # def get_queryset(self):
#     #     return self.model.objects.all()
def comments_all(request):
    comments_list = Comment.objects.all()
    posts = Post.objects.live()
    template_name = 'blog/comments.html'
    context = {'comments_list': comments_list,
                'posts': posts}
    return render(request, template_name, context)

def add_comment(request):
    try:
        message = request.POST['message']
        redirect_page = reverse('blog:comments')
    except KeyError:
        message = request.POST['separate_page_message']
        post_id = int(request.POST['post'])
        post = Post.objects.filter(pk = post_id)[0]
        slug = post.slug
        redirect_page = reverse('blog:detail', args = (slug,))
    
    if message == '':
        messages.add_message(request, messages.ERROR, 'You forgot to enter a message.')
        return HttpResponseRedirect(redirect_page)
    
    elif len(message) < 4:
        messages.add_message(request, messages.ERROR, 'Your message is too short.')
        return HttpResponseRedirect(redirect_page)
    
    else:
        post_id = int(request.POST['post'])
        new_comment = Comment(content = message, post = Post.objects.filter(pk = post_id)[0])
        new_comment.save()
        return HttpResponseRedirect(redirect_page)
    

        


