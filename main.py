import argparse
import os
import ipaddress
from multiprocessing import Pool


parser = argparse.ArgumentParser("Host Finder")
parser.add_argument("--p",
                    dest="prefix",
                    help="The prefix of the network like 192.168.0",
                    type=str,
                    default="192.168.0")
args = parser.parse_args()


def ping(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return True, host
    return False, host


if __name__ == "__main__":
    detected_host_list = []
    prefix = args.prefix
    prefix = prefix.strip()
    if not prefix.endswith("."):
        prefix += "."

    query_list = []
    for i in range(0, 255):
        host = prefix + str(i)

        try:
            ip = ipaddress.ip_address(host)
            query_list.append(host)
        except:
            print('Not valid IP : %s' % host)
            continue

    with Pool(50) as p:
        result = p.map(ping, query_list)
        for ok, host in result:
            if ok:
                detected_host_list.append(host)

    print('------------------------')
    print('Accessible host list:')
    for host in detected_host_list:
        print('%s' % host)
