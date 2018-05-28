
import re

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import exceptions
import yaml
import json
import os

class ScriptListKeys(object):

  def __init__(self, validBeforeTime):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    import subprocess
    proc = subprocess.Popen([dir_path + "/list_service_account_keys.sh"] + [validBeforeTime])
    out, err = proc.communicate()
    print(out)
