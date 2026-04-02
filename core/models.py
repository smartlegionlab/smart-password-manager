from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteConfig(SingletonModel):
    name = models.CharField(max_length=100, default='Smart Password Manager')
    description = models.TextField(default='Smart Password Manager')
    email = models.EmailField(default='')

    @property
    def has_empty_fields(self):
        status = all(
            [
                self.name,
                self.description,
                self.email,
            ]
        )
        return status

    def __str__(self):
        return self.name
