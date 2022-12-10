from django.contrib import admin

from .models import Tourist
from .models import hotels
from .models import Locals
from .models import POI_add
from .models import POI_rating


admin.site.register(Tourist)
admin.site.register(hotels)
admin.site.register(Locals)
admin.site.register(POI_add)
admin.site.register(POI_rating)

