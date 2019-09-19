"""Settings to override default settings."""

import logging
import dotenv
import os
from dotenv import load_dotenv
#
# Override settings
#

# AUTH STUFF

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ENV_PATH = os.environ["ND_ENV_PATH"] # must set manually

load_dotenv(ENV_PATH)

DEBUG = True if int(os.environ["ND_DEBUG"]) == 1 else False
COOKIE_SECRET= os.environ["ND_CK_S"]
COOKIE_KEY = os.environ["ND_CK_K"]
COOKIE_TIMEOUT_SECONDS = int(os.environ["ND_CK_TO_S"])
STALE_COOKIE_TIMEOUT_SECONDS = int(os.environ["ND_CK_STO_S"])
ND_LOGON_TOKEN_NAME = os.environ["ND_CK_NAME"]

ALLOWED_USERNAME_LIST = [u.lower().strip() for u in os.environ["ND_UNAME_CSV"].split(",")]
TMP_LOCALHOST_P = os.environ["ND_TMP_LOCALHOST_P"].strip() # OMG PLZ DON"T USE THIS FOR REAL

HTTP_PORT = int(os.environ["ND_PORT"])
HTTP_ADDRESS = os.environ["ND_BIND"]

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['simple_scheduler.jobs']


