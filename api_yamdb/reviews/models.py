from .validators import validate_year
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='категория')
    slug = models.SlugField(unique=True,
                            verbose_name='slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=50,
                            verbose_name='жанр')
    slug = models.SlugField(unique=True,
                            verbose_name='slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'жанр'

    def __str__(self):
        return self.name


class Title(models.Model):

    name = models.CharField(max_length=50, verbose_name='тайтл')
    year = models.PositiveSmallIntegerField(
        validators=[validate_year],
        db_index=True,
    )

    description = models.TextField(verbose_name='описание')

    genre = models.ManyToManyField(Genre,
                                   related_name='titles',
                                   blank=True,
                                   verbose_name='жанр')

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 blank=True,
                                 null=True,
                                 verbose_name='категория')

    rating = models.ForeignKey('Review',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='titles')

    class Meta:
        ordering = ('year',)
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['title', 'genre'],
                                               name='title_genre')]


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        'Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        )
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='Произведение'
    )

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique_review',)
        ]


class Comment(models.Model):

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')

    review_id = models.ForeignKey(Review,
                                  on_delete=models.CASCADE,
                                  related_name='comments')

    pub_date = models.DateTimeField('Дата добавления',
                                    auto_now_add=True,
                                    db_index=True)

    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'коммент'
        ordering = ['pub_date']
