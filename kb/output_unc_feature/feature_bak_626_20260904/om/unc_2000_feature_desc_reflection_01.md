# 激活支持用户属性反射

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当需要将用户接入属性映射到话单信息中时，需要激活接入用户属性反射功能。

**说明** 

适用于GGSN、PGW-C、SMF。

## 必备事项

前提条件

请仔细阅读WSFD-011309 支持用户属性反射。

数据

| 类别                | 参数名称                                  | 取值样例        | 获取方法   | 说明                                                                           |
|:------------------|:--------------------------------------|:------------|:-------|:-----------------------------------------------------------------------------|
| SET SRVNODERATPRI | RAT类型的第一优先级（FIRSTPRIORITY）            | RAT         | 本端规划   | 配置获取RAT Type的两种方式的优先级，两个参数的配置不能相同。                                           |
| SET SRVNODERATPRI | RAT类型的第二优先级（SECONDPRIORITY）           | SGSN_IP     | 本端规划   | 配置获取RAT Type的两种方式的优先级，两个参数的配置不能相同。                                           |
| ADD SRVNODERAT    | RAT类型（RATTYPE）                        | UTRAN       | 全网规划   | 配置SGSN/SGW的IP地址段与RAT类型间的映射关系表。                                               |
| ADD SRVNODERAT    | IP地址版本类型(IPVERSION)                   | IPV4        | 全网规划   | 配置SGSN/SGW的IP地址段与RAT类型间的映射关系表。                                               |
| ADD SRVNODERAT    | Service Node的起始IPv4地址（SRVNODESTARTV4） | 192.168.1.1 | 全网规划   | 配置SGSN/SGW的IP地址段与RAT类型间的映射关系表。                                               |
| ADD SRVNODERAT    | Service Node的结束IPv4地址（SRVNODEENDV4）   | 192.168.2.2 | 全网规划   | 配置SGSN/SGW的IP地址段与RAT类型间的映射关系表。                                               |
| ADD APN           | 根据SGSN/SGW映射RAT（SERVINGNODERAT）       | ENABLE      | 本端规划   | 配置使用SGSN/S-GW IP映射方式来获取RAT类型的开关。                                             |
| ADD CDRFIELDTEMP  | rat-type（RATTYPE）                     | ENABLE      | 与对端协商  | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |
| ADD CDRFIELDTEMP  | user-location-information（ULI）        | ENABLE      | 与对端协商  | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |
| ADD CDRFIELDTEMP  | ms-time-zone（MSTIMEZONE）              | ENALBE      | 与对端协商  | 配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。 |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置获取RAT Type的两种方式的优先级。

   **SET SRVNODERATPRI**
3. 配置SGSN/S-GW IP与RAT类型间的映射关系表。

   **ADD SRVNODERAT**
4. 配置SGSN/S-GW默认RAT类型。

   **ADD DFTSRVNODERAT**

   **说明** 

   SGSN/S-GW IP地址段与RAT类型的映射表配有默认项，当SGSN/S-GW IP在表中没有匹配项时，会用默认的RAT类型作为它对应的RAT类型。当要配置默认表项时，使用**ADD DFTSRVNODERAT**命令。
5. 配置话单中携带的字段。

   **ADD CDRFIELDTEMP**
6. 配置APN实例，设置是否允许此APN下的用户通过SGSN/S-GW-IP映射方式来获取RAT Type。

   **ADD APN**
7. 配置APN实例绑定话单字段模板。

   **SET APNCHARGECTRL**

## 任务示例

任务描述

配置用户通过RAT TYPE获取接入类型，并将用户的接入属性映射到话单中。

脚本

//配置获取RAT Type的两种方式的优先级。

```
SET SRVNODERATPRI:FIRSTPRIORITY=RAT,SECONDPRIORITY=SGSN_IP,NODETYPE=GGSN;
```

//配置SGSN/S-GW IP与RAT类型间的映射关系表。

```
ADD SRVNODERAT:IPVERSION=IPV4, SRVNODESTARTV4="192.168.1.1", SRVNODEENDV4="192.168.2.2", RATTYPE=UTRAN;
```

//配置SGSN/S-GW默认RAT类型。

```
SET DFTSRVNODERAT:RATTYPE=UTRAN,NODETYPE=GGSN;
```

//配置话单中携带的字段。

```
ADD CDRFIELDTEMP:TEMPLATENAME="cdr-field-test",RATTYPE=ENABLE,ULI=ENABLE,MSTIMEZONE=ENABLE;
```

//配置APN实例。

```
ADD APN:APN="apn-test",SERVINGNODERAT=ENABLE;
```

//配置APN实例绑定话单字段模板。

```
SET APNCHARGECTRL:APN="apn-test", GCDRTEMPLATE="cdr-field-test", PGWCDRTEMPLATE="cdr-field-test", SGWCDRTEMPLATE="cdr-field-test";
```