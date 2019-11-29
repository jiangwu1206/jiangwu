#!/bin/bash
#sed -i '/StrictHostKeyChecking/s/^#//; /StrictHostKeyChecking/s/ask/no/' /etc/ssh/ssh_config
#sed -i "/#UseDNS/ s/^#//; /UseDNS/ s/yes/no/" /etc/ssh/sshd_config

cat node.hosts | while read ip pwd; do
  sshpass -p $pwd ssh-copy-id -f $ip 2>/dev/null
done
 
