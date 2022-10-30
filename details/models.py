from django.db import models

class Details(models.Model):
    slackUsername = models.CharField(max_length=120, null=True)
    backend = models.BooleanField()
    age = models.IntegerField(max_length=2, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername

# Create your models here.
