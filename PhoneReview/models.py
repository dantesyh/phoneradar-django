from django.db import models
from django.template.defaultfilters import slugify


class Brand(models.Model):
    title = models.CharField(max_length=60)
    origin = models.CharField(max_length=20)
    manufacturing_since = models.IntegerField()
    slug = models.SlugField(max_length=150, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Model(models.Model):
    title = models.CharField(max_length=60)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    launch_date = models.DateField()
    platform = models.CharField(max_length=20)
    news_link = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    model = models.ManyToManyField(Model)
    date = models.DateField()
    slug = models.SlugField(max_length=150, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        model_slugs = list(self.model.all().values_list('slug', flat=True))
        self.slug = '%i-%s' % (self.id, slugify('-'.join(model_slugs)))
        super(Review, self).save(*args, **kwargs)
