
import re

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import exceptions
import yaml
import json


class LibraryListJobs(object):

  def __init__(self, dataset=None,state_filter=None):

    from google.cloud import bigquery
    #client = bigquery.Client(project='your_project)
    client = bigquery.Client()
    dataset = client.dataset(dataset)

    for j in client.list_jobs(state_filter=state_filter):
        if (j.job_type=='query'):
          print j.job_id
          break
