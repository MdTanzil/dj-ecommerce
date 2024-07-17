from django.db import models

# Create your models here.


class Banner(models.Model):
    """Model definition for Banner."""

    banner_image = models.ImageField(null=False, blank=True, upload_to="banner_images/")
    banner_url = models.URLField(null=False, blank=True)
    feature = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Banner."""
        self.banner_title
