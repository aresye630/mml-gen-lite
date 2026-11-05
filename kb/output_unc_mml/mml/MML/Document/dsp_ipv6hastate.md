# 查询IPv6组件与其他组件交互信息（DSP IPV6HASTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询IPv6组件与其他组件交互信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 交互组件类型 | 可选必选说明：必选参数 参数含义：该参数用来指定与IPv6组件交互组件类型。 数据来源：本端规划 取值范围：枚举类型。 FES：与FES组件交互信息。SOCK：与SOCK组件交互信息。CACHEM：与CACHEM组件交互信息。LDM：与LDM组件交互信息。PP6：IPv6组件状态。 默认值：无 |

#### 使用实例

- 显示IPv6组件与FES组件交互信息：

  ```
  DSP IPV6HASTATE: TYPE=FES;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

      PID: 0x6A0016,ucSubFlag: 0x1,ucCompStatus: 0x0,uiReferCount: 0x1
      PID: 0x6A0016  HaState: 0x0
      State: LSMLIB_SOCK_FSM_INIT FESState: (LSMLIB_FES_FSM_RUNNING LSMLIB_FES_FSM_RUNNING LSMLIB_FES_FSM_RUNNING)
      BatchUpdateSeq: 7 RealUpdateSeq: 990
      Version: 0 LastMsgSendTime: 0
      FlowCtl State: 0 CurFlowCtlBeginTime: 0 LastFlowCtlEndTime: 0
      RecvFlowCtlMsgTime: 0 TotalFlowCtlTimes: 0

      PID: 0x6A0016,ucSubFlag: 0x0,ucCompStatus: 0x1,uiReferCount: 0x1
      PID: 0x6A0016  HaState: 0x1
      State: LSMLIB_SOCK_FSM_INIT FESState: (LSMLIB_FES_FSM_INIT LSMLIB_FES_FSM_INIT LSMLIB_FES_FSM_INIT)
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      FlowCtl State: 0 CurFlowCtlBeginTime: 0 LastFlowCtlEndTime: 0
      RecvFlowCtlMsgTime: 0 TotalFlowCtlTimes: 0

  (结果个数 = 2)
  ---    END
  ```
- 显示IPv6组件与SOCK组件交互信息：

  ```
  DSP IPV6HASTATE: TYPE=SOCK;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

      PID: 0x650004  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x650008  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 1
      Version: 1 LastMsgSendTime: 3
      PID: 0x650019  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x65002A  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x650037  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 1
      Version: 1 LastMsgSendTime: 78

      PID: 0x650004  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650008  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650019  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x65002A  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650037  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0

  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 查询结果信息  | 用来显示查询结果信息。 |