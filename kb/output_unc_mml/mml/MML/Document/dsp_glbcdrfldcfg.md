# 查询全局生效CDR字段配置（DSP GLBCDRFLDCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示全局生效的各类型的话单字段的具体配置。

如果全局模板下某话单类型未绑定模板，则显示该话单类型的缺省配置信息。显示信息中如果模板名字为NULL，则表示是缺省配置信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示全局绑定的话单字段的具体配置信息：

```
DSP GLBCDRFLDCFG:;
```

```
RETCODE = 0  操作成功

全局生效的CDR字段配置
---------------------
                 G-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
               PGW-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
               SGW-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
           ePDG UE Local IP and Port  =  不携带该字段
              low-priority-indicator  =  不携带该字段
                    apn-rate-control  =  不携带该字段
                   mo-exception-data  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
                 ULI携带WLAN地址信息  =  不包含该字段。
                    sgw-address-ipv6  =  携带该字段
                       packet-number  =  不使能
                   object identifier  =  1.3.6.1.4.1.2011.2.63
                   object identifier  =  1.3.6.1.4.1.2011.2.63
                   mo-exception-data  =  不携带该字段
                    apn-rate-control  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
                    sgw-address-ipv6  =  携带该字段
                    sgw-address-ipv6  =  携带该字段
            ePDG UE Local IP 和 Port  =  不携带该字段
              low-priority-indicator  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                       packet-number  =  不使能
                uni-pdu-cp-only-flag  =  不携带该字段
                   object identifier  =  1.3.6.1.4.1.2011.2.63
           sgi-ptp-tunnelling-method  =  不携带该字段
                  pdp-type-extention  =  不携带该字段
                      scs-as-address  =  不携带该字段
                  pdp-type-extention  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
                 ULI携带WLAN地址信息  =  不包含该字段。
                  pdp-type-extention  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                    apn-rate-control  =  不携带该字段
              low-priority-indicator  =  不携带该字段
           sgi-ptp-tunnelling-method  =  不携带该字段
           sgi-ptp-tunnelling-method  =  不携带该字段
                uni-pdu-cp-only-flag  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                uni-pdu-cp-only-flag  =  不携带该字段
                      scs-as-address  =  不携带该字段
            ePDG UE Local IP 和 Port  =  不携带该字段
                      scs-as-address  =  不携带该字段
                       packet-number  =  不使能
                 ULI携带WLAN地址信息  =  不包含该字段。
                   mo-exception-data  =  不携带该字段
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                                | 输出项解释                                                            |
|:-------------------------------------|:-----------------------------------------------------------------|
| G-CDR话单字段模板名                         | G-CDR话单字段模板的名称。                                                  |
| apn-network-identifier               | G-CDR话单中是否包含APN网络节点标识信息。                                         |
| apn-selection-mode                   | G-CDR话单中是否包含APN选择模式信息。                                           |
| charge-characteristic-selection-mode | G-CDR话单中是否包含计费属性选择模式标志。                                          |
| diagnostics                          | G-CDR话单中是否携带diagnostics字段。                                       |
| dynamic-address-flag                 | G-CDR话单中是否携带dynamic-address-flag字段。                              |
| external-charging-identifier         | G-CDR话单中是否携带external-charging-identifier字段。                      |
| ims-signalling-context               | G-CDR话单中是否携带ims-signalling-context字段。                            |
| imsi-unauthenticated-flag            | G-CDR话单中是否携带iMSIunauthenticatedFlag字段。                           |
| list-of-service-data                 | G-CDR话单中是否携带list-of-service-data字段。                              |
| list-of-traffic-volume               | G-CDR话单中是否携带流量容器字段。                                              |
| local-record-sequence-number         | G-CDR话单中是否携带本地话单序列号字段。                                           |
| MSISDN                               | G-CDR话单中是否包含用户MSISDN信息。                                          |
| ms-time-zone                         | G-CDR话单中是否携带ms-time-zone字段。                                      |
| network-initiated-pdp-context        | G-CDR话单中是否携带network-initiated-pdp-context字段。                     |
| node-id                              | G-CDR话单中是否包含网络节点标识信息。                                            |
| pdn-connection-id                    | G-CDR话单中是否包含pdn-connection-id信息。                                 |
| pdp-type                             | G-CDR话单中是否包含PDP上下文类型信息。                                          |
| pgw-address-used                     | G-CDR话单中是否携带pgw-address-used字段。                                  |
| pgw-address-ipv6                     | G-CDR话单中是否携带pgw-address-ipv6字段。                                  |
| pgw-plmn-identifier                  | G-CDR话单中是否携带pgw-plmn-identifier字段。                               |
| ps-furnish-charging-information      | G-CDR话单中是否携带ps-furnish-charging-information字段。                   |
| rat-type                             | G-CDR话单中是否携带rat-type字段。                                          |
| record-extensions                    | G-CDR话单中是否携带recordExtensions字段。                                  |
| 扩展字段类型                               | G-CDR话单中携带的扩展字段类型。                                               |
| 业务URL存在标识                            | G-CDR话单扩展字段中是否携带内容计费业务的第一个URL。                                   |
| 业务使用时长存在标识                           | G-CDR话单扩展字段中是否携带内容计费业务的实际持续时长。                                   |
| 高精度时间标识                              | G-CDR话单扩展字段中是否填充高精度时间。                                           |
| Direct Tunnel记录                      | G-CDR话单扩展字段中是否携带DT模式期间的上下行流量及RNC/NodeB地址更新列表。                    |
| record-sequence-number               | G-CDR话单中是否携带record-sequence-number字段。                            |
| served-imeisv                        | G-CDR话单中是否携带served-imeisv字段。                                     |
| served-pdp-address                   | G-CDR话单中是否携带served-pdp-address字段。                                |
| sgsn-sgw-plmn-identifier             | G-CDR话单中是否包含sgsn/sgw-plmn-identifier标志。                          |
| start-time                           | G-CDR话单中是否携带startTime字段。                                         |
| stop-time                            | G-CDR话单中是否携带stopTime字段。                                          |
| threegpp2-user-location              | G-CDR话单中是否携带threegpp2-user-location字段。                           |
| user-location-information            | G-CDR话单中是否携带user-location-information字段。                         |
| PGW-CDR话单字段模板名                       | PGW-CDR话单字段模板的名称。                                                |
| apn-network-identifier               | PGW-CDR话单中是否包含APN网络节点标识信息。                                       |
| apn-selection-mode                   | PGW-CDR话单中是否包含APN选择模式信息。                                         |
| charge-characteristic-selection-mode | PGW-CDR话单中是否包含计费属性选择模式标志。                                        |
| diagnostics                          | PGW-CDR话单中是否携带diagnostics字段。                                     |
| dynamic-address-flag                 | PGW-CDR话单中是否携带dynamic-address-flag字段。                            |
| external-charging-identifier         | PGW-CDR话单中是否携带external-charging-identifier字段。                    |
| ims-signalling-context               | PGW-CDR话单中是否携带ims-signalling-context字段。                          |
| imsi-unauthenticated-flag            | PGW-CDR话单中是否携带iMSIunauthenticatedFlag字段。                         |
| list-of-service-data                 | PGW-CDR话单中是否携带list-of-service-data字段。                            |
| list-of-traffic-volume               | PGW-CDR话单中是否携带流量容器字段。                                            |
| local-record-sequence-number         | PGW-CDR话单中是否携带本地话单序列号字段。                                         |
| MSISDN                               | PGW-CDR话单中是否包含用户MSISDN信息。                                        |
| ms-time-zone                         | PGW-CDR话单中是否携带ms-time-zone字段。                                    |
| network-initiated-pdp-context        | PGW-CDR话单中是否携带network-initiated-pdp-context字段。                   |
| node-id                              | PGW-CDR话单中是否包含网络节点标识信息。                                          |
| pdn-connection-id                    | PGW-CDR话单中是否包含pdn-connection-id信息。                               |
| pdp-type                             | PGW-CDR话单中是否包含PDP上下文类型信息。                                        |
| pgw-address-used                     | PGW-CDR话单中是否携带pgw-address-used字段。                                |
| pgw-address-ipv6                     | PGW-CDR话单中是否携带pgw-address-ipv6字段。                                |
| pgw-plmn-identifier                  | PGW-CDR话单中是否携带pgw-plmn-identifier字段。                             |
| ps-furnish-charging-information      | PGW-CDR话单中是否携带ps-furnish-charging-information字段。                 |
| rat-type                             | PGW-CDR话单中是否携带rat-type字段。                                        |
| record-extensions                    | PGW-CDR话单中是否携带recordExtensions字段。                                |
| 扩展字段类型                               | PGW-CDR话单中携带的扩展字段类型。                                             |
| 业务URL存在标识                            | PGW-CDR话单扩展字段中是否携带内容计费业务的第一个URL。                                 |
| 业务使用时长存在标识                           | PGW-CDR话单扩展字段中是否携带内容计费业务的实际持续时长。                                 |
| 高精度时间标识                              | PGW-CDR话单扩展字段中是否填充高精度时间。                                         |
| Direct Tunnel记录                      | PGW-CDR话单扩展字段中是否携带DT模式期间的上下行流量及RNC/NodeB地址更新列表。                  |
| record-sequence-number               | PGW-CDR话单中是否携带record-sequence-number字段。                          |
| served-imeisv                        | PGW-CDR话单中是否携带served-imeisv字段。                                   |
| served-pdp-address                   | PGW-CDR话单中是否携带served-pdp-address字段。                              |
| sgsn-sgw-plmn-identifier             | PGW-CDR话单中是否包含sgsn/sgw-plmn-identifier标志。                        |
| start-time                           | PGW-CDR话单中是否携带startTime字段。                                       |
| stop-time                            | PGW-CDR话单中是否携带stopTime字段。                                        |
| threegpp2-user-location              | PGW-CDR话单中是否携带threegpp2-user-location字段。                         |
| user-location-information            | PGW-CDR话单中是否携带user-location-information字段。                       |
| SGW-CDR话单字段模板名                       | SGW-CDR话单字段模板的名称。                                                |
| apn-network-identifier               | SGW-CDR话单中是否包含APN网络节点标识信息。                                       |
| apn-selection-mode                   | SGW-CDR话单中是否包含APN选择模式信息。                                         |
| charge-characteristic-selection-mode | SGW-CDR话单中是否包含计费属性选择模式标志。                                        |
| diagnostics                          | SGW-CDR话单中是否携带diagnostics字段。                                     |
| dynamic-address-flag                 | SGW-CDR话单中是否携带dynamic-address-flag字段。                            |
| external-charging-identifier         | SGW-CDR话单中是否携带external-charging-identifier字段。                    |
| ims-signalling-context               | SGW-CDR话单中是否携带ims-signalling-context字段。                          |
| imsi-unauthenticated-flag            | SGW-CDR话单中是否携带iMSIunauthenticatedFlag字段。                         |
| list-of-service-data                 | SGW-CDR话单中是否携带list-of-service-data字段。                            |
| list-of-traffic-volume               | SGW-CDR话单中是否携带流量容器字段。                                            |
| local-record-sequence-number         | SGW-CDR话单中是否携带本地话单序列号字段。                                         |
| MSISDN                               | SGW-CDR话单中是否包含用户MSISDN信息。                                        |
| ms-time-zone                         | SGW-CDR话单中是否携带ms-time-zone字段。                                    |
| network-initiated-pdp-context        | SGW-CDR话单中是否携带network-initiated-pdp-context字段。                   |
| node-id                              | SGW-CDR话单中是否包含网络节点标识信息。                                          |
| pdn-connection-id                    | SGW-CDR话单中是否包含pdn-connection-id信息。                               |
| pdp-type                             | SGW-CDR话单中是否包含PDP上下文类型信息。                                        |
| pgw-address-used                     | SGW-CDR话单中是否携带pgw-address-used字段。                                |
| pgw-address-ipv6                     | SGW-CDR话单中是否携带pgw-address-ipv6字段。                                |
| pgw-plmn-identifier                  | SGW-CDR话单中是否携带pgw-plmn-identifier字段。                             |
| ps-furnish-charging-information      | SGW-CDR话单中是否携带ps-furnish-charging-information字段。                 |
| rat-type                             | SGW-CDR话单中是否携带rat-type字段。                                        |
| record-extensions                    | SGW-CDR话单中是否携带recordExtensions字段。                                |
| 扩展字段类型                               | SGW-CDR话单中携带的扩展字段类型。                                             |
| 业务URL存在标识                            | SGW-CDR话单扩展字段中是否携带内容计费业务的第一个URL。                                 |
| 业务使用时长存在标识                           | SGW-CDR话单扩展字段中是否携带内容计费业务的实际持续时长。                                 |
| 高精度时间标识                              | SGW-CDR话单扩展字段中是否填充高精度时间。                                         |
| Direct Tunnel记录                      | SGW-CDR话单扩展字段中是否携带DT模式期间的上下行流量及RNC/NodeB地址更新列表。                  |
| record-sequence-number               | SGW-CDR话单中是否携带record-sequence-number字段。                          |
| served-imeisv                        | SGW-CDR话单中是否携带served-imeisv字段。                                   |
| served-pdp-address                   | SGW-CDR话单中是否携带served-pdp-address字段。                              |
| sgsn-sgw-plmn-identifier             | SGW-CDR话单中是否包含sgsn/sgw-plmn-identifier标志。                        |
| start-time                           | SGW-CDR话单中是否携带startTime字段。                                       |
| stop-time                            | SGW-CDR话单中是否携带stopTime字段。                                        |
| threegpp2-user-location              | SGW-CDR话单中是否携带threegpp2-user-location字段。                         |
| user-location-information            | SGW-CDR话单中是否携带user-location-information字段。                       |
| ULI携带WLAN地址信息                        | 表示ULI被设置为ENABLE时，接入P-GW时user-location-information字段是否包含wifi位置信息。 |
| object identifier                    | 配置话单扩展字段中携带的object identifier。                                   |
| ePDG UE Local IP 和 Port              | 配置话单扩展字段中是否携带ePDG UE本地IP和端口。                                     |
| low-priority-indicator               | 配置话单中是否包含low-priority-indicator信息。                               |
| apn-rate-control                     | 配置话单中是否包含apn-rate-control信息。                                     |
| mo-exception-data                    | 配置话单中是否包含mo-exception-data-counter信息。                            |
| packet-number                        | 配置SCDR话单中是否携带uplinkPacketNum和downlinkPacketNum字段。                |
| cp-eps-optimisation-indicator        | 配置话单中是否携带cp-eps-optimisation-indicator字段。                        |
| sgw-address-ipv6                     | 配置话单中是否携带sgw-address-ipv6字段。                                     |
| serving-plmn-rate-control            | 配置话单中是否包含serving-plmn-rate-control信息。                            |
| uni-pdu-cp-only-flag                 | 配置话单中是否携带uni-pdu-cp-only-flag字段。                                 |
| sgi-ptp-tunnelling-method            | 配置话单中是否携带sgi-ptp-tunnelling-method字段。                            |
| pdp-type-extention                   | 配置话单中是否携带pdp-ype-extension字段。                                    |
| scs-as-address                       | 配置话单中是否携带scs-as-address字段。                                       |