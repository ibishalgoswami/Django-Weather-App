from django.db import models

# Create your models here.
class Weather_details(models.Model):

    city = models.CharField(max_length = 120)
    temp = models.FloatField()
    weather_details = models.CharField(max_length = 120)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Weather_details_by_users'