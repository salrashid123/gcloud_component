
import re

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import exceptions
import yaml
import json

from contextlib import contextmanager
import io
import sys
import googlecloudsdk.gcloud_main

@contextmanager
def stdout_redirector(stream):
    old_stdout = sys.stdout
    sys.stdout = stream
    try:
        yield
    finally:
        sys.stdout = old_stdout

class WrapperListInstances(object):

  def __init__(self, state="RUNNING"):

    f = io.StringIO()    
    _args = ['compute','instances','list','--format','json(NAME,EXTERNAL_IP,STATUS)', '--filter', 'status=' + state]
    with stdout_redirector(f):
      _CLI = googlecloudsdk.gcloud_main.CreateCLI([])
      _CLI.Execute(args=_args)
    result = f.getvalue()
    #instances = json.loads(result)
    #for instance in instances:
    #  print (instance['name'] + " has external IP address " + 
    #        instance['networkInterfaces'][0]['accessConfigs'][0]['natIP'])