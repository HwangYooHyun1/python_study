from django.contrib import admin
from .models import Address, BoardAddress, Member
# Register your models here.

admin.site.register(Address)
admin.site.register(BoardAddress)
admin.site.register(Member)
