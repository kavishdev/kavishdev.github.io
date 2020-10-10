#!/usr/bin/env python

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


def download_blob(source_blob_name,destination_filename ):
    bucket_name="kavishblog.appspot.com"
     # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('kavishblog-108187ed4d4f.json')
    # storage_client = storage.Client()
    emailid=storage_client.get_service_account_email(project="kavishblog")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(source_blob_name) 
 

    print("Account Email : ",emailid)
    print("Bucket Name   : ",bucket_name) 
    print("Downloading...: ",source_blob_name)    
    print("Blob          : ",blob)

    content=blob.download_as_string()
    fname=destination_filename
    with open(fname, 'wb') as f:
        f.write(content)
        f.close()               
    
#    print("Blob Content : %s" %(content.decode("utf-8")))
    
 
if __name__ == "__main__":
    print("Arguments ",sys.argv)
    download_blob(
        source_blob_name="python/"+sys.argv[1],
        destination_filename=sys.argv[1]
    )
