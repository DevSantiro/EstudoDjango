from django.contrib import admin

# Register your models here.

from .models import Task, Sequencia, mSequencia, Proteina

admin.site.register(Task)

admin.site.register(Sequencia)

admin.site.register(mSequencia)

admin.site.register(Proteina)
