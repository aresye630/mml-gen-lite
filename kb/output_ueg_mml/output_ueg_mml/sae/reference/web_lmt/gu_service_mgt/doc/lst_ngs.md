# 查询5G用户签约数据(LST NGS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询5G用户的签约数据信息，且不返回未签约的数据信息。

- 若需要查询单个用户的签约数据信息，请输入参数“IMSI”或“MSISDN”其中的一个，其他参数不输入。
- 若需要查询连续多个用户的签约数据信息，请输入参数“IMSI”或“MSISDN”的同时，再输入参数“用户个数”，其他参数不输入。
- 若需要查询不连续的多个用户的签约数据信息，请输入参数“IMSI文件名”或“MSISDN文件名”，其他参数不输入。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”四个参数必须有且只能有一个参数出现。
- “用户个数” 参数不能与“IMSI文件名”或“MSISDN文件名”同时存在，“用户个数”参数只能与“IMSI”或“MSISDN”一起出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                 |
|:------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 可选必选说明：条件可选参数 参数含义：用于指示系统按照哪个“IMSI”来查询5G用户的签约数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                               |
| ISDN        | MSISDN    | 可选必选说明：条件可选参数 参数含义：用于指示系统按照哪个“MSISDN”来查询5G用户的签约数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无 配置原则：无。                                                                                                                                                                              |
| RECORDCOUNT | 用户个数      | 可选必选说明：条件可选参数 参数含义：用于指示系统按照设置的用户个数来查询对应5G用户的签约数据。 取值范围：1～10000 默认值：无。 配置原则： 当需要为连续号码的多个用户查询5G用户的签约数据时配置该参数，配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，对连续号码的多个用户进行查询5G用户的签约数据。该参数是对连续号码的多个用户查询5G用户的签约数据，当只有一个用户时，该参数不必配置。当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 可选必选说明：条件可选参数 参数含义：用于指示系统按照哪个IMSI文件名来查询不连续的多个5G用户的签约数据。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。 配置原则：IMSI批操作文件包含多个不连续的待查询5G用户签约数据的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstngs.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。                                          |
| ISDNFILE    | MSISDN文件名 | 可选必选说明：条件可选参数 参数含义：用于指示系统按照哪个MSISDN文件名来查询不连续的5G用户的签约数据。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。 配置原则：MSISDN批操作文件包含多个不连续的待查询5G用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstngs.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。                                          |

## 使用实例

1. 查询“IMSI”为“460030913121001”的5G用户的签约数据，且不返回未签约的参数：

   ```
   LST NGS: IMSI="460030913121001";
   ```

   ```
   %%LST NGS: IMSI="460030913121001";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460030913121001
                             ISDN = 460030913121001
                           AMBRUP = 1                         
                           UPUNIT = bps                         
                           AMBRDW = 1                        
                           DWUNIT = bps 
                              MPS = FALSE
                              MCS = FALSE
                      DLBUFFERIND = NOT_REQUESTED
                         DLBUFFER = 0
                         AUTHTYPE = 5G-AKA
                      MICOALLOWED = FALSE
                    SMSSUBSCRIBED = TRUE
                            MTSMS = FALSE
                          MTSMSBA = FALSE
                          MTSMSBR = FALSE
                            MOSMS = FALSE
                          MOSMSBA = FALSE
                          MOSMSBR = FALSE
            NSSAIINCLUSIONALLOWED = TRUE
                        INGROUPID = 5-460003-01
                         SHAREDID = 46001-shared5

                           SNSSAI = 3
                        DEFSNSSAI = FALSE

                           SNSSAI = 1
                        DEFSNSSAI = TRUE
                              DNN = dnn
                          DEFAULT = TRUE
                      DNNQOSTPLID = 11

   		        PLMNID = 46002
                          CAGONLY = FALSE
                            CAGID = abcdef22
                            CAGID = abcdef23
   						
   		        PLMNID = 46003
                          CAGONLY = FALSE
                            CAGID = abcdef32
                            CAGID = abcdef33

   Total count = 37

   There is together 1 report

   ---    END
   ```
2. 查询“IMSI”为“460030913121001”的3个连续5G用户的签约数据：

   ```
   LST NGS: IMSI="460030913121001", RECORDCOUNT=3;
   ```

   ```
   %%LST NGS: IMSI="460030913121001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：18. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“IMSI文件名”为“lstngs.txt”的5G用户的签约数据：

   ```
   LST NGS: IMSIFILE="lstngs.txt";
   ```

   ```
   %%LST NGS: IMSIFILE="lstngs.txt";%%  
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：19. 使用CHK BATSTAT指令可查看此批操作的执行情况  

   There is together 1 report  

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD FORBIDAREATPL**

、

**ADD VSLIST**

、

**ADD NGCRRNODETPL**

和

**ADD SUB**

命令的参数说明。表1列出的是未包含在

**ADD FORBIDAREATPL**

、

**ADD VSLIST**

、

**ADD NGCRRNODETPL**

和

**ADD SUB**

命令参数说明中的输出项。

| 输出项名称                 | 输出项解释                 |
|:----------------------|:----------------------|
| AMBRUP                | UE级别上行速率              |
| UPUNIT                | UE级别上行速率单位            |
| AMBRDW                | UE级别下行速率              |
| DWUNIT                | UE级别下行速率单位            |
| MCS                   | 是否支持关键任务优先级服务         |
| DLBUFFERIND           | 是否提供签约高延迟通信时的下行缓存大小   |
| DLBUFFER              | 高延迟通信时的下行缓存大小         |
| AUTHTYPE              | 鉴权方式                  |
| MICOALLOWED           | 是否支持MICO模式            |
| INGROUPID             | 移动网络内部设备之间通信时互相传递的组ID |
| SHAREDID              | 为内部组创建的共享数据的ID        |
| SNSSAI                | 切片标识                  |
| DEFSNSSAI             | 是否默认S-NSSAI           |
| DNN                   | 数据网络名称                |
| DNNQOSTPLID           | 5GS DNNAPNQOS模板ID·    |
| NSSAIINCLUSIONALLOWED | 是否支持切片包含模式            |
| SUPSUBSREGTIMER       | 是否支持5G周期注册定时器签约       |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                                 | 处理建议                                                                                                                     |
|:--------|:-----------|:-----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 界面输入的参数不在相应的参数取值范围内。                                                                                 | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                         |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                     | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                       |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”或“MSISDN文件名”四个参数一个都没有输入。                                                    | 根据实际情况，重新输入参数，确保满足“IMSI”、“MSISDN”、“IMSI文件名”或“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1010 | 参数冲突       | 可能原因为如下之一： “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。 “用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。 “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                | 请根据IMSIFILE文件格式和ISDNFILE文件格式重新确定对应的批操作文件格式。                                                                              |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数 “IMSI”或“MSISDN”对应的用户未开户。                                              | 核实用户的IMSI号码或MSISDN号码，如果输入有误，重新输入正确的IMSI号码或MSISDN号码。                                                                      |
| ERR4104 | 非5G用户      | 用户未签约接入和移动管理数据。                                                                                      | 请执行LST AMDATA命令查询用户是否签约，若需要签约请参考MOD AMDATA命令为用户签约接入和移动管理数据后重新执行本命令进行查询。                                                  |

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