# 查询RADIUS计费服务器组的私有扩展属性（LST RDSACCTREQVSA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来显示指定RADIUS服务器组的RADIUS计费3gpp和3gpp2私有扩展属性的配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称                  | 参数说明                                                                         |
|:--------------|:----------------------|:-----------------------------------------------------------------------------|
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：可选参数 参数含义：RADIUS服务器组名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无 |

#### 使用实例

查询名为“radiusgroup”的RADIUS服务器组的Radius计费3gpp和3gpp2私有扩展属性信息：

```
%%LST RDSACCTREQVSA:RDSSVRGRPNAME="radiusgroup";
```

```
%%
RETCODE = 0  操作成功

RADIUS计费请求消息私有扩展属性
------------------------------
                     RADIUS Server Group名称  =  radiusgroup
                        支持3gpp私有扩展属性  =  支持
                           携带3GPP-IMSI属性  =  不携带该字段
                    携带3GPP-Charging-ID属性  =  携带该字段
                       携带3GPP-PDP-Type属性  =  携带该字段
                     携带3GPP-CG-Address属性  =  携带该字段
携带3GPP-GPRS-Negotiated-QoS-Profile扩展属性  =  携带该字段
                携带3GPP-SGSN（SGW）-Address  =  携带该字段
                   携带3GPP-GGSN-Address信元  =  携带该字段
                        携带IMSI-MCC-MNC信元  =  携带该字段
                        携带GGSN-MCC-MNC信元  =  携带该字段
                          携带3GPP-NSAPI属性  =  携带该字段
                 携带3GPP-Selection-Mode属性  =  携带该字段
       携带3GPP-Charging-Characteristics属性  =  携带该字段
             携带SGSN（SGW）-MCC-MNC扩展属性  =  携带该字段
                          携带IMEISV扩展属性  =  携带该字段
 Accouting Interim消息是否携带IMEISV扩展属性  =  不携带该字段
    Accouting Stop消息是否携带IMEISV扩展属性  =  不携带该字段
                   携带3GPP-RAT-Type扩展属性  =  携带该字段
              携带User-Location-Info扩展属性  =  携带该字段
                    携带3GPP-MS-TimeZone属性  =  携带该字段
                  携带stop-indicator扩展属性  =  携带该字段
                携带3GPP-Negotiated-DSCP属性  =  携带该字段
                   携带packet-filter扩展属性  =  携带该字段
              携带3GPP-SGSN-IPv6-Address属性  =  携带该字段
              携带3GPP-GGSN-IPv6-Address属性  =  携带该字段
                         携带twan-id扩展属性  =  不携带该字段
                       支持3gpp2私有扩展属性  =  支持
                      携带3gpp2-bsid私有属性  =  不携带该字段
                携带3GPP-CG-IPv6-Address属性  =  不携带该字段
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET RDSACCTREQVSA的参数说明。