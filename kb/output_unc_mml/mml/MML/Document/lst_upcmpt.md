# 查询UP节点协议兼容性配置（LST UPCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询UP节点协议兼容性配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数  参数含义：该参数用于指定UPF实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~36。参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。  默认值：无  配置原则：  该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |

## 使用实例

查询UPF实例标识为upf\_instance\_1的UP节点协议兼容性配置，执行如下命令：

```
%%LST UPCMPT: UPFINSTANCEID="upf_instance_1";%%
RETCODE = 0  操作成功

结果如下
--------
                                      UPF实例标识  =  upf_instance_1
                                  APN/DNN编码格式  =  不携带OI信息
                             网络切片选择辅助信息  =  继承
                          Node ID信元FQDN编码格式  =  点分格式
                             是否携带地址池占位符  =  继承全局
                 是否携带运营商定制的RAT Type信元  =  不使能
           是否携带运营商定制的L2TP User Info信元  =  不使能
         是否携带运营商定制的L2TP Tunnel Info信元  =  不使能
是否携带运营商定制的User Location Information信元  =  不使能
             是否携带UE IP Address信元的S/D标记位  =  不使能
                      网络实例Domain Name编码格式  =  点分格式
                                  是否支持OpenUPF  =  不支持OpenUPF
                           UPF Pa接口配置严格匹配  =  关闭Pa接口严格匹配
                                     L2TP隧道信息  =  不使能
                                  L2TP用户PCO信息  =  不使能
                             Http重定向对端接口值  =  Core
                   5G LAN是否按运营商定制方式实现  =  使能
                    APP保障专载预定义规则下发方式  =  使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                                 | 输出项解释                                                                                                                                              |
|:--------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| UPF实例标识                               | 该参数用于指定UPF实例标识。                                                                                                                                    |
| APN/DNN编码格式                           | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的APN/DNN信元编码格式。                                                                                                   |
| 网络切片选择辅助信息                            | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的SNSSAI信元是否为标准信元。                                                                                                 |
| Node ID信元FQDN编码格式                     | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的FQDN类型Node ID信元的编码格式。                                                                                            |
| 是否携带地址池占位符                            | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP消息是否携带地址池占位符。UNC向UDG申请双栈地址的时候，如果只有IPv6类型的地址池，则将IPv4地址池的位置用*代替，即为占位符。 以免对端将IPv6类型的地址池识别成IPv4类型。               |
| 是否携带运营商定制的RAT Type信元                  | 该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment/Modification Request消息中是否携带运营商定制的RAT Type信元。                                          |
| 是否携带运营商定制的L2TP User Info信元            | 该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP User Info信元。                                                 |
| 是否携带运营商定制的L2TP Tunnel Info信元          | 该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP Tunnel Info信元。                                               |
| 是否携带运营商定制的User Location Information信元 | 该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的User Location Information信元。                                      |
| 是否携带UE IP Address信元的S/D标记位            | 该参数用于指定UE IP Address信元是否携带S/D标记位。                                                                                                                  |
| 网络实例Domain Name编码格式                   | 该参数用于指定网络实例携带Domain Name时的编码格式。配置为点分格式时，部分场景下会使用点分格式。配置为LV格式时仅使用LV编码格式。                                                                            |
| 是否支持OpenUPF                           | 该参数用于指定对端UPF是否是OpenUPF。                                                                                                                            |
| UPF Pa接口配置严格匹配                        | 该参数用于指定UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)配置是否严格匹配。如果开关关闭，SMF上UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)可以共用。如果开关开启，UPLOGICINTF配置的Pa接口(Gn/S5S8 Pgw/n9a)不可以共用。 |
| L2TP隧道信息                              | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP隧道信息是否是华为私有信元格式。                                                                                             |
| L2TP用户PCO信息                           | 该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP用户PCO信息是否是华为私有信元格式。                                                                                          |
| HTTP重定向对端接口值                          | 该参数用于指定HTTP重定向对端接口值。                                                                                                                               |
| 定制携带UE IP地址的方式                        | 该参数用于通用DNN漫游分流特性中专网会话SMF是否通过运营商定制的信元格式携带大网UE IP地址信息给锚点UPF。                                                                                         |
| 路径迁移UserID信元编码格式                      | 该参数用于设置路径迁移UserID信元编码格式。                                                                                                                           |
| 路径迁移是否携带UserID信元                      | 该参数用于设置路径迁移是否携带UserID信元。                                                                                                                           |
| 5G LAN是否按运营商定制方式实现                    | 该参数用于控制5G LAN SMF是否按运营商定制方式实现。                                                                                                                     |
| APP保障专载预定义规则下发方式                      | 该参数用于控制SMF/GW-C发送给UPF/GW-U的PFCP Session Establishment/Modification Request消息中，专有承载中无SDFILTER信元时，APP保障预定义规则下发方式。                                    |