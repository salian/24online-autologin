'''
This is a script to log in to my internet account, which has a browser-based login. 
The username and password are hard-coded.
'''
my_username = "user123"
my_password = "password123"

try:
    import mechanize
except ImportError:
    import traceback
    import sys
    traceback.print_exc(sys.stdout) # default is sys.stderr, which is the error log 
    sys.exit(1)

br = mechanize.Browser()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)
br.open("http://172.18.1.1/24online/webpages/clientlogin.jsp?loginstatus=null&logoutstatus=null&message=null&liverequesttime=null&livemessage=null&url=null&isAccessDenied=null&fromlogout=null&sessionTimeout=null")
print br.response().read()

br.select_form(name="clientloginform")
br["username"] = my_username
br["password"] = my_password
br.submit()
