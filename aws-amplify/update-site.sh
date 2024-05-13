#!/bin/bash
echo enter region
read region
echo enter app id
read app_id
echo enter branch name
read branch_name
echo enter download URL
read download_url

aws amplify start-deployment --app-id $app_id --branch-name $branch_name --source-url $download_url --region $region

echo "https://$branch_name.$app_id.amplifyapp.com/"
firefox "https://$branch_name.$app_id.amplifyapp.com/"
