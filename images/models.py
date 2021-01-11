from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name


class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True)
    
