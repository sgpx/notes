# list all app IDs

`aws amplify list-apps | jq -r '.apps[] | .appId + " # "  +.name'`

# delete app

`aws amplify delete-app --app-id a123456`
