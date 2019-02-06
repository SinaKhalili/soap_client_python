from zeep import *
import time
import subprocess
import json
client = Client('http://localhost:8000/?wsdl')
currTime = time.time()
result = str(client.service.return_time())
afterTime = time.time()
elapsedTime = afterTime - currTime
timeAdjusted = elapsedTime / 2
print( " Got the JSON data in SOAP as a string : " + result)
print( " That took " + str(elapsedTime) + " secs")
print(" Converting it to JSON ")
data = json.loads(result)
print(" Extracting only the 'time' field from the JSON (which was sent over SOAP incase you forgot) ")
print(data['time'])
finalTime = data['time'] + timeAdjusted 
print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)

print("DONE")

