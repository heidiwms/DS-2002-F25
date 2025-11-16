import sys
import os
import urllib.parse
import mimetypes

import boto3
import requests


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 lab8_pythonscript.py <file_url> <bucket_name> <expiration_seconds>")
        sys.exit(1)

    file_url = sys.argv[1]
    bucket_name = sys.argv[2]
    _ = int(sys.argv[3])  # not used, but kept for assignment compatibility

    # Get a reasonable key name from the URL path
    parsed = urllib.parse.urlparse(file_url)
    object_key = os.path.basename(parsed.path)
    if not object_key:
        object_key = "file.gif"

    # Guess content type from file extension (fallback to image/gif)
    content_type = mimetypes.guess_type(object_key)[0] or "image/gif"

    # Fetch the remote file into memory
    resp = requests.get(file_url, stream=True)
    resp.raise_for_status()

    s3 = boto3.client("s3", region_name="us-east-1")

    # Upload to S3 with public-read and proper Content-Type
    s3.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=resp.content,
        ContentType=content_type,
        ACL="public-read",
    )

    # Build the public URL (for us-east-1)
    public_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

    print("Public URL:")
    print(public_url)


if __name__ == "__main__":
    main()
