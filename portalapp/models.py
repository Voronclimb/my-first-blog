from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
# Create your models here.
def upload_article_image_folder(instance,filename):
    filename = instance.slug + '.' + filename.split('.')[-1]
    return "{}/{}".format(instance.slug,filename)

class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField('Заголовок статьи',max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField('Тескт статьи')
    realized = models.DateTimeField('Дата публикации',auto_now=True)
    likes = models.PositiveIntegerField('лайки',default=0)
    deslikes = models.PositiveIntegerField('дизлайки',default=0)
    image = models.ImageField('Изображение',upload_to='')

    def __str__(self):
        return "Статья '{}', из категории '{}'".format(self.title,self.category.name)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
class Coomment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor = models.CharField('',max_length=50)
    commetn_text = models.CharField('',max_length=250)

    def __str__(self):
        return "Aвтор коментария {}".format(self.autor)
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"