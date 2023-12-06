#!/usr/bin/python3
"""the magic init"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
