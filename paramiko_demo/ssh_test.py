#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/19


import paramiko


# private_key = paramiko.RSAKey.from_private_key_file("test.txt")
private_key = paramiko.RSAKey.from_private_key_file("/private/var/root/.ssh/id_rsa")

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许链接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname="192.168.16.121", port=22, pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command("shutdown -h now")

# 获取命令执行结果
result = stdout.read()
print(result)

# 关闭连接
ssh.close()
