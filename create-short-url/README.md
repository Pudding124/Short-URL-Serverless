# Build the tool in aws cloud

Region: us-west-2

We need setting serval input parameter, list in below:
- domain <br>
  In pervious step 2, we will get this input parameter in route53 domain.
- bucket_name <br>
  Set your s3 bucket name that is must be unique name.
- bucket_secret <br>
  This secret will set in s3 permission and cloudfront to limit access control. <br>
  if we want to request bucket, we need set this key in request header.
- api_key <br>
  This secret will set in api-gateway and cloudfront to limit access control. <br>
  if we want to request api, we need set this key in request header.
- acm arn <br>
  In pervious step 2, we will get this input parameter in acm.

## Step

1. Fill in the parameters

    - handler.py (bucket_name)
    - env-dev.yml
      ```
      stage: dev

      setting:
        domain: <your domain>
        bucket_name: <your bucket_name>
        bucket_secret: <your bucket_secret>
        api_key: <your api_key>
        acm: <your acm>
      ```
    - setting domain in index.html

2. Deploy
    ```
    # deploy with serverless.yml
    
    serverless deploy --stage dev
    ```
    ```
    # get serverless info after deploy
    
    serverless info
    ```
3. Setting cloudfront domain in route53

    Setting A record with cloudfront dns in route53

5. push index.html to s3 bucket

    Upload index.html to s3 bucket root path
