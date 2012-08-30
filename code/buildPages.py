#!/usr/bin/python

#import cgi
#import cgitb; cgitb.enable()
import os, sys
import string
import re
from GoogleSpreadsheet import GoogleSpreadsheet

spreadsheet_id = "REPLACE_THIS_WITH_GOOGLE_SPREADHSHEET_ID"
worksheet_id = "od6"

spreadsheet = GoogleSpreadsheet(spreadsheet_id, worksheet_id)
nav_spreadsheet = GoogleSpreadsheet(spreadsheet_id, worksheet_id)

def gatherNavData(spreadsheet):
	navigation = []
	for row in spreadsheet:
		pageid = row['pageid']
		if pageid:
			navigation.append(row)
	return (navigation)

def printHeader():
	print '''<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<link rel="stylesheet" type="text/css" href="/styles.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js"></script>
<script type="text/javascript">
        $(document).ready(function() {
                setTimeout(function() {
                        // Slide
                        $('#menu1 > li > a.expanded + ul').slideToggle('medium');
                        $('#menu1 > li > a').click(function() {
                                $(this).toggleClass('expanded').toggleClass('collapsed').parent().find('> ul').slideToggle('medium');
                        });
                        $('#navigation .expand_all').click(function() {
                                $('#menu1 > li > a.collapsed').addClass('expanded').removeClass('collapsed').parent().find('> ul').slideDown('medium');
                        });
                        $('#navigation .collapse_all').click(function() {
                                $('#menu1 > li > a.expanded').addClass('collapsed').removeClass('expanded').parent().find('> ul').slideUp('medium');
                        });
                }, 250);
        });
</script>
</head>
<body>
<div id="container">
  <div id="header">
    <h1>goezinta example</h1>
  </div>
  <div id="wrapper">
    <div id="content">
'''

def printContent(row):
	content = row['content']
	if content:
		content = content.lstrip('\'')
		print content + "\n"

def printNavigation(row, navigation):
	LastMenuDepth = 0
	print'''
    </div>
  </div>
  <div id="navigation">
    <ul id="menu1" class="example_menu">
'''
	for nav in navigation:
		if nav['includeinmenu'].lstrip('\'') == "Yes" or nav['includeinmenu'].lstrip('\'') == 'Y' or nav['includeinmenu'].lstrip('\'') == 'yes' or nav['includeinmenu'].lstrip('\'') == 'y':
			IncludeInMenu = True
		else:
			IncludeInMenu = False
		if nav['includemenulink'].lstrip('\'') == "Yes" or nav['includemenulink'].lstrip('\'') == 'Y' or nav['includemenulink'].lstrip('\'') == 'yes' or nav['includemenulink'].lstrip('\'') == 'y':
			IncludeMenuLink = True
		else:
			IncludeMenuLink = False
		if nav['containssubmenu'].lstrip('\'') == "Yes" or nav['containssubmenu'].lstrip('\'') == 'Y' or nav['containssubmenu'].lstrip('\'') == 'yes' or nav['containssubmenu'].lstrip('\'') == 'y':
			ContainsSubMenu = True
		else:
			ContainsSubMenu = False
		MenuDepth = int(nav['menudepth'])
		if nav['pageid'] == row['pageid']:
			ActiveRow = True
		else:
			ActiveRow = False
		if nav['pageid'].lstrip('\'') == "/":
			Base = True
		else:
			Base = False
		if IncludeInMenu:
			if MenuDepth < LastMenuDepth:
				print "</ul></li>"
			if ActiveRow:
				print "<li class=\"active\">"
			else:
				print "<li>"
			if Base:
				if IncludeMenuLink:
					print "<a href=\"/\" "
				else:
					print "<a "
			else:
				if IncludeMenuLink:
					print "<a href=\"/" + nav['pageid'].lstrip('\'') + "/\""
				else:
					print "<a "
			if ContainsSubMenu:
				if int(row['menudepth']) > 0 and row['menugroup'] == nav['menugroup']:
					print "class = \"expanded\">" + nav['menutitle'].lstrip('\'') + "</a><ul>"
				else:
					print "class = \"collapsed\">" + nav['menutitle'].lstrip('\'') + "</a><ul>"
			else:
				print ">" + nav['menutitle'].lstrip('\'') + "</a></li>"
		LastMenuDepth = MenuDepth

	if LastMenuDepth > 0:
		print "</ul></li>"

	print'''
    </ul>
  </div>
'''

def printExtra(row):
	print "  <div id=\"extra\">\n"
	extra = row['extra']
	if extra:
		extra = extra.lstrip('\'')
		print extra + "\n"
	print "  </div>\n"

def printFooter():
	print '''
  <div id="footer">
    <p><a href="http://www.gnu.org/copyleft/">Copyleft</a> 2012</p>
  </div>
</div>
</body>
</html>'''

navigation = gatherNavData(nav_spreadsheet)

for row in spreadsheet:
	publish = row['publishpage']
	if publish.lstrip('\'') == 'Yes' or publish.lstrip('\'') == 'Y' or publish.lstrip('\'') == 'yes' or publish.lstrip('\'') == 'y':
		filepath = '/var/www/html/' + row['pageid'].lstrip('\'') 
		if not os.path.exists(filepath):
			os.makedirs(filepath)
		filename = filepath + '/index.html'
		output = open (filename, 'w')
		stdout = sys.stdout
		sys.stdout = output
	
		printHeader()
		printContent(row)
		printNavigation(row, navigation)
		printExtra(row)
		printFooter()
	
		output.close()
