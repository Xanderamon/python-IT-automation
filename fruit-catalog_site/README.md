# Fruit-Catalog Site-Updater ([^0])
> version 0.0.0a
Development status
: Project Statement

## Project goal ([^1])
```
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.
```

### Development checklist
- [ ] **Download** Supplier Data
- [ ] **Unpack** Supplier Data
- [ ] **Resize** all the images from 3000x2000 to 600x400
- [ ] **Convert** all the images from RGBA.tif to RGB.jpeg
- [ ] **Upload** the new images to the fruit-catalog site
- [ ] **Parse** the descriptions into JSON format
- [ ] **Upload** the JSON descriptions to the fruit-catalog site
- [ ] **Generate** a PDF update report
- [ ] **Send** the report as email attachment to the supplier

- [ ] Create a script which regularly **checks system health**
- [ ] Make the script **send email alerts** when needed

### Extra ([^2])
- [ ] Wrap all the workflow with an 'autorun' façade and a settings json file

---
### Version log:
v0.0.0 - 2020_08_10
: Produced the first version of this README file

v0.0.0a - 2020_08_11
: Produced the first version of the autorun.py, intended as 'façade" design pattern; updated the README with additional objectives.

---
[^0]: *I really should find the time to come up with better names*

[^1]: This is the final test assignement for Coursera's [Google IT Automation with Python](https://www.coursera.org/learn/automating-real-world-tasks-python/home/welcome)

[^2]: This part of the project is an extra step/challenge outside of the test requirements
