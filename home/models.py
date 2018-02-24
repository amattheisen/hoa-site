from django.db import models

class App(models.Model):
    app_title = models.CharField(max_length=20)

    def __str__(self):
        return self.app_title
