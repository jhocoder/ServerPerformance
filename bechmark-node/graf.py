import matplotlib.pyplot as plt
import numpy as np


servidores = ['Apache', 'Nginx', 'ApachePHP', 'NginxPHP', 'Node']
requests_per_second = [1598.04, 1552.29, 1658.93, 1598.04, 2000]  
time_per_request = [0.626, 0.644, 0.603, 0.626, 0.5]  #
transfer_rate = [1125.18, 1092.97, 1168.06, 1150, 1500]  #


fig, axs = plt.subplots(1, 3, figsize=(15, 5))


axs[0].bar(servidores, requests_per_second, color='skyblue')
axs[0].set_title('Requests per second')
axs[0].set_ylabel('Requests per second')
axs[0].set_xlabel('Servidor')


axs[1].bar(servidores, time_per_request, color='lightgreen')
axs[1].set_title('Time per request (ms)')
axs[1].set_ylabel('Time per request (ms)')
axs[1].set_xlabel('Servidor')


axs[2].bar(servidores, transfer_rate, color='lightcoral')
axs[2].set_title('Transfer rate (Kbytes/sec)')
axs[2].set_ylabel('Transfer rate (Kbytes/sec)')
axs[2].set_xlabel('Servidor')


plt.tight_layout()


plt.show()