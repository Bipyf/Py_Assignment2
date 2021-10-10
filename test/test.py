import sys
sys.path.insert(0, '../src') 
from news import Nnews

scrapper = Nnews()
scrapper.newspull()