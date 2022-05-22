from django.contrib import admin
from .models import Book


# Register your models here.
class BookManager(admin.ModelAdmin):
    # 显示列表字段
    list_display = ['id', 'title', 'price']
    # 控制链接到修改页
    list_display_links = ['title']
    # 过滤器(分类器)
    list_filter = ['title']
    # 搜索框(模糊查询)
    search_fields = ['title']
    # 添加在列表页可编辑字段
    list_editable = ['price']


admin.site.register(Book, BookManager)
