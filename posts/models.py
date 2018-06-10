from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    POST_TYPE = (
        (0, '공지사항'),
        (1, '자유게시판'),
    )
    title = models.CharField('title', max_length=50)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField('Content')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    type = models.PositiveSmallIntegerField('type', choices=POST_TYPE)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.id})

    def get_prev(self):
        return self.get_previous_by_create_date()

    def get_next(self):
        return self.get_next_by_create_date()


class PostComment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    content = models.TextField('content')

    class Meta:
        verbose_name = 'post comment'
        verbose_name_plural = 'post comments'
        ordering = ('-created_date',)

    def __str__(self):
        return self.content
