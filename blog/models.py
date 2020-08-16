from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from extentions.utils import jalali_converter
# Create your models here.

#my manager
class AricleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)



class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null = True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name='زیر دسته')
    title = models.CharField(max_length=200, verbose_name = "عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")


    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural ="دسته بندی ها"
        ordering = [ 'parent__id','position']
    def __str__(self):
        return self.title
    objects = CategoryManager()


class Articles(models.Model):
    STATUS_CHOICE=(
    ('p','منتشر شده'),
    ('d','پیش نویس')
    )
    title = models.CharField(max_length=200, verbose_name = "عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name = "دسته بندی", related_name="article")
    description = models.TextField(verbose_name = "محتوا")
    image = models.ImageField(upload_to="images", verbose_name = "عکس")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name = "وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']
    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius:5px;' src='{}'>".format(self.image.url))
    image_tag.short_description = "عکس"

    objects = AricleManager()
