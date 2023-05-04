from django.db import models



class Socialmedia(models.Model):
    facebook = models.CharField(max_length=255, unique=True,default=' ')
    twitter =  models.CharField(max_length=255, unique=True,default=' ')
    instagram = models.CharField(max_length=255, unique=True,default=' ')
    whatsapp =  models.CharField(max_length=255, unique=True,default=' ')


    class Meta:
        verbose_name_plural = "Social media url"

    def __str__(self):
        return self.facebook

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    
    def whatsapp_link(self):
        return f"https://api.whatsapp.com/send/?phone={self.whatsapp}&text=Hello%20World!&type=phone_number&app_absent=0"
    



    

class Contact(models.Model):
    mobile = models.CharField(max_length=255, unique=True,default=' ')
    email =  models.CharField(max_length=255, unique=True,default=' ')
    address = models.CharField(max_length=255, unique=True,default=' ')


    class Meta:
        verbose_name_plural = "Contacts infromation"

    def __str__(self):
        return self.mobile

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass