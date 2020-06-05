#!/usr/bin/env python3

import cgxinit
from cloudgenix import jd
import sys

if __name__ == "__main__":
    sdk, args = cgxinit.go()

    # read lines from file
    prefixes = [prefix.strip() for prefix in args["list"].readlines()]

    # find the prefix
    prefix = None
    natprefixes = sdk.get.natglobalprefixes().cgx_content["items"]
    for natprefix in natprefixes:
        if natprefix['name'] == args['prefix']:
            prefix = natprefix
    if not prefix:
        print("Prefix wasn't found")
        sys.exit()

    # add to the existing ipv4 list
    prefix['ipv4_prefixes'].extend(prefixes)
    # make sure all the entries are unique
    prefix['ipv4_prefixes'] = list(set(prefix['ipv4_prefixes']))

    resp = sdk.put.natglobalprefixes(prefix['id'], prefix)
    if not resp:
        print("Error. Couldn't update the global prefix list")
        jd(resp)
    else:
        print("Prefix updated succesfully")

