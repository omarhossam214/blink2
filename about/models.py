from django.db import models

# Create your models here.

class About(models.Model):
    All_About_Company = models.TextField()
    journey = models.TextField()
    who = models.TextField()
    img =  models.ImageField(upload_to = 'images',null=True)
    Money_Back = models.TextField()
    Customer_Service = models.TextField()
    Free_Shipping = models.TextField()
    version = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return f'About (v{self.version})'

    @classmethod
    def get_latest(cls):
        return cls.objects.latest('version')

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.who

    def save(self, *args, **kwargs):
        if not About.objects.exists():
            # If there is no existing object, create one
            super().save(*args, **kwargs)
        else:
            # If an object already exists, update it instead of creating a new one
            self.pk = About.objects.first().pk
            super().save(*args, **kwargs)