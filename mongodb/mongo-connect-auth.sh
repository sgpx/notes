#!/bin/bash
instance_ip=$(cat instance_ip.txt)
port=4000
admin_username=""
admin_password=""

echo mongo "mongodb://$admin_username:$admin_password@$instance_ip:$port/admin"
mongo "mongodb://$admin_username:$admin_password@$instance_ip:$port/admin"

