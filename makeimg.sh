#!/bin/sh
copyfilepath=($1)
isopath=($2)
newisoname=($3)

#echo $isopath/$newisoname.iso >/tmp/isoname.txt

cd $copyfilepath
sh -x rebuild_repo.sh 

sleep 5

mkisofs -R -J -T -r -l -d -joliet-long -allow-multidot -allow-leading-dots -no-bak -o $isopath/$newisoname.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -R -J -V CentOS_WOCLOUD_KILO_x86_64 -T $copyfilepath

