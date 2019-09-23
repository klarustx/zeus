
import pandas as pd
import sys
from SpeedDetection import *

def main():
	data_path=sys.argv[1]
	out_path=sys.argv[2]
	data = pd.read_csv('%s'%(data_path))
	caculate_process(data,out_path)
if __name__ == '__main__':
	main()
