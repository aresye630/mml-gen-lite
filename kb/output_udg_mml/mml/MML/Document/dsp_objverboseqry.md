# 查询对象反向绑定关系（DSP OBJVERBOSEQRY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于提供对象反向绑定关系查询的功能。根据运营商指定的配置信息反向查询出引用了该配置数据的配置信息。

#### 注意事项

IMSI/MSISDN号段反向查询只支持在UEG网元内执行。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VERBOSEQRYTYPE  | 对象反向查询类型        | 可选必选说明：必选参数 参数含义：该参数用于指定对象反向查询类型。 数据来源：本端规划 取值范围：枚举类型。 IPLIST_VERBOSE：IP列表反向查询。HOST_VERBOSE：主机名反向查询。FILTER_VERBOSE：过滤器反向查询。FLOW_FILTER_VERBOSE：流过滤器反向查询。IMSIMS_SEG_VERBOSE：IMSI/MSISDN号段反向查询。SERVICE_PROP_VERBOSE：业务属性反向查询。L7FILTER_VERBOSE：七层过滤器反向查询。PCC_ACT_PROP_VERBOSE：PCC动作属性反向查询。URR_VERBOSE：URR反向查询。URRGROUP_VERBOSE：URR组反向查询。RULE_VERBOSE：规则反向查询。PCC_POLICY_GRP_VERBOSE：PCC策略组反向查询。CATEGORY_PROP_VERBOSE：分类属性反向查询。EXTEND_PROP_VERBOSE：扩展属性反向查询。USER_PROFILE_VERBOSE：用户模板反向查询。ACL_VERBOSE：ACL反向查询。ACL_NODE_VERBOSE：ACL节点反向查询。USR_LOCATION_VERBOSE：用户位置反向查询。USR_LOC_GROUP_VERBOSE：用户位置组反向查询。QOS_PROP_VERBOSE：QoS属性反向查询。FLW_FLTR_GRP_V：流过滤器组反向查询。 默认值：无 配置原则：当需要查询某个配置对象记录被其他配置对象引用的关系时，需要选择相应的反向查询类型。 |
| IPLISTNAME      | IP列表名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“IPLIST_VERBOSE”时为必选参数。 参数含义：该参数用于指定IP列表名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD IPLIST配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| HOSTNAME        | Host配置名称        | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“HOST_VERBOSE”时为必选参数。 参数含义：该参数用于指定Host配置名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD HOST配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FILTERNAME      | 过滤器名字           | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“FILTER_VERBOSE”时为必选参数。 参数含义：该参数用于指定过滤器名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD FILTER配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| FILTERQRYTYPE   | 过滤器反向查询类型       | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“FILTER_VERBOSE”时为必选参数。 参数含义：该参数用于指定过滤器反向查询类型。 数据来源：本端规划 取值范围：枚举类型。 FLOW_FILTER_QRY：流过滤器绑定查询。ACL_NODE_QRY：ACL节点绑定查询。RULE_QRY：规则绑定查询。USER_PROFILE_QRY：用户模板绑定查询。PROT_DEFINE_QRY：自定义协议绑定查询。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| FLOWFILTERNAME  | 流过滤器名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“FLOW_FILTER_VERBOSE”时为必选参数。 参数含义：该参数用于指定流过滤器名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD FLOWFILTER配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SRVPROPNAME     | 业务属性名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“SERVICE_PROP_VERBOSE”时为必选参数。 参数含义：该参数用于指定业务属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD SERVICEPROP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| L7FILTERNAME    | 七层过滤器名字         | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“L7FILTER_VERBOSE”时为必选参数。 参数含义：该参数用于指定七层过滤器名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD L7FILTER配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PCCACTPROPNAME  | PCC动作属性名称       | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“PCC_ACT_PROP_VERBOSE”时为必选参数。 参数含义：该参数用于指定PCC动作属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD PCCACTIONPROP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| URRNAME         | URR名称           | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“URR_VERBOSE”时为必选参数。 参数含义：该参数用于指定URR名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD URR配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| URRGROUPNAME    | URR组名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“URRGROUP_VERBOSE”时为必选参数。 参数含义：该参数用于指定URR组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD URRGROUP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| URRGROUPQRYTYPE | URR组查询类型        | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“URRGROUP_VERBOSE”时为必选参数。 参数含义：该参数用于指定URR组查询类型。 数据来源：本端规划 取值范围：枚举类型。 PCC_POLICY_GRP_QRY：PCC策略组绑定查询。USER_PROFILE_QRY：用户模板绑定查询。CTX_START_QRY：上下文激活特定费率组绑定查询。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| RULENAME        | 规则名称            | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“RULE_VERBOSE”时为必选参数。 参数含义：该参数用于指定规则名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用 ADD RULE 或 ADD BLACKLISTRULE 命令配置生成。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PCCPOLICYGRPNM  | PCC策略组名称        | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“PCC_POLICY_GRP_VERBOSE”时为必选参数。 参数含义：该参数用于指定PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD PCCPOLICYGRP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CATEPROPNAME    | 分类属性名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“CATEGORY_PROP_VERBOSE”时为必选参数。 参数含义：该参数用于指定分类属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD CATEGORYPROP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| EXTENDPROPNAME  | 扩展属性名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“EXTEND_PROP_VERBOSE”时为必选参数。 参数含义：该参数用于指定扩展属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD EXTENDPROP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| USERPROFILENAME | 用户模板名称          | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“USER_PROFILE_VERBOSE”时为必选参数。 参数含义：该参数用于指定用户模板名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD USERPROFILE配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ACLNAME         | ACL名称           | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“ACL_VERBOSE”时为必选参数。 参数含义：该参数用于指定ACL名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD ACL配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ACLNODENAME     | ACL节点名称         | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“ACL_NODE_VERBOSE”时为必选参数。 参数含义：该参数用于指定ACL节点名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD ACLNODE配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LOCATIONNAME    | 位置名称            | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“USR_LOCATION_VERBOSE”时为必选参数。 参数含义：该参数用于指定位置名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LOCGROUPNAME    | 位置组名称           | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“USR_LOC_GROUP_VERBOSE”时为必选参数。 参数含义：该参数用于指定位置组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| QOSPROPNAME     | Qos属性名称         | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“QOS_PROP_VERBOSE”时为必选参数。 参数含义：该参数用于指定QoS属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD QOSPROP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| FLWFLTRGRPNAME  | 流过滤器组名称         | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“FLW_FLTR_GRP_V”时为必选参数。 参数含义：该参数用于指定流过滤器组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD FLOWFILTERGRP配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IMSIMSSEGNAME   | IMSI/MSISDN号段名称 | 可选必选说明：条件必选参数 前提条件：该参数在“VERBOSEQRYTYPE”配置为“IMSIMS_SEG_VERBOSE”时为必选参数。 参数含义：该参数用于指定IMSI/MSISDN号段名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

#### 使用实例

- 当运营商需要查询名字为“test\_iplist1”的IPLIST被哪些FILTER绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=IPLIST_VERBOSE,IPLISTNAME="test_iplist1";
  ```

  ```
  RETCODE = 0  Operation Success.

  IPList Binding Filter Information
  -------------------------
  IP List Name    Binding Filter Name 
  test_iplist1     test_filter1        
  test_iplist1     test_filter2        
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_host1”的HOST被哪些FILTER和SIGNADBRULE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=HOST_VERBOSE,HOSTNAME="test_host1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Host Binding Information
  -------------------------
  Host Configuration Name    Binding Filter Name    Binding Signature Database Rule Name 
  test_host1                 test_filter1           NULL                                 
  test_host1                 NULL                   test_signadbrule                   
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_filter1”的FILTER被哪些FLOWFILTER绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FILTER_VERBOSE,FILTERNAME="test_filter1",FILTERQRYTYPE=FLOW_FILTER_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  Filter Binding Flow Filter Information
  --------------------------------------
  Filter Name    Binding Flow Filter Name
  test_filter1   test_flowfilter1
  test_filter1   test_flowfilter2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_filter1”的FILTER被哪些ACLNODE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FILTER_VERBOSE,FILTERNAME="test_filter1",FILTERQRYTYPE=ACL_NODE_QRY;
  ```

  ```
   RETCODE = 0  Operation Success.

  Filter Binding ACL Node Information
  -----------------------------------
  Filter Name    Binding ACL Node Name
  test_filter1   test_aclnode1
  test_filter1   test_aclnode2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_filter1”的FILTER被哪些RULE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FILTER_VERBOSE,FILTERNAME="test_filter1",FILTERQRYTYPE=RULE_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  Filter Binding Rule Information
  -------------------------------
  Filter Name    Binding Rule Name 
  test_filter1   test_rule1
  test_filter1   test_rule2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_filter1”的FILTER被哪些USERPROFILE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FILTER_VERBOSE,FILTERNAME="test_filter1",FILTERQRYTYPE=USER_PROFILE_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  Filter Binding User Profile Information
  ---------------------------------------
  Filter Name    Binding User Profile Name
  test_filter1   test_userprofile1
  test_filter1   test_userprofile2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_filter1”的FILTER被哪些PROTOCOLDEFINE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FILTER_VERBOSE,FILTERNAME="test_filter1",FILTERQRYTYPE=PROT_DEFINE_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  Filter Binding Protocol Define Information
  ------------------------------------------
  Filter Name    Binding Self-defined Protocol Name
  test_filter1   test_protoclodefine1
  test_filter1   test_protoclodefine2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_flowfilter1”的FLOWFILTER被哪些RULE和FLOWFILTERGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FLOW_FILTER_VERBOSE,FLOWFILTERNAME="test_flowfilter1";
  ```

  ```
  RETCODE = 0  Operation Success.

  FlowFilter Binding Rule Information
  -----------------------------------
  Flow Filter Name    Binding Rule Name    Binding Flow Filter Group Name 
  test_flowfilter1    test_rule1           NULL                           
  test_flowfilter1    test_rule2           NULL                           
  test_flowfilter1    NULL                 test_flowfiltergrp1            
  (Number of results = 3) 
  ---    END
  ```
- 当运营商需要查询名字为“test\_imsimsisdnseg1”的IMSIMSISDNSEG被哪些IMSIMSISDNSEG绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=IMSIMS_SEG_VERBOSE,IMSIMSSEGNAME="test_imsimsisdnseg1";
  ```

  ```
  RETCODE = 0  Operation Success.

  IMSI/MSISDN Segment Binding Information
  -------------------------
  IMSI/MSISDN Segment Name    Binding IMSI/MSISDN Segment Group Name 
  test_imsimsisdnseg1         imsimsisdng                            
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_serviceprop1”的SERVICEPROP被哪些PCCPOLICYGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=SERVICE_PROP_VERBOSE,SRVPROPNAME="test_serviceprop1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Service Property Binding Information
  -------------------------
  Service Property Name    Binding PCC Policy Group Name 
  test_serviceprop1        test_pccpolicygrp1            
  test_serviceprop1        test_pccpolicygrp2            
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_L7FILTER”的L7FILTER被哪些FLOWFILTER绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=L7FILTER_VERBOSE,L7FILTERNAME="test_l7filter1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Layer 7 Filter Binding Information
  -------------------------
  Layer 7 Filter Name    Binding Flow Filter Name 
  test_l7filter1         test_flowfilter1         
  test_l7filter1         test_flowfilter2         
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_pccactionprop1”的PCCACTIONPROP被哪些PCCPOLICYGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=PCC_ACT_PROP_VERBOSE,PCCACTPROPNAME="test_pccactionprop1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Pcc Action Property Binding Information
  -------------------------
  PCC Action Property Name    Binding PCC Policy Group Name 
  test_pccactionprop1         test_pccpolicygrp1            
  test_pccactionprop1         test_pccpolicygrp2            
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_urr1”的URR被哪些URRGROUP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=URR_VERBOSE,URRNAME="test_urr1";
  ```

  ```
  RETCODE = 0  Operation Success.

  URR Binding Information
  -------------------------
  URR Name    Binding URRGroup Name                  
  test_urr1    test_urrgroup1               
  test_urr1    test_urrgroup2               
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_urrgroup1”的URRGROUP被哪些PCCPOLICYGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=URRGROUP_VERBOSE,URRGROUPNAME="test_urrgroup1",URRGROUPQRYTYPE=PCC_POLICY_GRP_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  URRGroup Binding PCC Policy Group Information
  ----------------------------------------------------
  URRGroup Name    Binding PCC Policy Group Name
  test_urrgroup1          test_pccpolicygrp1
  test_urrgroup1          test_pccpolicygrp2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_urrgroup1”的URRGROUP被哪些USERPROFILE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=URRGROUP_VERBOSE,URRGROUPNAME="test_urrgroup1",URRGROUPQRYTYPE=USER_PROFILE_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  URRGroup Binding User Profile Information
  ------------------------------------------------
  URRGroup Name    Binding User Profile Name
  test_urrgroup1          test_userprofile1
  test_urrgroup1          test_userprofile2
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_urrgroup1”的URRGROUP是否被GLBCTXREQRATE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=URRGROUP_VERBOSE,URRGROUPNAME="test_urrgroup1",URRGROUPQRYTYPE=CTX_START_QRY;
  ```

  ```
  RETCODE = 0  Operation Success.

  URRGroup Binding Ctx Start Rating Group Information
  ----------------------------------------------------------
         URRGroup  Name  =  test_urrgroup1
  Binding Ctx Start Object  Name  =  GlbCtxReqRate
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_rule1”的RULE被哪些USERPROFILE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=RULE_VERBOSE,RULENAME="test_rule1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Rule Binding Information
  -------------------------
                        Rule Name  =  test_rule1
        Binding User Profile Name  =  test_userprofile1
  Binding Service Statistics Name  =  NULL
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_pccpolicygrp1”的PCCPOLICYGRP被哪些RULE绑定和是否被AFPolicy绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=PCC_POLICY_GRP_VERBOSE,PCCPOLICYGRPNM="test_pccpolicygrp1";
  ```

  ```
  RETCODE = 0  Operation Success.

  PCC Policy Group Binding Information
  -------------------------
           PCC Policy Group Name  =  test_pccpolicygrp1
               Binding Rule Name  =  test_rule1
  Anti Fraud Policy Binding Flag  =  Yes
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_categoryprop1”的CATEGORYPROP被哪些RULE绑定和是否被AFPolicy绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=CATEGORY_PROP_VERBOSE,CATEPROPNAME="test_categoryprop1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Category Property Binding Information
  -------------------------
          Category Property Name  =  test_categoryprop1
               Binding Rule Name  =  test_rule1
  Anti Fraud Policy Binding Flag  =  Yes
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_extendprop1”的EXTENDPROP被哪些PCCPOLICYGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=EXTEND_PROP_VERBOSE,EXTENDPROPNAME="test_extendprop1";
  ```

  ```
  RETCODE = 0  Operation Success.

  Extend Property Binding Information
  -------------------------
  Extension Property Name    Binding PCC Policy Group Name 
  test_extendprop1           test_pccpolicygrp1            
  test_extendprop1           test_pccpolicygrp2            
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_userprofile1”的USERPROFILE被哪些BWMUSERGROUP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=USER_PROFILE_VERBOSE,USERPROFILENAME="test_userprofile1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  User Profile Binding Information
  --------------------------------
  User Profile Name  Binding User Group Name  

  test_userprofile1  test_bwmusergroup1       
  test_userprofile1  test_bwmusergroup2       
  (Number of results = 2)

  ---    END
  ```
- 当运营商需要查询名字为“test\_acl”的ACL被哪些APN绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=ACL_VERBOSE,ACLNAME="test_acl";
  ```

  ```
  RETCODE = 0  Operation Success.

  ACL Binding Information
  -------------------------
  ACL Name    Binding APN Name 
  test_acl    apn1             
  test_acl    apn2             
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_aclnode1”的ACLNODE被哪些ACL绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=ACL_NODE_VERBOSE,ACLNODENAME="test_aclnode1";
  ```

  ```
  RETCODE = 0  Operation Success.

  ACL Node Binding Information
  -------------------------
  ACL Node Name    Binding ACL Name 
  test_aclnode1    test_acl         
  test_aclnode1    test_acl1        
  (Number of results = 2)
  ---    END
  ```
- 当运营商需要查询名字为“test\_usrlocation1”的USRLOCATION被哪些USRLOCATIONGRP和HOTSPOTCELL绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=USR_LOCATION_VERBOSE,LOCATIONNAME="test_usrlocation1";
  ```

  ```
  RETCODE = 0  Operation Success.

  User Location Binding Information
  -------------------------
                Location Name  =  test_usrlocation1
    Binding Hotspot Cell Name  =  NULL
  Binding Location Group Name  =  test_usrlocationgrp1
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_usrlocationgrp1”的USRLOCATION被哪些USRPROFGROUP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=USR_LOC_GROUP_VERBOSE,LOCGROUPNAME="test_usrlocationgrp1";
  ```

  ```
  RETCODE = 0  Operation Success.

  User Location Group Binding Information
  -------------------------
              Location Group Name  =  test_usrlocationgrp1
  Binding User Profile Group Name  =  NULL
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_qosprop1”的QoSPROP被哪些PCCPOLICYGRP绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=QOS_PROP_VERBOSE,QOSPROPNAME="test_qosprop1";
  ```

  ```
  RETCODE = 0  Operation Success.

  QOS Property Binding Information
  -------------------------
              QoS Property Name  =  test_qosprop1
  Binding PCC Policy Group Name  =  test_pccpolicygrp1
  (Number of results = 1)
  ---    END
  ```
- 当运营商需要查询名字为“test\_flowfiltergrp1”的FLOWFILTERGRP被哪些RULE绑定时，则命令如下：

  ```
  DSP OBJVERBOSEQRY:VERBOSEQRYTYPE=FLW_FLTR_GRP_V,FLWFLTRGRPNAME="test_flowfiltergrp1";
  ```

  ```
  RETCODE = 0  Operation Success.

  FlowFilterGroup Binding Rule Information
  ----------------------------------------
  Flow Filter Group Name    Binding Rule Name 
  test_flowfiltergrp1       test_rule1         
  test_flowfiltergrp1       test_rule2         
  (Number of results = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称                | 输出项解释                     |
|:---------------------|:--------------------------|
| 过滤器名字                | 用于指定过滤器名字。                |
| 绑定的ACL节点名称           | 用于指定绑定的ACL节点名称。           |
| 绑定的流过滤器名称            | 用于指定绑定的流过滤器名称。            |
| 绑定的自定义协议名称           | 用于指定绑定的自定义协议名称。           |
| 绑定的用户模板名称            | 用于指定绑定的用户模板名称。            |
| 绑定的规则名称              | 用于指定绑定的规则名称。              |
| URR组名称               | 用于指定URR组名称。               |
| 绑定的上下文激活初始特定计费属性对象名称 | 用于指定绑定的上下文激活初始特定计费属性对象名称。 |
| 绑定的PCC策略组名称          | 用于指定绑定的PCC策略组名称。          |
| ACL节点名称              | 用于指定ACL节点名称。              |
| 绑定的ACL名称             | 用于指定绑定的ACL名称。             |
| ACL名称                | 用于指定ACL名称。                |
| 绑定的APN名称             | 用于指定绑定的APN名称。             |
| 分类属性名称               | 用于指定分类属性名称。               |
| 是否被防欺诈策略绑定           | 用于表示是否被防欺诈策略绑定。           |
| 扩展属性名称               | 用于指定扩展属性名称。               |
| 流过滤器名称               | 用于指定流过滤器名称。               |
| 绑定的流过滤器组名称           | 用于指定绑定的流过滤器组名称。           |
| 流过滤器组名称              | 用于指定流过滤器组名称。              |
| Host配置名称             | 用于指定Host配置名称。             |
| 绑定的过滤器名字             | 用于指定绑定的过滤器名字。             |
| 绑定的特征库规则协议名称         | 用于指定绑定的特征库规则名称。           |
| IP列表名称               | 用于指定IP列表名称。               |
| 七层过滤器名字              | 用于指定七层过滤器名字。              |
| PCC动作属性名称            | 用于指定PCC动作属性名称。            |
| PCC策略组名称             | 用于指定PCC策略组名称。             |
| Qos属性名称              | 用于指定QoS属性名称。              |
| 规则名称                 | 用于指定规则名称。                 |
| 绑定的业务统计名称            | 用于指定绑定的业务统计名称。            |
| 业务属性名称               | 用于指定业务属性名称。               |
| URR名称                | 用于指定URR名称。                |
| 绑定的URR组名称            | 用于指定绑定的URR组名称。            |
| 用户模板名称               | 用于指定用户模板名称。               |
| 绑定的用户组名称             | 用于指定绑定的用户组名称。             |
| 位置名称                 | 用于指定位置名称。                 |
| 绑定的热点小区名称            | 用于指定绑定的热点小区名称。            |
| 绑定的位置组名称             | 用于指定绑定的位置组名称。             |
| 位置组名称                | 用于指定位置组名称。                |
| 绑定的用户模板组名称           | 用于指定绑定的用户模板组名称。           |
| IMSI/MSISDN号段名称      | 用于指定IMSI/MSISDN号段名称。      |
| 绑定的IMSI/MSISDN号段组名称  | 用于指定绑定的IMSI/MSISDN号段组名称。  |