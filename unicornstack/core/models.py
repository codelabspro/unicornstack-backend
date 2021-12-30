from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    symbol=models.CharField(max_length=200)
    description=models.TextField()
    slug=models.SlugField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = "Assets"
        ordering = ["name", "created_at"]