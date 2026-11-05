# 显示TRP获取失败的gNodeB列表（DSP LCSTRPFAILLIST）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询显示TRP获取失败的gNodeB列表。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                   |
|:--------|:-------|:-----------------------------------------------------------------------|
| PODNAME | Pod名称  | 可选必选说明：可选参数 参数含义：Pod名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |

#### 使用实例

查询显示获取TRP失败的gNodeB列表，同时显示获取失败的次数、是否满足告警条件以及是否上报过告警：

```
DSP LCSTRPFAILLIST:;
```

```
RETCODE = 0  操作成功

获取TRP失败的gNodeB列表
--------------------------------
LCS NG-RAN信息                                                                                                                                                                                                                                                                                

The trpFailList on pod : lcs-e-pod-774b798c6f-nmvkh

-------------------------------

gNodeB ID    Amf FailNum         Ngran FailNum       TRP FailNum         TRP Exchange Failure Alarm Flag    TRP Alarm State   
1832160      1                   0                   1                   0                                  0

The trpFailList on pod : lcs-e-pod-774b798c6f-5fxvn

-------------------------------
There is no gNodeBId
                                                                                                                                                                                            
(结果个数 = 2)

---    END
```

#### 输出结果说明

| 输出项名称                           | 输出项解释                         |
|:--------------------------------|:------------------------------|
| gNodeB ID                       | 基站ID，表示发起过TRP流程的基站ID。         |
| AMF FailNum                     | AMF异常导致的TRP获取失败的次数。           |
| Ngran FailNum                   | 基站异常导致TRP获取失败的次数。             |
| TRP FailNum                     | TRP获取失败的总次数。                  |
| TRP Exchange Failure Alarm Flag | 标记是否达到上报gNodeB的TRP信息获取失败告警阈值。 |
| TRP Alarm State                 | 是否上报gNodeB的TRP信息获取失败告警。       |