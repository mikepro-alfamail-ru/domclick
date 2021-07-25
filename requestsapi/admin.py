from django.contrib import admin
from .models import Customers, Request, Staff, RequestsTypes

admin.site.register(Customers)
admin.site.register(Request)
admin.site.register(Staff)
admin.site.register(RequestsTypes)
