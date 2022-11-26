from django.contrib import admin

from .models import Tourist
from .models import hotels
from .models import Locals


admin.site.register(Tourist)
admin.site.register(hotels)
admin.site.register(Locals)
