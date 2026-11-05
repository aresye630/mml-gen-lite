# 查询AMF 3GPP注册信息数据（LST AMF3GPPREGINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户AMF 3GPP的注册信息数据。

- 如果查询单个用户的注册信息，请输入参数“IMSI”或“MSISDN”其中的一个，其他参数不输入。
- 若需要查询连续多个用户的注册信息，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”，其他参数不输入。
- 若需要查询不连续的多个用户的注册信息，请输入参数“IMSI文件名”或“MSISDN文件名”，其他参数不输入。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数必须有且只能有一个参数出现。
- “用户个数” 参数不能与“IMSI文件名”或“MSISDN文件名”同时存在，“用户个数”参数只能与“IMSI”或“MSISDN”一起出现。
- 执行该命令是否返回Purge状态变更时间，由**SET MAPCONF**命令中“支持查询用户的PURGE时间”参数控制。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                     |
|:------------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 可选必选说明：条件可选参数 参数含义：用于指示系统需要查询哪个IMSI号码的用户的AMF 3GPP注册信息数据。 取值范围：6~15位的十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                          |
| ISDN        | MSISDN    | 可选必选说明：条件可选参数 参数含义：用于指示系统需要查询哪个MSISDN号码的用户的AMF 3GPP注册信息数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                         |
| RECORDCOUNT | 用户个数      | 可选必选说明：条件可选参数 参数含义：用于指示系统需要查询连续多少个用户的AMF 3GPP注册信息数据业务。 取值范围：1~10000。 默认值：无。 配置原则： 该参数提供，代表以指定的IMSI或MSISDN为起始号码，号码连续的RECORDCOUNT个用户。该参数是对连续号码的多个用户查询AMF 3GPP注册业务，当只有一个用户时，该参数不必配置。当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 可选必选说明：条件可选参数 参数含义：用于指示系统需要查询哪个IMSI批操作文件中包含的用户的AMF 3GPP注册信息数据。 取值范围：1~16位字母或十进制数字组成的字符串。 默认值：无。 配置原则：IMSI批操作文件包含多个不连续的需要查询AMF 3GPP的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstamf3gpp.txt”，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。            |
| ISDNFILE    | MSISDN文件名 | 可选必选说明：条件可选参数 参数含义：用于指示系统需要查询哪个MSISDN批操作文件中包含的用户的AMF 3GPP注册信息数据。 配置原则：MSISDN批操作文件包含多个不连续的需要查询AMF 3GPP的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstamf3gpp.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。                       |

## 使用实例

1. 查询“IMSI号码”为“460990000000000”的用户的注册信息。

   ```
   LST AMF3GPPREGINFO: IMSI="460990000000000";
   ```

   ```
   %%LST AMF3GPPREGINFO: IMSI="460990000000000";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460990000000000
                             ISDN = 8613800000000
                    AMFINSTANCEID = 11112222-1111-2222-3333-111122223333
                          RATTYPE = NR
                SUPPORTEDFEATURES = 0000000000000000
                        PURGEFLAG = NOT PURGE
                          IMSVOPS = support
                 DEREGCALLBACKURI = http://172.16.202.146:8020/namf-uecm/v1/imsi-460990000000000/regist
                                    rations/amf-3gpp-access
              AMFSERVICENAMEDEREG = namf-evts
                      PCSCFRSTURI = /namf-uecm/v1/imsi-460990000000000/registrations/amf-3gpp-access
          AMFSERVICENAMEPCSCFREST = namf-evts
                          REGTIME = 2021-08-19 01:12:24
                        PURGETIME = 2023-06-19 15:37:00
                              MCC = 460
                              MNC = 005
                            AMFID = 111122
                   BACKUP_AMFINFO = amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org
                         URRP_AMF = REACHABLE
                       AMFREGFLAG = 0
                        SCPRTFLAG = FALSE
                      ROAMINGTYPE = LOCAL
                    VGMLCIPV4ADDR = 10.189.171.60
                    VGMLCIPV6ADDR = fe80:910a:2222:5498:8475:1111:3900:2020
                        VGMLCFQDN = Huawei.com
                       SBIBINDING = bl=nf-instance;nfinst=11112222-1111-2222-3333-111122223333;backupam
                                    finst=54804520-4191-46b3-955c-ac631f953ed8;
                   DNNENHANCEFLAG = TRUE
                            VPNID = 1

   Total count = 27

   There is together 1 report

   ---    END
   ```
2. 查询“IMSI号码”为“460000009123456”、“460000009123457”、“460000009123458”的3个连续用户的注册信息。

   ```
   LST AMF3GPPREGINFO: IMSI="460000009123456", RECORDCOUNT=3;
   ```

   ```
   %%LST AMF3GPPREGINFO: IMSI="460000009123456", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:Operation is successful Batch ID: 5. CHK BATSTAT can be used to obtain the status of batch operation

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**MOD AMF3GPPREGINFO**

命令的参数说明。表1列出的是未包含在

**MOD AMF3GPPREGINFO**

命令参数说明中的输出项。

| 输出项名称                   | 输出项说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUPPORTEDFEATURES       | AMF支持的特性能力标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PURGEFLAG               | AMF是否去注册的标志。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IMSVOPS                 | AMF是否支持IMS VoPS（IMS Voice over PS Sessions）能力。 not support：不支持support：支持                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DEREGCALLBACKURI        | 去注册时Uri。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PCSCFRSTURI             | 发生P-CSCF容灾恢复时用的Uri。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AMFSERVICENAMEPCSCFREST | 向哪个AMF服务名称发送P-CSCF恢复通知。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| REGTIME                 | 用户最近一次注册时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PURGETIME               | 用户最近一次Purge时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| BACKUP_AMFINFO          | 备份AMF。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| URRP_AMF                | UE在AMF上可达性状态。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AMFREGFLAG              | AMF注册标识。 bit0：初始注册标识。bit1：双注册标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SCPRTFLAG               | SCP路由标识，用于指示系统标识用户订阅请求消息是否经过SCP路由，默认为未经过SCP路由。 当SCPRTFLAG = TRUE时，表示经过SCP路由。当SCPRTFLAG = FALSE时，表示未经过SCP路由。 说明：该参数不支持通过营帐系统查询。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ROAMINGTYPE             | 对端相对于本地UDM所属的网络类型。基于AMF注册消息中携带的PLMN是否已通过ADD NGSPETYPE命令配置判断，如果未通过ADD NGSPETYPE命令配置，则基于消息携带的PLMN中MCC是否与用户IMSI前缀匹配判断。 取值范围： LOCAL：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“LOCAL”，或未通过ADD NGSPETYPE命令配置时，请求消息中携带的PLMN中MCC与用户IMSI前缀匹配时，判断用户漫游类型为“LOCAL”。LOCALDOMESTIC：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“LOCALDOMESTIC”。CROSSDOMESTIC：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“CROSSDOMESTIC”。LOCALINTERNATIONAL：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“LOCALINTERNATIONAL”。CROSSINTERNATIONAL：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“CROSSINTERNATIONAL”，或未通过ADD NGSPETYPE命令配置时，请求消息中携带的PLMN中MCC与用户IMSI前缀不匹配时，判断用户漫游类型为“CROSSINTERNATIONAL”。LOCALAREA：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“LOCALAREA”。CROSSAREA：AMF注册消息中携带的PLMN已通过ADD NGSPETYPE命令配置且“业务属性”取值为“CROSSAREA”。 说明：该参数不支持通过营帐系统查询。 |
| VGMLCIPV4ADDR           | 表示VGMLC的IPv4地址。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| VGMLCIPV6ADDR           | 表示VGMLC的IPv6地址。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| VGMLCFQDN               | 表示VGMLC IPv6地址的FQDN。该参数仅在PGW Web LMT界面执行该命令时显示，营帐侧查询不显示。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SBIBINDING              | 表示AMF向UDM注册时携带的3gpp-Sbi-Binding信息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DNNENHANCEFLAG          | 用户是否启用DNN下发增强特性。FALSE：未启用DNN下发增强特性。TRUE：启用DNN下发增强特性。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

该命令执行异常，会返回对应的错误码。常见错误码如表1 错误码列表所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                 | 处理建议                                                                                                              |
|:--------|:--------|:-----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 输入参数不符合参数取值范围。                                                                                       | 根据实际情况，重新输入，确保其取值符合要求。                                                                                            |
| ERR1005 | 文件不存在   | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                     | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                |
| ERR1009 | 参数丢失    | 参数“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数同时缺失。                                                     | 根据实际情况，“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数必须有且只能有一个参数出现。                                                    |
| ERR1010 | 参数冲突    | 可能的原因为如下之一： “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点： “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数必须有且只能有一个参数出现。“用户个数”不与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户   | 用户的“IMSI”或“MSISDN”输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                               | 核实IMSI或MSISDN号码，确保其对应的用户为5G用户并验证其正确性，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请参考ADD SUB页面给用户开户。                 |