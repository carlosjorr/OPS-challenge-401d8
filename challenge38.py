#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: This script scans a given URL for XSS vulnerabilities in its forms.
# Date:        aug 30 2023
# Modified by: carlos rojas

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### This function retrieves all HTML forms from a given URL ###
### It's essential for locating potential points of vulnerability ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### This function extracts relevant details from a form ###
### It captures the form's action, method, and input fields ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### This function submits a form with a specified value and checks for XSS ###
### It crafts a request with the provided value and analyzes the response ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### This function performs an XSS scan on a given URL ###
### It detects potential vulnerabilities and prints the form details ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerable!")</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### This main function accepts a URL input and triggers the XSS scan ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")
    print(scan_xss(url))

#Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

#positive detection

#[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
#[+] XSS Detected on https://xss-game.appspot.com/level1/frame
#[*] Form details:
#{'action': '',
 #'inputs': [{'name': 'query',
  #           'type': 'text',
   #          'value': '<script>alert("XSS Vulnerable!")</script>'},
    #        {'name': None, 'type': 'submit'}],
 #'method': 'get'}
#True



# negative detection

#[+] Detected 1 forms on http://dvwa.local/login.php.
#False