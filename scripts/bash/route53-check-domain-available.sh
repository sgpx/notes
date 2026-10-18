#!/bin/bash
AWS_DEFAULT_REGION=us-east-1 aws route53domains check-domain-availability --domain-name $1
