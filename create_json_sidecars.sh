#!/bin/bash

path_dataset_description=$1
path_task_json=$2

echo "{
	\"Name\": \"FAKE dataset for testing BIDS curation tools\",
	\"BIDSVersion\": \"1.10.1\",
	\"DatasetType\": \"raw\",
	\"License\": \"CC0\",
	\"Authors\": \"Iacovella, V.\"
}" > $path_dataset_description

echo "{
   \"trial\":{
      \"Description\":\"The category of the trial\",
      \"Levels\":{
         \"A\":\"A\",
         \"B\":\"B\",
         \"C\":\"C\",
         \"D\":\"D\"
      }
   },
   \"response\":{
      \"Description\":\"The response given by the participant\",
      \"Levels\":{
         \"A\":\"A\",
         \"B\":\"B\",
         \"C\":\"C\",
         \"D\":\"D\",
         \"0\":\"No response\"
      }
   },
   \"rt\":{
      \"Description\":\"reaction time for giving the response\",
      \"unit\":\"s\"
   }
}" > $path_task_json

