#-*- coding: utf-8 -*-

from django.contrib import admin
from notepad.models import Project, Note, NoteItem

admin.site.register(Project)
admin.site.register(Note)
admin.site.register(NoteItem)
