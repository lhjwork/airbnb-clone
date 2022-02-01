from django.contrib import admin
from . import models 
from django.contrib.auth.admin import UserAdmin
from test.test_c_locale_coercion import AVAILABLE_TARGETS

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    #fieldsets은 tuple을 가지고 있다. 
    fieldsets = UserAdmin.fieldsets+ (
        (
            "Banana",
            {
                "fields":(
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    
              )
            }
        ),
    )

#admin.site.register(models.User, CustomUserAdmin)
