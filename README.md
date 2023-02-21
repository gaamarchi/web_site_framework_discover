# web_site_framework_discover

project for educational purposes  
  
Project that can discover the framework that was used to build the site using python  
```python framework_discover.py path_ico```
  
  
demonstration

code used to resolve a flag of the [tryhackme](https://tryhackme.com)  
`curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico -o /desktop/favicon.ico`  
`python framework_discorver.py /desktop/favicon.ico`  
  
however if the file with the hash is damaged or want to update it use the command within the project folder  
`python scrapping.py`
  
  
  
- note
the entire base of the hash-framework relationship was picked up on [owasp](https://wiki.owasp.org/index.php/OWASP_favicon_database)'s free-to-use website
