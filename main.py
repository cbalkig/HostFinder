import argparse
import os
import ipaddress

parser = argparse.ArgumentParser("Host Finder")
parser.add_argument("--p",
                    dest="prefix",
                    help="The prefix of the network like 192.168.0",
                    type=str,
                    default="192.168.0")
args = parser.parse_args()

if __name__ == "__main__":
    detected_host_list = []
    prefix = args.prefix
    prefix = prefix.strip()
    if not prefix.endswith("."):
        prefix += "."

    for i in range(0, 255):
        host = prefix + str(i)

        try:
            ip = ipaddress.ip_address(host)
        except:
            print('Not valid IP : %s' % host)
            continue

        response = os.system("ping -c 1 " + host)
        if response == 0:
            detected_host_list.append(host)

    print('------------------------')
    print('Accessible host list:')
    for host in detected_host_list:
        print('%s' % host)
