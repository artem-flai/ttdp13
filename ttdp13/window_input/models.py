from django.db import models

class WindowInput(models.Model):
    text_input = models.JSONField()