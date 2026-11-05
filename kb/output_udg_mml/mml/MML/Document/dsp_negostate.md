# 显示所有进程的协商状态信息（DSP NEGOSTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示所有运行进程的协商状态信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| SRCLOCID        | 源进程ID  | 可选必选说明：可选参数 参数含义：该参数表示源进程ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                    |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

显示所有运行进程的协商状态信息：

```
DSP NEGOSTATE:SRCLOCID=2,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
源进程ID   目的进程ID         仲裁状态         协商状态             协商序列号      Semagt组件状态    Semagt组件开工序列号          协商联调结果           协商过程事件          时间             

2              3              NULL             UNDEFINE             0                   NG              41927                        DISCONNECT            CREATE CB             01-19 14:29:54.844641 
2              3              PRIMARY          AVAILABLE            1484836193          OK              41927                        DISCONNECT            RECV UPDATE MSG       01-19 14:29:55.654868 
2              3              PRIMARY          AVAILABLE            1484836193          OK              41927                        DISCONNECT            RECV UPDATE MSG       01-19 14:29:55.654965 
2              3              PRIMARY          AVAILABLE            1484836193          OK              41927                        DISCONNECT            RECV NEGO MSG         01-19 14:29:55.655040 
2              3              PRIMARY          AVAILABLE            1484836193          OK              41927                        DISCONNECT            RECV NEGO MSG         01-19 14:29:55.659070 
2              3              PRIMARY          AVAILABLE            1484836193          OK              41927                        CONNECT               UPDATE COMM STATE     01-19 14:29:55.659228 
2              4              NULL             UNDEFINE             0                   NG              35567                        DISCONNECT            CREATE CB             01-19 14:29:52.466983 
2              4              PRIMARY          AVAILABLE            1484836192          OK              35567                        DISCONNECT            RECV UPDATE MSG       01-19 14:29:56.655126 
2              4              PRIMARY          AVAILABLE            1484836192          OK              35567                        DISCONNECT            RECV UPDATE MSG       01-19 14:29:56.655268 
2              4              PRIMARY          AVAILABLE            1484836192          OK              35567                        DISCONNECT            RECV NEGO MSG         01-19 14:29:56.655411 
2              4              PRIMARY          AVAILABLE            1484836192          OK              35567                        DISCONNECT            RECV NEGO MSG         01-19 14:29:56.659387 
2              4              PRIMARY          AVAILABLE            1484836192          OK              35567                        CONNECT               UPDATE COMM STATE     01-19 14:29:56.659603 
2              6              NULL             UNDEFINE             0                   NG              4294967295                   DISCONNECT            CREATE CB             01-19 14:29:54.844862 
2              7              NULL             UNDEFINE             0                   NG              4294967295                   DISCONNECT            CREATE CB             01-19 14:29:52.467202 
2              8              NULL             UNDEFINE             0                   NG              4294967295                   DISCONNECT            CREATE CB             01-19 14:29:54.845256 
2              1000           NULL             UNDEFINE             0                   NG              53729                        DISCONNECT            CREATE CB             01-19 14:30:04.680693 
2              1000           PRIMARY          AVAILABLE            1484836205          OK              53729                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.893831 
2              1000           PRIMARY          AVAILABLE            1484836205          OK              53729                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.893907 
2              1000           PRIMARY          AVAILABLE            1484836205          OK              53729                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.894001 
2              1000           PRIMARY          AVAILABLE            1484836205          OK              53729                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.895255 
2              1000           PRIMARY          AVAILABLE            1484836205          OK              53729                        CONNECT               UPDATE COMM STATE     01-19 14:30:05.895689 
2              1001           NULL             UNDEFINE             0                   NG              53728                        DISCONNECT            CREATE CB             01-19 14:30:04.680995 
2              1001           PRIMARY          AVAILABLE            1484836205          OK              53728                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.869220 
2              1001           PRIMARY          AVAILABLE            1484836205          OK              53728                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.869330 
2              1001           PRIMARY          AVAILABLE            1484836205          OK              53728                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.869433 
2              1001           PRIMARY          AVAILABLE            1484836205          OK              53728                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.871550 
2              1001           PRIMARY          AVAILABLE            1484836205          OK              53728                        CONNECT               UPDATE COMM STATE     01-19 14:30:05.872081 
2              1002           NULL             UNDEFINE             0                   NG              53677                        DISCONNECT            CREATE CB             01-19 14:30:04.681264 
2              1002           PRIMARY          AVAILABLE            1484836205          OK              53677                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.545050 
2              1002           PRIMARY          AVAILABLE            1484836205          OK              53677                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.551993 
2              1002           PRIMARY          AVAILABLE            1484836205          OK              53677                        CONNECT               UPDATE COMM STATE     01-19 14:30:05.552558 
2              10001          NULL             UNDEFINE             0                   NG              53726                        DISCONNECT            CREATE CB             01-19 14:30:04.681518 
2              10001          PRIMARY          AVAILABLE            1484836205          OK              53726                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.893375 
2              10001          PRIMARY          AVAILABLE            1484836205          OK              53726                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.893451 
2              10001          PRIMARY          AVAILABLE            1484836205          OK              53726                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.893536 
2              10001          PRIMARY          AVAILABLE            1484836205          OK              53726                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.894829 
2              10001          PRIMARY          AVAILABLE            1484836205          OK              53726                        CONNECT               UPDATE COMM STATE     01-19 14:30:05.895030 
2              10002          NULL             UNDEFINE             0                   NG              53727                        DISCONNECT            CREATE CB             01-19 14:30:04.682133 
2              10002          PRIMARY          AVAILABLE            1484836205          OK              53727                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.876526 
2              10002          PRIMARY          AVAILABLE            1484836205          OK              53727                        DISCONNECT            RECV UPDATE MSG       01-19 14:30:05.876606 
2              10002          PRIMARY          AVAILABLE            1484836205          OK              53727                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.876682 
2              10002          PRIMARY          AVAILABLE            1484836205          OK              53727                        DISCONNECT            RECV NEGO MSG         01-19 14:30:05.878975 
2              10002          PRIMARY          AVAILABLE            1484836205          OK              53727                        CONNECT               UPDATE COMM STATE     01-19 14:30:05.879128 
(结果个数 = 43)
---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释                   |
|:--------------|:------------------------|
| 源进程ID         | 表示源进程ID。                |
| 目的进程ID        | 表示目的进程ID。               |
| 仲裁状态          | 表示目的端进程仲裁状态。            |
| 协商状态          | 表示目的端进程协商状态。            |
| 协商序列号         | 表示目的端进程协商序列号。           |
| Semagt组件状态    | 表示订阅目标端进程的Semagt组件状态。   |
| Semagt组件开工序列号 | 表示目标端进程的Semagt组件的开工序列号。 |
| 协商联调结果        | 表示源与目标端进程协商联调结果。        |
| 协商过程事件        | 表示协商过程事件。               |
| 时间            | 表示协商过程事件发生的时间。          |