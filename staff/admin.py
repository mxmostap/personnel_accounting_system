from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)
class SalaryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Salary, SalaryAdmin)
class SickListAdmin(admin.ModelAdmin):
    pass
admin.site.register(SickList, SickListAdmin)
class VacationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vacation, VacationAdmin)
