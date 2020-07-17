from django.contrib import admin
from .models import Branch, Person, Country, State

# Register your models here.

admin.site.register(Branch)
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(State)
