from django.db import models

# Create your models here.


class Branch(models.Model):
    class Meta:
        db_table = 'authentication_branch'

    name = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.__dict__)


class Person(models.Model):
    class Meta:
        db_table = 'authentication_person'

    id = models.IntegerField
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.__dict__)


class Country(models.Model):
    class Meta:
        db_table = 'authentication_country'

    id = models.IntegerField
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.__dict__)


class State(models.Model):
    class Meta:
        db_table = 'authentication_state'

    id = models.IntegerField
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, related_name='Country', default=1, on_delete=None)

    def __str__(self):
        return "{}".format(self.__dict__)
