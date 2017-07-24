# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.macro import wrapper_list_instances
from googlecloudsdk.command_lib.macro import flags
from googlecloudsdk.command_lib.macro import util

class WrapperListInstances(base.Command):
  """Start Cloud Endpoints App."""

  @staticmethod
  def Args(parser):
    flags.WrapperAddStateFlag(parser)

  def Run(self, args):
    wrapper_list_instances.WrapperListInstances(args.state)