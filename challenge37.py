#!/usr/bin/env python3

import requests
import webbrowser

targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():

    print('''
          .---. .---.
         :     : o   :    me want cookie!
     _..-:   o :     :-.._    /
 .-''  '  `---' `---' "   ``-.
.'   "   '  "  .    "  . '  "  `.
:   '.---.,,.,...,.,.,.,..---.  ' ;
`. " `.                     .' " .'
 `.  '`.                   .' ' .'
  `.    `-._           _.-' "  .'  .----.
    `. "    '"--...--"'  . ' .'  .'  o   `.
      ''')

def send_cookie_and_open_with_browser():
    response_with_cookie = requests.get(targetsite, cookies=cookie)
    response_content = response_with_cookie.text

    # Save the response content to an HTML file
    with open('response.html', 'w') as html_file:
        html_file.write(response_content)

    # Open the HTML file in a web browser
    webbrowser.open('response.html')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

send_cookie_and_open_with_browser()
