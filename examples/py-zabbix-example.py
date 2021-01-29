from pyzabbix import ZabbixMetric, ZabbixSender
from pyzabbix import ZabbixSender
import ssl

# Send metrics to zabbix trapper
packet = [
  ZabbixMetric('test-zabbix-host', 'RDS.BinLogDiskUsage.Average', 3),
]

result = ZabbixSender(use_config=True,socket_wrapper=lambda sock: ssl.wrap_socket(sock).send(packet)

print(result)