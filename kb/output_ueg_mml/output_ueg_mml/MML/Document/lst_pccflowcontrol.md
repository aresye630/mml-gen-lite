# 查询PCC流控配置（LST PCCFLOWCONTROL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于查询UNC重授权请求的消息发送速率和SMF接收PCF的Npcf\_SMPolicyControl\_UpdateNotify消息的速率。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询PCC流控配置：

```
LST PCCFLOWCONTROL:;
```

```
RETCODE = 0  操作成功

PCC流控配置参数
---------------
Revalidation发送速率  =  25
UpdateNotify消息接收速率 = 2000
TerminateNotify消息接收速率 = 2000
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET PCCFLOWCONTROL的参数说明。