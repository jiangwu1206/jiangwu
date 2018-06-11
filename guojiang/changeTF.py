#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from fabric.api import *
from dev_num_calc_ip import *

env.shell = "/bin/bash -c"
env.host_string = '10.0.1.132'
env.user = 'pi'
env.password = 'letmego555'
env.sudo_prefix = "sudo -S"


dev_num=900
NewIP = dev_to_ip(dev_num)
command = "sudo sed -i 's|192.168.2.45|"+NewIP+"|g' /etc/dhcpcd.conf"

try:
	run(command)
	reboot(wait=3)
except Exception as e:
	print(str(e))