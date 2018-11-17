!#/bin/bash
echo @WakkaFlakka@13! | passwd --stdin death
echo @WakkaFlakka@13! | passwd --stdin root
echo %ChuppaLuppa%13! | passwd --stdin picklerick
grep -e /bash  /etc/passwd | cut -d: -f1 > pickle.txt
sed s/^/'usermod -s @sbin@nologin '/ pickle.txt > dill.txt
sed s/'usermod -s @sbin@nologin root'/'!#@bin@bash@'/ dill.txt > llama.txt
sed s_@_'/'_ llama.txt > ugh.txt
sed s_@_'/'_ ugh.txt > ugh2.txt
sed s_@_'/'_ ugh2.txt > ugh3.txt
grep -v ‘death’ ugh3.txt > ugh4.txt
grep -v 'picklerick' ugh4.txt > fish.sh
chmod +x fish.sh


cut -d: -f1 /etc/passwd > death.txt
sed s/^/'passwd -l '/ death.txt > dill.txt
sed s/'passwd -l root'/'!#@bin@bash@'/ dill.txt > llama.txt
sed s_@_'/'_ llama.txt > ugh.txt
sed s_@_'/'_ ugh.txt > ugh2.txt
sed s_@_'/'_ ugh2.txt > ugh3.txt
grep -v ‘death’ ugh3.txt > ugh4.txt
grep -v 'picklerick' ugh4.txt > cake.sh
chmod +x cake.sh


rm -f /etc/motd
chmod 750 /usr/bin/python?
chmod 750 /usr/bin/perl
chmod 750 /etc/issue
chmod 750 /etc/issue.net
chmod 750 /usr/bin/gcc
chmod 751 /var/log/
chmod 650 /var/log/lastlog
chmod 650 /var/log/firewalld
chmod 650 /var/log/btmp
chmod 750 /bin/dmesg
chmod 750 /bin/uname
chmod 750 /home/*
echo "tty1" > /etc/securetty
yum clean metadata
dnf clean metadata
yum clean all
dnf clean all

service acpid stop
service portmap stop
service cpuspeed stop
service apmd stop
service autofs stop
service bluetooth stop
service hidd stop
service firstboot stop
service cups stop
service gpm stop
service hplip stop
service isdn stop
service kudzu stop
service kdump stop
service mcstrans stop
service pcscd stop
service readahead_early stop
service readahead_later stop
service setroubleshoot stop
service rhnsd stop
service xfs stop
service yum-updatesd stop
service avahi-daemon stop
chkconfig acpid off
chkconfig portmap off
chkconfig cpuspeed off
chkconfig apmd off
chkconfig autofs off
chkconfig bluetooth off
chkconfig hidd off
chkconfig firstboot off
chkconfig cups off
chkconfig gpm off
chkconfig hplip off
chkconfig isdn off
chkconfig kudzu off
chkconfig kdump off
chkconfig mcstrans off
chkconfig pcscd off
chkconfig readahead_early off
chkconfig readahead_later off
chkconfig setroubleshoot off
chkconfig rhnsd off
chkconfig xfs off
chkconfig yum-updatesd off
chkconfig avahi-daemon off

ifconfig up enp3s0
yum -y install wireshark ntpdate aide rsyslog

cp /etc/rsyslog.conf /etc/copyrsyslog.conf
sed s/’’*.* @@remote-host:514”/”*.* @@192.168.10.168:514”/ /etc/copyrsyslog.conf > rsyslog.conf
service rsyslog restart
rm -f /etc/copyrsyslog.conf
rm -f *.txt

