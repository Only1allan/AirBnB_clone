#!/usr/bin/python3
"""Initialize  filestorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
