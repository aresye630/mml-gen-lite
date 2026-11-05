# 查询PCRF（LST CPPCRF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于查询PCRF的基本信息。

可以查询一条指定的PCRF信息，也可以查询所有的PCRF。

#### 注意事项

- 查询特定的PCRF时，必须输入PCRF主机名称。
- 如果不输入参数则是查询全部的PCRF。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                    |
|:---------|:--------|:------------------------------------------------------------------------------------------------------------------------|
| HOSTNAME | PCRF主机名 | 可选必选说明：可选参数 参数含义：该参数用于指定PCRF的主机名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询名称为“pcrf1”的PCRF的信息：

  ```
  LST CPPCRF:HOSTNAME="pcrf1";
  ```

  ```
  RETCODE = 0  操作成功。

  PCRF信息
  --------
                      PCRF主机名  =  pcrf1
                        PCRF域名  =  www.huawei.com
                         VPN实例  =  vpn1
  Supported-Features动态协商开关  =  使能
                     Feature列表  =  3GPP Rel-8 Gx功能
                          DSCP值  =  255
                           wal值  =  0
  (结果个数 = 1)
  ---    END
  ```
- 查询系统中所有的PCRF信息：

  ```
  LST CPPCRF:;
  ```

  ```
  RETCODE = 0  操作成功。

  PCRF信息
  --------
  PCRF主机名    PCRF域名           VPN实例    Supported-Features动态协商开关    Feature列表                              DSCP值    wal值

  pcrf1         www.huawei.com    vpn1       使能                              3GPP Rel-8 Gx功能                        255       0    
  pcrf2         www.hw.com         vpn2       不使能                            3GPP Rel-8 Gx功能 & 3GPP Rel-9 Gx功能    255       0    
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD CPPCRF的参数说明。