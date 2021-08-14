from django.db import models

# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    # 表示名を返す
    def __str__(self):
        return self.title
