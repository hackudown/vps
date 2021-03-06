#!/usr/bin/env python

import sys
import os
import _env
from vps_mgr import VPSMgr
import conf
import getopt
from ops.saas_rpc import VM_STATE, VM_STATE_CN


def usage():
    print "%s vps_id" % (sys.argv[0])
    return


def close_vps(vps_id):
    client = VPSMgr()
    vps = None
    try:
        vps = client.query_vps(vps_id)
    except Exception, e:
        print "failed to query vps state: [%s] %s" % (type(e), str(e))
        return
    if not vps:
        print "not backend data for vps %s" % (vps_id)
        return
    if vps.state != VM_STATE.CLOSE and vps.host_id == client.host_id:
        print "vps %s state=%s, is not to be close" % (vps_id, VM_STATE_CN[vps.state])
        return
    try:
        client.vps_close(vps)
        print "done"
    except Exception, e:
        print type(e), e
    return


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage()
        os._exit(0)
    optlist, args = getopt.gnu_getopt(sys.argv[1:], "", [
        "help",
    ])

    for opt, v in optlist:
        if opt == '--help':
            usage()
            os._exit(0)
    vps_id = int(args[0])

    close_vps(vps_id)




# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 :
