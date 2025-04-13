# Cloud Resume Challenge

## Week 1 Challenge

### Website Frontend  

Create a cloud-hosted resume as the frontend of the application. You can find my [resume](https://anupamadhir.com) here.
I used HTML and CSS to build a responsive web page and hosted it in an S3 bucket as a static website behind a CloudFront(CDN) distribution.
I bought the domain name from Namecheap and used Amazon Certificate Manager to generate an SSL certificate to enable https on my website.
I setup Amazon Route 53 as the DNS provider and setup the alias records to point to the CloudFront Distribution.

![](.idea/images/Terraform-3.drawio.png)


### Route 53 Settings:

![](.idea/images/Route53.png)

### CloudFront Settings:

![](.idea/images/CloudFront.png)

![](.idea/images/CloudFront1.png)

### Certificate Manager:
Request a public Certificate in the N. Virginia Region for anupamadhir.com
and add the subdomains.
![](.idea/images/RequestCert.png)

Issued Certificate
![](.idea/images/ACM.png)

### S3 Bucket:
Created 2 Buckets. The files are uploaded to anupamadhir.com and www.anupamadhir.com redirects request to anupamadhir.com bucket.
<br>
![](.idea/images/S3Buckets.png)

<br>

#### Under Bucket Permissions turned on Block public access

![](.idea/images/S3BucketPermissions.png)


<br>

#### Enabled static website hosting for bucket

![](.idea/images/S3BucketProperties.png)

_Route 53 → Cloudfront → Certificate Manager → S3 bucket_

## Week 2 Challenge

### Backend Infrastructure  

The resume website should show the number of views. I wrote a lambda function in Python to update and fetch the number of views.  

The application flow upto this point is:  

_Lambda -> DynamoDB_  

### Connecting Frontend to Backend  

To update the views in the website, we need to connect the frontend to the backend infrastructure.  
I created and deployed a REST API using API Gateway for this purpose and added a javascript to the website to get the views using the API Gateway.
I spent a considerable amount of time getting the javascript to communicate with DynamoDB via the API Gateway. I resolved this issue by enabling CORS on API Gateway.

![](.idea/images/APIGateway.png)

The application flow upto this point is:  

_Route 53 → Cloudfront → Certificate Manager → S3 bucket → API Gateway →Lambda → DynamoDB_

## Week 3 Challenge

I terraformed my Cloud Resume Challenge. 
Terraform is an Infrastructure-as-Code(IAC) tool which I used to provision the AWS resources used in my website. I used frontend and backend modules to logically group my resources.  
This was a totally new area for me and I encountered issues running Terraform apply which I fixed by using iamadmin user since using an assumed role was the cause root cause of the problem.  
I also got errors since I needed to stringify the json response from the lambda function since I used Lambda Proxy integration in the API Gateway.

![](.idea/images/Malformedjson.png)
