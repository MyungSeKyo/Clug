from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView, RedirectView
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    paginate_by = 1
    ordering = ('-modify_date',)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        # 로그인 성공후 이전 페이지로 리다이렉션 시킴
        context['next'] = 'a'

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostForm

    def get_success_url(self):
        messages.info(self.request, '게시물이 작성되었습니다.')
        return super(PostCreateView, self).get_success_url()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    form_class = PostForm

    def get_success_url(self):
        messages.info(self.request, '게시물이 수정되었습니다.')
        return super(PostUpdateView, self).get_success_url()


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')

    def get(self, request, *args, **kwargs):
        response = self.delete(request, *args, **kwargs)
        messages.info(request, '게시물이 삭제되었습니다.')
        return response

