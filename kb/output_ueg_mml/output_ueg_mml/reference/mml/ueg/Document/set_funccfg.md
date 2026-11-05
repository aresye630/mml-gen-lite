# 设置HLR配置信息(SET FUNCCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于设置安装产品的配置管理资源信息。

## 注意事项

无。

## 参数说明

| 参数标识                  | 参数名称                  | 参数说明                                                                                                                                                              |
|:----------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEVICENAME            | 设备名称                  | 其值域类型为字符串，用于具体描述一个设备名称，以便于识别。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                            |
| DEVICETYPE            | 设备型号                  | 其值域类型为字符串，用于具体描述一个设备型号，以便于识别。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                            |
| DEVICEHARDWARE        | 设备硬件平台                | 其值域类型为字符串，用于具体描述一个设备硬件平台，以便于识别。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                          |
| DEVICEPROVIDER        | 设备供应商                 | 其值域类型为字符串，用于具体描述一个设备供应商，以便于识别。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                           |
| PORT2MNUM             | 已配置2M端口数              | 此参数用于设置已配置2M端口数。 取值范围：0～2147483647。 默认值：无。                                                                                                                        |
| PORT64KNUM            | 已配置64k端口数             | 此参数用于设置已配置64k端口数。 取值范围：0～2147483647。 默认值：无。                                                                                                                       |
| MAXNUMPDPADDRESS      | 最大可存储的PDP地址数          | 此参数用于设置最大可存储的PDP地址数。 取值范围：0～2147483647。 默认值：无。                                                                                                                    |
| BAKUPHLRNUMBER        | 备份的HLR编号              | 此参数用于设置备份的HLR编号。 取值范围：长度不超过15的字符串。 默认值：无。                                                                                                                         |
| MAXNUMNPCPMSISDN      | 最大可存储的外网之间携转的MSISDN个数 | 此参数用于设置最大可存储的外网之间携转的MSISDN个数。 取值范围：0～2147483647。 默认值：无。                                                                                                           |
| MAXMAPCAPACITY        | MAP消息处理能力             | 此参数用于设置MAP消息处理能力。 取值范围：0～2147483647。 默认值：无。                                                                                                                       |
| MAXNUMM3UALNK         | 最大M3ua链路数             | 此参数用于设置最大M3ua链路数。 取值范围：0～2147483647。 默认值：无。                                                                                                                       |
| FUNCTYPE              | 网元功能类型                | 此参数用于设置网元功能类型。HLR(HLR)NPHLR(NPHLR)NPMSC(NPMSC)RESERVED_1(保留编号计划1)RESERVED_2(保留编号计划2)NPUDM(NPUDM)IMSHSS(IMSHSS) 默认值：HLR。                                           |
| ISSEPARATING          | FE和BE是否分离部署           | 此参数用于设置FE和BE是否分离部署。 取值范围： FALSE（否）TRUE（是） 缺省值：FALSE。                                                                                                              |
| HLRSUPPORTEDSEROPFLAG | HLR支持服务类型操作标志         | 此参数用于指定对业务属性是增加、删除或修改。ADD（增加）：在文件中增加一项业务特性列表。MOD（修改）：依据业务属性参数值索引修改业务特性列表。RMV（删除）：依据业务属性参数值索引删除业务特性列表。                                                             |
| HLRSUPPORTEDSERINDEX  | 业务属性参数索引              | 此参数用于指定需要修改或者删除的业务属性参数值索引。 取值范围：0～2147483647。 默认值：无。                                                                                                              |
| HLRSUPPORTEDSERVICES  | 业务属性参数值               | 此参数用于指定增加或修改的业务属性参数值。 取值范围：长度不超过256的字符串。 默认值：无。                                                                                                                   |
| VNFINSTANCEID         | VNF实例ID               | 用于指定VNF实例ID。可以通过该命令定义该参数取值，用于唯一标识一个UDM。 取值范围：长度不超过256的字符串。 默认值：无。                                                                                                 |
| UDRVNFINSTANCEID      | UDR VNF实例ID           | 用于指定UDR网元的VNF实例ID。 取值范围：长度不超过256的字符串。 默认值：无。                                                                                                                      |
| UDRFQDN               | UDR全量域名               | 用于指定UDR网元的全量域名。 取值范围：长度不超过128的字符串。 默认值：无。                                                                                                                         |
| UDRLABEL              | UDR标签                 | 用于指定USCDB网元类型的网元名称，以便于识别。 取值范围：长度不超过256的字符串。 默认值：无。                                                                                                               |
| USEDBSIP              | 网元IP获取方式              | 用于指定网管获取本端网元IP地址列表和远端网元IP地址列表的方式。 取值范围： 0：网管通过DSG相关配置命令（SRVIPADDR/RIPADDR）获取网元IP地址列表和远端网元IP地址列表。1：网管通过DBS相关配置命令（DBSIPADDR/DBSRIPADDR）获取网元IP地址列表和远端网元IP地址列表。 默认值：1 |
| RESERVED1             | 预留参数1                 | 预留参数，长度不超过256的字符串。                                                                                                                                                |
| RESERVED2             | 预留参数2                 | 预留参数，长度不超过256的字符串。                                                                                                                                                |
| AUTOSWITCH            | 自动上报北向开关              | 用于标识是否自动获取“最大可存储的IMSI个数”、“最大可存储的MSISDN个数”、“5G最大用户数”、“5G最大活动用户数”、“4G最大用户数”、“4G最大活动用户数”并上报北向网管系统。 取值范围： YES（是） NO（否） 默认值：NO（否）。 说明：功能开启后，自动上报功能依赖UDM和LCM、BE连接正常。    |
| MAXNUMIMSI            | 最大可存储的IMSI个数          | 此参数用于设置最大可存储的IMSI个数。 取值范围：0～2147483647。 默认值：无。                                                                                                                    |
| MAXNUMMSISDN          | 最大可存储的MSISDN个数        | 此参数用于设置最大可存储的MSISDN个数。 取值范围：0～2147483647。 默认值：无。                                                                                                                  |
| MAXNGCIMSI            | 5G最大用户数               | 此参数用于设置支持的5G最大用户数。 该参数的取值为“eMBB切片BE用户数”Licene授权值，可登录“USCDB MML命令”界面，执行DSP LICRATE命令查询。 取值范围：0～2147483647。 默认值：无。                                                  |
| MAXDYNNGCIMSI         | 5G最大活动用户数             | 此参数用于设置支持的5G最大活动用户数。 该参数的取值为“eMBB切片FE用户数”Licene授权值，可登录“USCDB MML命令”界面，执行DSP LICRATE命令查询。 取值范围：0～2147483647。 默认值：无。                                                |
| MAXEPCIMSI            | 4G最大用户数               | 此参数用于设置支持的4G最大用户数。 该参数的取值为“LTE BE基本软件”Licene授权值，可登录“USCDB MML命令”界面，执行DSP LICRATE命令查询。 取值范围：0～2147483647。 默认值：无。                                                   |
| MAXDYNEPCIMSI         | 4G最大活动用户数             | 此参数用于设置支持的4G最大活动用户数。 该参数的取值为“LTE FE基本软件”Licene授权值，可登录“USCDB MML命令”界面，执行DSP LICRATE命令查询。 取值范围：0～2147483647。 默认值：无。                                                 |

## 使用实例

设置设备名称为“HLR”，设别型号为“HLR9820”，设备硬件平台为“OSTA”，设备供应商为“HuaWei”，已配置2M端口数为“0”，已配置64k端口数为“2”，最大可存储的IMSI个数为“0”，最大可存储的MSISDN个数为“0”，最大可存储的PDP地址数为“0”，备份的HLR编号为“FFFFFFFFFFFFFFF”，最大可存储的外网之间携转的MSISDN个数为“0”，MAP消息处理能力为“0”，最大M3ua链路数为“0”，网元功能类型为“HLR”，HLR支持服务类型操作标志为“MOD”，业务属性参数索引为“1”，业务属性参数值为“100000”，命令如下：

```
SET FUNCCFG: DEVICENAME="HLR", DEVICETYPE="HLR9820", DEVICEHARDWARE="OSTA", DEVICEPROVIDER="HuaWei", PORT2MNUM=0, PORT64KNUM=2, MAXNUMIMSI=0, MAXNUMMSISDN=0, MAXNUMPDPADDRESS=0, BAKUPHLRNUMBER="5", MAXNUMNPCPMSISDN=1000, MAXMAPCAPACITY=2000, MAXNUMM3UALNK=3000, FUNCTYPE=HLR, HLRSUPPORTEDSEROPFLAG=MOD, HLRSUPPORTEDSERINDEX=1, HLRSUPPORTEDSERVICES="100000";
```