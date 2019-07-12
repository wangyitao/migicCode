#!/bin/bash
PYTHON_VERSION=3.7.3
INSTALL_DIR=/opt/python3
sed -i 's/ONBOOT=no/ONBOOT=yes/g' /etc/sysconfig/network-scripts/ifcfg-ens33
service network restart
yum -y update
yum -y groupinstall "Development tools"
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
yum -y install wget vim net-tools
rm -rf /var/cache/yum/*
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz
if [ ! -d $INSTALL_DIR ];then
    mkdir $INSTALL_DIR
fi
mv Python-$PYTHON_VERSION.tar.xz $INSTALL_DIR
cd $INSTALL_DIR
tar -xvJf Python-$PYTHON_VERSION.tar.xz
rm -rf Python-$PYTHON_VERSION.tar.xz && cd Python-$PYTHON_VERSION
./configure --prefix=$INSTALL_DIR
make && make install && make distclean
rm -rf $INSTALL_DIR/Python-$PYTHON_VERSION/
cd $INSTALL_DIR/bin/
./pip3 install --no-cache-dir --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
./pip3 install --no-cache-dir pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple
echo "export PATH=${INSTALL_DIR}/bin/:$PATH" >> ~/.bashrc
reboot
