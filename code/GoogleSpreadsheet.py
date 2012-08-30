try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom

class GoogleSpreadsheet:
	''' An iterable google spreadsheet object.  Each row is a dictionary with an entry for each field, keyed by the header.  GData libraries from Google must be installed.'''
	
	def __init__(self, spreadsheet_id, worksheet_id, user='programmer@mydomain.org', password='atleast8characters', source=''):
		gd_client = gdata.spreadsheet.service.SpreadsheetsService()
		gd_client.email = user
		gd_client.password = password
		gd_client.source = source
		gd_client.ProgrammaticLogin()
		
		self.count = 0
		self.rows = self.formRows(gd_client.GetListFeed(spreadsheet_id, worksheet_id))
		
	def formRows(self, ListFeed):
		rows = []
		for entry in ListFeed.entry:
			d = {}
			for key in entry.custom.keys():
				d[key] = entry.custom[key].text
			rows.append(d)
		return rows
			
	def __iter__(self):
		return self
		
	def next(self):
		if self.count >= len(self.rows):
			self.count = 0
			raise StopIteration
		else:
			self.count += 1
			return self.rows[self.count - 1]
	
	def __getitem__(self, item):
		return self.rows[item]
		
	def __len__(self):
		return len(self.rows)
