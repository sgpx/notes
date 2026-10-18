#!/bin/bash
echo aws iam create-role --role-name lambda-iam --assume-role-policy-document "$(cat role-text.json)"
aws iam create-role --role-name lambda-iam --assume-role-policy-document "$(cat role-text.json)"
