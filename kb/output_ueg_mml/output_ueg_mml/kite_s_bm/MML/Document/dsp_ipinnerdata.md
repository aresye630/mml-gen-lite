# 查询PP4模块内部数据（DSP IPINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询PP4模块内部数据。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                          |
|:-------|:-------|:------------------------------------------------------------------------------|
| TYPE   | 内部数据类型 | 可选必选说明：必选参数 参数含义：该参数指定查询的类型。 数据来源：本端规划 取值范围：枚举类型。 LSM_LIB：本地会话管理库信息。 默认值：无    |
| CID    | 组件CID  | 可选必选说明：可选参数 参数含义：该参数指定CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无 |

#### 使用实例

查询PP4模块内部数据：

```
DSP IPINNERDATA: TYPE=LSM_LIB, CID="0x80660019";
```

```
        RETCODE = 0  操作成功。

        结果如下
        --------
        查询结果数据 =
        -------------------------------------
                  Cid: 0x80660019
                  Pid: 0x660012
        -------------------------------------
        LsmLib data:
        CompHandle         : 0x60600010d910  DebugSwitchId       : 137625601       PartnerPid        : 0x6a0013
        PartnerSubState    : Available       PartnerSmoothFes    : INIT            PartnerSmoothSeq  : 7
        PartnerRealSeq     : 265             PartnerVersion      : 0               LastSendMsgSec    : 0
        FlowCtlState       : 0               CurFlowCtlBeginTime : 0               LastFlowCtlEndTime: 0
        RecFlowCtlEndTime  : 0               TotalFlowCtlTimes   : 0               CurSecond         : 5563
        FirstSockUpSec     : 3               LsmLibFsmState      : RUNNING         EnterStateSecond  : 6

        (结果个数 = 1)
        ---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释              |
|:--------|:-------------------|
| 查询结果数据  | 用来显示IP模块内部的查询结果数据。 |