import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

 
@anvil.server.callable
def get_results(kwargs):
  results = app_tables.change_notes.search(tables.order_by('change_date', ascending = False),**kwargs)
  return results