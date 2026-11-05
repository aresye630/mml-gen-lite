# 查询配置的DB参数（LST DBPARAS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询配置的DB参数。

## 注意事项

参数PARANAME取值为SdbCompressSwitch、SdbCompressMsgSize或SdbCompressAlgorithm时，其对应的PARAVALUE取值若通过SET DBPARAS命令完成了配置，则可通过本命令查询具体取值，若未经过配置，其系统初始值仅能通过OPR DBGDATA: DBGTYPE=CELLTYPE, CELLTYPE=\*, DEBUGNAME="DDF DSP PLUGIN WHERE DATABASETYPE IS sdb";命令进行查询，其中CELLTYPE的取值为进程类型。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARANAME | 参数名称   | 可选必选说明：可选参数  参数含义：参数名称。  数据来源：本端规划 取值范围： SdbBatchDuration（打包发送时间间隔（毫秒））SdbBatchMaxQueueLen（打包发送最大队列长度）SdbMultiOpMaxSize（单个数据包最大尺寸（字节））DdbSrvVerifyCycle（业务DDB服务端核查周期）DdbSfSrvVerifyCycle（平台DDB服务端核查周期）DdbClientVerifyCycle（业务DDB客户端核查周期）DdbSfClientVerifyCycle（平台DDB客户端核查周期）DdbSrvVerifyTimer（业务DDB服务端核查定时器周期（ms））DdbSfSrvVerifyTimer（平台DDB服务端核查定时器周期（ms））DdbClientVerifyTimer（业务DDB客户端核查定时器周期（ms））DdbSfClientVerifyTimer（平台DDB客户端核查定时器周期（ms））DdbSfSrvAllowWindowPush（平台DDB服务端允许窗口推送）DdbSrvAllowWindowPush（业务DDB服务端允许窗口推送）DdbSfSrvWindowSize（平台DDB服务端窗口大小）DdbSrvWindowSize（业务DDB服务端窗口大小）SdbMaxScanRate（SDB最大扫描速率）SdbTableRecordThreshold（SDB表记录阈值）SdbMaxSubmitLen（SDB表记录最大提交长度（KB））SdbCompressSwitch（SDB带宽压缩开关）SdbCompressMsgSize（SDB带宽压缩大小）SdbCompressAlgorithm（SDB带宽压缩算法）  默认值：无  配置原则：无 |

## 使用实例

查询配置的SDB打包参数

```
LST DBPARAS: PARANAME=SdbBatchDuration;
```

## 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 参数名称    | 参数名称。   |
| 参数值     | 参数值。    |