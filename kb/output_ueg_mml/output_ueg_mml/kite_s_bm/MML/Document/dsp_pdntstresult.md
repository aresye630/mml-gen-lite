# 查询PDN侧路由探测结果（DSP PDNTSTRESULT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来显示系统和PDN服务器之间的路由是否正常。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                               |
|:------------|:-------|:---------------------------------------------------------------------------------------------------|
| DISPLAYMODE | 显示模式   | 可选必选说明：可选参数 参数含义：用于指定查询模式。 数据来源：本端规划 取值范围：枚举类型。 SUCCESS：显示所有探测成功的结果。FAIL：显示所有探测失败的结果。 默认值：无 配置原则：无 |

#### 使用实例

- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.1.1.1之间的路由是否正常，探测方式是PING。显示探测结果：

  ```
  DSP PDNTSTRESULT:;
  ```

  ```
  RETCODE = 0  Operation Success.  

  PDN侧路由探测结果信息
  -------------------------- 
  结果  =   
  Pool name:pool-test    VPN-instance:NULL   Tigger Type:NONE    Execute Time:1970-01-01 08:00:00  Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING  Packet length:0 
  Probed advertised route network segments:4   Successful:2    Failed:2    Probe status:completed 
  Advertised route network segment info: 
  ------------------------------------------------ 
  No.     TestSrcIp             Advertised Route Network Segment      Probe Result 
  1       10.0.0.0              10.0.0.0/24                           Failed     
  2       10.0.1.0              10.0.1.0/26                           Abnormal        
  3       10.0.2.0              10.0.3.0/24                           Successful     
  4       10.0.3.0              10.0.3.0/26                           Successful

  (结果个数  = 1)
  ```
- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.26.0.115之间的路由是否正常，配置的探测源IP为10.122.122.3，探测方式为TRACERT。显示探测结果：

  ```
  DSP PDNTSTRESULT:;
  ```

  ```
  RETCODE = 0  Operation Success.  
  PDN侧路由探测结果信息
  -------------------------- 
  结果=   
  Pool name:pool-test    VPN-instance:vpn-test  Tigger Type:NONE   Execute Time:1970-01-01 08:00:00  Source IP address:10.122.122.3    Destination IP address:10.26.0.115    DSCP:0    Probe mode:TRACERT 
  Test hops:18     Probe status:completed 
  Track 10.26.0.115 routing through up to 30 hops 
  No.     Gateway address                        Probe packet delay 
  1       10.3.112.1                 10 ms    10 ms    10 ms 
  2       10.32.216.1                19 ms    19 ms    19 ms 
  3       10.32.216.1                39 ms    19 ms    19 ms 
  4       10.32.136.23               19 ms    39 ms    39 ms 
  5       10.32.168.22               20 ms    39 ms    39 ms 
  6       10.32.197.4                59 ms    119 ms   39 ms 
  7       10.119.2.5                 59 ms    59 ms    39 ms 
  8       10.16.70.13               80 ms    79 ms    99 ms 
  9       10.16.71.6                139 ms   139 ms   159 ms 
  10      10.16.197.4               199 ms   180 ms   300 ms 
  11      10.16.7.2                 300 ms   239 ms   239 ms 
  12      * * *                                                
  13      10.11.4.72                 59 ms    499 ms   279 ms 
  14      * * *                                                
  15      * * *                                                
  16      * * *                                                
  17      * * *                                                
  18      10.26.0.115 (10.26.0.115)   339 ms   279 ms   279 ms  

  (结果个数 = 1)
  ```
- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.26.0.115之间的路由是否正常，配置的探测源IP为10.1.1.1，探测方式为DNS。显示探测结果：

  ```
  DSP PDNTSTRESULT:;
  ```

  ```
  RETCODE = 0  Operation Success.  

  PDN侧路由探测结果信息
  -------------------------- 
  结果  =   
  Pool name:pool-test    VPN-instance:NULL   Tigger Type:NONE    Execute Time:1970-01-01 08:00:00  Source IP address:10.1.1.1    Destination IP address:10.26.0.115    DSCP:0    Probe mode:DNS
  Probed advertised route network segments:1    Successful:0    Failed:1    Probe status:completed
  Advertised route network segment info:
  --------------------------------------
  No.     TestSrcIp                Advertised Route Network Segment                Probe Result
  1        10.1.1.1                  10.1.1.1/32                                     Failed

  (结果个数 = 1)
  ```
- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.1.1.1之间的路由是否正常，探测方式是PING。显示成功的探测结果：

  ```
  DSP PDNTSTRESULT: DISPLAYMODE=SUCCESS;
  ```

  ```
  RETCODE = 0  Operation Success.  

  PDN侧路由探测结果信息
  -------------------------- 
  结果  =   
  Pool name:pool-test    VPN-instance:NULL   Tigger Type:NONE    Execute Time:1970-01-01 08:00:00  Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING  Packet length:0 
  Probed advertised route network segments:4   Successful:2    Failed:2    Probe status:completed 
  Advertised route network segment info: 
  ------------------------------------------------ 
  No.     TestSrcIp             Advertised Route Network Segment      Probe Result  
  1       10.0.2.0              10.0.3.0/24                           Successful     
  2       10.0.3.0              10.0.3.0/26                           Successful

  (结果个数 = 1)
  ```
- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.1.1.1之间的路由是否正常，探测方式是PING。显示失败的探测结果：

  ```
  DSP PDNTSTRESULT: DISPLAYMODE=FAIL;
  ```

  ```
  RETCODE = 0  Operation Success.  

  PDN侧路由探测结果信息
  -------------------------- 
  结果  =   
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:NONE    Execute Time:1970-01-01 08:00:00  Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING  Packet length:0 
  Probed advertised route network segments:4   Successful:2    Failed:2    Probe status:completed 
  Advertised route network segment info: 
  ------------------------------------------------ 
  No.     TestSrcIp             Advertised Route Network Segment      Probe Result
  1       10.0.2.0              10.0.3.0/24                           Failed
  2       10.0.3.0              10.0.3.0/26                           Abnormal

  (结果个数 = 1)
  ```
- 探测地址池名称为pool-test的地址池中路由网段和PDN服务器10.1.1.1之间的路由是否正常，探测方式是PING。显示探测五分钟之后的探测结果：

  ```
  DSP PDNTSTRESULT:;
  ```

  ```
  RETCODE = 0  Operation Success.  

  PDN侧路由探测结果信息
  -------------------------- 
  结果  =   
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:NONE    Execute Time:1970-01-01 08:00:00  Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING  Packet length:0 
  Probed advertised route network segments:4096   Successful:4094    Failed:2    Probe status:completed 
  Advertised route network segment info: 
  ------------------------------------------------ 
  No.     TestSrcIp             Advertised Route Network Segment      Probe Result
  1       10.0.2.0              10.0.3.0/24                           Failed
  2       10.0.3.0              10.0.3.0/26                           Abnormal
  .....
  .....
  4096    10.10.1.0             10.10.1.0/26                          Success
  ------------------------------------------------ 
  由于规格限制,本次探测未覆盖全量子段,建议基于Section进行全量探测

  (结果个数 = 1)
  ```
- 没有启动PDN侧路由探测的查询结果：

  ```
  DSP PDNTSTRESULT:;
  ```

  ```
  RETCODE = 20111  There is no data in the table.

  No matching result is found
  ---    END
  ```

#### 输出结果说明

| 输出项名称                                    | 输出项解释       |
|:-----------------------------------------|:------------|
| Pool name                                | 指定地址池名字。    |
| VPN-instance                             | 指定VPN名字。    |
| Source IP address                        | 探测源地址。      |
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
| Tigger Type                              | 探测触发方式。     |
| Execute Time                             | 执行时间。       |