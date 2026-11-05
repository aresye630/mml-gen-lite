# 查询Radius鉴权请求消息携带的属性（LST RDSAUTHREQATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来显示指定RADIUS服务器组的可选鉴权消息属性。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                                                   |
|:--------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数  参数含义：RADIUS服务器组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。 |

## 使用实例

查询名为“radiusgroup”的Radius服务器组的可选鉴权消息属性信息：

```
%%LST RDSAUTHREQATTR: RDSSVRGRPNAME="radiusgroup";%%
RETCODE = 0  操作成功

结果如下
--------
              RADIUS服务器组名称  =  radiusgroup
                 Acct-Session-Id  =  禁止
                          NAS-ID  =  禁止
                     NAS ID Type  =  APN
                    NAS ID Value  =  NULL
                            IMSI  =  禁止
                     Charging-ID  =  禁止
                     Prepaid-ind  =  禁止
                         GGSN-IP  =  禁止
                  SGSN (S-GW)-IP  =  禁止
                   Requested-APN  =  禁止
                     GGSN-Vendor  =  禁止
                    GGSN-Version  =  禁止
           Request Authenticator  =  禁止
           Acct-Multi-Session-Id  =  允许
                 Event-Timestamp  =  允许
             NAS-Port-Id属性开关  =  禁止
               NAS-Port-Id属性值  =  UNC
UE-Local-IP-Address和UE-UDP-Port  =  禁止
              Calling-Station-Id  =  使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                           | 输出项解释                                   |
|:--------------------------------|:----------------------------------------|
| RADIUS服务器组名称                    | RADIUS服务器组名。                            |
| Acct-Session-Id                 | 指定是否支持鉴权请求消息中携带Acct-Session-Id属性。       |
| NAS-ID                          | 指定是否支持鉴权请求消息中携带NAS-ID属性。                |
| NAS ID Type                     | 指定NAS-ID类型。                             |
| NAS ID Value                    | 指定NAS-ID类型具体值。                          |
| IMSI                            | 指定是否支持鉴权请求消息中携带224号IMSI属性。              |
| Charging-ID                     | 指定是否支持鉴权请求消息中携带225号Charging-ID属性。       |
| Prepaid-ind                     | 指定是否支持鉴权请求消息中携带226号Prepaid-ind属性。       |
| GGSN-IP                         | 指定是否支持鉴权请求消息中携带227号GGSN-IP属性。           |
| SGSN (S-GW)-IP                  | 指定是否支持鉴权请求消息中携带228号SGSN（SGW）-IP属性。      |
| Requested-APN                   | 指定是否支持鉴权请求消息中携带HW-Requested-APN属性。      |
| GGSN-Vendor                     | 指定是否支持鉴权请求消息中携带GGSN-Vendor属性。           |
| GGSN-Version                    | 指定是否支持鉴权请求消息中携带GGSN-Version属性。          |
| Request Authenticator           | 指定是否支持鉴权请求消息中携带Message-Authenticator属性。 |
| Acct-Multi-Session-Id           | 指定是否支持鉴权请求消息中携带Acct-Multi-Session-ID属性。 |
| Event-Timestamp                 | 指定是否支持鉴权请求消息中携带Event-Time属性。            |
| NAS-Port-Id属性开关                 | 指定是否支持携带NAS-Port-Id属性。                  |
| NAS-Port-Id属性值                  | 指定NAS-Port-Id信元携带的填充值。                  |
| UE-Local-IP-Address和UE-UDP-Port | 指定是否支持鉴权请求消息中携带WLAN地址。                  |
| Calling-Station-Id              | 该参数用于指定鉴权请求消息中是否携带Calling-Station-Id属性。 |