# 查询CHR配置（LST CHRCFG）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询CHR（Call History Record）配置。 CHR功能是定位及分析用户故障的有利工具，可以提供所有用户的呼叫历史记录。CHR可以记录每个用户在呼叫过程中出现的问题并保存在Genex服务器中，网管部门在需要的时候，可以查询特定用户的呼叫历史记录，迅速定位故障原因。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询所有CHR配置：

LST CHRCFG:;

```
%%LST CHRCFG:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
Gb模式流程成功时上报选项  =  NULL
Gb模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & Inter System Change & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & Suspend & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14 & RESERVED15
Iu模式流程成功时上报选项  =  NULL
Iu模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & SRNS Relocation & Inter System Change & IU Release & Service Request & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & RAB Assignment in Service Request & Suspend & Location Report & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14
S1模式流程成功时上报选项  =  NULL
S1模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Tracking Area Update & Inter System Change & S1 Handover & X2 Handover & Service Request & Paging & S1 Release & UE Requested PDN Connectivity & UE or MME Requested PDN Disconnection & Dedicated Bearer Activation & Bearer Modification & Dedicated Bearer Deactivation & SGS Paging & SRVCC & Location Report & Control Plane Service Request & P-GW-initiated PDN Disconnect & VoLTE Bearer Deleted Unexpectedly & Connection Suspend & Connection Resume & Reroute NAS & E-RAB Modification Indication & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6
冲突流程时上报选项  =  NULL
附加流程上报选项  =  NULL
CHR单据设备号填充方式  =  SGSN号
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET CHRCFG**的参数说明。