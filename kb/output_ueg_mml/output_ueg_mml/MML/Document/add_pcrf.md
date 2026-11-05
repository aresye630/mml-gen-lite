# 增加PCRF实体(ADD PCRF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该操作在重启进程后才能生效，是否继续？

该命令为配置类命令，用于在配置数据库中增加一条本端PCRF实体数据记录。

## 注意事项

- 一个OMU只管理一个PCRF功能实体。
- 该命令添加的PCRF实体数据记录的“本地主机名”是ESN信息的组成部分。
- 增加实体之后，需要执行如下操作才能生效。
  1. 登录“OM Portal”，在界面上选择“应用管理 > MML”，在CSP网元下，执行**DSP POD**命令，查询pcf中的所有Pod类型。

     命令示例如下：

     ```
     DSP POD: TYPE=byType, PODTYPE="pcf";
     ```
  2. 执行**RST POD**命令，重启HLB、DLB、PES和DUS服务。

     **须知** 

     重启各服务时，输入的Pod类型需与1中查询结果保持一致。

     重启虚拟机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务，如果没有部署SRV-L虚拟机，则无需复位pcf-srvl1-pod231和pcf-srvl2-pod231*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvl1-pod231", FORCEFLAG=true, MEID="20";
     RST POD: TYPE=byType, PODTYPE="pcf-srvl2-pod231", FORCEFLAG=true, MEID="20";
     RST POD: TYPE=byType, PODTYPE="pcf-srvr1-pod231", FORCEFLAG=true, MEID="20";
     RST POD: TYPE=byType, PODTYPE="pcf-srvra-pod231", FORCEFLAG=true, MEID="20";
     RST POD: TYPE=byType, PODTYPE="pcf-srvrb-pod231", FORCEFLAG=true, MEID="20";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="20";
     ```

     重启裸机服务命令示例如下：

     ```
     /*重启HLB、DLB、DUS服务*/
     RST POD: TYPE=byType, PODTYPE="dus-pod231", FORCEFLAG=true, MEID="20";
     RST POD: TYPE=byType, PODTYPE="pcf-link-pod231", FORCEFLAG=true, MEID="20";
     /*重启PES服务*/
     RST POD: TYPE=byType, PODTYPE="pcf-srvs-pod231", FORCEFLAG=true, MEID="20";
     ```
  3. 在USCDB网元下，执行**CLR CLUSTER**命令，清除Session备份数据。

     命令示例如下：

     ```
     CLR CLUSTER: SERVICETYPE="UPCF-SESSION";
     ```

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                       |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCRFID | PCRF标识 | 用于在UPCF配置库中定义一个PCRF功能实体。 取值范围：1 默认值：无。                                                                                                                                                                                                                                                                     |
| EN     | 实体名称   | 用于具体描述本端PCRF实体的名称，以便于识别。其值域类型为字符串，区分大小写。 取值范围：长度不超过128的字符串 默认值：无。                                                                                                                                                                                                                                          |
| DN     | 本地域名   | 用于标识本端实体域名。该参数在配置和查询时都不区分大小写。 取值范围：长度不超过64的字符串 默认值：无。  说明： 本地域名支持的字符有：大写字母（A～Z）、小写字母（a～z）、数字（0～9）、中划线（-）、点（.）和特殊字符（ ! @ # $ % ^ & * ( ) _ + [ ] { } : | < > ? / ` ~ ），当配置取值中包括特殊字符时，需要与对端协商一致。                                                                                                             |
| HN     | 本地主机名  | 用于在UPCF配置库中定义本端实体主机名，必须全网唯一。该参数在配置和查询时都不区分大小写。 取值范围：长度不超过127的字符串 默认值：无。  说明： “本地主机名”必须配置为实体名称+本地域名的形式。例如：“实体名称”为“pcrf”，“本地域名”为“huawei.com”，则“本地主机名”为“pcrf.huawei.com”。本地主机名支持的字符有：大写字母（A～Z）、小写字母（a～z）、数字（0～9）、中划线（-）、点（.）和特殊字符（ ! @ # $ % ^ & * ( ) _ + [ ] { } : | < > ? / ` ~ ），当配置取值中包括特殊字符时，需要与对端协商一致。 |

## 使用实例

1. 增加本端PCRF实体。PCRF实体标识为1，PCRF实体域名为huawei.com，主机名为pcrf.huawei.com。

   ```
   ADD PCRF: PCRFID=1, DN="huawei.com", HN="pcrf.huawei.com";
   ```
2. 增加本端PCRF实体。PCRF实体标识为1，PCRF实体名称为PCRF，PCRF实体域名为huawei.com，主机名为pcrf.huawei.com。

   ```
   ADD PCRF: PCRFID=1, EN="PCRF", DN="huawei.com", HN="pcrf.huawei.com";
   ```