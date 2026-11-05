# 增加HLRSN与本局信息(ADD HLRSNOFI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于增加HLRSN与本局信息的对应关系数据。

当操作员在PGW Web LMT通过执行**SET MAPSERV**命令将“本局信息选取方式”参数设为“OMU\_HLRSN”或“ OMU\_IMSIPREFIX”时配置的数据会在业务流程中生效。

- “本局信息选取方式”参数设为“OMU\_HLRSN”时：
  - 在业务流程中UDM会按照实际正在使用业务的用户IMSI、IMPI或IMPU在数据库查找开户时所在的HLRSN，再根据该命令配置的对应关系来获取“本局GT”、“本局HLR号码”、“本局主机名”、“本局域名”、“IMS本局主机名”和“IMS本局域名”等数据。
  - 如果UDM根据用户数据对应的HLRSN无法获取相应的对应关系则按照“本局信息选取方式”参数设为“DEFAULT”的情况处理。
- “本局信息选取方式”参数设为“OMU\_IMSIPREFIX”时：
  - 在业务流程中UDM首先按照实际正在使用业务的用户IMSI，根据**ADD IMSIHLRSN**命令配置的IMSI前缀和HLRSN的对应关系获取HLRSN，然后使用该命令配置的对应关系来获取“本局GT”、“本局HLR号码”、“本局主机名”、“本局域名”、“IMS本局主机名”和“IMS本局域名”等数据。
  - 在这种场景中需要同时执行**ADD HLRSNOFI**命令和**ADD IMSIHLRSN**命令来配置数据。业务流程中数据未匹配成功则UDM按照“本局信息选取方式”参数设为“DEFAULT”的情况处理。

## 注意事项

- “本局GT”、“本局HLR号码”、“本局主机名”、“本局域名”、“归属GT”、“归属HLR号码”、“IMS本局主机名”和“IMS本局域名”八个参数必须至少输入其中之一。
- “本局GT”和“本局HLR号码”参数必须同时输入。
- “本局主机名”和“本局域名”参数必须同时输入。
- “归属GT”和“归属HLR号码”参数必须同时输入。
- “IMS本局主机名”和“IMS本局域名”参数必须同时输入。
- 通过本命令增加HLRSN与本局信息的对应关系数据时，若本端类型为IWF，则配置的“本局主机名”需要和IWF本端主机名保持一致，此时必须先在**ADD DMLE**命令中配置“主机名”，且“本端设备类型”必须为“IWF(IWF)”。
- 如果本命令增加的主机名，未在DMLE命令中与之对应的配置，执行本命令增加主机名将导致HLRSNOFI多主机名业务处理异常。请在华为技术支持指导下执行该操作。

## 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                            |
|:--------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号   | 用于标识一个HLR序列号索引。 取值范围：1～255 默认值：无。                                                                                                                                                               |
| LOCGT         | 本局GT     | 用于标识本局GT（Global Title）码，当UDM查询与其交互的设备GMSC、SMSC、SCP不在SET SELIST命令（PGW Web LMT上执行）设置的业务实体为“HPLMNSNGREY”的业务实体表中，则使用该参数构建SCCP（Signaling Connection and Control Part）消息的主叫地址。 取值范围：1～16位BCD码。 默认值：无。 |
| HLRNO         | 本局HLR号码  | 用于标识本局HLR号码。对于需要使用HLR号码的消息流程，例如位置更新、Reset流程等，当UDM查询与其交互的设备GMSC、SMSC、SCP不在SET SELIST命令（PGW Web LMT上执行）设置的业务实体为“HPLMNSNGREY”的业务实体表中使用该参数。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                           |
| LOCALHOST     | 本局主机名    | 用于标识本局主机名。在处理Diameter消息流程时使用该参数。 取值范围：1～127位字符串。 默认值：无。                                                                                                                                         |
| LOCALREALM    | 本局域名     | 用于标识本局域名名称。在处理Diameter消息流程时使用该参数。 取值范围：1～127位字符串。 默认值：无。                                                                                                                                        |
| DEFGT         | 归属GT     | 用于标识归属GT码，当UDM查询与其交互的设备GMSC、SMSC、SCP存在于SET SELIST命令（PGW Web LMT上执行）设置的业务实体为“HPLMNSNGREY”的业务实体表中，则使用该参数构建SCCP消息的主叫地址。 取值范围：1～16位BCD码。 默认值：无。                                                     |
| DEFHLRNO      | 归属HLR号码  | 用于标识归属HLR号码。对于需要使用HLR号码的消息流程，例如位置更新、Reset流程等，当UDM查询与其交互的设备GMSC、SMSC、SCP存在于SET SELIST命令（PGW Web LMT上执行）设置的业务实体为“HPLMNSNGREY”的业务实体表中使用该参数。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                          |
| IMSLOCALHOST  | IMS本局主机名 | 用于标识IMS域的本局主机名称。在处理Diameter消息流程时使用该参数。 取值范围：长度不超过127的字符串。 默认值：无。                                                                                                                                |
| IMSLOCALREALM | IMS本局域名  | 用于标识IMS域的本局域名。在处理Diameter消息流程时使用该参数。 取值范围：长度不超过127的字符串。 默认值：无。                                                                                                                                  |

## 使用实例

- “本局信息选取方式”参数设为“OMU\_HLRSN”时：
  1. 操作员在PGW Web LMT通过执行**SET MAPSERV**命令将“本局信息选取方式”参数设为“OMU\_HLRSN”。`SET MAPSERV: OFI_MODE=OMU_HLRSN;`
  2. 操作员登录OM Portal，在“UDM MML命令”界面上执行**ADD DMLE**命令配置“本端设备类型”为“IWF(IWF)”的**“主机名”**（可选流程，当本端类型为IWF时，该流程必选）。

     ```
     ADD DMLE: EN="IWF-HSS", LOCTYPE=IWF, DN="huawei.com", HN="iwf1.huawei.com", DEFLOCAL=NO;
     ```
  3. 操作员登录OM Portal，在“UDM MML命令”界面上执行**ADD HLRSNOFI**命令增加一条HLRSN与本局信息的对应关系数据。

     ```
     ADD HLRSNOFI: HLRSN=1, LOCGT=K'8613801, HLRNO="8613901", LOCALHOST="iwf1.huawei.com", LOCALREALM="huawei.com", DEFGT=K'8613801001, DEFHLRNO="8613901001";
     ```
- “本局信息选取方式”参数设为“OMU\_IMSIPREFIX”时：
  1. 操作员在PGW Web LMT通过执行**SET MAPSERV**命令将“本局信息选取方式”参数设为“OMU\_IMSIPREFIX”。`SET MAPSERV: OFI_MODE=OMU_IMSIPREFIX;`
  2. 操作员登录OM Portal，在“UDM MML命令”界面上执行**ADD DMLE**命令配置“本端设备类型”为“IWF(IWF)”的**“主机名”**（可选流程，当本端类型为IWF时，该流程必选）。

     ```
     ADD DMLE: EN="IWF-HSS", LOCTYPE=IWF, DN="huawei.com", HN="iwf1.huawei.com", DEFLOCAL=NO;
     ```
  3. 操作员登录OM Portal在“UDM MML命令”界面上执行**ADD HLRSNOFI**命令增加一条HLRSN与本局信息的对应关系数据。

     ```
     ADD HLRSNOFI: HLRSN=1, LOCGT=K'8613801, HLRNO="8613901", LOCALHOST="iwf1.huawei.com", LOCALREALM="huawei.com", DEFGT=K'8613801001, DEFHLRNO="8613901001";
     ```
  4. 操作员登录OM Portal在“UDM MML命令”界面上执行**ADD IMSIHLRSN**命令增加一条IMSI前缀与HLRSN数据的对应关系数据。

     ```
     ADD IMSIHLRSN: IMSIPREFIX="86139029", HLRSN=1;
     ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                                                | 原因分析                                                   | 处理建议                                                                                          |
|-------:|:-------------------------------------------------------------------------------------|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| 264056 | 指定的HLRSN已经存在                                                                         | “HLR序列号”参数已被使用。                                        | 使用LST HLRSNOFI命令查询后，重新输入“HLR序列号”。                                                             |
| 264057 | 参数LOCGT和参数HLRNO必须共存                                                                  | 没有同时输入“本局GT”和“本局HLR号码”参数。                              | “本局GT”和“本局HLR号码”参数必须同时输入。                                                                     |
| 264058 | 参数LOCALHOST和参数LOCALREALM必须共存                                                         | 没有同时输入“本局主机名”和“本局域名”参数。                                | “本局主机名”和“本局域名”参数必须同时输入。                                                                       |
| 264059 | 参数DEFGT和DEFHLRNO必须共存                                                                 | 没有同时输入“归属GT”和“归属HLR号码”参数。                              | “归属GT”和“归属HLR号码”参数必须同时输入。                                                                     |
| 299545 | 参数IMSLOCALHOST和参数IMSLOCALREALM必须共存                                                   | 没有同时输入“IMS本局主机名”和“IMS本局域名”参数。                          | “IMS本局主机名”和“IMS本局域名”参数必须同时输入。                                                                 |
| 264060 | 关键参数LOCGT、HLRNO、LOCALHOST、LOCALREALM、DEFGT、DEFHLRNO、IMSLOCALHOST和IMSLOCALREALM不能全部为空 | 除了“HLR序列号”，未输入其它参数。                                    | “本局GT”、“本局HLR号码”、“本局主机名”、“本局域名”、“归属GT”、“归属HLR号码”、“IMS本局主机名”和“IMS本局域名”八个参数必须至少输入其中之一。          |
| 483044 | 参数的值的长度超过上限                                                                          | 输入的以下参数值超出最大范围： 本局HLR号码本局主机名本局域名归属HLR号码IMS本局主机名IMS本局域名 | 请重新输入参数的值，确保其在取值范围内。                                                                          |
| 264003 | 指定的DMLE不存在。请执行LST DMLE查看已经存在的DMLE对象。                                                 | 输入的主机名和域名没有匹配的Diameter本端实体的数据记录。                       | 根据实际情况，重新输入参数，确保输入的主机名和域名已配置。 执行LST DMLE命令查询系统已配置本端Diameter本端实体数据记录。执行本命令，重新输入系统已配置的主机名和域名信息。 |