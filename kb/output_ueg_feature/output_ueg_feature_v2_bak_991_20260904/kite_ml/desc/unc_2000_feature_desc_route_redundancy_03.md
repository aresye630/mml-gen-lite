# 激活静态地址用户路由冗余

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当需要保证静态IP地址网段内的用户选择到UPF的可靠性时，激活静态地址用户路由冗余功能。

**说明** 

适用PGW-C、SMF。

## 对系统的影响

该操作对系统正常运行没有影响。

## 必备事项

前提条件

请仔细阅读GWFD-020807 静态地址用户路由冗余特性概述。

数据

| 类别               | 参数名称                    | 取值样例                         | 获取方法     | 说明                                   |
|:-----------------|:------------------------|:-----------------------------|:---------|:-------------------------------------|
| ADD CPADDRPOOL   | 地址池名称（POOLNAME）         | pool01                       | 本端规划     | 为采用静态地址分配方式的用户配置对应的地址池。              |
| ADD CPADDRPOOL   | IP地址类型（IPVERSION）       | IPV4                         | 本端规划     | 为采用静态地址分配方式的用户配置对应的地址池。              |
| ADD CPADDRPOOL   | POOLTYPE（地址池类型）         | UDM                          | 本端规划     | 为采用静态地址分配方式的用户配置对应的地址池。              |
| ADD CPADDRPOOL   | CHECKIPVALID（检查地址合法性）   | Enable                       | 本端规划     | 为采用静态地址分配方式的用户配置对应的地址池。              |
| ADD CPSECTION    | Pool名称（POOLNAME）        | pool01                       | 本端规划     | 配置本地地址池里的地址段                         |
| ADD CPSECTION    | Section序号（SECTIONNUM）   | 1                            | 本端规划     | 配置本地地址池里的地址段                         |
| ADD CPSECTION    | IP类型（IPVERSION）         | IPv4                         | 本端规划     | 配置本地地址池里的地址段                         |
| ADD CPSECTION    | IPV4开始地址（V4STARTIP）     | 10.0.0.0                     | 全网规划     | 配置本地地址池里的地址段                         |
| ADD CPSECTION    | IPV4结束地址（V4ENDIP）       | 10.1.2.3                     | 全网规划     | 配置本地地址池里的地址段                         |
| ADD ADDRPOOLGRP  | POOLGRPNAME（地址池组名称）     | poolgroup01                  | 本端规划     | 配置地址池组。                              |
| ADD ADDRPOOLGRP  | POOLGRPTYPE（地址池类型）      | UDM                          | 本端规划     | 配置地址池组。                              |
| ADD POOLBINDGRP  | POOLGRPNAME（地址池组名称）     | poolgroup01                  | 已配置数据中获取 | 已通过ADD ADDRPOOLGRP配置。                |
| ADD POOLBINDGRP  | POOLNAME（地址池名称）         | pool01                       | 已配置数据中获取 | 已通过ADD CPADDRPOOL配置。                 |
| ADD UPNODE       | UPF实例名称（NFINSTANCENAME） | UPF_Instance_1UPF_Instance_2 | 全网规划     | 配置静态地址用户使用的UPF。 已通过ADD PNFPROFILE配置。 |
| ADD UPNODE       | 地址分配属性（ADDRALLOCMODE）   | INHERIT                      | 本端规划     | -                                    |
| ADD ADDRUPGROUP  | UPF组名称（UPFGRPNAME）      | upfgroup01                   | 本端规划     | 配置静态地址用户使用的UPF组。                     |
| ADD ADDRUPGROUP  | UPF组类型（UPFGRPTYPE）      | UDM                          | 本端规划     | -                                    |
| ADD UPFBINDGRP   | UPFGRPNAME（UPF组名称）      | upfgroup01                   | 已配置数据中获取 | 已通过ADD ADDRUPGROUP配置。                |
| ADD UPFBINDGRP   | UPFID（UPF实例标识）          | UPF_Instance_1UPF_Instance_2 | 已配置数据中获取 | 已通过ADD UPNODE配置。                     |
| ADD UPFBINDGRP   | PRIORITY（优先级）           | 01                           | 本端规划     | -                                    |
| ADD CPPOOLGRPMAP | MAPPINGNAME（映射名称）       | mapping01                    | 本端规划     | -                                    |
| ADD CPPOOLGRPMAP | POOLGRPNAME（地址池组名称）     | poolgroup01                  | 已配置数据中获取 | 已通过ADD ADDRUPGROUP配置。                |
| ADD CPPOOLGRPMAP | UPFGRPNAME（UPF组名称）      | upfgroup01                   | 已配置数据中获取 | 已通过ADD ADDRUPGROUP配置。                |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 创建本地静态地址地址池。

   **ADD CPADDRPOOL**
3. 配置本地地址池里的地址段。

   **ADD CPSECTION**

   **须知** 

   - 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。
   - 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。
4. 配置地址池组名称。

   **ADD ADDRPOOLGRP**
5. 配置地址池与地址池组绑定。

   **ADD POOLBINDGRP**
6. 配置静态地址用户使用的主、备UPF。

   **ADD UPNODE**
7. 配置静态地址用户使用的UPF组。

   **ADD ADDRUPGROUP**
8. 配置主、备UPF与UPF组绑定。

   **ADD UPFBINDGRP**
9. 配置地址池组与UPF组绑定。

   **ADD CPPOOLGRPMAP**

## 任务示例

任务描述

某企业用户接入网络时，为用户分配的IP地址采用静态IP地址分配方式。配置UPF名称为UPF\_Instance\_1的UPF1为主用UPF，配置UPF名称为UPF\_Instance\_2的UPF2为备用UPF，当主用UPF故障时，可以为用户选择到备用UPF进行业务，提高业务可靠性。

UPF\_Instance\_1和UPF\_Instance\_2上已经配置包含网段10.0.0.0~10.1.2.3的地址池信息，需要配置静态IP地址段10.0.0.0~10.1.2.3到UPF\_Instance\_1和UPF\_Instance\_2的关系，在主用UPF正常时，为用户选择到主用UPF，在主用UPF故障时，为用户选择到备用UPF。

脚本

//创建本地地址池。

```
ADD CPADDRPOOL: POOLNAME="pool01", IPVERSION=IPv4, POOLTYPE=UDM, CHECKIPVALID=Enable;
```

//配置本地地址池里的IPv4地址段。

```
ADD CPSECTION: POOLNAME="pool01", SECTIONNUM=1, IPVERSION=IPv4, V4STARTIP="10.0.0.0", V4ENDIP="10.1.2.3";
```

//配置地址池组名称。

```
ADD CPADDRPOOLGRP: POOLGRPNAME="poolgroup1", POOLGRPTYPE=UDM;
```

//配置地址池与地址池组绑定。

```
ADD POOLBINDGRP: POOLGRPNAME="poolgroup1", POOLNAME="pool01";
```

//配置静态地址用户使用的主、备UPF。

```
ADD UPNODE: NFINSTANCENAME="UPF_Instance_1", ADDRALLOCMODE=INHERIT;
ADD UPNODE: NFINSTANCENAME="UPF_Instance_2", ADDRALLOCMODE=INHERIT;
```

//配置静态地址用户使用的UPF组。

```
ADD ADDRUPGROUP: UPFGRPNAME="upfgroup1", UPFGRPTYPE=UDM;
```

//配置主、备UPF与UPF组绑定。

```
ADD UPFBINDGRP: UPFGRPNAME="upfgroup1", UPFID="UPF_Instance_1", PRIORITY=0;
ADD UPFBINDGRP: UPFGRPNAME="upfgroup1", UPFID="UPF_Instance_2", PRIORITY=1;
```

//配置地址池组与UPF组绑定。

```
ADD CPPOOLGRPMAP: MAPPINGNAME="mapping01", POOLGRPNAME="poolgroup1", UPFGRPNAME="upfgroup1";
```