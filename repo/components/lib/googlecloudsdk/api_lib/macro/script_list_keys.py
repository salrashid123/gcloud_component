
import re

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import exceptions
import yaml
import json


class ScriptListKeys(object):

  def __init__(self, some_arg="RUNNING"):

    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    import subprocess
    proc = subprocess.Popen(["list_service_account_keys.sh"],cwd=dir_path)
    out, err = proc.communicate()
    print(out)
