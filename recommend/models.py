from django.db import models

from article.models import Article

# Create your models here.


class Recommend(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    all_be_like = models.CharField(blank=True, null=True, max_length=500, verbose_name='所有喜欢的用户')
    class Meta:
        verbose_name = '相似度推荐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.all_be_like

    def all_be_like_increase(self, article_id):
        self.all_be_like = self.all_be_like + ',' + str(article_id)
        self.save(update_fields='all_be_like')

    def all_be_like_decrease(self, article_id):
        temp = self.all_be_like.split(',')
        temp2 = [int(i) for i in temp]
        temp2.remove(article_id)
        self.all_be_like = str(temp2)[1:-1]
        self.save(update_fields='all_be_like')