import sys
import pandas as pd
import numpy as np
import xlrd
import datatypets
def main():
	data_path=sys.argv[1]
	out_path=sys.argv[2]
	data = xlrd.open_workbook('%s'%(data_path))
	datatypets.datatypetf(data,out_path)
if __name__ == '__main__':
	main()
