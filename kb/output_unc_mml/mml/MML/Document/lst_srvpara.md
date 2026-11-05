# 查询业务参数配置（LST SRVPARA）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：NCG**

用于查询NCG相关参数信息。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                    |
|:------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVPARATYPE | 业务参数类型 | 可选必选说明：必选参数 参数含义：用于指定对哪一类业务参数进行修改。 数据来源：本端规划 取值范围：枚举类型。 GATRACEMSGPARA：Ga跟踪消息长度。PASSIVEPARA：PASSIVE模式参数。ANOTHERNODEDOWNPARA：另一节点发生故障。CDMPULLMODEPARA：PULL分发模式参数。GALICCTRLALM：GA License控制告警阈值。GALICPARA：GA License参数。BICONVERGENCE：BI收敛参数。PORTCONSTR：端口约束。 默认值：无 配置原则：无 |

#### 使用实例

- 查询业务参数类型为“Ga跟踪消息长度”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=GATRACEMSGPARA;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
   业务参数类型  =  Ga跟踪消息长度
  Ga跟踪消息长度  =  LONG
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“PASSIVE模式参数”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=PASSIVEPARA;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
  业务参数类型  =  PASSIVE模式参数
      起始端口  =  20060
      结束端口  =  20090
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“另一节点发生故障”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=ANOTHERNODEDOWNPARA;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
  业务参数类型  =  另一节点发生故障
  业务控制参数  =  开启
  (结果个数 = 1)
  ---    END
  ```

- 查询业务参数类型为“PULL分发模式参数”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=CDMPULLMODEPARA;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  ---------
                            业务参数类型  =  PULL分发模式参数
                        SFTP最大超时次数  =  5
  SFTP服务器端向客户端请求消息的时间间隔  =  60
                   SFTP CPU最高占比（%）  =  100
                    FTP CPU最高占比（%）  =  100
  (结果个数 = 1)
  ---    END
  ```

- 查询业务参数类型为“GA License控制告警阈值”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=GALICCTRLALM;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  -------------------------
                       业务参数类型  =  GA License控制告警阈值
                容量告警百分比（%）  =  80
            容量告警恢复百分比（%）  =  70
               告警检测周期（分钟）  =  20
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“GA License参数”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=GALICPARA;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  -------------------------
                       业务参数类型  =  GA License参数
            会话结束及时释放License  =  关闭
      会话结束后License延迟释放时间  =  3
            切换场景及时释放License  =  关闭
  (结果个数 = 1)
  ```
- 查询业务参数类型为“BI收敛参数”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=BICONVERGENCE;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  -------------------------
                       业务参数类型  =  BI收敛参数
                     Ga业务权重调整  =  关闭
                         业务RU约束  =  关闭
  (结果个数 = 1)
  ---    END
  ```
- 查询业务参数类型为“端口约束”的业务参数配置：

  ```
  LST SRVPARA: SRVPARATYPE=PORTCONSTR;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下:
  -------------------------
               SFTP模式分发任务最大端口  =  0
               SFTP模式分发任务最小端口  =  0
               SFTP模式备份任务最大端口  =  0
               SFTP模式备份任务最小端口  =  0
    FTP Passive模式分发任务最大数据端口  =  0
    FTP Passive模式分发任务最小数据端口  =  0
    FTP Passive模式备份任务最大数据端口  =  0
    FTP Passive模式备份任务最小数据端口  =  0
       FTP Port模式分发任务最大数据端口  =  35000
       FTP Port模式分发任务最小数据端口  =  30000
       FTP Port模式备份任务最大数据端口  =  40000
       FTP Port模式备份任务最小数据端口  =  35001
            FTP模式分发任务最大控制端口  =  0
            FTP模式分发任务最小控制端口  =  0
            FTP模式备份任务最大控制端口  =  0
            FTP模式备份任务最小控制端口  =  0
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称                   | 输出项解释                                         |
|:------------------------|:----------------------------------------------|
| 业务参数类型                  | 用于指定对哪一类业务参数进行修改。                             |
| Ga跟踪消息长度                | 用于设置Ga跟踪消息并且消息类型是DataTransferRequest时的上报长度控制。 |
| 起始端口                    | PULL模式下FTP PASSIVE和PORT模式的起始端口。               |
| 结束端口                    | PULL模式下FTP PASSIVE和PORT模式的结束端口。               |
| 业务控制参数                  | 软参值的开关状态。                                     |
| SFTP最大超时次数              | PULL模式下SFTP服务端的ClientAliveCountMax参数。         |
| SFTP服务器端向客户端请求消息的时间间隔   | PULL模式下SFTP服务端的ClientAliveInterval参数。         |
| SFTP CPU最高占比（%）         | PULL模式下SFTP服务端的CPU最高占比。                       |
| FTP CPU最高占比（%）          | PULL模式下FTP服务端的CPU最高占比。                        |
| 容量告警百分比（%）              | 上报告警ALM-82015的GA接口系统话务量峰值占License值百分比。        |
| 容量告警恢复百分比（%）            | 恢复告警ALM-82015的GA接口系统话务量峰值占License值百分比。        |
| 告警检测周期（分钟）              | 告警ALM-82015的检测周期。                             |
| 会话结束及时释放License         | 会话结束及时释放License的开关状态。                         |
| 会话结束后License延迟释放时间      | 会话结束后License延迟释放时间，单位为分钟。                     |
| 切换场景及时释放License         | 切换场景及时释放License的开关状态。                         |
| Ga业务权重调整                | 234G业务调整5G权重的开关状态                             |
| 业务RU约束                  | 业务RU禁止234G业务的开关状态                             |
| SFTP模式分发任务最大端口          | PUSH分发任务 SFTP模式下的CG侧最大端口                      |
| SFTP模式分发任务最小端口          | PUSH分发任务 SFTP模式下的CG侧最小端口                      |
| SFTP模式备份任务最大端口          | PUSH备份任务 SFTP模式下的CG侧最大端口                      |
| SFTP模式备份任务最小端口          | PUSH备份任务 SFTP模式下的CG侧最小端口                      |
| FTP Passive模式分发任务最大数据端口 | PUSH分发任务 FTP Passive模式下的CG侧最大数据端口             |
| FTP Passive模式分发任务最小数据端口 | PUSH分发任务 FTP Passive模式下的CG侧最小数据端口             |
| FTP Passive模式备份任务最大数据端口 | PUSH备份任务 FTP Passive模式下的CG侧最大数据端口             |
| FTP Passive模式备份任务最小数据端口 | PUSH备份任务 FTP Passive模式下的CG侧最小数据端口             |
| FTP Port模式分发任务最大数据端口    | PUSH分发任务 FTP Port模式下的CG侧最大数据端口                |
| FTP Port模式分发任务最小数据端口    | PUSH分发任务 FTP Port模式下的CG侧最小数据端口                |
| FTP Port模式备份任务最大数据端口    | PUSH备份任务 FTP Port模式下的CG侧最大数据端口                |
| FTP Port模式备份任务最小数据端口    | PUSH备份任务 FTP Port模式下的CG侧最小数据端口                |
| FTP模式分发任务最大控制端口         | PUSH分发任务 FTP 模式下的CG侧最大控制端口                    |
| FTP模式分发任务最小控制端口         | PUSH分发任务 FTP 模式下的CG侧最小控制端口                    |
| FTP模式备份任务最大控制端口         | PUSH备份任务 FTP 模式下的CG侧最大控制端口                    |
| FTP模式备份任务最小控制端口         | PUSH备份任务 FTP 模式下的CG侧最小控制端口                    |