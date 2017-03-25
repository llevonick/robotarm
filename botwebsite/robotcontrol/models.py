from __future__ import unicode_literals
from django.utils.encoding import force_bytes

from django.db import models

# Create your models here.

class Position(models.Model):
    pos_1 = models.IntegerField(default = 0)
    pos_2 = models.IntegerField(default = 0)
    pos_3 = models.IntegerField(default = 0)
    pos_4 = models.IntegerField(default = 0)
    pos_5 = models.IntegerField(default = 0)

    def __str__(self):
        return force_bytes('%d %d %d %d %d' % (self.pos_1, self.pos_2, self.pos_3, self.pos_4, self.pos_5))
