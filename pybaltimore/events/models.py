from django.db import models


class LocalEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True,
                                   max_length=200)
    date = models.DateField()
    datetime = models.DateTimeField(blank=True)
    hidden = models.BooleanField(help_text="if this is selected the event will not be shown on the public site")
    location = models.TextField(blank=True)
    external_link = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def publishable_datetime(self):
        if self.datetime:
            return self.datetime
        else:
            return self.date
