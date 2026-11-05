# 查询ND与其他组件之间交互状态信息（DSP NDHASTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询ND与其他组件的交互信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                                                    |
|:-------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 交互组件的类型 | 可选必选说明：必选参数 参数含义：该参数用来指定与ND组件交互的组件类型。 数据来源：本端规划 取值范围：枚举类型。 IFM：与IFM组件交互信息。FES：与FES组件交互信息。LDM：与LDM组件交互信息。ND：ND组件状态。EUM：与EUM组件交互信息。 默认值：无 |

#### 使用实例

- 显示ND与LDM组件的交互信息：

  ```
  DSP NDHASTATE: TYPE=LDM;
  ```

  ```
          RETCODE = 0  操作成功。
          结果如下
          --------
          查询结果信息
          ND Pid:0x0073002c
          Count: 0x2
          PID: 0x240009 PipeFsm:ND_PIPE_FSM_OPENED ServiceId:0x378
          PipeId: 0x80034
          PID: 0x8078000F PipeFsm:ND_PIPE_FSM_INIT ServiceId:0x378
          PeerPipeId: 0xC0080035

          (结果个数 = 1)
          ---    END
  ```
- 显示ND与IFM组件的交互信息：

  ```
  DSP NDHASTATE: TYPE=IFM;
  ```

  ```
          RETCODE = 0  操作成功。
          结果如下
          --------
          查询结果数据

          ND Pid:0x0073003b
              PID: 0x7A0011
              Consumer State: IF_CONSUMER_STATE_RUNNING, Send Register Time: 18837s, Receive Keep Alive Time: 0s
              Producer State: IF_PRODUCER_STATE_RUNNING, Seq: 2, TransNum: 0

          ND Pid:0x0073003a
              PID: 0x7A0011
              Consumer State: IF_CONSUMER_STATE_RUNNING, Send Register Time: 5s, Receive Keep Alive Time: 0s
              Producer State: IF_PRODUCER_STATE_RUNNING, Seq: 2, TransNum: 0

         (结果个数 = 2)
         ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释          |
|:--------|:---------------|
| 查询结果数据  | 用来显示ND的查询结果数据。 |