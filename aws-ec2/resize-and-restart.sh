#!/usr/bin/env bash
set -euo pipefail

INSTANCE_ID=""
echo "enter instance id"
read INSTANCE_ID
echo "enter new volume size"
NEW_SIZE_GB="50"
read NEW_SIZE_GB

echo "resizing $INSTANCE_ID EBS volume to $NEW_SIZE_GB GB"

# Tag/locate root volume (assumes typical single-root setup)
ROOT_VOL_ID="$(
  aws ec2 describe-instances \
    --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].BlockDeviceMappings[?Ebs.VolumeId!=null].Ebs.VolumeId | [0]' \
    --output text
)"

if [[ -z "$ROOT_VOL_ID" || "$ROOT_VOL_ID" == "None" ]]; then
  echo "Could not determine root EBS volume for $INSTANCE_ID"
  exit 1
fi

echo "Root volume: $ROOT_VOL_ID"

# Shutdown instance
aws ec2 stop-instances --instance-ids "$INSTANCE_ID" >/dev/null
aws ec2 wait instance-stopped --instance-ids "$INSTANCE_ID"

# Modify EBS size (only increasing is allowed)
aws ec2 modify-volume --volume-id "$ROOT_VOL_ID" --size "$NEW_SIZE_GB" >/dev/null

# Wait until modification is complete
aws ec2 wait volume-available --volume-ids "$ROOT_VOL_ID"

# Restart instance
aws ec2 start-instances --instance-ids "$INSTANCE_ID" >/dev/null
aws ec2 wait instance-running --instance-ids "$INSTANCE_ID"

echo "Done: $INSTANCE_ID resized to ${NEW_SIZE_GB}GB and restarted."
