from django.db import models


# Create your models here.
class Snippets(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
