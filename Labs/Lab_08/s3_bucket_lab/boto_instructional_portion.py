import boto3
import mimetypes

s3 = boto3.client("s3", region_name="us-east-1")

bucket = "ds2002-f25-udz4mu"
local_file = "heart.png"
key = "heart.png" 

content_type, _ = mimetypes.guess_type(local_file)
if content_type is None:
    content_type = "application/octet-stream"

with open(local_file, "rb") as f:
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=f,
        ACL="public-read",
        ContentType=content_type,
        ContentDisposition="inline"
    )

public_url = f"https://{bucket}.s3.us-east-1.amazonaws.com/{key}"
print(public_url)
