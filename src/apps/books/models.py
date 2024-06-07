from django.db import models


class Author(models.Model):
    """ Author model
    """
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    birth_date = models.DateField(verbose_name="Дата рождения")
    death_date = models.DateField(verbose_name="Дата смерти", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('-id',)


class Category(models.Model):
    """ Category model
    """
    name = models.CharField(verbose_name="Название", max_length=200, unique=True, db_index=True)
    parent = models.ForeignKey(
        to='self',
        verbose_name="Родительская категория",
        on_delete=models.SET_NULL,
        related_name='children',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)


class Book(models.Model):
    """ Book model
    """
    image = models.ImageField(verbose_name="Изображение", upload_to="books/")
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        to=Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        related_name='books'
    )
    authors = models.ManyToManyField(
        to=Author,
        verbose_name="Авторы",
        related_name='books'
    )
    publication_date = models.DateField(verbose_name="Дата публикации")
    is_published = models.BooleanField(verbose_name="Опубликован", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-id',)
