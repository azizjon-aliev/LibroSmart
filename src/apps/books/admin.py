from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Author, Book


class BaseModelAdmin(admin.ModelAdmin):
    """ Base model admin """
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    """ Category admin
    """
    list_display = ('name', 'parent',)
    search_fields = ('name',)
    list_filter = ('parent',)
    autocomplete_fields = ('parent',)


@admin.register(Author)
class AuthorAdmin(BaseModelAdmin):
    """ Author admin
    """
    list_display = ('first_name', 'last_name', 'birth_date', 'death_date',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('birth_date', 'death_date',)
    date_hierarchy = 'birth_date'


@admin.register(Book)
class BookAdmin(BaseModelAdmin):
    """ Book admin
    """
    list_display = ('title', 'image_preview', 'price', 'category', 'is_published',)
    search_fields = ('title', 'description',)
    list_filter = ('category', 'authors', 'is_published',)
    autocomplete_fields = ('category', 'authors',)
    readonly_fields = ('image_preview',)

    fieldsets = (
        (
            "Изображение",
            {
                'fields': (
                    'image',
                    'image_preview',
                )
            }
        ),
        (

            "Общая информация",
            {
                'fields': (
                    'title',
                    'description',
                    'price',
                    'category',
                    'authors',
                )
            },
        ),
        (
            "Публикация",
            {
                'fields': (
                    'is_published',
                    'publication_date',
                ),
            }
        )
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="{100}" height={100} />')

    image_preview.short_description = 'Превью изображения'
    image_preview.allow_tags = True
    image_preview.empty_value_display = '-пусто-'
