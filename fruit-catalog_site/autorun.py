#!/usr/bin/env python3
import sys
import subprocess

#Project-Specific functions:
##import get_settings
##import changeImage, supplier_image_upload, run, reports, report_email

verbose = True

def verb(text):
  if verbose:
   print(text)

def main(argv):
  verb("Collecting execution parameters...")
  #TODO:
  #Write a settings.json and a get_settings.py parser for 'arg' assignement
  ##arg = get_settings.read("settings.json")
  arg = {}
  arg["gdrive_file_id"] = dict(enumerate(argv)).get(1, "1LePo57dJcgzoK4uiI_48S01Etck7w_5f")
  arg["source_file_name"] = dict(enumerate(argv)).get(2, "supplier-data.tar.gz")
  

  #Download & Unpack
  verb("Downloading and Unpacking source files...")
  ##subprocess.call(["./download_drive_file.sh", arg["gdrive_file_id"], arg["source_file_name"])
  ##subprocess.call(["tar", "xf", arg["source_file_name"]])
  
  source_files_folder = arg["source_file_name"].split('.')[0]
  
  # @Images:
  #Resize & Convert
  verb("Resizing and Converting images in {}/images...".format(source_files_folder))
  ##changeImage.processAll(source=source_files_folder+"/images", target_dims=(600,400), target_mode="RGB", target_format=".jpeg")
  #Upload
  ##supplier_image_upload.uploadAll(source=source_files_folder+"/images", target=".jpeg")
  
  # @Descriptions
  #Parse & Post
  verb("Parsing and Posting descriptions in {}/descriptions...".format(source_files_folder))
  ##run.parsepostAll(source=source_files_folder+"/descriptions", address="http://[linux-instance-external-IP]/fruits")
  
  # @Report
  verb("Generating and sending the report PDF to the supplier...")
  #Make
  ##reports.make(###)
  #Send
  ##report_email.send(###)
  return 0

if __name__ == "__main__":
  if main(sys.argv) == 0:
    print("Execution Terminated Successfully.")
  #print("Press the Return key to exit...")
  #input("")
