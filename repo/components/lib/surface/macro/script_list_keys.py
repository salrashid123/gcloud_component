# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.macro import script_list_keys
from googlecloudsdk.command_lib.macro import flags
from googlecloudsdk.command_lib.macro import util

class ScriptListKeys(base.Command):

  @staticmethod
  def Args(parser):
    flags.ScriptAddArgFlag(parser)

  def Run(self, args):
    script_list_keys.ScriptListKeys(args.some_arg)