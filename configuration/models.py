
from django.db import models

"""
This module is intended to hold configurations such as
initial bumps limit
initial credit limit
etc
"""

class Configuration(models.Model):
    """List of configurations for the entire website"""

    # About the website
    about_us = models.TextField(default="", help_text="This is mardown enabled")
    
    
    #social media links
    #facebook link
    facebook_url = models.URLField(default="")
    #twitter link
    twitter_url = models.URLField(default="")
    #linkdn link
    linkdn_url = models.URLField(default="")
    #instagram link
    instagram_url = models.URLField(default="")
    #whatsapp link
    whatsapp_url = models.URLField(default="")
    #whatsapp link
    youtube_url = models.URLField(default="")

    #site phone
    site_phone1 = models.CharField(max_length=25,default="", help_text="Phone number associated with the website.")
    site_phone2 = models.CharField(max_length=25,default="", help_text="Phone number associated with the website.")
    site_phone3 = models.CharField(max_length=25,default="", help_text="Phone number associated with the website.")

    #site email
    site_email = models.EmailField(default="fabamall@fabamall.com")


    # extra image limits 
    def __str__(self):
        return "Site Configuration"
        
    def save(self, *args, **kwargs):
        self.id = 1
        super().save(*args, **kwargs)

    @classmethod
    def object(cls) -> 'Configuration':
        return cls.objects.get_or_create(id=1)[0]
    