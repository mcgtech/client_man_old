from django.contrib import admin
from .models import Person, Note, Address, Telephone

admin.site.register(Person)
admin.site.register(Note)
admin.site.register(Address)
admin.site.register(Telephone)