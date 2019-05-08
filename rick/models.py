from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings # 引入 setings.py 文件，即可使用SEO这些字段
# from django.contrib.auth.models import User
from django.shortcuts import reverse

import markdown
import re

# 分类
class Category(models.Model):

    # 分类名字
    name = models.CharField('文章分类',max_length=128)
    # slug 用作分类路径，独一无二
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_article_list(self):
        return Article.objects.filter(category=self)

# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(
        '描述', max_length=240, default=settings.SITE_DESCRIPTION,
        help_text='用来作为SEO中description,长度参考SEO标准'
        )

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'tag': self.name})

    def get_article_list(self):
        """返回当前标签下所有发表的文章列表"""
        return Article.objects.filter(tags=self)

# 文章关键词，用来作为 SEO 中 keywords
class Keyword(models.Model):
    name = models.CharField('文章关键词', max_length=20)

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name
# 文章
class Article(models.Model):
    title = models.CharField(verbose_name="文章标题",max_length=128)
    # 文章内容
    body = models.TextField(verbose_name='文章内容')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    views = models.IntegerField(verbose_name='阅览量', default=0)
    likes = models.IntegerField(verbose_name='喜爱量', default=0)
    # 文章唯一标识符
    # 文章标记用id即可，删除分类后所有文章设为空值set_null
    category = models.ForeignKey(Category, 'on_delete=models.SET_NULL,',verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    keywords = models.ManyToManyField(
        Keyword, verbose_name='文章关键词',
        help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够'
        )

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()


