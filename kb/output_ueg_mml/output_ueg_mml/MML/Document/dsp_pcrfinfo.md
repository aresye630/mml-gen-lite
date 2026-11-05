# 显示PCRF具体信息（DSP PCRFINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询指定PCRF的详细信息，包括主机名、域名、地址以及supported features协商结果等。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                       |
|:---------|:-------|:---------------------------------------------------------------------------------------------------------------------------|
| HOSTNAME | 主机名    | 可选必选说明：必选参数 参数含义：该参数用于指定被查询的PCRF主机名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

查询主机名为“pcrf1”的PCRF详细信息：

```
DSP PCRFINFO:HOSTNAME="pcrf1";
```

```
RETCODE = 0  操作成功

PCRF具体信息
------------
结果  =  
Pcrf config information
-----------------------
                           host = pcrf1
                          realm = www.huawei.com
                           dscp = 255
                            wal = 0
                            vpn = vpn1
 supported features negotiation = DISABLE
                 feature config = rel8 
     feature negotiation result = NULL
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                          | 输出项解释                   |
|:-------------------------------|:------------------------|
| host                           | PCRF主机名。                |
| realm                          | 域名。                     |
| ip                             | IP地址。                   |
| port                           | 端口号。                    |
| sctp-endpoint                  | SCTP端点名。                |
| supported features negotiation | Supported features协商开关。 |
| feature config                 | 配置的feature。             |
| feature negotiation result     | feature协商结果。            |
| wal                            | PCRF的流控阈值。              |
| dscp                           | PCC信令报文的DSCP值。          |