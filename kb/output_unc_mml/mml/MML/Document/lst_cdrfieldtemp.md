# 查询话单字段模板（LST CDRFIELDTEMP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询指定话单字段模板的具体配置信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称    | 参数说明                                                                         |
|:-------------|:--------|:-----------------------------------------------------------------------------|
| TEMPLATENAME | 话单字段模板名 | 可选必选说明：可选参数 参数含义：指定话单字段模板的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |

#### 使用实例

查询名为“cdrfieldtemp”的话单字段模板信息：

```
LST CDRFIELDTEMP: TEMPLATENAME="cdrfieldtemp";
```

```
RETCODE = 0  操作成功

CDR字段模板
-----------
                      话单字段模板名  =  cdrfieldtemp
              apn-network-identifier  =  包含该字段。
                  apn-selection-mode  =  包含该字段。
charge-characteristic-selection-mode  =  包含该字段。
                         diagnostics  =  携带该字段
                dynamic-address-flag  =  携带该字段
        external-charging-identifier  =  携带该字段
              ims-signalling-context  =  携带该字段
           imsi-unauthenticated-flag  =  不携带该字段
                list-of-service-data  =  携带该字段
              list-of-traffic-volume  =  携带该字段
        local-record-sequence-number  =  携带该字段
                              MSISDN  =  包含该字段。
                        ms-time-zone  =  携带该字段
       network-initiated-pdp-context  =  携带该字段
                             node-id  =  包含该字段。
                   pdn-connection-id  =  不包含该字段。
                            pdp-type  =  包含该字段。
                    pgw-address-used  =  不携带该字段
                    pgw-address-ipv6  =  携带该字段
                 pgw-plmn-identifier  =  不携带该字段
     ps-furnish-charging-information  =  携带该字段
                            rat-type  =  携带该字段
               record-extensions开关  =  携带该字段
             运营商record-extensions  =  内容计费
                     业务URL存在标识  =  携带该字段
                业务使用时长存在标识  =  不携带该字段
                      高精度时间标识  =  不包含该字段。
                   Direct Tunnel记录  =  不携带该字段
              record-sequence-number  =  携带该字段
                       served-imeisv  =  携带该字段
                  served-pdp-address  =  携带该字段
            sgsn-sgw-plmn-identifier  =  包含该字段。
                          start-time  =  不携带该字段
                           stop-time  =  不携带该字段
             threegpp2-user-location  =  携带该字段
           user-location-information  =  携带该字段
                 ULI携带WLAN地址信息  =  不包含该字段。
                   object identifier  =  1.3.6.1.4.1.2011.2.63
       cp-eps-optimisation-indicator  =  不携带该字段
                    sgw-address-ipv6  =  携带该字段
                   mo-exception-data  =  不携带该字段
            ePDG UE Local IP 和 Port  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                  pdp-type-extention  =  不携带该字段
                       packet-number  =  不使能
                    apn-rate-control  =  不携带该字段
           sgi-ptp-tunnelling-method  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
                      scs-as-address  =  不携带该字段
                uni-pdu-cp-only-flag  =  不携带该字段
              low-priority-indicator  =  不携带该字段
                              Snssai  =  不携带该字段
                             SscMode  =  不携带该字段
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD CDRFIELDTEMP的参数说明。