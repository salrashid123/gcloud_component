# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.macro import library_list_jobs


class LibraryListJobs(base.Command):
  """Lists currently running BQ jobs"""

  detailed_help = {
      'DESCRIPTION':
          'List BQ Jobs in a given running state',
      'EXAMPLES':
          """\
          List all against a dataset in a given running state

          """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--dataset',
        required=True,
        help='Dataset in context')
    parser.add_argument(
        '--state_filter',
        required=True,
        choices=sorted(['running','pending','done']),
        help='state_filter for the job,in context')

  def Run(self, args):
    print args
    library_list_jobs.LibraryListJobs(args.dataset,args.state_filter)
