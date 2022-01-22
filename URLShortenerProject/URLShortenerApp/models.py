from django.db import models

class URLRecords(models.Model):
    long_url = models.URLField(verbose_name = "Longer URL")
    short_url = models.CharField(max_length = 15, unique = True, verbose_name = "Shorter URL")
    request_times = models.IntegerField(default = 0, verbose_name = "Shorter URL Requested Times")
    date_created = models.DateTimeField(auto_now_add = True, verbose_name = "Created Date")

    class Meta:
        verbose_name = "URLRecords"
        verbose_name_plural = verbose_name
        db_table = "URLRecords"

    def __str__(self):
        return f"Shorten {self.long_url} to {self.short_url}"