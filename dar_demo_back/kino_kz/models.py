from django.db import models
from datetime import datetime


class MovieManager(models.Manager):
    def create_movie(self, id, title, genre, premiere, description, age, poster):
        movie = self.create(id=id, title=title, genre=genre, premiere=premiere, description=description,
                            age=age, poster=poster)
        return movie


class ComingSoonMovieManager(models.Manager):
    def create_movie(self, id, title, genre, premiere, description, age, poster):
        movie = self.create(id=id, title=title, genre=genre, premiere=premiere, description=description,
                            age=age, poster=poster)
        return movie

class CinemaManager(models.Model):
    def create_cinema(self, title, poster, address, phone, description):
        cinema = self.create_cinema(id=id, title=title, poster=poster, address=address, phone=phone,
                                    description=description)
        return cinema


class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=200, blank=False, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    premiere = models.DateField(blank=True, default=datetime.now())
    description = models.TextField(blank=False, null=True)
    age = models.PositiveIntegerField(default=0)
    poster = models.CharField(max_length=200, blank=True, null=True)

    objects = MovieManager()

    def __str__(self):
        return self.title


class ComingSoonMovie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=200, blank=False, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    premiere = models.DateField(blank=True)
    description = models.TextField(blank=False, null=True)
    age = models.PositiveIntegerField(default=0)
    poster = models.CharField(max_length=200, blank=True, null=True)

    objects = ComingSoonMovieManager()

    def __str__(self):
        return self.title


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    name = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Cinema(models.Model):
    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'
    title = models.CharField(max_length=200, blank=False, null=True)
    poster = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=False, null=True)
    phone = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, related_name=None, default=None)

    def __str__(self):
        return '{}'.format(self.title)


