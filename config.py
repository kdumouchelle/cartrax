__author__ = 'Kyle Dumouchelle'
# CPSC409 final, 12/09/2015

import os

# obtain folder where this script resides
dir = os.path.abspath(os.path.dirname(__file__))
DATABASE="items.db"
USERNAME = 'kid'
PASSWORD = 'squid'
WTF_CSRF_ENABLED = True
SECRET_KEY = "b'\xfa\x1d\xb4\x12~\xed\xac0\x08\xd4S\xc1@{x\xec\x9a\xde[\x86'"

# define the full path for the database
DATABASE_PATH = os.path.join(dir, DATABASE)
