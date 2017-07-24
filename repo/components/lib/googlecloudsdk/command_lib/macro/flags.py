

from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.util import times

WRAPPER_COLLECTION = 'macro.wrapper.list_instances'
SCRIPT_COLLECTION = 'macro.script.list_keys'
LIBRARY_COLLECTION = 'macro.library.list_jobs'

# Flags.
def WrapperAddStateFlag(parser):

  def _CompletionCallback(parser):
    del parser  # Unused by Callback.
    return ['macro', 'wrapper_list_instances', '--state' ]

  parser.add_argument(
      '--state',
      completion_resource=WRAPPER_COLLECTION,
      list_command_callback_fn=_CompletionCallback,
      required=True,
      help='PROVISIONING|STAGING|RUNNING|STOPPING|TERMINATED')

def WrapperParseStateFlag(args):
  return resources.REGISTRY.Parse(
      args.state,      
      params={'state': args.MakeGetOrRaise('--state')},
      collection=WRAPPER_COLLECTION)


def ScriptAddArgFlag(parser):

  def _CompletionCallback(parser):
    del parser  # Unused by Callback.
    return ['macro', 'script_list_keys', '--some_arg' ]

  parser.add_argument(
      '--some_arg',
      completion_resource=SCRIPT_COLLECTION,
      list_command_callback_fn=_CompletionCallback,
      required=False,
      help='some_arg')

def ScriptParseArgFlag(args):
  return resources.REGISTRY.Parse(
      args.state,      
      params={'some_arg': args.MakeGetOrRaise('--some_arg')},
      collection=SCRIPT_COLLECTION)

def LibraryAddArgFlag(parser):

  def _CompletionCallback(parser):
    del parser  # Unused by Callback.
    return ['macro', 'library_list_jobs', '--some_arg' ]

  parser.add_argument(
      '--some_arg',
      completion_resource=LIBRARY_COLLECTION,
      list_command_callback_fn=_CompletionCallback,
      required=False,
      help='some_arg')

def LibraryParseArgFlag(args):
  return resources.REGISTRY.Parse(
      args.state,      
      params={'some_arg': args.MakeGetOrRaise('--some_arg')},
      collection=LIBRARY_COLLECTION)      