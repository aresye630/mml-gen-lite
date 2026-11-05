# 激活漫游控制特性(适用于SGSN/MME)

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活漫游控制特性的操作过程。

漫游控制，是指UEG提供互联PLMN表的配置，只有用户的归属PLMN属于互联PLMN表才能够接入本UEG。漫游控制特性使网络具有限制用户移动范围和业务访问的能力。

适用于SGSN、MME。

## 对系统的影响

该操作对系统正常运行没有影响。

## 必备事项

前提条件

请仔细阅读GWFD-021102 漫游控制特性概述。

数据

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CONNECTPLMN** | 移动国家码（MCC） | 460 | 全网规划 | 互联的PLMN参数 |
|  | 移动网号（MNC） | 00 |  |  |
|  | 匹配IMSI（MATCHIMSI） | 1234 |  |  |
|  | 国家码（CC） | 86 |  |  |
|  | 运营商标识（NOID） | 3 |  |  |
|  | 是否允许SM业务（SM） | YES |  |  |
|  | 最大承载数（MAXSMNUM） | 2 |  |  |
|  | 是否允许SMS业务（SMS） | YES |  |  |
|  | 是否允许纠正短消息中心（SMSCR） | YES |  |  |
|  | 纠正后的短消息中心（SMSCT） | 861395678956778 |  |  |
|  | 是否允许LCS业务（LCS） | YES |  |  |
|  | 协议类型（S5S8TYPE） | GTP |  |  |
|  | 运营商名称（COUNTRYORAREANAME） | noname |  |  |
|  | 专属互连PLMN（EXCLUSIVEPLMN） | NO |  |  |
| **SET CHGPLMNCHAR** | PLMN（PLMN类型） | VPLMN | 全网规划 | 漫游PLMN用户的计费属性参数 |
|  | MP（生成M-CDR） | YES |  |  |
|  | SP（生成S-CDR） | YES |  |  |
|  | SMOP（生成S-SMO-CDR） | YES |  |  |
|  | SMTP（生成S-SMT-CDR） | YES |  |  |
|  | LCSMOP（生成LCS-MO-CDR） | YES |  |  |
|  | LCSMTP（生成LCS-MT-CDR） | YES |  |  |
|  | LCSNIP（生成LCS-NI-CDR） | YES |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 增加互联的PLMN，并配置允许的业务。

   **ADD CONNECTPLMN**
3. 设置漫游PLMN用户的计费属性参数。

   **SET CHGPLMNCHAR**

   参数“PLMN”（PLMN类型）选择“VPLMN”（拜访PLMN）。

## 任务示例

任务描述

增加一个互联的PLMN，PLMN ID为46000，国家码是86，允许这个互连PLMN用户使用纠正短消息中心业务，纠正后的短消息中心为861395678956778，并配置该VPLMN用户不生成LCS-NI-CDR话单。

脚本

//增加互联的PLMN，其移动国家码为“460”，移动网号为“00”，国家码为“86”，是否允许纠正短消息中心选择“YES”，纠正后的短消息中心为“861395678956778”，其他参数默认。

```
ADD CONNECTPLMN: MCC="460", MNC="00", CC="86", SMS=YES, SMSCR=YES, SMSCT="861395678956778";
```

//设置漫游用户的话单控制属性，配置其不生成LCS-NI-CDR，其他参数默认。

```
SET CHGPLMNCHAR: PLMN=VPLMN, LCSNIP=NO;
```

版权所有 © 华为技术有限公司
