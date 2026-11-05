# 配置Hostfile的数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

当运营商在部署分组交换网，新增MME时，可通过配置Hostfile数据，用于MME在以下流程中进行域名解析：

- 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。
- 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。

**说明** 

进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：

- DNS服务器是网络中专门提供域名解析服务的服务器。
- DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。
- 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。

MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

Hostfile数据包含网元的FQDN（Fully Qualified Domain Name，标准规范域名）和HOSTNAME（主机名称），如下表所示。

| 网元         | 域名解析使用场景                                                                                                                                                                                                         | HOSTNAME格式定义                                                                                                                                                                                                                                                   | FQDN格式定义                                                                                                                                                                                                                                                                           |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S-GW       | 在Attach/TAU/Handover流程中，根据TAI选择S-GW。                                                                                                                                                                             | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> TOPON：代表优选拓扑最近的节点。TOPOFF：代表不优选拓扑最近的节点。 SINGLE-LABEL-INTERFACE-NAME：用于命名一个节点的特定接口。 CANONICAL-NODE-NAME：一个节点的规范命名。                                                                        | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG                                                                                                                                                                                               |
| P-GW       | 签约了动态P-GW时，在Attach/PDN连接建立流程中，根据APN选择P-GW。                                                                                                                                                                       | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | <APNNI>.APN.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG                                                                                                                                                                                                                                  |
| P-GW       | 签约了静态P-GW时，在Attach/PDN连接建立流程中，根据Hostname查找已签约的P-GW。                                                                                                                                                              | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | -                                                                                                                                                                                                                                                                                  |
| MME        | 在Inter MME的Handover流程中，根据TAI选择MME。                                                                                                                                                                               | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG                                                                                                                                                                                               |
| MME        | 在Inter MME的Attach/TAU流程中，根据GUTI选择MME。                                                                                                                                                                            | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | MMEC<MMEC>.MMEGI<MMEGI>.MME.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG                                                                                                                                                                                                                  |
| Gn/Gp SGSN | 在Inter RAT的Attach/TAU/NACC流程中，根据RAI/LAI选择Gn/Gp SGSN。                                                                                                                                                             | RACAAAA.LACBBBB.MNCYYY.MCCZZZ.GPRSAAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | -  说明： 配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。                                                                                                                                                                                           |
| Gn/Gp SGSN | 在Inter RAT的Handover流程中，根据RNC选择Gn/Gp SGSN。                                                                                                                                                                        | RNCXXXX.MNCYYY.MCCZZZ.GPRSXXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RAC=0x25B，XXXX输入为“025B”。 YYY: 对端SGSN下属RNC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端SGSN下属RNC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。                                                     | -  说明： 配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。                                                                                                                                                                                           |
| S4 SGSN    | 在Inter RAT的Attach/TAU流程中，根据RAI/LAI选择S4 SGSN。  说明： Inter RAT的NACC/Handover流程中，根据RNC ID还是根据RAI/LAI选择S4 SGSN取决于命令设置SGSN/MME选择策略（SET PESELPLCY）的参数“使用RNC ID域名 （RNCID）”设置，如果不使用“ RNCID（RNC ID域名）”，系统会组装RAI/LAI域名进行查询。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG AAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 |
| S4 SGSN    | 在Inter RAT的NACC/Handover流程中，根据RNC ID选择S4 SGSN。                                                                                                                                                                   | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | RNCXXXX.RNC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG XXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RNC ID=0x25B，XXXX输入为“025B”。 YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。                                                            |
| MSC        | 在SRVCC语音切换流程中，根据RAI选择MSC。                                                                                                                                                                                        | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORGAAAA: 对端MSC的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 BBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。      |
| MSC        | 在SRVCC语音切换流程中，根据LAI选择MSC。                                                                                                                                                                                        | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>                                                                                                                                                                                         | LACBBBB.LAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORGBBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。                                                                    |

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

数据

上图中，各网元的基本信息如下（FQDN及HOSTNAME见数据表）：

- MME上配置的本PLMN的S5/S8协议类型为GTP。
- 在Attach/TAU/Handover流程中，根据TAI选择S-GW。网络中有归属于本PLMN的S-GW1，S-GW1支持的TAC取值为“1101”，MNC为“001”，MCC为“123”
- 在Attach/PDN连接建立流程中，根据APN选择P-GW1。网络中有归属于本PLMN的P-GW1，P-GW1支持的APN取值为“HUAWEI1.COM”，MNC为“001”，MCC为“123”。
- 运营商在用户A的签约数据中，为APN签约了P-GW2的FQDN，且FQDN为P-GW2的主机名。网络中有归属于本PLMN的P-GW2，P-GW2支持的APN取值为“HUAWEI1.COM”。
- 在Inter MME的Handover流程中，根据TAI选择MME1。网络中有归属于本PLMN的MME1，MME1支持的TAC取值为“1101”，MNC为“001”，MCC为“123”
- 在Inter MME的Attach/TAU流程中，根据GUTI选择MME2。网络中有归属于本PLMN的MME2，MME2的MME group ID为“8001”，MME code为“12”，MNC为“001”，MCC为“123”。
- 在Inter RAT的Attach/TAU/NACC流程中，根据RAI/LAI选择Gn/Gp SGSN1。网络中有归属于本PLMN的Gn/Gp SGSN：Gn/Gp SGSN1，Gn/Gp SGSN1支持的RAC取值为“002B”，LAC为“02D9”，MNC为“001”，MCC为“123”。
- 在Inter RAT的Handover流程中，根据RNC选择Gn/Gp SGSN2。网络中有归属于本PLMN的Gn/Gp SGSN：Gn/Gp SGSN2，Gn/Gp SGSN2支持的RNC取值为“025B”，MNC为“001”，MCC为“123”。
- 在Inter RAT的Attach/TAU/NACC/Handover流程中根据RAI/LAI选择S4 SGSN。 网络中有归属于本PLMN的S4 SGSN：S4 SGSN3，S4 SGSN支持的RAC取值为“002B”，LAC为“02D9”，MNC为“001”，MCC为“123”。
- 在SRVCC语音切换流程中，根据LAI选择MSC。网络中有归属于本PLMN的MSC，MSC支持的LAC为“02D9”，MNC为“001”，MCC为“123”。

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别           | 参数名称                 | 取值样例                                                                                                           | 获取方法            | 说明                                                                        |
|:-------------|:---------------------|:---------------------------------------------------------------------------------------------------------------|:----------------|:--------------------------------------------------------------------------|
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 1                                                                                                              | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | topon.s11.eth1.gw32.nodes                                                                                      | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.33                                                                                                   | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN     | 域名（FQDN）             | TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG                                                        | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN     | 主机名索引（HSINDEX）       | 1                                                                                                              | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN     | 网元类型（ENTITY）         | SGW                                                                                                            | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN     | 接口类型（INTYPE）         | S11                                                                                                            | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD DNSN     | S5接口协议类型（S5PROTOCOL） | GTP                                                                                                            | 参见“水平网设LLD文档 ”。 | 根据TAI选择S-GW，配置S-GW网元的DNS记录。 如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。 |
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 2 3                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | topon.s8.eth2.gw32.nodes topon.s5.eth3.gw32.nodes                                                              | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.81 10.16.139.82                                                                                      | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD DNSN     | 域名（FQDN）             | HUAWEI1.COM.APN.EPC.MNC001.MCC123.3GPPNETWORK.ORG                                                              | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD DNSN     | 主机名索引（HSINDEX）       | 2                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD DNSN     | 网元类型（ENTITY）         | PGW                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD DNSN     | 接口类型（INTYPE）         | S5                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD DNSN     | S5接口协议类型（S5PROTOCOL） | GTP                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置P-GW网元的DNS记录。                                                           |
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 4 5                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | topon.s10.eth4.mmec11.mmegi8001.mme topon.s10.eth5.mmec12.mmegi8001.mme                                        | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.2 10.16.139.3                                                                                        | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD DNSN     | 域名（FQDN）             | TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG MMEC12.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD DNSN     | 主机名索引（HSINDEX）       | 4 5                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD DNSN     | 网元类型（ENTITY）         | MME                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD DNSN     | 接口类型（INTYPE）         | S10                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置MME网元的DNS记录。                                                            |
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 6 7                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置Gn/Gp SGSN网元的DNS记录。                                                     |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | RAC002B.LAC02D9.MNC001.MCC123.GPRS RNC025B.MNC001.MCC123.GPRS                                                  | 参见“水平网设LLD文档 ”。 | 配置Gn/Gp SGSN网元的DNS记录。                                                     |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置Gn/Gp SGSN网元的DNS记录。                                                     |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.10 10.16.139.11                                                                                      | 参见“水平网设LLD文档 ”。 | 配置Gn/Gp SGSN网元的DNS记录。                                                     |
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 8                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | topon.s3.eth6.mnc001.mcc123.gprs                                                                               | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.12                                                                                                   | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD DNSN     | 域名（FQDN）             | RAC002B.LAC02D9.RAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG                                                          | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD DNSN     | 主机名索引（HSINDEX）       | 8                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD DNSN     | 网元类型（ENTITY）         | SGSN                                                                                                           | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD DNSN     | 接口类型（INTYPE）         | Gs                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置S4 SGSN网元的DNS记录。                                                        |
| ADD IPV4DNSH | 主机名索引（HSINDEX）       | 9                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD IPV4DNSH | 主机名（HOSTNAME）        | topon.sv.eth7.mnc001.mcc123.org                                                                                | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD IPV4DNSH | 地址区间号（ADDRSECTION）   | SECTION1                                                                                                       | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD IPV4DNSH | IPV4ADDR1（IPv4地址1）   | 10.16.139.22                                                                                                   | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD DNSN     | 域名（FQDN）             | LAC02D9.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG                                                                  | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD DNSN     | 主机名索引（HSINDEX）       | 9                                                                                                              | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD DNSN     | 网元类型（ENTITY）         | MSC                                                                                                            | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |
| ADD DNSN     | 接口类型（INTYPE）         | Sv                                                                                                             | 参见“水平网设LLD文档 ”。 | 配置MSC网元的DNS记录。                                                            |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. **可选：**配置S-GW网元的DNS记录。

   根据TAI选择S-GW，需要配置S-GW网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

   ```
   ADD IPV4DNSH: HSINDEX=1, HOSTNAME="topon.s11.eth1.gw32.nodes", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.33";
   ADD DNSN: FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11, S5PROTOCOL=GTP;
   ```
3. **可选：**配置P-GW网元的DNS记录。
   1. **可选：**根据APN选择P-GW，需要配置P-GW网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=2, HOSTNAME="topon.s8.eth2.gw32.nodes", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.81";
      ADD DNSN: FQDN="HUAWEI1.COM.APN.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=2, ENTITY=PGW, INTYPE=S5, S5PROTOCOL=GTP;
      ```
   2. **可选：**根据Hostname查找已签约的P-GW，需要配置P-GW网元的DNS记录，包含Hostfile文件的A解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=3, HOSTNAME="topon.s5.eth3.gw32.nodes", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.82";
      ```
4. **可选：**配置MME网元的DNS记录。
   1. **可选：**根据TAI值选择MME，需要配置MME网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=4, HOSTNAME="topon.s10.eth4.mmec11.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.2";
      ADD DNSN: FQDN="TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=4, ENTITY=MME, INTYPE=S10;
      ```
   2. **可选：**根据GUTI值选择MME，需要配置MME网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=5, HOSTNAME="topon.s10.eth5.mmec12.mmegi8001.mme", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.3";
      ADD DNSN: FQDN="MMEC12.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG", HSINDEX=5, ENTITY=MME, INTYPE=S10;
      ```
5. **可选：**配置Gn/Gp SGSN网元的DNS记录。
   1. **可选：**Attach/TAU/NACC流程根据RAI/LAI值选择Gn/Gp SGSN，需要配置Gn/Gp SGSN网元的DNS记录，包含Hostfile文件的A解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=6, HOSTNAME="RAC002B.LAC02D9.MNC001.MCC123.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.10";
      ```
   2. **可选：**Handover流程根据RNC值选择Gn/Gp SGSN，需要配置Gn/Gp SGSN网元的DNS记录，包含Hostfile文件的A解析记录。

      ```
      ADD IPV4DNSH: HSINDEX=7, HOSTNAME="RNC025B.MNC001.MCC123.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.11";
      ```
6. **可选：**配置S4 SGSN网元的DNS记录。

   Attach/TAU/NACC/Handover流程根据RAI/LAI选择S4 SGSN，需要配置S4 SGSN网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

   ```
   ADD IPV4DNSH: HSINDEX=8, HOSTNAME="topon.s3.eth6.mnc001.mcc123.gprs", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.12";
   ADD DNSN: FQDN="RAC002B.LAC02D9.RAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=8, ENTITY=SGSN, INTYPE=S3;
   ```
7. **可选：**配置MSC网元的DNS记录。

   SRVCC语音切换流程中，根据LAI选择MSC，需要配置MSC网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

   ```
   ADD IPV4DNSH: HSINDEX=9, HOSTNAME="topon.sv.eth7.mnc001.mcc123.org", ADDRSECTION=SECTION1, IPV4ADDR1="10.16.139.22";
   ADD DNSN: FQDN="LAC02D9.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG", HSINDEX=9, ENTITY=MSC, INTYPE=Sv;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 执行以下命令，查询具体配置是否与数据规划表中的值一致。

   LST DNSN

   LST IPV4DNSH