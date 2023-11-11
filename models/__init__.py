#!/usr/bin/python3
"""
init file used to define package
and to create a unique 'FileStorege' insance
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
