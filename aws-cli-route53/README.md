# list zones

aws route53 list-hosted-zones

# get zone

aws route53 get-hosted-zone --id $zone_id

# get zone DNS records

aws route53 list-resource-record-sets --hosted-zone-id $zone_id
