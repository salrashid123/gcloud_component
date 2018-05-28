# Copyright 2014 Google Inc. All Rights Reserved.

"""Cloud Script start command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.macro import wrapper_list_instances

class WrapperListInstances(base.Command):
  """Lists GCE instances in a given running state"""

  detailed_help = {
      'DESCRIPTION':
           'List the instances in the current project based on state',
      'EXAMPLES':
          """\
                $ gcloud macro wrapper-list-instances --state RUNNING

                [
                  {
                    "name": "janus",
                    "networkInterfaces": [
                      {
                        "accessConfigs": [
                          {
                            "natIP": "35.193.54.213"
                          }
                        ]
                      }
                    ],
                    "status": "RUNNING"
                  }
                ]
          """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--state',
        required=True,
        choices=sorted(['RUNNING','STOPPED','TERMINATED']),
        help='Instance state to filter on.')


  def Run(self, args):
    wrapper_list_instances.WrapperListInstances(args.state)
