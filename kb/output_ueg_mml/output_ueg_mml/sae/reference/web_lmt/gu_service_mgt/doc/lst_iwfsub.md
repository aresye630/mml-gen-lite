# 查询IWF用户数据（LST IWFSUB）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询UTA用户的数据，主要包括缓存的用户4G基本信息、APN信息和5G动态信息等。

- 若需要查询单个用户的签约数据，请输入参数“IMSI”或“MSISDN”。
- 若需要查询连续多个用户的签约数据，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”。系统将会从输入的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的数据。
- 若需要查询不连续的多个用户的签约数据，请输入参数“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置，用户个数参数只能与“IMSI”或“MSISDN”一起出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                    |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 可选必选说明：可选参数 参数含义：用于标识要查询哪个IMSI号码对应的UTA用户数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                       |
| ISDN        | MSISDN    | 可选必选说明：可选参数 参数含义：用于标识要查询哪个MSISDN号码对应的UTA用户数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                     |
| RECORDCOUNT | 用户个数      | 可选必选说明：可选参数 参数含义：用于标识查询UTA用户数据的用户数目。 取值范围：1～10000。 默认值：无。 配置原则： 当需要查询连续号码的多个用户的签约数据时配置。配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的签约数据。该参数是对连续号码的多个用户进行签约数据查询，当只有一个用户时，该参数不必配置。 当一次查询的用户个数很多时，对系统性能无影响，但查询的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 可选必选说明：可选参数 参数含义：用于标识IMSI批操作文件。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。 配置原则：IMSI批操作文件包含多个不连续的待查询签约数据的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstiwfsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。                                   |
| ISDNFILE    | MSISDN文件名 | 可选必选说明：可选参数 参数含义：用于标识MSISDN批操作文件。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。 配置原则：MSISDN批操作文件包含多个不连续的待查询签约数据的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstiwfsub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。                             |

## 使用实例

1. 查询“IMSI”为“460000009123456”的UTA用户的数据，且不返回未签约的参数:

   ```
   %%LST IWFSUB: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                             IMSI = 460000009123456
                           MSISDN = 860011222
                            STATE = 0

   "IWF Cached 4G basic information"
                           ODBPOS = NOBPOS
                     NRNOTALLOWED = FALSE
                  NR5GSNOTALLOWED = FALSE
                    EPCNOTALLOWED = FALSE
                    NGCNOTALLOWED = FALSE
                           AMBRUP = 111
                           UPUNIT = Kbps
                           AMBRDW = 111
                           DWUNIT = Kbps
                             RFSP = 1
                         TAUTIMER = 1
                       ACTIVETIME = 0
                              MPS = FALSE
                         DLBUFFER = 0
                      UEUSAGETYPE = 65535
                          HSSHOST = iwf.huawei.com
                         HSSREALM = huawei.com
                    CHARGE_GLOBAL = 0100

   "IWF Cached 4G APN information"
                              APN = abc.com
                        CONTEXTID = 1
                          PDNTYPE = IPV4
                              QCI = 8
                         PRILEVEL = 1
                    PREEMPTIONCAP = TRUE
                    PREEMPTIONVUL = TRUE
                              LBO = TRUE
                        NONIPFLAG = FALSE
                           CHARGE = 0800
                        IWK5GSIND = TRUE
                         PGWCFQDN = xyz.com
                           UEIPV4 = 192.168.21.181
                       PGWCPLMNID = 460011
                        EPSAMBRUP = 2147483647
                           UPUNIT = Kbps
                        EPSAMBRDW = 2147483647
                           DWUNIT = Kbps
                     DEFAULT_FLAG = 1

   "Dynamic Status Information For AMF"
                       AMF_DYN_ID = 1
                    AMFINSTANCEID = 11112222-1111-2222-3333-111122223333
                SUPPORTEDFEATURES = 0000000000000000
                        PURGEFLAG = FALSE
                          IMSVOPS = UNKOWN
                 DEREGCALLBACKURI = http://127.200.254.64:8888/namf-uecm/v1/imsi-46
                                    0456789321874/registrations/amf-3gpp-access
                          REGTIME = 2020-03-31 01:50:20
                       TIME_STAMP = 2020-03-31 06:43:15
                              MCC = 045
                              MNC = 012
                            AMFID = 111122
                         URRP_AMF = REACHABLE
                          RATTYPE = NR

   Total count = 54

   There is together 1 report

   ---    END
   ```
2. 查询第一个“IMSI”号码为“460000009123456”的3个连续UTA用户的数据：

   ```
   LST IWFSUB: IMSI="460000009123456", RECORDCOUNT=3;
   ```

   ```
   %%LST IWFSUB: IMSI="460000009123456", RECORDCOUNT=3;%% 
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：1. 使用CHK BATSTAT指令可查看此批操作的执行情况  

   There is together 1 report 

    ---    END
   ```
3. 查询“MSISDN文件名”为“lstiwfsub.txt”的UTA用户的数据：

   ```
   LST IWFSUB: IMSIFILE="lstiwfsub.txt";
   ```

   ```
   %%LST IWFSUB: IMSIFILE="lstiwfsub.txt";%%  
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：2. 使用CHK BATSTAT指令可查看此批操作的执行情况  

   There is together 1 report  

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，具体参数含义请参见表1的参数说明。

| 输出项名称             | 输出项解释                                                                                                                                  |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN             | 用于标识一个HLR序列号。                                                                                                                          |
| IMSI              | 用于标识IMSI号码。                                                                                                                            |
| MSISDN            | 用于标识MSISDN号码。                                                                                                                          |
| STATE             | 用于标识缓存数据是否有效。 0：代表缓存有效。 1：代表缓存无效。                                                                                                      |
| ODBPOS            | 用于标识运营商决定的闭锁-闭锁分组业务。 NOBPOS：不闭锁分组业务。BAPOS：闭锁所有的分组业务。BHPLMNAPROAM：当用户在VPLMN漫游时闭锁接入点在HPLMN的分组业务。BALLAPROAM：当用户在VPLMN漫游时闭锁接入点在VPLMN的分组业务。 |
| NRNOTALLOWED      | 用于标识是否限制NR作为第二RAT。TRUE：限制 FALSE：不限制                                                                                                    |
| NR5GSNOTALLOWED   | 用于标识是否限制用户接入NR网络。 TRUE：限制接入 FALSE：允许接入                                                                                                 |
| EPCNOTALLOWED     | 用于标识是否限制用户接入EPC网络。 TRUE：限制接入 FALSE：允许接入                                                                                                |
| NGCNOTALLOWED     | 用于标识是否限制用户接入5GC网络。 TRUE：限制接入 FALSE：允许接入                                                                                                |
| AMBRUP            | 用于标识UE级别上行速率的参数。                                                                                                                       |
| UPUNIT            | 用于标识“UE级别上行速率”的单位。 bps：bit/s Kbps：Kbit/s                                                                                               |
| AMBRDW            | 用于标识UE级别下行速率的参数。                                                                                                                       |
| DWUNIT            | 用于标识“UE级别下行速率”的单位。 bps：bit/s Kbps：Kbit/s                                                                                               |
| RFSP              | 用于标识无线频率选择优先级。                                                                                                                         |
| TAUTIMER          | 用于标识用户是否签约周期RA/TA更新时间间隔功能。                                                                                                             |
| ACTIVETIMER       | 用于标识终端保持IDLE状态的时长。                                                                                                                     |
| MPS               | 用于标识是否给用户提供多媒体优先级业务。                                                                                                                   |
| DLBUFFER          | 用于标识签约高延迟通信时，下行缓存的大小。                                                                                                                  |
| UEUSAGETYPE       | 用于标识用户UE应用类型。                                                                                                                          |
| HSSHOST           | 用于标识ULA消息携带的HSS主机名。                                                                                                                    |
| HSSREALM          | 用于标识ULA消息携带的HSS域名                                                                                                                      |
| CHARGE_GLOBAL     | 用于标识ULA消息携带的UE级别的计费特性。                                                                                                                 |
| APN               | 用于标识EPS域UE级别的APN运营商标识符。                                                                                                                |
| CONTEXTID         | 用于表示接入点名称的上下文标识。                                                                                                                       |
| PDNTYPE           | 用于标识PDN类型。 IPV4 IPV6 IPV4IPV6 IPV4_OR_IPV6                                                                                             |
| QCI               | 用于标识QoS分类识别码。                                                                                                                          |
| PRILEVEL          | 标识用户在网络资源拥塞时的优先级。                                                                                                                      |
| PREEMPTIONCAP     | 用于标识是否允许该业务数据流占有优先级相对较低的业务数据流的资源。 TRUE：允许FALSE：禁止                                                                                      |
| PREEMPTIONVUL     | 用于标识是否允许该业务数据流丢失分配给它的资源，用于接纳一个优先级相对较高的业务数据流。 TRUE：允许FALSE：禁止                                                                           |
| LBO               | 用于标识漫游场景下DNN是否允许会话锚点功能。 TRUE：允许 FALSE：禁止                                                                                               |
| NONIPFLAG         | 是否是Non-IP PDN类型的APN。 TRUE：是Non-IP PDN类型的APN FALSE：非Non-IP PDN类型的APN                                                                    |
| CHARGE            | 用于标识计费特性。                                                                                                                              |
| IWK5GSIND         | 用于标识是否选择5G融合网关。 TRUE：选择 FALSE：不选择                                                                                                      |
| PGWCFQDN          | 用于标识PGW-C+SMF的FQDN信息。                                                                                                                  |
| PGWCPLMNID        | 用于标识PGW-C+SMF的PLMN标识。                                                                                                                  |
| UEIPV4            | 用于标识用户IPV4地址。                                                                                                                          |
| UEIPV6            | 用于标识用户IPV6地址。                                                                                                                          |
| EPSAMBRUP         | 用于标识APN级别上行速率的参数。                                                                                                                      |
| UPUNIT            | 用于标识APN级别上行速率的单位。                                                                                                                      |
| EPSAMBRDW         | 用于标识APN级别下行速率的参数。                                                                                                                      |
| DWUNIT            | 用于标识APN级别下行速率的单位。                                                                                                                      |
| DEFAULT_FLAG      | 用于标识是否为默认APN。 1：默认0：非默认                                                                                                                |
| AMF_DYN_ID        | 用于返回AMF的动态ID。                                                                                                                          |
| AMFINSTANCEID     | 用于返回用户在NRF注册时的AMF标识。                                                                                                                   |
| SUPPORTEDFEATURES | 用于返回AMF的特性支持能力。 取值范围：16进制字符串，bit0为最右边字符的最低bit位。每个bit位表示一个特性支持能力。                                                                       |
| PURGEFLAG         | 用于返回AMF在UDM中是否被去注册。 取值范围：TRUE：已经被去注册 FALSE：未被去注册                                                                                       |
| IMSVOPS           | 用于返回AMF是否支持IMS VoPS能力。 取值范围： NOT SUPPORT：不支持 SUPPORT：支持 UNKNOWN：未知状态                                                                   |
| DEREGCALLBACKURI  | 用于返回UDM给AMF发送去注册时，消息中的URI取值。                                                                                                           |
| REGTIME           | 用于返回用户最近一次注册时间。                                                                                                                        |
| PURGETIME         | 用户最近一次Purge时间。                                                                                                                         |
| TIME_STAMP        | 用于标识当前系统时间。                                                                                                                            |
| MCC               | 用于标识移动国家码。                                                                                                                             |
| MNC               | 用于标识移动网络码。                                                                                                                             |
| AMFID             | 用于返回AMF的标识。                                                                                                                            |
| URRP_AMF          | 用于返回UE在AMF上的可达性状态。 取值范围：UNREACHABLE：不可达 REACHABLE：可达 REGULATORY_ONLY：仅用于管理策略优先级服务。                                                     |
| RATTYPE           | 用于返回用户终端通过S6a接口接入网络的无线接入技术类型。                                                                                                          |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 消息解释       | 原因分析                                                                                                | 处理建议                                                                                                                     |
|:--------|:-----------|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| ERR1003 | 无效的参数名     | 输入的参数标识不正确。                                                                                         | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                         |
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。 参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                 |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                    | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                       |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                   | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                              |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。 “用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。 “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                              | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                          |
| ERR3007 | 记录不存在      | 输入的参数“IMSI”或“MSISDN”对应的用户已开户，但是没有UTA相关数据。                                                           | 无。                                                                                                                       |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                               | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                             |

## 参考信息

**IMSIFILE文件格式**

IMSIFILE文件包含不连续的IMSI号码，格式如下所示：

```
IMSI1 
IMSI2 
IMSI3 
IMSI4 
…… 
IMSIn
```

IMSIn为6～15位的十进制数字，行结束为回车换行符，行与行之间不能存在空行。

第一行和最后一行数据必须是有效数据，不能是空格、空行或Tab键。

**ISDNFILE文件格式**

ISDNFILE文件包含不连续的MSISDN号码，格式如下所示：

```
MSISDN1 
MSISDN2 
MSISDN3 
MSISDN4 
…… 
MSISDNn
```

MSISDNn为1～15位的十进制数字，行结束为回车换行符，行与行之间不能存在空行。

第一行和最后一行数据必须是有效数据，不能是空格、空行或Tab键。

**批操作资源文件存放位置**

在PGW Web LMT执行批操作处理前，要上传预先编写的批操作资源文件到PGW Server的指定目录。

批操作资源文件可通过PGW Web LMT的文件上传功能上传到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。

例如，当前的SYSHLRSN为“1”，操作员名称为“admin”，则存储批操作资源文件的目录为：“/opt/pgw/pgwtmpfile/001admin”。

其中，SYSHLRSN和操作员名称均为当前登录的系统HLRSN和操作员。系统HLRSN可以通过命令**LST SYSHLRSN**进行查询。