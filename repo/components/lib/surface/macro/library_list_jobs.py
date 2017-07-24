# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.macro import library_list_jobs
from googlecloudsdk.command_lib.macro import flags
from googlecloudsdk.command_lib.macro import util

class LibraryListJobs(base.Command):

  @staticmethod
  def Args(parser):
    flags.LibraryAddArgFlag(parser)

  def Run(self, args):
    library_list_jobs.LibraryListJobs(args.some_arg)