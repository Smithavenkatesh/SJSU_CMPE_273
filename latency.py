#"""
#Question:
#Pick one IP from each region, find network latency from via the below code snippet
#(ping 3 times), and finally sort regions by the average latency.
#http://ec2-reachability.amazonaws.com/
#Sample output:
#1. us-west-1 [50.18.56.1] - Smallest average latency
#2. xx-xxxx-x [xx.xx.xx.xx] - x
#3. xx-xxxx-x [xx.xx.xx.xx] - x
#...
#15. xx-xxxx-x [xx.xx.xx.xx] - Largest average latency
#"""

import subprocess

str1 = "Average"
regions = ['us-east-1','us-east-2','us-west-1','us-west-2','us-gov-west-1','ca-central-1','eu-west-1','eu-central-1','eu-west-2','ap-northeast-1','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-south-1','sa-east-1']
host = ['34.192.0.54','52.15.55.0','52.8.191.254','50.112.120.53','52.222.9.163','52.60.50.0','46.51.178.50','52.28.63.252','52.56.34.0','46.51.255.254','52.79.52.64','46.137.255.254','52.62.63.252','52.66.66.2','54.94.0.66']
var1 = []

var2 = input("Do you have a Windows(1) or a MAC(2)?")
if (int(var2)) == 1:

	for num in range(0,15):
		p = subprocess.Popen(["ping", "-n", "3", host[num]],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
		out, error = p.communicate()
	
		str3 = out.decode("utf-8")#converts to string
		i = (str3).find(str1)#gets substring after 'average[10 spaces]' after getting output from ping.
		str3 = str3[i+10:].split("ms")[0]# splits ms in 10ms
		var1.append(int(str3))
#code for Mac, change in ping option
else:
	for num in range(0,15):
		p = subprocess.Popen(["ping", "-c", "3", host[num]],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
		out, error = p.communicate()
	
		str3 = out.decode("utf-8")#converts to string
		i = (str3).find(str1)#gets substring after 'average[10 spaces]' after getting output from ping.
		str3 = str3[i+10:].split("ms")[0]# splits ms in 10ms
		var1.append(int(str3))

var1,regions = zip(*sorted(zip(var1,regions)))# to sync sorting of both lists var1 and regions
print ("--------")
for num in range(0,15):
	print (regions[num],end="") 
	print("    ---    ",end="") 
	print(var1[num])
