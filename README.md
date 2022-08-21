# Short-URL-Serverless

This repo is for fast build a shorturl tool in aws cloud with serverless framework.
<br><br>
It has several advantages, such as:
- IAC
- Less code
---
## Build Step
1. Install env

    ```
    # install serverless in global

    npm install -g serverless
    ```

2. Prepare resource

    - Deploy with your own aws credentials
    - Apply for your own domain in aws route53
    - Create the ACM with this domain in us-east-1 (cloudfront will use it)

3. Build the tool in aws cloud
    
    Follow the README instructions for create-short-url

