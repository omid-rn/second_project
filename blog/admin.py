from django.contrib import admin
from . import models
# Register your models here.

def make_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "منتشر شد."
        else:
            message_bit = "منتشر شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,message_bit))
make_published.short_description = "مقاله به انتشار گذاشته شود"


def make_darft(modeladmin, request, queryset):
            rows_updated = queryset.update(status='d')
            if rows_updated == 1:
                message_bit = "پیش نویس شد."
            else:
                message_bit = "پیش نویس شدند"
            modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,message_bit))
make_darft.short_description = "مقاله به پیش نویس گذاشته شود."


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position","title","parent","slug","status")
    list_filter = (["status"])
    search_fields = ("description","title")
    prepopulated_fields = {'slug':('title',)}

    def category_to_str(self,obj):
        return "categories"


admin.site.register(models.Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","image_tag","slug","jpublish","status","category_to_str")
    list_filter = ("publish","status")
    search_fields = ("description","title")
    prepopulated_fields = {'slug':('title',)}
    ordering = ("-publish","status")

    def category_to_str(self,obj):
        return "‍‍، ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "دسته بندی"
    actions = [make_published,make_darft]


admin.site.register(models.Articles, ArticleAdmin)
