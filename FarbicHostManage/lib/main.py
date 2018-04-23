#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import pickle
import threading
import paramiko

far_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(lib_dir)
sys.path.append(far_dir)
from common import show
from conf import settings


def create_host():
    """
    create a new host method.save host name, host port, user name and user password in file form.
    :return:
    """
    hostname = input("Input hostname IP>>>:").strip()
    port = input("Input host ssh port>>>:").strip()
    username = input("Input host login username>>>:").strip()
    password = input("Input host login password>>>:").strip()

    host_dict = {
        "hostname":hostname,
        "port":port,
        "username":username,
        "password":password,
        "status":0
    }
    host_dir = settings.HOST_DIR + "/" + hostname
    if hostinfo_write(host_dict,hostname):
        show("create host success....","info")
        return True
    else:
        show("create host error....","error")
        return False


def connect_host():
    """
    connect host method,
    :return:
    """
    hostinfo_list = hostinfo_read()
    if len(hostinfo_list) == 0:
        print("\033[31;1m There is no host at the moment. Please create the host first \033[0m")
        exit()
    print("\033[32;1m|----- host list -----\033[0m")
    for dic in hostinfo_list:
        show("\t hostname: %s"%dic["hostname"],"msg")
        TH = threading.Thread(target=ssh_parse,args=(dic,))
        TH.setDaemon(True)
        TH.start()
        TH.join()


def ssh_parse(dic):
    """
    use ssh connect host.if can't connect ,make it's status to 0 ,else to 1
    :param dic:
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=dic["hostname"],
                    port=int(dic["port"]),
                    username=dic["username"],
                    password=dic["password"])
    except Exception as e:
        show("host[%s] connect failed...\t Reason:%s"%(dic["hostname"],e),"error")
        dic["status"] = 0
        hostinfo_write(dic,dic["hostname"])
    else:
        show("host[%s]connect success..."%(dic["hostname"]),"a")
        dic["status"] = 1
        hostinfo_write(dic,dic["hostname"])
    ssh.close()


def hostinfo_read():
    """
    list host info
    :return:
    """
    hostinfo_list = []
    for file in os.listdir(settings.HOST_INFO):
        filename = settings.HOST_INFO + "/" + file
        print(filename)
        hostinfo_list.append(pickle.load(open(filename,"rb")))
    return hostinfo_list


def hostinfo_write(host_dict,hostname):
    """
    save the content to the file with pickle..
    :param host_dict: document content
    :param hostname: file name
    :return:
    """
    hostfile = settings.HOST_INFO + "/" + hostname
    with open(hostfile,"wb") as f:
        f.write(pickle.dumps(host_dict))
        return True


def run_host():
    """
    operate command host
    :return:
    """
    try:
        active_host = []
        hostinfo_list = hostinfo_read()
        for dic in hostinfo_list:
            if dic["status"] == 1:
                active_host.append(dic)

        if len(active_host) == 0:
            print("\033[31;1m At present, there is no connection host. "
                  "Please connect the host first to ensure that the host can connect properly \033[0m")
            exit()
        show("connect host:","msg")
        for i,j in enumerate(active_host):
            show("%s:%s"%(i+1,j["hostname"]),"msg")

        chioce = input("Input You choice host>>>:").strip()
        if chioce == "all":
            host_parse(active_host)
        else:
            list = []
            list.append(active_host[int(chioce)-1])
            host_parse(list)
    except Exception as e:
        show("chioce run host error....", "error")


def host_parse(list):
    while True:
        command = input("Input command[q=quit]>>>:").strip()
        if command == "help":
            help_info = """
|------- [help] -------
    1: [put     ] upload files.
    2: [get     ] download files.
    3: [df      ] show disk info.
    4: [ls      ] view file or dirname.
    5: [uname   ] view the system information.
    6: [ifconfig] view the network information
    """
            show(help_info,"msg")
        elif command == "put":
            dir = input("Input upload files name>>>:").strip()
            local_dir = settings.LOCAL_DIR + "/" + dir
            if not os.path.exists(local_dir):
                show("filename doesn't exist...","msg")
            dir0 = input("Input file path>>>:").strip()
            for dic in list:
                TH = threading.Thread(target=put_method, args=(dic, local_dir, dir0,))
                TH.start()
                TH.join()
        elif command == "get":
            dir1 = input("Input download files path>>>:").strip()
            res_list = dir1.split("/")
            local_dir = settings.LOCAL_DIR + "/" + res_list[len(res_list) - 1]
            for dic in list:
                TH = threading.Thread(target=get_method, args=(dic, dir1, local_dir,))
                TH.start()
                TH.join()
        elif command == "q":
            break
        else:
            for dic in list:
                TH = threading.Thread(target=command_method, args=(dic, command,))
                TH.start()
                TH.join()


def get_method(dic,dir, local_dir):
    try:
        nonlocal_dir = "/" + dic["username"] + dir
        transport = paramiko.Transport(dic["hostname"], int(dic["port"]))
        transport.connect(username=dic["username"], password=dic["password"])
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(nonlocal_dir, local_dir)
        show("host [%s] download file seccess" % dic["hostname"], "info")
    except Exception as e:
        show("host [%s] error：%s" % (dic["hostname"], e), "error")


def command_method(dic,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=dic["hostname"], port=int(dic["port"]), username=dic["username"], password=dic["password"])
        stdin, stdout, sterr = ssh.exec_command(command)
        result = stdout.read()
        print(result.decode())
    except Exception as e:
        show("host [%s] error：%s" % (dic["hostname"], e), "error")


def dir_read(dirname):
    """
    list dirname file
    :param dirname:
    :return:
    """
    for roots, dirs, files in os.walk(dirname):
        return files


def put_method(dic,local_dir,dir):
    try:
        nonlocal_dir = "/" + dic["username"] + dir
        print(nonlocal_dir)
        transport = paramiko.Transport(dic["hostname"], int(dic["port"]))
        transport.connect(username=dic["username"], password=dic["password"])
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_dir,nonlocal_dir)
        show("host [%s] upload file seccess.." % dic["hostname"], "info")
    except Exception as e:
        show("host [%s] error：%s" % (dic["hostname"], e), "error")


def main_func():
    """
    main function,call program function
    :return:
    """
    menu_dic = {"1":create_host,"2":connect_host,"3":run_host}
    menu_info = """
|----- Welcome To Fabric Host management interface -----
    1: create new host
    2: connect host
    3: command host
    4: exit program
    """
    while True:
        show(menu_info, "info")
        chioce = input("Input You Choice>>>:").strip()
        if chioce == "1":
            create_host()
            continue
        if chioce == "2":
            connect_host()
            continue
        if chioce == "3":
            run_host()
            continue
        if chioce == "4":
            show("exit program success....","info")
            exit()
        else:
            show("Input Error...","error")