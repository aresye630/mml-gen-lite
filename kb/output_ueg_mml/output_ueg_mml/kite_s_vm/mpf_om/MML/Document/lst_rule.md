# 查询规则（LST RULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用于查询规则。

#### 注意事项

支持批量查询。如果不输入策略名称，则查询系统中所有的规则。如果输入了策略类型，则查询系统中配置为本策略类型的所有规则。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                |
|:-----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RULENAME   | 规则名称   | 可选必选说明：可选参数 参数含义：该参数用于设置规则名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：设置该参数时表示查询指定名称的规则，未设置该参数时表示查询系统中所有的规则。                                                                                                                      |
| POLICYTYPE | 策略类型   | 可选必选说明：可选参数 参数含义：该参数用于设置策略类型。 数据来源：本端规划 取值范围：枚举类型。 MTP：Mec流策略控制，代表该规则可以配置MTP策略，用于实现Mec业务流控制功能。BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。 默认值：无 配置原则：根据部署的业务策略选择相应的策略类型。 |

#### 使用实例

- 查询一条名为testrule的规则：

  ```
  LST RULE: RULENAME="testrule";
  ```

  ```
  RETCODE = 0  操作成功

  规则信息
  --------
                                        规则名称  =  testrule
                                        策略类型  =  PCC
                                  黑名单规则标识  =  普通规则
                                    流过滤器名称  =  testflowfiltername
                                  流过滤器组名称  =  NULL
                                      时间段名称  =  NULL
                                      全局优先级  =  65535
                                   PCC策略组名称  =  pccpolicygroup
                                    分类属性名称  =  NULL
                                      头增强名称  =  NULL
                              Radius消息触发标识  =  不使能
                Radius消息触发时报文默认处理动作  =  转发
                           Web Proxy IP-Farm名称  =  NULL
                          IP重定向虚拟IP协议版本  =  IPV4
                                IP重定向IPv6地址  =  ::
                                  IP重定向IP地址  =  0.0.0.0
                      Captive Portal IP-Farm名称  =  NULL
                                 重标记或FPI选择  =  重标记
                                  Remark配置类型  =  CLASS
                                  Remark分类类型  =  NULL
                                          重标记  =  NULL
                                           FPI值  =  NULL
                                      业务链名称  =  NULL
                                本地业务分流标识  =  不使能
                                  防火墙策略名称  =  NULL
                        流过滤器或流过滤器组选择  =  流过滤器
                                  智能重定向名称  =  NULL
                                 DNS重写动作名字  =  NULL
  指定业务触发radius消息发送时的业务报文延时时间  =  0
                                     Qos属性名称  =  NULL
                                 ADC静默通知标识  =  使能
                                   URL重定向名称  =  NULL
         NatFlag  =  NAT
  (结果个数 = 1)

  ---    END
  ```
- 查询所有规则：

  ```
  LST RULE:;
  ```

  ```
  RETCODE = 0  操作成功

  规则信息
  --------
  规则名称   策略类型  黑名单规则标识  流过滤器名称        流过滤器组名称  时间段名称  全局优先级  PCC策略组名称   分类属性名称  头增强名称  Radius消息触发标识  Radius消息触发时报文默认处理动作  Web Proxy IP-Farm名称  IP重定向虚拟IP协议版本  IP重定向IPv6地址  IP重定向IP地址  Captive Portal IP-Farm名称  重标记或FPI选择  Remark配置类型  Remark分类类型  重标记  FPI值  业务链名称  本地业务分流标识  防火墙策略名称  流过滤器或流过滤器组选择  智能重定向名称  DNS重写动作名字  指定业务触发radius消息发送时的业务报文延时时间  Qos属性名称  ADC静默通知标识  URL重定向名称  

  testrule   PCC       普通规则        testflowfiltername  NULL            NULL        65535       pccpolicygroup  NULL          NULL        不使能              转发                              NULL                   IPV4                    ::                0.0.0.0         NULL                        重标记           CLASS           NULL            NULL    NULL   NULL        不使能            NULL            流过滤器                  NULL            NULL             0                                               NULL         使能             NULL           
  testrule2  PCC       普通规则        testflowfiltername  NULL            NULL        65535       pccpolicygroup  NULL          NULL        不使能              转发                              NULL                   IPV4                    ::                0.0.0.0         NULL                        重标记           CLASS           NULL            NULL    NULL   NULL        不使能            NULL            流过滤器                  NULL            NULL             0                                               NULL         使能             NULL           
  (结果个数 = 2)

  ---    END
  ```

#### 输出结果说明

| 输出项名称               | 输出项解释                    |
|:--------------------|:-------------------------|
| 黑名单规则标识             | 用于显示黑名单规则标识。             |
| MTP策略组名称            | 用于显示MTP策略组名称。            |
| 分类属性名称              | 用于显示分类属性名称。              |
| Web Proxy IP-Farm名称 | 用于显示Web Proxy IP-Farm名称。 |

其余输出项请参见ADD BLACKLISTRULE的参数说明。