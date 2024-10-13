from django.contrib import admin
from .models import Breed, Dog

class BreedAdmin(admin.ModelAdmin):

    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

    fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')
class DogAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')

    fields = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')


admin.site.register(Breed, BreedAdmin)
admin.site.register(Dog, DogAdmin)