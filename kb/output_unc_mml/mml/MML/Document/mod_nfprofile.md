# 修改NF实例概述信息（MOD NFPROFILE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBC、CBCF**

该命令用于修改NF实例的概述信息。对于已向NRF注册过的NF实例，使用该命令修改NF实例的概述信息后，将会触发其向NRF发起更新流程。

## 注意事项

- 该命令执行后立即生效。

- 使用该命令修改NF实例的概述信息后，将会向NRF发起更新流程。
- NF状态不支持选择Suspend状态。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:---------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称     | 可选必选说明：必选参数  参数含义：本参数用于指定NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则： 本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，AMF_Instance_0。本参数来源于ADD NFUUID命令中的“NF实例名称”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NFSTATUS       | NF状态       | 可选必选说明：可选参数  参数含义：本参数用于指定NF状态。  数据来源：全网规划 取值范围： “Invalid（Invalid）”：表示当前NF处于无效态，如果配置成该值，NF注册的时候将不携带任何状态给NRF，在NF发现过程中，NRF也不会选择此类NF。“Registered（Registered）”：表示当前NF处于注册态。在NF发现过程中，NRF只会选择该状态下的NF。“Suspend（Suspend）”：表示当前NF处于挂起态，与NRF之间不再保持心跳，N次心跳超时之后（NRF上可配置，默认为3次），NRF上的此NF的状态即变化成Suspend状态。“Undiscoverable（Undiscoverable）”：表示当前NF处于不可被服务发现状态，与NRF之间的还会保持心跳，且心跳消息会携带此状态。当NF处于运维状态下，比如正在进行用户迁移等，不希望在NF发现流程中被选中时，可以置为此状态，迁移完毕后通过该命令对应的MOD命令修改为注册态即可。  默认值：无  配置原则：无                                                                                                                                                                                                                 |
| HTTPLEIDX      | http地址实例标识 | 可选必选说明：可选参数  参数含义：本参数用于指定http地址实例标识。  数据来源：全网规划  取值范围：整数类型，取值范围是0~255。  默认值：无  配置原则：  该参数已不再使用，请使用ADD SBIAPLE配置HTTP本端实体组标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| FQDN           | 域名         | 可选必选说明：可选参数  参数含义：本参数用于指定NF域名信息。本参数指定的域名中可以不包含PLMN信息，主要用于本网内的域名查询场景。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则： FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。不能用“-”或者“.”开头和结尾，中间不能出现连续的两个“.”。例如amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org。此参数对AMF无效。NF注册时的FQDN只以AMF配置ADD AMFINFO的AMF名称为准。此参数对SMF无效。NF注册时的FQDN只以SMF配置ADD SMFINFO的SMF名称为准。输入单空格将删除该参数已有配置项。                                                                                                                                                                                                                                                                   |
| INTERPLMNFQDN  | PLMN间域名    | 可选必选说明：可选参数  参数含义：本参数用于指定PLMN间域名。当NF涉及跨PLMN网络间的NF发现时，需要为NF配置“PLMN间域名”。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则： INTERPLMNFQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线“_”。不能用“-”或者“_”或者“.”开头和结尾，中间不能出现连续的两个“.”。例如，amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org。此参数对AMF无效。AMF注册时NFPROFILE中携带的INTERPLMNFQDN只以ADD AMFINFO中的配置为准。此参数对SMF无效。SMF注册时NFPROFILE中携带的INTERPLMNFQDN只以ADD SMFINFO中的配置为准。输入单空格将删除该参数已有配置项。                                                                                                                                                                                                             |
| CAPACITY       | 容量         | 可选必选说明：可选参数  参数含义：本参数用于指定NF的相对权重（与其他同类型NF实例相比）。特别地，如果NF容量的绝对值不超过本参数的取值范围，那么本参数可以直接取用容量绝对值。例如AMF可接入的用户数是50000，那么该AMF的容量就可以用50000表示。  数据来源：全网规划  取值范围：整数类型，取值范围是0~65535。值越大表示容量越大。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRIORITY       | 优先级        | 可选必选说明：可选参数  参数含义：本参数用于指定NF的优先级（与其他同类型NF实例相比）。在NF选择过程中，NF会选择高优先级的NF，如果两个或多个NF的优先级一样，NF则会根据“容量”做进一步的判断。  数据来源：全网规划  取值范围：整数类型，取值范围是0~65535。值越小优先级越高。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LOAD           | 负载         | 可选必选说明：可选参数  参数含义：本参数用于指定NF的负载。NRF可能会将此参数作为NF选择的依据。  数据来源：全网规划  取值范围：整数类型，取值范围是0~100。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| LOCALITY       | 位置信息       | 可选必选说明：可选参数  参数含义：本参数用于指定NF的位置描述信息，比如NF所在的地域信息描述等。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~150。  默认值：无  配置原则：  本参数的构成字符建议是字母A～Z或a～z、数字0～9、中划线“-”、和下划线"_"例如，Shanghai-DataCenter。  在中国区组网，该参数建议配置为点分格式：“大区标识.数据中心标识.资源池标识”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ALLOWEDNFTYPES | 支持的NF类型    | 可选必选说明：可选参数  参数含义：本参数用于指定本NF实例向NRF注册完成后，在后续的NF发现流程中能够访问本NF实例的NF类型。如果不配置，表示允许所有类型的NF访问。  数据来源：全网规划 取值范围： AllowNfINVALID（AllowNfINVALID）AllowNfNRF（AllowNfNRF）AllowNfUDM（AllowNfUDM）AllowNfAMF（AllowNfAMF）AllowNfSMF（AllowNfSMF）AllowNfAUSF（AllowNfAUSF）AllowNfNEF（AllowNfNEF）AllowNfPCF（AllowNfPCF）AllowNfSMSF（AllowNfSMSF）AllowNfNSSF（AllowNfNSSF）AllowNfUDR（AllowNfUDR）AllowNfLMF（AllowNfLMF）AllowNfGMLC（AllowNfGMLC）AllowNf5G_EIR（AllowNf5G_EIR）AllowNfSEPP（AllowNfSEPP）AllowNfUPF（AllowNfUPF）AllowNfN3IWF（AllowNfN3IWF）AllowNfAF（AllowNfAF）AllowNfUDSF（AllowNfUDSF）AllowNfBSF（AllowNfBSF）AllowNfCHF（AllowNfCHF）AllowNfNWDAF（AllowNfNWDAF）AllowNfMAX（AllowNfMAX）  默认值：无  配置原则：无 |

## 使用实例

运营商A需要修改NFINSTANCENAME为AMF\_Instance\_0的NF实例，将PRIORITY改为20。

```
MOD NFPROFILE: NFINSTANCENAME="AMF_Instance_0", PRIORITY=20;
```