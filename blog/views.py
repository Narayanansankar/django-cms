from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import BlogPost
from blog.forms import BlogPostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'