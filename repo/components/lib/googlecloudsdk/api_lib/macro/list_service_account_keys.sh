#!/bin/bash

for project in $(gcloud projects list --format="value(projectId)" --filter=`gcloud config list --format="value(core.project)"`)
do
  echo "ProjectId:  $project"
  for robot in $(gcloud beta iam service-accounts list --project $project --format="value(email)")
   do
     echo "    -> Robot $robot"
     for key in $(gcloud beta iam service-accounts keys list --iam-account $robot --project $project --format="value(name.basename())")
        do
          echo "        $key" 
     done
   done
done