from django.db import models


class ToDo(models.Model):
    title = models.CharField('task name', max_length=100)
    is_complete = models.BooleanField('finished', default=False)

    class Meta:
        # singular_name = 'task'
        # plural_name = 'tasks'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title
