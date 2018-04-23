##### 作业要求


```
1. 运行程序列出主机组或者主机列表
2. 选择指定主机或主机组
3. 选择让主机或者主机组执行命令或者向其传输文件（上传/下载）
4. 充分使用多线程或多进程
5. 不同主机的用户名密码、端口可以不同
```


##### 功能实现

```
1、创建主机
2、运行程序列出主机列表
3、选择指定主机或主机组
4、选择让主机或主机组执行命令或传输文件
```


##### 脚本文件介绍

```
D:.
│  REMINE
│
├─bin
│      start.py      # 类Farbic启动程序脚本
│      __init__.py
│
├─conf
│  │  settings.py    # 目录配置文件脚本
│  │  settings.pyc
│  │  __init__.py
│  │  __init__.pyc
│  │
│  └─__pycache__
│          settings.cpython-35.pyc
│          settings.cpython-36.pyc
│          __init__.cpython-35.pyc
│          __init__.cpython-36.pyc
│
├─db                # 主机存放目录
│      192.168.180.72
│
├─lib
│  │  common.py     # 日志生成脚本
│  │  common.pyc
│  │  main.py       # 主函数脚本部分
│  │  main.pyc
│  │  __init__.py
│  │  __init__.pyc
│  │
│  └─__pycache__
│          common.cpython-35.pyc
│          common.cpython-36.pyc
│          main.cpython-35.pyc
│          main.cpython-36.pyc
│          __init__.cpython-35.pyc
│          __init__.cpython-36.pyc
│
├─localhost       # 文件存放目录
│      __init__.py
│
└─logs            # 日志存放目录
        sys_messages.log
        __init__.py
```



##### 程序使用示例

一、创建新主机

```
|----- Welcome To Fabric Host management interface -----
    1: create new host
    2: connect host
    3: command host
    4: exit program
     
Input You Choice>>>:1
Input hostname>>>:192.168.165.41
Input host port>>>:22
Input login username>>>:root
Input login password>>>:NFjd1234
 create host success....
```


二、创建连接主机

```
Input You Choice>>>:2
D:\Python3VisualStudio\FarbicHostManage\db/192.168.165.41
D:\Python3VisualStudio\FarbicHostManage\db/192.168.180.72
|----- host list -----
 	 hostname: 192.168.165.41 
 host[192.168.165.41]connect success... 
 	 hostname: 192.168.180.72 
 host[192.168.180.72]connect success... 
```

三、登陆主机，执行操作命令


```
Input You Choice>>>:3
D:\Python3VisualStudio\FarbicHostManage\db/192.168.165.41
D:\Python3VisualStudio\FarbicHostManage\db/192.168.180.72
 connect host: 
 1:192.168.165.41 
 2:192.168.180.72 
Input You choice host>>>:1
Input command[q=quit]>>>:help
 
|------- [help] -------
    1: [put     ] upload files.
    2: [get     ] download files.
    3: [df      ] show disk info.
    4: [ls      ] view file or dirname.
    5: [uname   ] view the system information.
    6: [ifconfig] view the network information
     
Input command[q=quit]>>>:df -h
Filesystem           Size  Used Avail Use% Mounted on
/dev/mapper/cl-root   37G  3.0G   35G   8% /
devtmpfs             910M     0  910M   0% /dev
tmpfs                920M     0  920M   0% /dev/shm
tmpfs                920M   17M  904M   2% /run
tmpfs                920M     0  920M   0% /sys/fs/cgroup
/dev/sda1           1014M  186M  829M  19% /boot
tmpfs                184M     0  184M   0% /run/user/0

Input command[q=quit]>>>:ls
anaconda-ks.cfg
epel-release-7-9.noarch.rpm
jumpserver
pysphere-0.1.7
pysphere-0.1.7.zip
pysphere-master
pysphere-master.zip
SDKDemo
vsphere-automation-sdk-python

Input command[q=quit]>>>:ifconfig
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.165.41  netmask 255.255.255.224  broadcast 192.168.165.63
        inet6 fe80::250:56ff:feb0:66cc  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:b0:66:cc  txqueuelen 1000  (Ethernet)
        RX packets 3843150  bytes 300289217 (286.3 MiB)
        RX errors 0  dropped 261091  overruns 0  frame 0
        TX packets 3519459  bytes 190197393 (181.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1  (Local Loopback)
        RX packets 36977752  bytes 7897775181 (7.3 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 36977752  bytes 7897775181 (7.3 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


Input command[q=quit]>>>:get
Input download files path>>>:/root/epel-release-7-9.noarch.rpm
 host [192.168.165.41] error：[Errno 2] No such file 
Input command[q=quit]>>>:/root/anaconda-ks.cfg

Input command[q=quit]>>>:quit

Input command[q=quit]>>>:q
 
|----- Welcome To Fabric Host management interface -----
    1: create new host
    2: connect host
    3: command host
    4: exit program
     
```

四、退出操作程序

```
|----- Welcome To Fabric Host management interface -----
    1: create new host
    2: connect host
    3: command host
    4: exit program
     
Input You Choice>>>:4
 exit program success.... 
```
