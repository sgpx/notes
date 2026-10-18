#!/usr/bin/env python3
"""
Domain Email Security Checker for foo.com
Checks SPF, DKIM, and DMARC records and provides a status report.
Requires: pip install dnspython
"""

import dns.resolver
import dns.exception
import sys

DOMAIN = sys.argv[-1]
print("DOMAIN", DOMAIN)
def get_spf_record(domain):
    """Check SPF TXT record for domain."""
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt in rdata.strings:
                if txt.startswith(b'v=spf1'):
                    return txt.decode('utf-8'), "PASS"
        return "No SPF record found", "FAIL"
    except Exception as e:
        return f"Error: {str(e)}", "FAIL"

def get_dkim_record(domain):
    """Check default DKIM selector (default._domainkey)."""
    try:
        dkim_query = f"google._domainkey.{domain}"
        answers = dns.resolver.resolve(dkim_query, 'TXT')
        for rdata in answers:
            txt = rdata.to_text().strip('"')
            if 'v=DKIM1' in txt:
                return txt, "PASS"
        return "No default DKIM record found", "FAIL"
    except Exception as e:
        return f"No DKIM (default selector): {str(e)}", "FAIL"

def get_dmarc_record(domain):
    """Check DMARC record."""
    try:
        dmarc_query = f"_dmarc.{domain}"
        answers = dns.resolver.resolve(dmarc_query, 'TXT')
        for rdata in answers:
            txt = rdata.to_text().strip('"')
            if 'v=DMARC1' in txt:
                return txt, "PASS"
        return "No DMARC record found", "FAIL"
    except Exception as e:
        return f"Error: {str(e)}", "FAIL"

def status_report():
    """Generate comprehensive status report."""
    print(f"\n{'='*60}")
    print(f"EMAIL SECURITY CHECK REPORT for {DOMAIN}")
    print(f"{'='*60}\n")
    
    spf_record, spf_status = get_spf_record(DOMAIN)
    print(f"🔍 SPF Record:  {spf_status}")
    print(f"   {spf_record}\n")
    
    dkim_record, dkim_status = get_dkim_record(DOMAIN)
    print(f"🔍 DKIM Record: {dkim_status}")
    print(f"   {dkim_record}\n")
    
    dmarc_record, dmarc_status = get_dmarc_record(DOMAIN)
    print(f"🔍 DMARC Record:{dmarc_status}")
    print(f"   {dmarc_record}\n")
    
    # Overall status
    statuses = [spf_status, dkim_status, dmarc_status]
    passes = sum(1 for s in statuses if s == "PASS")
    
    print(f"📊 SUMMARY:")
    print(f"   PASS: {passes}/3 checks")
    print(f"   FAIL: {3-passes}/3 checks")
    
    if passes == 3:
        print("   ✅ FULLY PROTECTED")
    elif passes >= 2:
        print("   ⚠️  MOSTLY PROTECTED (Fix remaining)")
    else:
        print("   ❌ HIGH RISK - Configure email security ASAP")
    
    print(f"{'='*60}")

if __name__ == "__main__":
    status_report()
