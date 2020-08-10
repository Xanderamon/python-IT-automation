#!/usr/bin/env python3

import os
import requests

ext_ip = requests.get('https://api.ipify.org').text.strip()
feedback_post_url = "http://" + str(ext_ip) + "/feedback/"

feedback_dir = "/data/feedback"

def txt_to_dict(file):
  with open(file) as f:
    dict = {"title":f.readline().strip(), "name":f.readline().strip(),
            "date":f.readline().strip(), "feedback":f.read().strip()}
    return dict

def post_feedback(dict):
  response = requests.post(feedback_post_url, json=dict)
  if response.status_code == 201:
    print("Post successful.")
  else:
    print("Post failed with status " + str(response.status_code))
#    print(response.text)

if __name__ == "__main__":
  for file in os.listdir(feedback_dir):
    if os.path.splitext(file)[1] == ".txt":
      post_feedback(txt_to_dict(os.path.join(feedback_dir,file)))
