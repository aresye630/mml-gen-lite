# 修改Diameter AAA服务器组（MOD DIAMAAAGRP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C**

此命令用于修改一个Diameter AAA组。根据网络规划，需要改变PGW向Diameter AAA服务器组中Diameter AAA请求授权时携带的消息属性时，操作员可以执行此命令修改。

## 注意事项

该命令执行后对新接入的non-3GPP会话生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称                | 参数说明                                                                                                                                                                                |
|:------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GROUPNAME   | Diameter AAA组名      | 可选必选说明：必选参数  参数含义：该参数用于指定Diameter AAA组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。  默认值：无  配置原则：无                                                                            |
| PGWIDENTITY | PDN GW Identity携带方式 | 可选必选说明：可选参数  参数含义：该参数用于指定PDN GW Identity携带方式。  数据来源：全网规划 取值范围： “HOST_NAME（P-GW主机名）”：表示向Diameter AAA请求授权时携带P-GW的主机名称。“IP（P-GW IP地址）”：表示向Diameter AAA请求授权时携带P-GW的IP地址。  默认值：无  配置原则：无 |

## 使用实例

根据网络规划，需要修改名称为“diametergroup”的Diameter AAA组，设置向Diameter AAA请求授权时携带P-GW的hostname名称：

```
MOD DIAMAAAGRP:GROUPNAME="diametergroup",PGWIDENTITY=HOST_NAME;
```