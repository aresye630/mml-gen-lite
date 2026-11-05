# 增加RCS业务(ADD HRCSSERVICE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于签约RCS业务。RCS业务为客户提供设备管理功能，通过该功能可以采集手机用户的个人数据，签约后RCS业务可以与IMS-HSS业务共享SIP Digest鉴权的密码和SIFC（Shared Initial Filter Criteria）信息。

## 注意事项

- 需要提前在系统中通过**ADD HSIFCTPL**命令增加模板ID为4097，4099，4353和4609的共享SIFC模板。
- IMPI必须通过**ADD HSDAINF**签约SIP Digest鉴权，SIP Digest鉴权必须通过用户名和密码的形式进行签约。
- 必须首先为IMS用户开户，然后通过**ADD HIMSI**和**ADD HISDN**操作使IMSI、MSISDN与IMPI之间建立关联关系。
- IMS用户下所有的IMPU需要通过**SET HSPSHARE**共享Service Profile。

## 参数说明

| 参数标识           | 参数名称    | 参数说明                                                                                                                          |
|:---------------|:--------|:------------------------------------------------------------------------------------------------------------------------------|
| IMSI           | IMSI    | 用于指定签约RCS业务的用户的IMSI值，该参数必须先由ADD HIMSI操作定义，然后才能在此处索引。IMSI采用E.212格式。例如：460001234567890。 取值范围：长度为6位～15位的十进制数字(0～9)组成的字符串。 默认值：无。 |
| ISDN           | MSISDN  | 用于指定与IMSI关联的MSISDN值，该参数需要先由ADD HISDN操作定义，然后才能在此处索引。ISDN采用E.164格式。例如：861381234567890。 取值范围：长度不超过15位的十进制数字(0～9)组成的字符串。 默认值：无。   |
| WHOLESALEID    | RCS分发标识 | 用于区分不同的RCS服务特性标识，显示用户与第三方的合约关系（例如：网络虚拟的操作者）。 取值范围：长度不超过128位的字符串。 默认值：无。                                                       |
| SEGMENTID      | RCS计费方式 | 用于区分RCS服务特性，表示分配给用户的计费方式。 取值范围：0～10：预付费1：后付费 默认值：无。                                                                           |
| ACPTTERMSTATUS | 条款接受状态  | 用于描述RCS业务接受请求的状态。 取值范围： NOTPROCESSED：未处理。TCACCEPTED：TC接受。TCDENIED：TC拒绝。TCPENDING：TC接受，待激活。NOPERMISSION：TC未准许。 默认值：无。          |

## 使用实例

在开局场景下，为IMS用户开户并签约RCS业务，需要进行如下步骤：

1. 增加共享SIFC模板。

   增加模板ID为4097，4099，4353和4609的共享SIFC模板。

   ```
   ADD HSIFCTPL: TPLID=4097, TPLNAME="SIFCTPL4097", COMMENT="SIFCTPL4097";
   ADD HSIFCTPL: TPLID=4099, TPLNAME="SIFCTPL4099", COMMENT="SIFCTPL4099";
   ADD HSIFCTPL: TPLID=4353, TPLNAME="SIFCTPL4353", COMMENT="SIFCTPL4353";
   ADD HSIFCTPL: TPLID=4609, TPLNAME="SIFCTPL4609", COMMENT="SIFCTPL4609";
   ```
2. 使用用户名和密码形式签约SIP Digest鉴权。

   将“IMPI”参数值设置为“+86123456789@huawei.com”，“用户名称”参数值设置为“+86123456789@huawei.com”，“密码”参数值设置为“123”，“域名”参数值设置为**“huawei.com”，**执行如下命令：

   ```
   ADD HSDAINF: IMPI="+86123456789@huawei.com", HUSERNAME="+86123456789@huawei.com", PWD="*****", REALM="huawei.com";
   ```
3. 给IMS用户开户。

   将“SUBID”参数值设置为“+86123456789”，“IMPI”参数值设置为“+86123456789@huawei.com”，“IMPU”参数值设置为“sip:+86123456789@huawei.com”，执行如下命令：

   ```
   ADD HSUB: SUBID="+86123456789", IMPI="+86123456789@huawei.com", IMPU="sip:+86123456789@huawei.com";
   ```
4. 给IMS用户新增IMPU。

   将“IMPI”参数值设置为“+86123456789@huawei.com”，“IMPU”参数值设置为“sip:impuinfo\_base@huawei.com”，执行如下命令：

   ```
   ADD HIMPU: IMPI="+86123456789@huawei.com", IMPU="sip:impuinfo_base@huawei.com";
   ```
5. 增加IMSI号码，使IMSI与IMPI之间建立关联关系。

   将“IMPI”参数值设置为“+86123456789@huawei.com”，“IMSI”参数值设置为“460009876543210”，执行如下命令：

   ```
   ADD HIMSI: IMPI="+86123456789@huawei.com", IMSI="460009876543210";
   ```
6. 增加MSISDN号码，使IMSI与MSISDN之间建立关联关系。

   将“IMSI”参数值设置为“460009876543210”，“ISDN”参数值设置为“8613955555555”，执行如下命令：

   ```
   ADD HISDN: IMSI="460009876543210", ISDN="8613955555555";
   ```
7. 给IMS用户下所有的IMPU共享Service Profile。

   将“BASEIMPU”参数值设置为“sip:impuinfo\_base@huawei.com”，“IMPU”参数值设置为“sip:+86123456789@huawei.com”，执行如下命令：

   ```
   SET HSPSHARE: BASEIMPU="sip:impuinfo_base@huawei.com", IMPU="sip:+86123456789@huawei.com";
   ```
8. 签约RCS业务。

   将“IMSI”参数值设置为“460009876543210”，“ISDN”参数值设置为“8613955555555”，“分发标识”参数值设置为“1234”，“计费方式”参数值设置为“0”，“条款接受状态”参数值设置为“TCACCEPTED”，执行如下命令：

   ```
   ADD HRCSSERVICE: IMSI="460009876543210", ISDN="8613955555555", WHOLESALEID="1234", SEGMENTID=0, ACPTTERMSTATUS=TCACCEPTED;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释                      | 原因分析                                                          | 处理建议                                                                             |
|----------:|:---------------------------|:--------------------------------------------------------------|:---------------------------------------------------------------------------------|
| 900003466 | 关联的IMS用户未开户或者和IMPI关联关系不存在。 | IMS用户未开户。未执行ADD HIMSI与IMSI建立关联关系。未执行ADD HISDN与MSISDN建立关联关系。   | 通过ADD_HSUB或者ADD_HHSSSUB给IMS用户开户。通过ADD HIMSI与IMSI建立关联关系。通过ADD HISDN与MSISDN建立关联关系。 |
| 900003467 | MSISDN不存在或者未与指定的IMSI关联。    | MSISDN输入错误。未执行ADD HISDN与IMSI建立关联关系。                           | 重新输入MSISDN。通过ADD HISDN与IMSI建立关联关系。                                               |
| 900003468 | Digest鉴权的密码不存在。            | 未签约SIP Digest鉴权。                                              | 通过ADD_HSDAINF签约SIP Digest鉴权。                                                     |
| 900003469 | SPID不存在。                   | 说明用户没有号，只有卡。                                                  | 通过ADD_HIMPU签约IMPU号码。                                                             |
| 900003471 | RCS业务已经存在。                 | 已签约RCS业务。                                                     | —                                                                                |
| 900003523 | 密钥丢失                       | 当SET MAPSERV命令中的“随机密钥默认ID”参数为非0，“随机密钥默认ID”参数对应的随机密钥材料不存在或不完整。 | 联系华为技术支持处理。                                                                      |