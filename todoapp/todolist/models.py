from django.db import models


class ToDo(models.Model):
    title = models.CharField('task name', max_length=100)
    is_complete = models.BooleanField('finished', default=False)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title
