def datatypetf(data):
	table = data.sheets()[0]
	nrows = table.nrows        
	ncols = table.ncols 
	items = ncols-2     #items is the number of item
	firstcolvalue = table.col_values(0)
	firstcolvalues = firstcolvalue[1:nrows]
	secondcolvalue = table.col_values(1)
	secondcolvalues = secondcolvalue[1:nrows]
	pingwei = list(set(firstcolvalues)) 
	xuesheng = list(set(secondcolvalues))  
	f = open('/home/klarus/temp/wenfaxueyaun/17.txt','a')
	f.write('label1\n')
	for i in range(len(pingwei)):
	    f.write(str(int(pingwei[i]))+'=')
	    f.write('\n')
	f.write('label2\n')
	for j in range(len(xuesheng)):
	    f.write(str(int(xuesheng[j]))+'=')
	    f.write('\n')
	f.write('label3\n')
	for m in range(items):
	    f.write(str(m+1)+'=')
	    f.write('\n')
	f.write('Data =')
	for i in range(nrows):
	    for j in range(ncols):
	        if i!=0:
	           if j!=2:
	              f.write(str(int(table.cell(i,j).value)))
	           else:
	              f.write('1-'+str(items)+',')
	              f.write(str(int(table.cell(i,j).value)))
	           if j!=(ncols-1):
	              f.write(',')
	    f.write('\n')
	f.close() 
