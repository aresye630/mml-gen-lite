# 显示IPsuit信息（DSP IPSUIT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询IPSUIT信息。

#### 注意事项

Owner PodName标识此IPSuit绑定的ownerid，Binding PodName标识此IPSuit绑定的实例的PodName。当发生ISU/APU发生故障倒换期间，Owner PodName和Binding PodName可能不一致。当IPSuit对应的token挂起时，Binding PodName可能为空，标识当前IPSuit未和任何ISU/APU绑定。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称      | 参数说明                                                                                          |
|:-----------|:----------|:----------------------------------------------------------------------------------------------|
| IPSUITNAME | IPSuit 名称 | 可选必选说明：可选参数 参数含义：IP Suit的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。此名称系统自动生成，取值为1~64。 默认值：无 配置原则：无 |

#### 使用实例

- 查询IPSUIT信息，IPSUITNAME为“1”：

  ```
  DSP IPSUIT: IPSUITNAME="1";
  ```

  ```
  RETCODE = 0 操作成功。

  IPSuit 信息
  -----------
  Result  =  
                                IPSuit Name  =  1
                              Owner PodName  =  isu-pod-1
                            Binding PodName  =  isu-pod-1
               n3if1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.1
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:0
                               VPN Instance  =  NULL
               s1-uif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.2
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:1
                               VPN Instance  =  NULL
               paif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.5
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:2
                               VPN Instance  =  NULL
               s5-sif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.3
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:3
                               VPN Instance  =  NULL
               n9cif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.4
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:4
                               VPN Instance  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有IPSUIT信息：

  ```
  DSP IPSUIT:;
  ```

  ```
  RETCODE = 0 操作成功。

  IPSuit 信息
  -----------
  Result
                                    IPSuit Name  =  1
                              Owner PodName  =  isu-pod-1
                            Binding PodName  =  isu-pod-1
               n3if1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.1
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:0
                               VPN Instance  =  NULL
               n9cif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.2
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:1
                               VPN Instance  =  NULL
               paif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.3
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:2
                               VPN Instance  =  NULL
               s1-uif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.4
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:3
                               VPN Instance  =  NULL
               s5-sif1/1/0 Interface Info : 
                               IPV4 Address  =  192.168.0.5
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:4
                               VPN Instance  =  NULL  

                                IPSuit Name  =  2
                              Owner PodName  =  isu-pod-0
                            Binding PodName  =  isu-pod-0
               paif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.6
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:5
                               VPN Instance  =  NULL
               s1-uif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.7
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:6
                               VPN Instance  =  NULL
               s5-sif1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.8
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:7
                               VPN Instance  =  NULL
               n3if1/2/0 Interface Info : 
                               IPV4 Address  =  192.168.0.9
                               IPV6 Address  =  2001:0DB8:0:0:0:0:0:8
                               VPN Instance  =  NULL                              
  (结果个数 = 2)

  --- END
  ```

#### 输出结果说明

| 输出项名称              | 输出项解释                                                                       |
|:-------------------|:----------------------------------------------------------------------------|
| IPSuit Name        | 标识IPSuit名称，为系统自动生成，取值范围为1~64。                                               |
| Owner PodName      | 标识此IPSuit绑定的ownerid，当IPSuit未绑定ownerid时，显示为“NULL”。                           |
| Binding PodName    | 标识此IPSuit绑定的实例的PodName，当IPSuit未绑定实例PodName时，显示为“NULL”。                      |
| xxx Interface Info | 标识此IPSsuit下的逻辑接口信息，支持IPSuit的逻辑接口类型：s5-sif，s1-uif，saif，paif，n3if，n9cif，scif。 |
| IPV4 Address       | 标识逻辑接口的IPV4地址，当逻辑接口没有绑定IPV4地址时，显示为“NULL”。                                   |
| IPV6 Address       | 标识逻辑接口的IPV6地址，当逻辑接口没有绑定IPV6地址时，显示为“NULL”。                                   |
| VPN Instance       | 标识逻辑接口的VPN实例，当逻辑接口没有绑定VPN实例时，显示为“NULL”。                                     |