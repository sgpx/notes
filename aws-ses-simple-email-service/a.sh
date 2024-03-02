#!/bin/bash
RECIPIENT="recipient@example.com"
SENDER="sender@example.com"
SUBJECT="Test Email via AWS CLI"
BODY='This is a test email.

Foo Bar Baz.'

aws ses send-email \
    --from "$SENDER" \
    --destination "ToAddresses=$RECIPIENT" \
    --message "Subject={Data=\"$SUBJECT\"},Body={Text={Data=\"$BODY\"}}"
