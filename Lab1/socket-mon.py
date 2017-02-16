import psutil
from collections import OrderedDict #OrderedDict remembers the order in which the elements have been inserted:

all_process = {}

#collect all connection of type 'TCP' and check if laddr and raddr exists
for p in psutil.net_connections(kind='tcp'):
	if p.laddr and p.raddr:
		if p.pid in all_process:
			        	all_process[p.pid].append("\""+str(p.pid)+"\",\""+str(p.laddr[0])+"@"+str(p.laddr[1])+"\",\""+str(p.raddr[0])+"@"
			        		+str(p.raddr[1])+"\",\""+str(p.status)+"\"")
        	else:
    				all_process[p.pid] = ["\""+str(p.pid)+"\",\""+str(p.laddr[0])+"@"+str(p.laddr[1])+"\",\""+str(p.raddr[0])+"@"
    				+str(p.raddr[1])+"\",\""+str(p.status)+"\""]
		  

# dictionary sorted by length of the value string and then by PID if length of string are equal
print ("\"pid\",\"laddr\",\"raddr\",\"status\"")
sortedDict = OrderedDict(sorted(all_process.items(), key=lambda t: (len(t[1]),t[0]),reverse=True))

for key, value in sortedDict.items():
	for i in value:
		print (i)
