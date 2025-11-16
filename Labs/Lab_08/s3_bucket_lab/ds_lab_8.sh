#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <local_file> <bucket_name> <expiration_seconds>"
  exit 1
fi

LOCAL_FILE="$1"
BUCKET="$2"
EXPIRATION="$3"

if [ ! -f "$LOCAL_FILE" ]; then
  echo "File not found: $LOCAL_FILE"
  exit 1
fi

OBJECT_KEY="$(basename "$LOCAL_FILE")"
S3_URI="s3://${BUCKET}/${OBJECT_KEY}"

aws s3 cp "$LOCAL_FILE" "$S3_URI"
aws s3 presign "$S3_URI" --expires-in "$EXPIRATION"
