from django.contrib import admin
from .models import User, product, categories
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# class UserAdmin(UserAdmin):
#     model = User()
#     fieldsets = UserAdmin.fieldsets + (
#         ('Extra Fields', {'fields':
#                               ('atype',
#                                'earning',
#                                'name')}),
#     )


admin.site.register(User)
admin.site.register(product)
admin.site.register(categories)
#admin.site.register(report)