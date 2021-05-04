from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"] 
    form = RegModelForm
    # --"__unicode__", 
    # list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta:
    #     model = Registrado

# Register your models here.
admin.site.register(Registrado, AdminRegistrado)    