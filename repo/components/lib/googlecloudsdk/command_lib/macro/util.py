

import os

from googlecloudsdk.core.updater import local_state


class Error(Exception):
  """Exceptions for the endpoints_util module."""


class ScriptNotFoundError(Error):
  """An error when the parser in appcfg fails to parse the values we pass."""

  def __init__(self, error_str):
    super(ScriptNotFoundError, self).__init__(error_str)

