#!/bin/bash


#Variables
SFTPHOSTNAME="192.168.1.1"
SFTPUSERNAME="user"
SFTPPASSWORD="password"
FOLDER="/home/$HOME/sftp"
#SFTP CONNECTION
output=$(/export/home/$HOME/bin/sshpass -p $SFTPPASSWORD sftp $SFTPUSERNAME@$SFTPHOSTNAME << !
    cd $FOLDER
    get data_output
 exit
!);

list="email_address@domain.com email_address@domain.com"


cat data_output | mailx -s "$(echo -e "Title name \nContent-Type: text/html")" -r email_address@domain.com $list
