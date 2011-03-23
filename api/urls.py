#-*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from piston.resource import Resource
from gtdnotepad.api.handlers import ProjectHandler, NoteHandler, NoteItemHandler

project_resource = Resource(ProjectHandler)
note_resource = Resource(NoteHandler)
note_item_resource = Resource(NoteItemHandler)

urlpatterns = patterns('',
   url(r'^projects/(?P<id>\d+)$', project_resource),
   url(r'^projects$',project_resource),

   
)

