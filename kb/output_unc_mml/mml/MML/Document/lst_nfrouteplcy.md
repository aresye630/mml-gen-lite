# 查询NF路由策略（LST NFROUTEPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF、AMF、SMSF、NCG、NSSF、CBC、CBCF**

该命令用于查询对端NF路由策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                            |
|:--------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------|
| INFOTYPE      | 信息类型   | 可选必选说明：可选参数  参数含义：该参数用于指定信息类型。  数据来源：全网规划 取值范围： “NFID（NFID）”：使用NF实例ID信息“IP（IP）”：使用IP信息“FQDN（FQDN）”：使用FQDN信息  默认值：无  配置原则：无      |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：该参数在"INFOTYPE"配置为"IP"时为条件必选参数。  参数含义：该参数用于指定IP地址类型。  数据来源：全网规划 取值范围： IPTypeV4（IPTypeV4）IPTypeV6（IPTypeV6）  默认值：无  配置原则：无 |

## 使用实例

- 查询所有对端NF路由策略；

  ```
  %%LST NFROUTEPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  索引  信息类型  NF实例标识      IP地址类型  IPv4前缀     IPv6前缀              IPv4掩码长度   IPv6掩码长度  FQDN后缀         路由策略     SCP组号  3gpp-sbi-Target-apiroot填写策略   拨测模式            

  1     NFID      udm_instance_0  NULL        0.0.0.0      ::                    0              0             NULL             直连通信     NULL	   优先填写IP			     继承
  2     IP        NULL            IPTypeV4    192.168.0.0  ::           	       24             0             NULL             通过SCP通信  NULL	   优先填写IP			     继承
  3     IP        NULL            IPTypeV6    0.0.0.0      2001:db8:1:1:1:1:1:0  0              120           NULL             通过SCP通信  NULL	   优先填写IP			     继承
  4     FQDN      NULL            NULL        0.0.0.0      ::           	       0              0             udm1.huawei.com  通过SCP通信  NULL	   优先填写IP			     继承
  (结果个数 = 4)

  ---    END
  ```
- 查询所有按NF实例标识配置的路由策略；

  ```
  %%LST NFROUTEPLCY: INFOTYPE=NFID;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                             索引  =  1
                       NF实例标识  =  udm_instance_0
                         路由策略  =  直连通信
                          SCP组号  =  NULL
  3gpp-sbi-Target-apiroot填写策略  =  优先填写IP
                         拨测模式  =  继承
  (结果个数 = 1)

  ---    END
  ```
- 查询所有按IP配置的路由策略；

  ```
  %%LST NFROUTEPLCY: INFOTYPE=IP, IPADDRESSTYPE=IPTypeV4;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                             索引  =  2
                         IPv4前缀  =  192.168.0.0
                     IPv4掩码长度  =  24
                         路由策略  =  通过SCP通信
                          SCP组号  =  NULL
  3gpp-sbi-Target-apiroot填写策略  =  优先填写IP
                         拨测模式  =  继承
  (结果个数 = 1)

  ---    END
  ```
- 查询所有按FQDN配置的路由策略。

  ```
  %%LST NFROUTEPLCY: INFOTYPE=FQDN;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                             索引  =  4
                         FQDN后缀  =  udm1.huawei.com
                         路由策略  =  通过SCP通信
                          SCP组号  =  NULL
  3gpp-sbi-Target-apiroot填写策略  =  优先填写IP
                         拨测模式  =  继承
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称                       | 输出项解释                                                     |
|:----------------------------|:----------------------------------------------------------|
| 索引                          | 该参数用于指定索引。                                                |
| FQDN后缀                      | 该参数用于指定FQDN后缀。                                            |
| 路由策略                        | 该参数用于指定到对端NF的路由策略。                                        |
| SCP组号                       | 该参数用于指定SCP组号。                                             |
| 3gpp-sbi-Target-apiroot填写策略 | 该参数用于指定通过SCP Model C间接路由通信时，3gpp-sbi-Target-apiroot的填写策略。 |
| 拨测模式                        | 该参数用于指定通过SCP Model C间接路由通信时的拨测模式。                         |
| NF实例标识                      | 该参数用于指定对端NF实例标识。                                          |
| 信息类型                        | 该参数用于指定信息类型。                                              |
| IP地址类型                      | 该参数用于指定IP地址类型。                                            |
| IPv4前缀                      | 该参数用于指定IPv4前缀。                                            |
| IPv6前缀                      | 该参数用于指定IPv6前缀。                                            |
| IPv4掩码长度                    | 该参数用于指定IPv4类型地址的掩码长度。                                     |
| IPv6掩码长度                    | 该参数用于指定IPv6类型地址的掩码长度。                                     |