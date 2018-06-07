from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField('Content')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_previous_post(self):
        return self.get_previous_by_create_date()

    def get_next_post(self):
        return self.get_next_by_create_date()
