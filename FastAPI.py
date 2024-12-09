#!/usr/bin/env python3
#  coding=utf-8
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: KhulnaSoft, Ltd
#  Date: 2022-06-28 15:13:25 +0100 (Tue, 28 Jun 2022)
#
#  https://github.com/BuildScale/templates
#
#  License: see accompanying KhulnaSoft, Ltd LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn
#  and optionally send me feedback to help steer this or other code I publish
#
#  https://www.linkedin.com/company/khulnasoft
#

# ============================================================================ #
#                     F a s t A P I   S t a r t e r   A p p
# ============================================================================ #

# https://fastapi.tiangolo.com/
#
# https://github.com/tiangolo/fastapi

# Usage:
#
#   pip install fastapi "uvicorn[standard]"
#
#       uvicorn <filename>:<fastapi_app>
#
#  run: uvicorn api:app --reload
#
#  http://127.0.0.1:8000
#
#  http://127.0.0.1:8000/docs   # autogenerated API docs
#
#  http://127.0.0.1:8000/redoc  # alternative API docs

# XXX: DO NOT NAME THIS FILE 'fastapi.py' as it'll break the fastapi import
#      Don't even do this with differing capitalization as it may break on case insensitive filesystems that are non-case preserving
#      It is named FastAPI.py only for convenience and ease of finding in this repo here

"""

FastAPI Starter App

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

#import logging
#import os
#import re
#import sys
#import time
#import traceback
# from typing import Union
from fastapi import FastAPI

__author__ = 'KhulnaSoft, Ltd'
__version__ = '0.1'

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}