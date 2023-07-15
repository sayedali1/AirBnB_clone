#!/usr/bin/python3
""" init the storage file """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
