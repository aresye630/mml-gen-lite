# 设置DB参数（SET DBPARAS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于设置DB参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PARANAME                | PARAVALUE   |
|:------------------------|:------------|
| SdbBatchDuration        | 1000        |
| SdbBatchMaxQueueLen     | 20          |
| SdbMultiOpMaxSize       | 10000       |
| DdbSrvVerifyCycle       | 6000        |
| DdbSfSrvVerifyCycle     | 6000        |
| DdbClientVerifyCycle    | 6000        |
| DdbSfClientVerifyCycle  | 6000        |
| DdbSrvVerifyTimer       | 200         |
| DdbSfSrvVerifyTimer     | 200         |
| DdbClientVerifyTimer    | 200         |
| DdbSfClientVerifyTimer  | 200         |
| DdbSfSrvAllowWindowPush | true        |
| DdbSrvAllowWindowPush   | true        |
| DdbSfSrvWindowSize      | 10          |
| DdbSrvWindowSize        | 10          |
| SdbMaxScanRate          | 0           |
| SdbTableRecordThreshold | 110         |
| SdbMaxSubmitLen         | 96          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARANAME  | 参数名称   | 可选必选说明：必选参数  参数含义：参数名称。  数据来源：本端规划 取值范围： SdbBatchDuration（打包发送时间间隔（毫秒））SdbBatchMaxQueueLen（打包发送最大队列长度）SdbMultiOpMaxSize（单个数据包最大尺寸（字节））DdbSrvVerifyCycle（业务DDB服务端核查周期）DdbSfSrvVerifyCycle（平台DDB服务端核查周期）DdbClientVerifyCycle（业务DDB客户端核查周期）DdbSfClientVerifyCycle（平台DDB客户端核查周期）DdbSrvVerifyTimer（业务DDB服务端核查定时器周期（ms））DdbSfSrvVerifyTimer（平台DDB服务端核查定时器周期（ms））DdbClientVerifyTimer（业务DDB客户端核查定时器周期（ms））DdbSfClientVerifyTimer（平台DDB客户端核查定时器周期（ms））DdbSfSrvAllowWindowPush（平台DDB服务端允许窗口推送）DdbSrvAllowWindowPush（业务DDB服务端允许窗口推送）DdbSfSrvWindowSize（平台DDB服务端窗口大小）DdbSrvWindowSize（业务DDB服务端窗口大小）SdbMaxScanRate（SDB最大扫描速率）SdbTableRecordThreshold（SDB表记录阈值）SdbMaxSubmitLen（SDB表记录最大提交长度（KB））SdbCompressSwitch（SDB带宽压缩开关）SdbCompressMsgSize（SDB带宽压缩大小）SdbCompressAlgorithm（SDB带宽压缩算法）  默认值：无。  配置原则：无 |
| PARAVALUE | 参数值    | 可选必选说明：必选参数  参数含义：参数值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无。  配置原则：  当参数类型取值为"SdbCompressSwitch"， 取值范围为"0"或"2"。当参数类型取值为"SdbCompressMsgSize"， 取值范围为"0~1048576"。当参数类型取值为"SdbCompressAlgorithm"， 取值范围为"0~2"。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## 使用实例

设置SDB打包参数。

```
SET DBPARAS: PARANAME=SdbBatchDuration, PARAVALUE="111";
```