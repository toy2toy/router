#!/usr/bin/env python3

import sys
def ip_checker(ip:str)->bool:
    segments=ip.split('.')
    if 4 != len(segments):
        print(f"{ip} is segmented into {segments}")
        return False

    for x in segments:
        if x.isnumeric():
            x_integer = int(x)
            if x_integer < 1 or x_integer >= 255:
                print(f"{x} is out of range")
                return False
        else:
            print(f"{x} is not numeric")
            return False

    return True


def main():
    if 2 != len(sys.argv):
        print(f"Usage: {sys.argv[0]} ip-address")
        sys.exit()

    ip=sys.argv[1]
    print(f"calling ip_checker {ip}")
    is_valid_ip=ip_checker(ip)
    if True == is_valid_ip:
        print(f"ip_checker says {ip} valid")
    else:
        print(f"ip_checker says {ip} invalid")

main()
