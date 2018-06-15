from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from django.contrib import messages
from django.db.models import Q
from django.views.generic.detail import SingleObjectMixin

from .models import Post
from .forms import PostForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    paginate_by = 5
    ordering = ('-create_date',)

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        keyword = self.request.GET.get('q')

        if keyword:
            return queryset.filter(Q(title__contains=keyword) | Q(content__contains=keyword))
        else:
            return queryset


class PostDetailView(SingleObjectMixin, ListView):
    template_name = 'posts/detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Post.objects.all())
        return super(PostDetailView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        author = request.user
        content = request.POST.get('content')
        self.object.postcomment_set.create(author=author, content=content)
        messages.info(request, '댓글이 작성되었습니다.')
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PostDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context

    def get_queryset(self):
        return self.object.postcomment_set.order_by('created_date').all()


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

