import pandas as pd
import numpy as np
import xlrd
import datatypets
def main():
	data_path=sys.argv[1]
	data = xlrd.open_workbook('%s'%(data_path))
	datatypets.datatypetf(data)
if __name__ == '__main__':
	main()