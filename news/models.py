# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)