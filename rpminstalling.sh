#!/bin/sh
rpm_createrepo=`rpm -qa|grep createrepo|head -c 10`
rpm_lrzsz=`rpm -qa|grep lrzsz|head -c 5`
dir=`pwd`

if [ "$rpm_createrepo" = "createrepo" ];then
	echo "createrepo installed"
	else 
	echo "createrepo not install"
	cd $dir/rpm/createrepo
	rpm -ivh *.rpm
fi

if [ "$rpm_lrzsz" = "lrzsz" ];then
        echo "lrzsz installed"
        else
        echo "lrzsz not install"
        cd $dir/rpm/lrzsz
        rpm -ivh *.rpm
fi
