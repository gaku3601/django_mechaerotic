from django.db import models

# Create your models here.
class SexyActress(models.Model):
    name = models.CharField(max_length=20, unique=True)
    memo = models.TextField()

    """
    管理画面上で表示させる項目を設定する
    """
    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=50, unique=True)
    sexyActress = models.ForeignKey(SexyActress, related_name='videos', on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    memo = models.TextField()

    def __str__(self):
        return self.title
