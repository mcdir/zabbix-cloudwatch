from pyZabbixSender import pyZabbixSender

test_host="zabbix agent"

# Creating a sender object
z = pyZabbixSender(server="zabbix-server", port=10051)

# Adding data (without timestamp)
z.addData(host=test_host, key="RDS.BinLogDiskUsage.Average", value="777")

# Ready to send your data?
results = z.sendData()

# Check if everything was sent as expected
if results[0][0] != z.RC_OK:
  print("oops!")

print(results)

