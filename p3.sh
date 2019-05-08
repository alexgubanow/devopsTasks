#!/bin/bash
#check status of sshd and redirect result to file, include errors by following &
service ssh status &>> status.log