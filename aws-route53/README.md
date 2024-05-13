# Route53

domain name management

# hosted zone

container for site records (DNS, routing traffic, etc)

# domains

## check domain availability

aws route53domains check-domain-availability --domain-name myapp.io

## list domains

aws route53domains list-domains

# dns and hosted zones

## list zones

aws route53 list-hosted-zones

## get zone

aws route53 get-hosted-zone --id $zone_id

## get zone DNS records

aws route53 list-resource-record-sets --hosted-zone-id $zone_id

## create new DNS record

```
{
    "Comment": "Create a new DNS record",
    "Changes": [
        {
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "xyz.foobar.com",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [
                    {
                        "Value": "1.2.3.4"
                    }
                ]
            }
        }
    ]
}
```

```
aws route53 change-resource-record-sets --hosted-zone-id /hostedzone/ABCDEFGHIJKLMNO --change-batch file://a.json
```
