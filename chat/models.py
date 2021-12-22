from datetime import datetime
from django.db import models

class Msg(models.Model):
    pub_date = models.DateTimeField('date published', default=datetime.today())
    words = models.TextField(default=' ')
