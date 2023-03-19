from django.db import models

class Record(models.Model):
    long_url = models.URLField(unique = True)
    short_url = models.CharField(unique = True, max_length = 15)
    request_times = models.IntegerField(default = 0)
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = verbose_name
        db_table = "record"

    def __str__(self):
        return f"Shorten {self.long_url} to {self.short_url}"