import json
from path import Path as path
import os

def get_host_url():
    PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /edx-platform/lms
    REPO_ROOT = PROJECT_ROOT.dirname()
    ENV_ROOT = REPO_ROOT.dirname()
    CONFIG_ROOT = path(os.environ.get('CONFIG_ROOT', ENV_ROOT))
    SERVICE_VARIANT = os.environ.get('SERVICE_VARIANT', None)
    CONFIG_PREFIX = SERVICE_VARIANT + "." if SERVICE_VARIANT else ""
    with open(CONFIG_ROOT / CONFIG_PREFIX + "auth.json") as auth_file:
        AUTH_TOKENS = json.load(auth_file)
    return  AUTH_TOKENS.get("HOST_URL")