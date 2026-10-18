#!/bin/bash
echo enter region
read region
echo enter app name
read app_name
echo enter branch name
read branch_name
echo enter download URL
read download_url

app_id=$(aws amplify create-app --name $app_name | jq -r '.app.appId')
aws amplify create-branch --app-id $app_id --branch-name $branch_name --region $region
aws amplify start-deployment --app-id $app_id --branch-name $branch_name --source-url $download_url --region $region

echo "https://$branch_name.$app_id.amplifyapp.com/"
firefox "https://$branch_name.$app_id.amplifyapp.com/"
