#!/bin/bash
###############################################################################
#
# @ File Name  : remote_install.sh
# @ Date       : 2013-6-06
# @ Author     : gaofeilong <gfl198810@gmail.com>
# @ Usage      : ./remote_install.sh host username password
# @ Description: 远程执行命令脚本
#
# ############################################################################/

SYS_TMP_DIR=/tmp
CUR_TIME=`date +"%Y-%m-%d-%H-%M-%S"`
TMP_DIR=$SYS_TMP_DIR/$CUR_TIME
INSTALL_TAR_PACKAGE="install.sh"

# $1: host
# $2: username
# $3: password
copy_install_files()
{
        host=$1
        user=$2
        passwd=$3

        echo "$user@$host $passwd"

        ssh $user@$host 'mkdir -p $TMP_DIR' <<-EOF
gfl
EOF

}

main()
{
        if [[ $# -ne 3 ]]; then
                echo "invalid argument"
                echo "  usage: $0 host username password"
                exit 1
        fi

        copy_install_files $@
}
main $@
