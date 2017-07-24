
import re

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import exceptions
import yaml
import json


class LibraryListJobs(object):

  def __init__(self, some_arg="RUNNING"):

    from google.cloud import bigquery
    client = bigquery.Client(project='your_project')
    dataset = client.dataset('your_dataset')

    for j in client.list_jobs(state_filter='done'):
        if (j.job_type=='query'):
          print j.id
          break