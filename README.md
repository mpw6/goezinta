goezinta
========

Python-based CMS system that uses Google spreadsheets on the back end.  

This is a simple CMS system that generates static web pages where the content of the pages is stored in a Google spreadsheet.  This allows end users who may only know simple HTML but who are very familiar with spreadsheets, to manage a set of webpages.

Example spreadsheet may be viewed here: https://docs.google.com/spreadsheet/ccc?key=0As1la0W5jXA3dGJUUVlNR2VteGNmS191VU9TNDRTa1E  
Example website my be viewed here:  http://goezinta.com/example/

Directory Structure:

setup/ contains Google Spreadsheet example data  
code/ contains Python code to generate pages  
www/ contains webroot example files

Requirements:

Python 2.7 (http://www.python.org/download/)  
Google gdata-2.0.14 for Python (http://code.google.com/p/gdata-python-client/downloads/list)

A google spreadsheet with the columns shown in Example.ods or Example.xls must be created and shared with a user identified in GoogleSpreadsheet.py.  
The spreadsheet ID must be added to buildPages.py.

The filepath in buildPages.py should be adjusted to match your local setup.


