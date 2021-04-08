# zendesk user list fetch 


## How to run this thing
### Create and activate virtualenv
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

### Create and load .env 
```bash
$ nano .env

SUBDOMAIN=your_subdomain_for_zendesk # https://{SUBDOMAIN}.zendesk.com
EMAIL=email_for_zendesk_login
PASSWORD=password_for_zendesk_login
```
Press **ctrl + x**, then **y** and finally hit **ENTER** to save the file

### Run the program
```bash
$ python zendesk.py
```

The output files will be located under the **generated_csv** directory.
