from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=50, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)

    # pub = models.CharField('出版社', max_length=100, default='')

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s-%s' % (self.title, self.price)


# class Author(models.Model):
#     name = models.CharField('姓名', max_length=50,default='')
#     age = models.DecimalField('年龄',)
