#djangoのdbライブラリをmodelsって名前で使用できるようにするぜ
#djangoのutisライブラリをtimezoneって名前で使用できるようにするぜ
from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """カテゴリ"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#class：オブジェクトを定義するぜ！名前はPostな！
#models.Model：ポストはDjango Modelだ！データベースに保存しなきゃ！
class Post(models.Model):
    #さて、プロパティを設定するか

    #models.ForeignKey：ほかのモデルへのリンク
    #on_delete=models.CASCADE：一緒に削除される。)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_data = models.DateTimeField(
        default=timezone.now)
    published_data = models.DateTimeField(
        blank=True,null = True)
    #category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


