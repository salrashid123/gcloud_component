# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

import datetime
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import arg_parsers

from googlecloudsdk.api_lib.macro import script_list_keys

class ScriptListKeys(base.Command):
  """Lists Service Account keys for all projects"""

  detailed_help = {
      'DESCRIPTION':
          'List Service Account keys for all projects',
      'EXAMPLES':
          """\
          List all service account keys for all service accounts and all projects.

          Optionally pass filter to only show those service account keys expiring _before_
          a certin date

          """,
  }

  @staticmethod
  def Args(parser):
    # TODO: figure out if there is a way to use type=arg_parser.Datetime.Parse())      
    parser.add_argument(
        '--validBeforeTime',
        required=False,
        default = "2020-05-28T03:26:42Z",
        help='List only service accounts valid before this time')

  def Run(self, args):
    try:
        datetime.datetime.strptime(args.validBeforeTime, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        raise ValueError("Incorrect data format, should be %Y-%m-%dT%H:%M:%SZ (eg.2020-05-28T03:26:42Z )")

    script_list_keys.ScriptListKeys(args.validBeforeTime)
