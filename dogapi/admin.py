from django.contrib import admin
from .models import Breed

class DogAdmin(admin.ModelAdmin):

    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

    fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

admin.site.register(Breed, DogAdmin)
