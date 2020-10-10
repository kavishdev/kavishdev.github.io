#!/usr/bin/env python3

# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START storage_upload_file]
from google.cloud import storage


def upload_blob(source_file_name, destination_blob_name):
    bucket_name="kavishblog.appspot.com"
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"
 # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('kavishblog-108187ed4d4f.json')
    # storage_client = storage.Client()
    emailid=storage_client.get_service_account_email(project="kavishblog")
    print("Hello is your ",emailid)
    buckets=storage_client.list_buckets()
    for b in buckets:
        print("Bucket ",b.name)

    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


# [END storage_upload_file]

if __name__ == "__main__":
    print("Arguments ",sys.argv)
    upload_blob(
        source_file_name=sys.argv[1],
        destination_blob_name="python/"+sys.argv[1],
    )
