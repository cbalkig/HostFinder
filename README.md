# HostFinder

How to execute:
```
python -m pip install -r requirements.txt
python main.py --p 192.168.0
```

Output sample:
```
(venv) (base) Balks-MacBook-Pro:HostFinder balki$ python main.py --p 192.168.0
PING 192.168.0.0 (192.168.0.0): 56 data bytes

--- 192.168.0.0 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss
PING 192.168.0.1 (192.168.0.1): 56 data bytes
64 bytes from 192.168.0.1: icmp_seq=0 ttl=64 time=5.246 ms

--- 192.168.0.1 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.246/5.246/5.246/0.000 ms
PING 192.168.0.2 (192.168.0.2): 56 data bytes

...

--- 192.168.0.253 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss
PING 192.168.0.254 (192.168.0.254): 56 data bytes

--- 192.168.0.254 ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss
------------------------
Accessible host list:
192.168.0.1
192.168.0.14
192.168.0.101
(venv) (base) Balks-MacBook-Pro:HostFinder balki$ 

```
