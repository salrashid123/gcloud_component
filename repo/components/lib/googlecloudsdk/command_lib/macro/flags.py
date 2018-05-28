

from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.util import times

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.util import completers


WRAPPER_COLLECTION = 'macro.wrapper.list_instances'
SCRIPT_COLLECTION = 'macro.script.list_keys'
LIBRARY_COLLECTION = 'macro.library.list_jobs'

# Flags.

class InstanceCompleter(completers.ListCommandCompleter):
  def __init__(self, **kwargs):
    super(InstanceCompleter, self).__init__(
        collection='macro.wrapper-list_instances',
        list_command='macro wrapper-list_instances --state',
        **kwargs)

def States(parser):
  parser.add_argument(
      'state',
      '-s',
      required=True,
      completer=InstanceCompleter,
      help='State')
