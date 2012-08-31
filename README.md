goezinta
========

Python-based CMS system that uses Google spreadsheets on the back end.  

It's called goezinta, as in, "The content in this spreadsheet goezinta these web pages." This simple CMS system allows end users the ability to update the content across any number of static webpages simply by updating a spreadsheet. One row in the spreadsheet becomes one webpage. It allows end users who may only know simple HTML but who are very familiar with spreadsheets, to manage a set of webpages. It is currently a simple design, but it is very extensible. It includes a jQuery navigation menu that is sync'd across all pages.

Developed because it solved a need after regularly being asked to create sets of webpages that shared the same layout but had slightly different content on each page. Adding a page meant that all the pages had to be updated to fix the nav menus. This solves syncing the menus and allows a non-technical person to make changes to the page contents without a cumbersome content management system interface. The vast majority of business people understand spreadsheets, so this uses a spreadsheet because people understand them.

Directory Structure:

* setup/ contains Google Spreadsheet example data  
* code/ contains Python code to generate pages  
* www/ contains webroot example files

Requirements:

* Python 2.7 (http://www.python.org/download/)  
* Google gdata-2.0.14 for Python (http://code.google.com/p/gdata-python-client/downloads/list)

Explore:

* Example spreadsheet may be viewed here: https://docs.google.com/spreadsheet/ccc?key=0As1la0W5jXA3dGJUUVlNR2VteGNmS191VU9TNDRTa1E  
* Example website may be viewed here:  http://goezinta.com/example/

Get started:

* A google spreadsheet with the columns as shown abouve or in Example.ods or Example.xls must be created and shared with a user identified in GoogleSpreadsheet.py.  
* The spreadsheet ID must be added to buildPages.py.  
* The filepath in buildPages.py should be adjusted to match your local setup.

Acknowledgement and Thanks:

Funded by National Institues of Health  
Developed at Yale University for use by the School of Medicine's Vaccarino Lab http://vaccarinolab.org and Gerstein Lab http://gersteinlab.org
