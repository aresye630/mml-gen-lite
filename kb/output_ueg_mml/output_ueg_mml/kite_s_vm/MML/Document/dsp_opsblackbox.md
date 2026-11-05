# 显示开放可编程系统的维护信息（DSP OPSBLACKBOX）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示开放编程系统的维护信息。当python脚本执行失败时，可以通该命令查询系统维护信息。

维护信息包含python虚拟机、助手状态机、脚本状态机和开放可编程接口的信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                       |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FUNCTYPE | 功能类型   | 可选必选说明：必选参数 参数含义：该参数用于表示操作的黑匣子类型。 python虚拟机的维护信息：python虚拟机的黑匣子信息。 助手状态机的维护信息：助手状态机的黑匣子信息。 脚本状态机的维护信息：脚本状态机的黑匣子信息。 开放可编程接口的维护信息：开放可编程接口的黑匣子信息。 数据来源：本端规划 取值范围：枚举类型。 pythonvm：python虚拟机的维护信息。assistant：助手状态机的维护信息。script：脚本状态机的维护信息。opis：开放可编程接口的维护信息。 默认值：无 |

#### 使用实例

- 显示python虚拟机的维护信息：

  ```
  DSP OPSBLACKBOX:FUNCTYPE=pythonvm;
  ```

  ```
   RETCODE = 0  操作成功。

  结果如下
  ------------------------
  输出字符串

  170119-08:30:37.628240 [PVME][L:123670] PVME wait ack time ,so reset.
  170119-08:30:37.628301 [PVME][L:123670]
      ProcessId:0x112c
      CurentScriptid:0
      stRecvPvmCtrReq.iFd:11
      stSendPvmCtrRsp.iFd:12
      stSendApprRsp.iFd:15
      stSendAppStdIn.iFd:14
      Magic:38641544548121548004
      Debug:0x1
      Interrupted:0x0
      LastReadPipeMsg:0x805e88
      Recevied:124587450
  ---    END
  ```
- 显示助手状态机的维护信息：

  ```
  DSP OPSBLACKBOX:FUNCTYPE=assistant;
  ```

  ```
   RETCODE = 0  操作成功。

  结果如下
  ------------------------
  输出字符串

  02-06 02:45:59:696 Assistant FSM: Vsid=0, Name="_bfd_mtp.py", id=1, State=S8(stop), Event=E7(suspend), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:696 Assistant FSM: Vsid=0, Name="_bfd_mtp.py", id=1, State=S8(stop), Event=E1(updateExec), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:696 Assistant FSM: Vsid=0, Name="_bfd_mtp.py", id=1, State=S8(stop), Event=E19(ScriptSubStart), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:696 Assistant FSM: Vsid=0, Name="_ldp_mtp.py", id=3, State=S8(stop), Event=E7(suspend), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:706 Assistant FSM: Vsid=0, Name="_ldp_mtp.py", id=3, State=S8(stop), Event=E1(updateExec), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:706 Assistant FSM: Vsid=0, Name="_ldp_mtp.py", id=3, State=S8(stop), Event=E19(ScriptSubStart), Result=0x0, NextState=S8(stop).
  02-06 02:45:59:706 Assistant FSM: Vsid=0, Name="_ospf_mtp.py", id=4, State=S8(stop), Event=E7(suspend), Result=0x0, NextState=S8(stop).
  ---    END
  ```
- 显示脚本状态机的维护信息：

  ```
  DSP OPSBLACKBOX:FUNCTYPE=script;
  ```

  ```
   RETCODE = 0  操作成功。

  结果如下
  ------------------------
  输出字符串

  02-06 02:45:59:745 VsId (0) Script (0) FSM: State = S1(INIT), Event = E5(AUTO_START_REQ), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:45:59:759 VsId (0) Script (1) FSM: State = S1(INIT), Event = E1(ALLOC_PROCESSID_REQ), Result = 0x0, NextState = S2(ACTION)
  02-06 02:45:59:839 VsId (0) Script (1) FSM: State = S2(ACTION), Event = E3(BACK_START_REQ), Result = 0x0, NextState = S4(READY)
  02-06 02:46:00:121 VsId (0) Script (1) FSM: State = S4(READY), Event = E7(SCRIPT_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:157 VsId (0) Script (9) FSM: State = S1(INIT), Event = E1(ALLOC_PROCESSID_REQ), Result = 0x0, NextState = S2(ACTION)
  02-06 02:46:00:207 VsId (0) Script (9) FSM: State = S2(ACTION), Event = E3(BACK_START_REQ), Result = 0x0, NextState = S4(READY)
  02-06 02:46:00:220 VsId (0) Script (2) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:227 VsId (0) Script (3) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:269 VsId (0) Script (4) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:282 VsId (0) Script (5) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:311 VsId (0) Script (6) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  02-06 02:46:00:32   VsId (0) Script (7) FSM: State = S4(READY), Event = E8(SCRIPT_THREAD_START_RSP), Result = 0x0, NextState = S5(RUNNING)
  ---    END
  ```
- 显示开放可编程接口的维护信息：

  ```
  DSP OPSBLACKBOX:FUNCTYPE=opis;
  ```

  ```
   RETCODE = 0  操作成功。

  结果如下
  ------------------------
  输出字符串

  02-06 02:46:04:776 CMD_PROC FSM(Id=64): State=S1(ready), Event=E1(recvCommand), Result=0x0, NextState=S2(nonConfig)
  02-06 02:46:04:859 CMD_PROC FSM(Id=64): State=S2(nonConfig), Event=E2(cmdRespond), Result=0x0, NextState=S1(ready)
  02-06 02:46:04:899 CMD_PROC FSM(Id=64): State=S1(ready), Event=E1(recvCommand), Result=0x0, NextState=S2(nonConfig)
  02-06 02:46:04:911 CMD_PROC FSM(Id=64): State=S2(nonConfig), Event=E2(cmdRespond), Result=0x0, NextState=S1(ready)
  02-06 02:46:04:943 CMD_PROC FSM(Id=64): State=S1(ready), Event=E1(recvCommand), Result=0x0, NextState=S2(nonConfig)
  02-06 02:46:04:958 CMD_PROC FSM(Id=64): State=S2(nonConfig), Event=E2(cmdRespond), Result=0x0, NextState=S1(ready)
  02-06 02:46:04:980 CMD_PROC FSM(Id=64): State=S1(ready), Event=E1(recvCommand), Result=0x0, NextState=S2(nonConfig)
  02-06 02:46:04:990 CMD_PROC FSM(Id=64): State=S2(nonConfig), Event=E2(cmdRespond), Result=0x0, NextState=S1(ready)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                                     |
|:--------|:------------------------------------------|
| 输出字符串   | OPS记录的python虚拟机、助手状态机、脚本状态机和开放可编程接口的维护信息。 |