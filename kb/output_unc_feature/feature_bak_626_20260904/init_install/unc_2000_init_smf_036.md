# 配置和NF直连

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

- 如果网络中部署了NRF，则需执行配置到NRF的数据。
- 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行本章节操作，手工配置SMF与周边NF的逻辑连接。
- 当网络中既部署了NRF，又本地配置了周边NF时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认为优先选择本地配置的NF。
- 下述以配置SMF到周边UDM、PCF、CHF及AMF为例，说明配置本地NRF功能的基本步骤。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- UNC软件安装已完成。
- 已经获取网设LLD文档。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别             | 参数名称                        | 取值样例                                                                                                                                                                | 获取方法                              | 说明                                                                      |
|:---------------|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|:------------------------------------------------------------------------|
| ADD PNFPROFILE | NF实例标识（NFINSTANCEID）        | UDM_Instance_0 PCF_Instance_0 CHF_instance_0 a6a61c6f-0d3a-4221-b1da-424eda3ccf67                                                                                   | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | NF类型（NFTYPE）                | NfUDM NfPCF NfCHF NfAMF                                                                                                                                             | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | NF状态（NFSTATUS）              | Registered                                                                                                                                                          | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | 域名（FQDN）                    | udm01.node.mnc003.mcc123.3gppnetwork.org pcf01.node.mnc003.mcc123.3gppnetwork.org chf01.node.mnc003.mcc123.3gppnetwork.org amf01.node.mnc003.mcc123.3gppnetwork.org | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | IP地址类型（IPADDRESSTYPE）       | IPTypeV4                                                                                                                                                            | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | IPV4地址1（IPV4ADDRESS1）       | 10.255.255.180 10.255.255.181 172.16.134.66 172.16.1.5                                                                                                              | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFPROFILE | 端口号（PORT）                   | 8080                                                                                                                                                                | 全网规划                              | 增加对端NF实例概述信息。 “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。 |
| ADD PNFSERVICE | NF实例标识（NFINSTANCEID）        | UDM_Instance_0 PCF_Instance_0 CHF_Instance_0 a6a61c6f-0d3a-4221-b1da-424eda3ccf67                                                                                   | 全网规划                              | 增加对端NF服务实例信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。         |
| ADD PNFSERVICE | 服务实例标识（SRVINSTANCEID）       | Service_Instance_0 Service_Instance_1                                                                                                                               | 全网规划                              | 增加对端NF服务实例信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。         |
| ADD PNFSERVICE | 服务名称（SERVICENAME）           | NudmSdm NudmUecm NpcfSmPlcCtrl NchfConvCharg NamfComm NamfEvts                                                                                                      | 全网规划                              | 增加对端NF服务实例信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。         |
| ADD PNFSERVICE | 协议模式（SCHEMA）                | http                                                                                                                                                                | 全网规划                              | 增加对端NF服务实例信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。         |
| ADD PNFSERVICE | 服务实例状态（NFSERVICESTATUS）     | REGISTERED                                                                                                                                                          | 全网规划                              | 增加对端NF服务实例信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。         |
| ADD PNFPLMN    | NF实例标识（NFINSTANCEID）        | UDM_Instance_0 PCF_Instance_0 CHF_Instance_0 a6a61c6f-0d3a-4221-b1da-424eda3ccf67                                                                                   | 全网规划                              | 增加对端NF的PLMN信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。        |
| ADD PNFPLMN    | 移动国家码（MCC）                  | 123                                                                                                                                                                 | 全网规划                              | 增加对端NF的PLMN信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。        |
| ADD PNFPLMN    | 移动网号（MNC）                   | 03                                                                                                                                                                  | 全网规划                              | 增加对端NF的PLMN信息。 对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行LST NFUUID获取。        |
| ADD PNFSUPI    | 索引（INDEX）                   | 1 2 0 7                                                                                                                                                             | 本端规划                              | 增加对端NF的SUPI信息。                                                          |
| ADD PNFSUPI    | NF实例标识（NFINSTANCEID）        | UDM_Instance_0 PCF_Instance_0 CHF_Instance_0 a6a61c6f-0d3a-4221-b1da-424eda3ccf67                                                                                   | 全网规划                              | 增加对端NF的SUPI信息。                                                          |
| ADD PNFSUPI    | 查询方式（QUERYTYPE）             | START_END                                                                                                                                                           | 全网规划                              | 增加对端NF的SUPI信息。                                                          |
| ADD PNFSUPI    | 起始号段（RANGESTART）            | 123031200100001 123031340010001 12303170100001                                                                                                                      | 全网规划                              | 增加对端NF的SUPI信息。                                                          |
| ADD PNFSUPI    | 终止号段（RANGEEND）              | 123031200200001 123031340020001 12303170200001                                                                                                                      | 全网规划                              | 增加对端NF的SUPI信息。                                                          |
| ADD PNFGPSI    | 索引（INDEX）                   | 1 2                                                                                                                                                                 | 本端规划                              | 增加对端NF的GPSI信息。                                                          |
| ADD PNFGPSI    | NF实例标识（NFINSTANCEID）        | PCF_Instance_0 CHF_Instance_0                                                                                                                                       | 全网规划                              | 增加对端NF的GPSI信息。                                                          |
| ADD PNFGPSI    | 查询方式（QUERYTYPE）             | START_END                                                                                                                                                           | 全网规划                              | 增加对端NF的GPSI信息。                                                          |
| ADD PNFGPSI    | 起始号段（RANGESTART）            | 123031340010001                                                                                                                                                     | 全网规划                              | 增加对端NF的GPSI信息。                                                          |
| ADD PNFGPSI    | 终止号段（RANGEEND）              | 123031340020001                                                                                                                                                     | 全网规划                              | 增加对端NF的GPSI信息。                                                          |
| ADD PNFNS      | 索引（INDEX）                   | 1 2                                                                                                                                                                 | 本端规划                              | 配置对端NF实例支持的服务切片信息。                                                      |
| ADD PNFNS      | NF实例标识（NFINSTANCEID）        | UDM_Instance_0 PCF_Instance_0                                                                                                                                       | 全网规划                              | 配置对端NF实例支持的服务切片信息。                                                      |
| ADD PNFNS      | 切片/服务类型（SST）                | 1                                                                                                                                                                   | 全网规划                              | 配置对端NF实例支持的服务切片信息。                                                      |
| ADD PNFNS      | 切片分类器（SD）                   | 010101                                                                                                                                                              | 全网规划                              | 配置对端NF实例支持的服务切片信息。                                                      |
| ADD PNFPCFINFO | NF实例标识（NFINSTANCEID）        | PCF_Instance_0                                                                                                                                                      | 全网规划                              | 增加本地配置的对端PCF实例信息。                                                       |
| ADD PNFPCFINFO | Rx接口Diameter主机名（RXDIAMHOST） | huawei.com                                                                                                                                                          | 全网规划                              | 增加本地配置的对端PCF实例信息。                                                       |
| ADD PNFPCFINFO | Rx接口Diameter域名（RXDIAMREALM） | huawei.com                                                                                                                                                          | 全网规划                              | 增加本地配置的对端PCF实例信息。                                                       |
| ADD PNFDNN     | 索引（INDEX）                   | 2                                                                                                                                                                   | 本端规划                              | 配置的对端NF实例支持的DNN及其归属切片的信息。                                               |
| ADD PNFDNN     | NF实例标识（NFINSTANCEID）        | PCF_Instance_0                                                                                                                                                      | 全网规划                              | 配置的对端NF实例支持的DNN及其归属切片的信息。                                               |
| ADD PNFDNN     | 数据网络名称（DNN）                 | huawei.com                                                                                                                                                          | 全网规划                              | 配置的对端NF实例支持的DNN及其归属切片的信息。                                               |
| ADD PNFDNN     | 对端NF的切片索引（PNFNSINDEX）       | 0                                                                                                                                                                   | 本端规划                              | 配置的对端NF实例支持的DNN及其归属切片的信息。                                               |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置到UDM的数据，包括UDM的Profile、Service、PLMN信息、支持的SUPI范围等信息。

   ```
   ADD PNFPROFILE:NFINSTANCEID="UDM_Instance_0", NFTYPE=NfUDM, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.255.255.180", PORT=8080;
   ADD PNFSERVICE:NFINSTANCEID="UDM_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NudmSdm, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
   ADD PNFSERVICE:NFINSTANCEID="UDM_Instance_0", SRVINSTANCEID="Service_Instance_1", SERVICENAME=NudmUecm, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
   ADD PNFPLMN:NFINSTANCEID="UDM_Instance_0", MCC="123", MNC="03";
   ADD PNFSUPI:INDEX=1, NFINSTANCEID="UDM_Instance_0", QUERYTYPE=START_END, RANGESTART="123031200100001", RANGEEND="123031200200001";
   ADD PNFNS:INDEX=1, NFINSTANCEID="UDM_Instance_0", SST=1, SD="010101";
   ```
3. **可选：**配置到PCF的数据，包括PCF的Profile、Service、PLMN信息、支持的SUPI范围等信息。如果在配置与PCF对接数据中已完成该配置则跳过本步骤。

   ```
   ADD PNFPROFILE:NFINSTANCEID="PCF_Instance_0", NFTYPE=NfPCF, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.255.255.181", PORT=8080;
   ADD PNFSERVICE:NFINSTANCEID="PCF_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NpcfSmplcCtrl, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
   ADD PNFPLMN:NFINSTANCEID="PCF_Instance_0", MCC="123", MNC="03";
   ADD PNFSUPI:INDEX=2, NFINSTANCEID="PCF_Instance_0", QUERYTYPE=START_END, RANGESTART="123031340010001", RANGEEND="123031340020001";
   ADD PNFPCFINFO:NFINSTANCEID="PCF_Instance_0", RXDIAMHOST="huawei.com", RXDIAMREALM="huawei.com";
   ADD PNFDNN:INDEX=2, NFINSTANCEID="PCF_Instance_0", DNN="huawei.com", PNFNSINDEX=2;
   ADD PNFNS:INDEX=2, NFINSTANCEID="PCF_Instance_0", SST=1, SD="010101";
   ADD PNFGPSI:INDEX=1, NFINSTANCEID="PCF_Instance_0", QUERYTYPE=START_END, RANGESTART="123031340010001", RANGEEND="123031340020001";
   ```
4. 配置到CHF的数据，包括CHF的Profile、Service、支持的SUPI范围等信息。

   ```
   ADD PNFPROFILE:NFINSTANCEID="CHF_instance_0", NFTYPE=NfCHF, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="172.16.134.66", PORT=8080;
   ADD PNFSERVICE:NFINSTANCEID="CHF_Instance_0", SRVINSTANCEID="Service_instance_0", SERVICENAME=NchfConvCharg, SCHEMA=http;
   ADD PNFSUPI:INDEX=3, NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END, RANGESTART="12303170100001", RANGEEND="12303170200001";
   ADD PNFGPSI:INDEX=2, NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END, RANGESTART="123031340010001", RANGEEND="123031340020001";
   ```
5. 配置到AMF的数据，包括AMF的Profile、Service、PLMN等信息。

   ```
   ADD PNFPROFILE:NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", NFTYPE=NfAMF, NFSTATUS=Registered, IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="172.16.1.5", PORT=8080;
   ADD PNFSERVICE:NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NamfComm, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
   ADD PNFSERVICE:NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", SRVINSTANCEID="Service_Instance_1", SERVICENAME=NamfEvts, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
   ADD PNFPLMN:NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", MCC="123", MNC="03";
   ```