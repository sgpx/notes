#!/bin/bash
aws route53 list-hosted-zones | jq -r '.HostedZones.[] | .Id + " ### " + .Name'
