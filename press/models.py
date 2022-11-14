from django.db import models

# Create your models here.

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class ServiceSubType(models.Model):
    service_type = models.ForeignKey(ServiceType, related_name="subtypes", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    service_sub_type = models.ForeignKey(ServiceSubType, related_name="services", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_delivered = models.DateTimeField()
    image = models.ImageField('services/')

    def __str__(self) -> str:
        return self.title

class Testimonies(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="testimoies/")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-date_created",)

class Message(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return " - ".join({self.name, self.subject})


class Workers(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="workers/")

    instagram_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.full_name
