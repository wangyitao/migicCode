#!/bin/bash
PYTHON_VERSION=3.7.3
INSTALL_DIR=/opt/python3
sed -i 's/ONBOOT=no/ONBOOT=yes/g' /etc/sysconfig/network-scripts/ifcfg-ens33
service network restart
yum -y update
yum -y groupinstall "Development tools"
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
yum -y install wget vim net-tools
wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-$PYTHON_VERSION.tar.xz
if [[ -d ${INSTALL_DIR} ]];then
    rm -rf ${INSTALL_DIR}
fi
mkdir ${INSTALL_DIR}
mv Python-${PYTHON_VERSION}.tar.xz ${INSTALL_DIR}
cd ${INSTALL_DIR}
tar -xvJf Python-${PYTHON_VERSION}.tar.xz
rm -rf Python-${PYTHON_VERSION}.tar.xz && cd Python-$PYTHON_VERSION
./configure --prefix=${INSTALL_DIR}
make && make install && make distclean
rm -rf ${INSTALL_DIR}/Python-${PYTHON_VERSION}/
if [[ -d ~/.pip ]];then
    rm -rf ~/.pip
fi
mkdir ~/.pip
echo "[global]
    index-url = https://pypi.mirrors.ustc.edu.cn/simple/
[install]
    trusted-host=mirrors.aliyun.com " > ~/.pip/pip.conf
cd ${INSTALL_DIR}/bin/
./pip3 install --no-cache-dir --upgrade pip
./pip3 install --no-cache-dir pipenv
echo "export PATH=${INSTALL_DIR}/bin/:'$PATH'" >> ~/.bashrc
echo "[mariadb]
name = MariaDB
baseurl = https://mirrors.ustc.edu.cn/mariadb/yum/10.4/centos7-amd64/
gpgkey=https://mirrors.ustc.edu.cn/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1" > /etc/yum.repos.d/mariadb.repo
yum -y update
yum -y install mariadb-server mariadb-client
echo "[mysqld]
character-set-server=utf8
collation-server=utf8_unicode_ci
skip-character-set-client-handshake" >> /etc/my.cnf
systemctl start mariadb
systemctl enable mariadb
rm -rf /var/cache/yum/*
reboot
