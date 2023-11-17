from django.db import models

class Note(models.Model):
    note = models.CharField(max_length=2000, default="")
    date_at = models.DateTimeField(auto_now_add=True)
    idf = models.AutoField(primary_key=True)
