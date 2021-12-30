from django.db import models


# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=355)
    slug = models.CharField(max_length=255, blank=True, null=True)
    countryCode = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.country


class Summary(models.Model):
    country = models.CharField(max_length=355)
    countryCode = models.CharField(max_length=55)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.country + str(self.date)


class Global(models.Model):
    country = models.CharField(max_length=355)
    countryCode = models.CharField(max_length=55)
    newConfirmed = models.IntegerField()
    totalConfirmed = models.IntegerField()
    newDeaths = models.IntegerField()
    totalDeaths = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.country
