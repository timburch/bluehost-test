I developed my solution on an AWS EC2 instance (http://35.153.193.70/) using the Bitnami Django Stack image. You can test my solution there.

I ran out of time before I could finish the 'EMAIL' functionality. That page is essentially a placeholder, displaying the same content as 'LIST.'

Given more time, I would finish that last module using Django's QuerySet API, specifically the union function; develop an authentication layer, unit tests, and better form validation, e.g., ensuring that an uploaded CSV file is properly formatted; and generally tidy up the code, which is a bit messy. I might also merge the templates for ADD and LOAD into one, passing it the appropriate form based on the action.

Please let me know if you have any questions. Thanks.