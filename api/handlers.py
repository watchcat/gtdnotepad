#-*- coding: utf-8 -*-

from piston.handler import BaseHandler
from gtdnotepad.notepad.models import Project, Note, NoteItem

class ProjectHandler(BaseHandler):
    model = Project

class NoteHandler(BaseHandler):
    model = Note

class NoteItemHandler(BaseHandler):
    model = NoteItem


