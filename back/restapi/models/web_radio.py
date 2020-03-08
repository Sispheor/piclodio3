from django.db import models


class WebRadio(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    # a default WebRadio is the web radio the user can launch when click on play.
    # The last started web radio become the default one
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return "[WebRadio] name: %s, url: %s, is_default: %s" % (self.name, self.url, self.is_default)
