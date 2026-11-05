---
id: ''
name: 配置Hostfile的数据
ne_type: UNC
type: feature
description: '当运营商在部署分组交换网，新增MME时，可通过配置Hostfile数据，用于MME在以下流程中进行域名解析：  * 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。 * 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。  进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：  * DNS服务器是网络中专门提供域名解析服务的服务器。 * DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。 * 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。  MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。  Hostfile数据包含网元的FQDN（Fully Qualified Domain Name，标准规范域名）和HOSTNAME（主机名称），如下表所示。  **表1** 不同网元的域名解析使用场景及Hostfile数据格式  | 网元 | 域名解析使用场景 | HOSTNAME格式定义 | FQDN格式定义  | | | --- | --- | --- | ---  | | | **S-GW** | 在Attach/TAU/Handover流程中，根据TAI选择S-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>   * TOPON：代表优选拓扑最近的节点。TOPOFF：代表不优选拓扑最近的节点。 * SINGLE-LABEL-INTERFACE-NAME：用于命名一个节点的特定接口。 * CANONICAL-NODE-NAME：一个节点的规范命名。 | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG | | **P-GW** | 签约了动态P-GW时，在Attach/PDN连接建立流程中，根据APN选择P-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | <APNNI>.APN.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG | |  | 签约了静态P-GW时，在Attach/PDN连接建立流程中，根据Hostname查找已签约的P-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | - | | **MME** | 在Inter MME的Handover流程中，根据TAI选择MME。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG | |  | 在Inter MME的Attach/TAU流程中，根据GUTI选择MME。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | MMEC<MMEC>.MMEGI<MMEGI>.MME.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG | | **Gn/Gp SGSN** | 在Inter RAT的Attach/TAU/NACC流程中，根据RAI/LAI选择Gn/Gp SGSN。 | RACAAAA.LACBBBB.MNCYYY.MCCZZZ.GPRS  * AAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 * BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | -  说明：  配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。  | | |  | 在Inter RAT的Handover流程中，根据RNC选择Gn/Gp SGSN。 | RNCXXXX.MNCYYY.MCCZZZ.GPRS  * XXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RAC=0x25B，XXXX输入为“025B”。 * YYY: 对端SGSN下属RNC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN下属RNC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | -  说明：  配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。  | | | **S4 SGSN** | 在Inter RAT的Attach/TAU流程中，根据RAI/LAI选择S4 SGSN。  说明：  * Inter RAT的NACC/Handover流程中，根据RNC ID还是根据RAI/LAI选择S4 SGSN取决于命令**设置SGSN/MME选择策略（SET PESELPLCY）**的参数“使用RNC ID域名 （RNCID）”设置，如果不使用“ RNCID（RNC ID域名）”，系统会组装RAI/LAI域名进行查询。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   * AAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 * BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | |  | 在Inter RAT的NACC/Handover流程中，根据RNC ID选择S4 SGSN。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | RNCXXXX.RNC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   * XXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RNC ID=0x25B，XXXX输入为“025B”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | | **MSC** | 在SRVCC语音切换流程中，根据RAI选择MSC。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | * RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   + AAAA: 对端MSC的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。   + BBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。   + YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。   + ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | |  | 在SRVCC语音切换流程中，根据LAI选择MSC。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | * LACBBBB.LAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   +
  BBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。   + YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。   + ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 |'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置Hostfile的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，可通过配置Hostfile数据，用于MME在以下流程中进行域名解析：* 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。* 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：* DNS服务器是网络中专门提供域名解析服务的服务器。* DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。* 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。Hostfile数据包含网元的FQDN（Fully Qualified Domain Name，标准规范域名）和HOSTNAME（主机名称），如下表所示。**表1** 不同网元的域名解析使用场景及Hostfile数据格式| 网元 | 域名解析使用场景 | HOSTNAME格式定义 | FQDN格式定义  | || --- | --- | --- | ---  | || **S-GW** | 在Attach/TAU/Handover流程中，根据TAI选择S-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME>   * TOPON：代表优选拓扑最近的节点。TOPOFF：代表不优选拓扑最近的节点。 * SINGLE-LABEL-INTERFACE-NAME：用于命名一个节点的特定接口。 * CANONICAL-NODE-NAME：一个节点的规范命名。 | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG || **P-GW** | 签约了动态P-GW时，在Attach/PDN连接建立流程中，根据APN选择P-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | <APNNI>.APN.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG ||  | 签约了静态P-GW时，在Attach/PDN连接建立流程中，根据Hostname查找已签约的P-GW。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | - || **MME** | 在Inter MME的Handover流程中，根据TAI选择MME。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG ||  | 在Inter MME的Attach/TAU流程中，根据GUTI选择MME。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | MMEC<MMEC>.MMEGI<MMEGI>.MME.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG || **Gn/Gp SGSN** | 在Inter RAT的Attach/TAU/NACC流程中，根据RAI/LAI选择Gn/Gp SGSN。 | RACAAAA.LACBBBB.MNCYYY.MCCZZZ.GPRS  * AAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 * BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | -  说明：  配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。  | ||  | 在Inter RAT的Handover流程中，根据RNC选择Gn/Gp SGSN。 | RNCXXXX.MNCYYY.MCCZZZ.GPRS  * XXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RAC=0x25B，XXXX输入为“025B”。 * YYY: 对端SGSN下属RNC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN下属RNC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 | -  说明：  配置对端Gn/Gp SGSN的IP地址时，不需要配置NAPTR记录。如果在Hostfile中查询不到Gn/Gp SGSN的记录，则向DNS Server查询记录。  | || **S4 SGSN** | 在Inter RAT的Attach/TAU流程中，根据RAI/LAI选择S4 SGSN。  说明：  * Inter RAT的NACC/Handover流程中，根据RNC ID还是根据RAI/LAI选择S4 SGSN取决于命令**设置SGSN/MME选择策略（SET PESELPLCY）**的参数“使用RNC ID域名 （RNCID）”设置，如果不使用“ RNCID（RNC ID域名）”，系统会组装RAI/LAI域名进行查询。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   * AAAA: 对端SGSN的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。 * BBBB: 对端SGSN的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 ||  | 在Inter RAT的NACC/Handover流程中，根据RNC ID选择S4 SGSN。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | RNCXXXX.RNC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   * XXXX: 对端SGSN下属RNC，16进制，以0补全高位，例如RNC ID=0x25B，XXXX输入为“025B”。 * YYY: 对端SGSN的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。 * ZZZ: 对端SGSN的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 || **MSC** | 在SRVCC语音切换流程中，根据RAI选择MSC。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | * RACAAAA.LACBBBB.RAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   + AAAA: 对端MSC的RAC，16进制，以0补全高位，例如RAC=0x2B，AAAA输入为“002B”。   + BBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。   + YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。   + ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 ||  | 在SRVCC语音切换流程中，根据LAI选择MSC。 | <"TOPON"|"TOPOFF">.<SINGLE-LABEL-INTERFACE-NAME>.<CANONICAL-NODE-NAME> | * LACBBBB.LAC.EPC.MNCYYY.MCCZZZ.3GPPNETWORK.ORG   + BBBB: 对端MSC的LAC，16进制，以0补全高位，例如LAC=0x2D9，BBBB输入为“02D9”。   + YYY: 对端MSC的PLMN中MNC，10进制，以0补全高位，例如MNC=0，YYY输入为“000”。   + ZZZ: 对端MSC的PLMN中MCC，10进制，以0补全高位，例如MCC=123，ZZZ输入为“123”。 |

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '根据TAI选择S-GW，配置S-GW网元的DNS记录。  如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_ipv4dnsh_list_1:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置P-GW网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_1:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_ipv4dnsh_list_2:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置P-GW网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list_3:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置MME网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_2:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_ipv4dnsh_list_4:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置MME网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_3:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_ipv4dnsh_list_5:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置Gn/Gp SGSN网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list_6:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置Gn/Gp SGSN网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list_7:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置S4 SGSN网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_4:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_ipv4dnsh_list_8:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置MSC网元的DNS记录。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_5:
      type: items
      properties:
        FQDN:
          name: '域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
  examples:
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'topon.s11.eth1.gw32.nodes'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.33'
    add_dnsn_list:
    - FQDN: 'TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: SGW
      INTYPE: S11
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_ipv4dnsh_list_1:
    - HSINDEX: 2
      HOSTNAME: 'topon.s8.eth2.gw32.nodes'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.81'
    add_dnsn_list_1:
    - FQDN: 'HUAWEI1.COM.APN.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 2
      ENTITY: PGW
      INTYPE: S5
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_ipv4dnsh_list_2:
    - HSINDEX: 3
      HOSTNAME: 'topon.s5.eth3.gw32.nodes'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.82'
    add_ipv4dnsh_list_3:
    - HSINDEX: 4
      HOSTNAME: 'topon.s10.eth4.mmec11.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.2'
    add_dnsn_list_2:
    - FQDN: 'TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 4
      ENTITY: MME
      INTYPE: S10
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_ipv4dnsh_list_4:
    - HSINDEX: 5
      HOSTNAME: 'topon.s10.eth5.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.3'
    add_dnsn_list_3:
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC000.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 5
      ENTITY: MME
      INTYPE: S10
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_ipv4dnsh_list_5:
    - HSINDEX: 6
      HOSTNAME: 'RAC002B.LAC02D9.MNC001.MCC123.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.10'
    add_ipv4dnsh_list_6:
    - HSINDEX: 7
      HOSTNAME: 'RNC025B.MNC001.MCC123.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.11'
    add_ipv4dnsh_list_7:
    - HSINDEX: 8
      HOSTNAME: 'topon.s3.eth6.mnc001.mcc123.gprs'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.12'
    add_dnsn_list_4:
    - FQDN: 'RAC002B.LAC02D9.RAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 8
      ENTITY: SGSN
      INTYPE: S3
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_ipv4dnsh_list_8:
    - HSINDEX: 9
      HOSTNAME: 'topon.sv.eth7.mnc001.mcc123.org'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.22'
    add_dnsn_list_5:
    - FQDN: 'LAC02D9.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 9
      ENTITY: MSC
      INTYPE: Sv
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置S-GW网元的DNS记录。

### 根据TAI选择S-GW，需要配置S-GW网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_sgw_dns_record -%}
    {%- for item in add_ipv4dnsh_list -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_sgw_dns_record -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置P-GW网元的DNS记录。

#### 3.1 **可选：**根据APN选择P-GW，需要配置P-GW网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_pgw_dns_record and is_scenario_select_pgw_by_apn -%}
    {%- for item in add_ipv4dnsh_list_1 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_pgw_dns_record and is_scenario_select_pgw_by_apn -%}
    {%- for item in add_dnsn_list_1 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 **可选：**根据Hostname查找已签约的P-GW，需要配置P-GW网元的DNS记录，包含Hostfile文件的A解析记录。

```jinja2
{%- if is_optional_config_pgw_dns_record and is_scenario_select_pgw_by_hostname -%}
    {%- for item in add_ipv4dnsh_list_2 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置MME网元的DNS记录。

#### 4.1 **可选：**根据TAI值选择MME，需要配置MME网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_mme_dns_record and is_scenario_select_mme_by_tai -%}
    {%- for item in add_ipv4dnsh_list_3 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_mme_dns_record and is_scenario_select_mme_by_tai -%}
    {%- for item in add_dnsn_list_2 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 **可选：**根据GUTI值选择MME，需要配置MME网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_mme_dns_record and is_scenario_select_mme_by_guti -%}
    {%- for item in add_ipv4dnsh_list_4 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_mme_dns_record and is_scenario_select_mme_by_guti -%}
    {%- for item in add_dnsn_list_3 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置Gn/Gp SGSN网元的DNS记录。

#### 5.1 **可选：**Attach/TAU/NACC流程根据RAI/LAI值选择Gn/Gp SGSN，需要配置Gn/Gp SGSN网元的DNS记录，包含Hostfile文件的A解析记录。

```jinja2
{%- if is_optional_config_gngp_sgsn_dns_record and is_scenario_select_sgsn_by_railai -%}
    {%- for item in add_ipv4dnsh_list_5 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 **可选：**Handover流程根据RNC值选择Gn/Gp SGSN，需要配置Gn/Gp SGSN网元的DNS记录，包含Hostfile文件的A解析记录。

```jinja2
{%- if is_optional_config_gngp_sgsn_dns_record and is_scenario_select_sgsn_by_rnc -%}
    {%- for item in add_ipv4dnsh_list_6 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 **可选：**配置S4 SGSN网元的DNS记录。

### Attach/TAU/NACC/Handover流程根据RAI/LAI选择S4 SGSN，需要配置S4 SGSN网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_s4_sgsn_dns_record -%}
    {%- for item in add_ipv4dnsh_list_7 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_s4_sgsn_dns_record -%}
    {%- for item in add_dnsn_list_4 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**配置MSC网元的DNS记录。

### SRVCC语音切换流程中，根据LAI选择MSC，需要配置MSC网元的DNS记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

```jinja2
{%- if is_optional_config_msc_dns_record -%}
    {%- for item in add_ipv4dnsh_list_8 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_msc_dns_record -%}
    {%- for item in add_dnsn_list_5 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

