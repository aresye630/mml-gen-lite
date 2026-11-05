# 显示PDN自动探测结果（DSP PDNAUTOTSTRESULT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

显示PDN自动探测结果。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                |
|:---------|:-------|:--------------------------------------------------------------------------------------------------------------------|
| PATHNAME | 路径名称   | 可选必选说明：可选参数 参数含义：该参数用于指定用于连通性探测的路径名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：配置的路径名称应满足路径名称的取值范围。 |

#### 使用实例

- 显示路径名为test1，探测方式为PING的PDN自动探测结果：

  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING    Packet length:100
  Probed advertised route network segments:1    Successful:0    Failed:1    Probe status:completed
  Advertised route network segment info:
  --------------------------------------
  No.     Advertised Route Network Segment                Probe Result
  1       10.0.0.0/31                                     Failed
  (结果个数 = 1)

  ---    END
  ```
- 显示路径名为test1，探测方式为DNS的PDN自动探测结果：

  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.10    DSCP:0    Probe mode:DNS    Domain name:
  Probed advertised route network segments:1    Successful:0    Failed:1    Probe status:completed
  Advertised route network segment info:
  --------------------------------------
  No.     Advertised Route Network Segment                Probe Result
  1       10.0.0.0/31                                     Failed
  (结果个数 = 1)

  ---    END
  ```
- 显示路径名为test1，探测方式为TRACERT的PDN自动探测结果：

  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:v4pool2    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.10    DSCP:0    Probe mode:TRACERT
  Test hops:1    Probe status:completed
  Track 10.1.1.10 routing through up to 30 hops:
  No.     Gateway address                                                                     Probe packet delay        
  1       10.1.1.10 (10.1.1.10)                                                           20 ms     20 ms     10 ms
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称                                    | 输出项解释       |
|:-----------------------------------------|:------------|
| Path Name                                | 路径名称。       |
| Pool name                                | 地址池名称。      |
| VPN-instance                             | 指定VPN名字。    |
| Destination IP address                   | 探测目的地址。     |
| DSCP                                     | 指定DSCP值。    |
| TC                                       | 指定TC值。      |
| Probe mode                               | 探测方式。       |
| Packet length                            | 报文长度。       |
| Probed advertised route network segments | 探测发布路由网段个数。 |
| Successful                               | 成功个数。       |
| Failed                                   | 失败个数。       |
| Probe status                             | 探测状态。       |
| Advertised Route Network Segment         | 发布路由网段。     |
| Probe Result                             | 探测结果。       |
| Test hops                                | 探测跳数。       |
| Gateway address                          | 网关地址。       |
| Probe packet delay                       | 探测报文时延。     |
| Execute Time                             | 探测时间。       |
| Trigger Type                             | 触发方式        |