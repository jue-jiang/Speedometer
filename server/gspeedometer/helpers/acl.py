#!/usr/bin/python2.4
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper functions with access control checks."""

__author__ = 'mdw@google.com (Matt Welsh)'

from google.appengine.api import users
from google.appengine.ext import db
from gspeedometer import config


def UserIsAdmin():
  """Whether current user is an admin."""
  user = users.get_current_user()
  if user and user.email() and user.email() in config.ADMIN_USERS:
    return True
  return False
