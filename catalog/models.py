# encoding:utf-8
from django.db import models
from django.template import defaultfilters


def get_upload_path(instance, filename):
    return os.path.join(
        "catalog", filename)


class Service(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    slug = models.SlugField()
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to=get_upload_path, null=True, blank=True)
    active = models.BooleanField(verbose_name="Activo", default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("catalog_service", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name[:50])
        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Area(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    slug = models.SlugField()
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to=get_upload_path, null=True, blank=True)
    active = models.BooleanField(verbose_name="Activo", default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("catalog_area", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name[:50])
        super(Area, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Item(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    slug = models.SlugField()
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to=get_upload_path, null=True, blank=True)
    active = models.BooleanField(verbose_name="Activo", default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("catalog_item", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name[:50])
        super(Item, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name