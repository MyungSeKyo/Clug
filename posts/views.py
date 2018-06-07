from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    paginate_by = 10
    ordering = ('-modify_date',)

