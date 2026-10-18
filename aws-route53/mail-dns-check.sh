#!/bin/bash
DOMAIN="zscreen.co"

echo "=========================================="
echo " DNS DIAGNOSTIC FOR: $DOMAIN"
echo "=========================================="

echo ""
echo "--- 1. NAME SERVERS (AWS Route53 check) ---"
dig +short NS $DOMAIN

echo ""
echo "--- 2. MX RECORDS (Mail delivery) ---"
dig +short MX $DOMAIN

echo ""
echo "--- 3. SPF RECORD (Root TXT) ---"
# Grepping for v=spf1 to isolate it from other TXT records
dig +short TXT $DOMAIN | grep "v=spf1"

echo ""
echo "--- 4. DKIM RECORD (Selector: google) ---"
dig +short TXT google._domainkey.$DOMAIN

echo ""
echo "--- 5. DMARC RECORD (_dmarc) ---"
dig +short TXT _dmarc.$DOMAIN

echo ""
echo "=========================================="