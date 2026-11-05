# 查询用户数据(LST SUBDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 参考信息

## 命令功能

**须知** 

本命令属于高危命令，执行不当会增加数据库的负荷，引起系统过载，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于查询内存库中满足指定条件的用户数据，查询结果以文本格式保存在PGW如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。例如，当前系统HLRSN为“001”，操作员名称为“admin”，则存储查询结果的目录为：“/opt/pgw/pgwtmpfile/001admin”。查询结果的文件名格式为“查询对象-时间-序列号.txt”，例如：CountOfAuc-2010-03-01-05-24-25-064.txt。

查询结果可以通过PGW Web LMT上的“文件管理器”下载到本地。

**说明** 

- **SET MAPSERV**命令中的“LST命令导出文件压缩控制”取值不为“0”且**LST SUBDATA**查询结果大于或者等于“LST命令导出文件压缩控制”设置的取值时，查询结果的文件格式为“查询对象-时间-序列号.tar.gz”。**LST SUBDATA**命令报文中查询结果的文件格式固定显示为“查询对象-时间-序列号.txt”。
- 查询结果包含用户的个人数据，如：IMSI、MSISDN等，因此您需遵循所适用国家的法律或贵公司的用户隐私政策并采取足够的措施，以确保用户的个人数据受到充分的保护，并严格控制查询结果文件的访问权限。
- 在从运营商网络获取数据前，必须要获得运营商的授权。
- 若需从运营商网络中获取必要的数据，需要运营商维护人员对其中的个人数据进行匿名化处理，匿名化后的数据由运营商维护人员审核后提供，以防止个人数据泄露。匿名化处理工具可以在http://support.huawei.com/网站获取，获取方法请参见产品手册“匿名化工具安全策略”页面。

## 注意事项

- 执行该命令会消耗较多的系统资源，影响系统性能，请在话务量较低的时候执行。
- 当“查询条件”为下列任一值时，“起始参数”和“结束参数”长度必须相等。
  - RangeByIMSI（根据IMSI号段查询用户数据）
  - RangeByMSISDN（根据MSISDN号段查询用户数据）
  - RoamAtCSRangeByVLR（根据VLR号段查询CS域漫游的用户数据）
  - RoamAtCSRangeByIMSI（根据IMSI号段查询CS域漫游的用户数据）
  - RoamAtCSRangeByMSISDN（根据MSISDN号段查询CS域漫游的用户数据）
  - RoamAtPSRangeBySGSN（根据SGSN号段查询PS域漫游的用户数据）
  - RoamAtPSRangeByIMSI（根据IMSI号段查询PS域漫游的用户数据）
  - RoamAtPSRangeByMSISDN（根据MSISDN号段查询PS域漫游的用户数据）
  - NotRoamAtCSRangeByIMSI（根据IMSI号段查询CS域未漫游的用户数据）
  - NotRoamAtCSRangeByMSISDN（根据MSISDN号段查询CS域未漫游的用户数据）
  - NotRoamAtPSRangeByIMSI（根据IMSI号段查询PS域未漫游的用户数据）
  - NotRoamAtPSRangeByMSISDN（根据MSISDN号段查询PS域未漫游的用户数据）
  - MimsiRangeByIMSI（根据IMSI号段查询多IMSI的用户数据）
  - RoamAtMMERangeByIMSI（根据IMSI号段查询MME漫游用户数）
  - RoamAtMMERangeByMSISDN（根据MSISDN号段查询MME漫游用户数）
- 该命令不允许进行批操作。
- 建议在执行本命令前先登录“系统管理”页面，执行**DSP EXPTASK**命令查询所有导出任务的状态，若当前已经有两个任务处在“running”状态，建议当这两个任务的状态为“COMPLETED”后再执行本命令。
- 执行本命令前，请确保已通过“USCDB MML命令”界面执行**ADD SRVIPADDR**命令增加DMA类型的IP地址。
- 当数据量过大时，执行本命令前可以通过配置软参**“EXPORTSPEED（导出速度）”**值为“500”来提高用户数据查询效率，导出完成后恢复原配置。当前导出速度可以通过****LST INSP****命令查询。
- 该命令只能导出2G以内大小的文件。
- 可以在“系统管理”页面执行**DSP EXPTASK**命令查询该命令导出任务的状态。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                    |
|:---------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESULT   | 查询对象   | 用于标识查询用户数据的类型，具体查询对象请参见表1。                                                                                                                                                                                                              |
| COND     | 查询条件   | 用于标识查询用户数据的条件，具体查询条件请参见表1。                                                                                                                                                                                                              |
| PARA1    | 起始IMSI | 用于标识查询用户数据的范围起始值，具体起始参数请参见表1。                                                                                                                                                                                                           |
| PARA2    | 结束IMSI | 用于标识查询用户数据的范围结束值，具体结束参数请参见表1。                                                                                                                                                                                                           |
| SORTSUPP | 支持排序   | 仅当本命令中的“查询对象”参数为“DataOfSub”、“DataOfAuc”、“DataOfSubRoamAtCS”、“DataOfSubRoamAtPS”、“DataOfSubNotRoamAtCS”、“DataOfSubNotRoamAtPS”、“DataOfMimsi”或“DataOfEpsSub”时该参数有效，用于标识查询用户数据时是否排序。 取值范围：FALSE：查询数据时不做排序，用于提升查询速度。TRUE：查询数据时做排序。 默认值：TRUE |

## 使用实例

1. 查询某个MSISDN号段的开户用户数目，起始MSISDN为“4604567890000”，结束MSISDN为“4604567899999”：

   ```
   LST SUBDATA: RESULT=CountOfSub, COND=RangeByMSISDN, PARA1="4604567890000", PARA2="4604567899999";
   ```

   ```
   %%LST SUBDATA: RESULT=CountOfSub, COND=RangeByMSISDN, PARA1="4604567890000", PARA2="4604567899999";%%
   RETCODE = 0 SUCCESS0001:操作成功

   CountOfSub-2012-05-01-05-24-25-064.txt

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询本HLR内CS域漫游的用户总数：

   ```
   LST SUBDATA:RESULT=CountOfSubRoamAtVLR, COND=RoamAtCS;
   ```

   ```
   %%LST SUBDATA:RESULT=CountOfSubRoamAtVLR, COND=RoamAtCS;%%
   RETCODE = 0 SUCCESS0001:操作成功

   CountOfSubRoamAtVLR-2012-03-01-05-22-25-065.txt

   Total count = 1

   There is together 1 report

   ---    END
   ```
3. 查询某个MSISDN号段的EPS用户数目，起始MSISDN为“4604567890000”，结束MSISDN为“4604567899999”：

   ```
   LST SUBDATA: RESULT=CountOfEpsSub, COND=RangeByMSISDN, PARA1="4604567890000", PARA2="4604567899999";
   ```

   ```
   %%LST SUBDATA: RESULT=CountOfEpsSub, COND=RangeByMSISDN, PARA1="4604567890000", PARA2="4604567899999";%%
   RETCODE = 0 SUCCESS0001:操作成功

   CountOfEpsSub-2012-03-04-05-24-25-059.txt

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 参考信息

| 查询对象                                                                                                             | 查询条件                                            | 起始参数                                   | 结束参数                                   |
|:-----------------------------------------------------------------------------------------------------------------|:------------------------------------------------|:---------------------------------------|:---------------------------------------|
| CountOfSub（开户用户数目） DataOfSub（开户用户的主IMSI、MSISDN号码）                                                                | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfSub（开户用户数目） DataOfSub（开户用户的主IMSI、MSISDN号码）                                                                | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSub（开户用户数目） DataOfSub（开户用户的主IMSI、MSISDN号码）                                                                | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSub（开户用户数目） DataOfSub（开户用户的主IMSI、MSISDN号码）                                                                | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfAuc（鉴权数据数目） DataOfAuc（鉴权数据的IMSI、鉴权算法）                                                                     | AllAuc（所有鉴权数据）                                  | -                                      | -                                      |
| CountOfAuc（鉴权数据数目） DataOfAuc（鉴权数据的IMSI、鉴权算法）                                                                     | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfAuc（鉴权数据数目） DataOfAuc（鉴权数据的IMSI、鉴权算法）                                                                     | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubRoamAtCS（CS域漫游用户数目） CountOfSubRoamAtVLR（CS域用户漫游在各VLR漫游的数目） DataOfSubRoamAtCS（漫游用户的主IMSI、MSISDN和所在的VLR） | RoamAtCS（CS域漫游总数）                               | -                                      | -                                      |
| CountOfSubRoamAtCS（CS域漫游用户数目） CountOfSubRoamAtVLR（CS域用户漫游在各VLR漫游的数目） DataOfSubRoamAtCS（漫游用户的主IMSI、MSISDN和所在的VLR） | RoamAtCSRangeByVLR（根据VLR号段查询CS域漫游用户数）           | 起始VLR 取值范围：6～15位十进制数字组成的字符串。 默认值：无。    | 结束VLR 取值范围：6～15位十进制数字组成的字符串。 默认值：无。    |
| CountOfSubRoamAtCS（CS域漫游用户数目） CountOfSubRoamAtVLR（CS域用户漫游在各VLR漫游的数目） DataOfSubRoamAtCS（漫游用户的主IMSI、MSISDN和所在的VLR） | RoamAtCSRangeByIMSI（根据IMSI号段查询CS域漫游用户数）         | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSubRoamAtCS（CS域漫游用户数目） CountOfSubRoamAtVLR（CS域用户漫游在各VLR漫游的数目） DataOfSubRoamAtCS（漫游用户的主IMSI、MSISDN和所在的VLR） | RoamAtCSRangeByMSISDN（根据MSISDN号段查询CS域漫游用户数）     | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubRoamAtCS（CS域漫游用户数目） CountOfSubRoamAtVLR（CS域用户漫游在各VLR漫游的数目） DataOfSubRoamAtCS（漫游用户的主IMSI、MSISDN和所在的VLR） | RoamAtCSRangeByHLRSN（根据HLRSN查询CS域漫游用户数）         | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubRoamAtPS（PS域漫游用户数目） CountOfSubRoamAtSGSN（用户漫游在各SGSN漫游的数目） DataOfSubRoamAtPS（漫游用户的主IMSI、MSISDN和所在的SGSN） | RoamAtPS（PS域漫游总数）                               | -                                      | -                                      |
| CountOfSubRoamAtPS（PS域漫游用户数目） CountOfSubRoamAtSGSN（用户漫游在各SGSN漫游的数目） DataOfSubRoamAtPS（漫游用户的主IMSI、MSISDN和所在的SGSN） | RoamAtPSRangeBySGSN（根据SGSN号段查询PS域漫游用户数）         | 起始SGSN号码 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 | 结束SGSN号码 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubRoamAtPS（PS域漫游用户数目） CountOfSubRoamAtSGSN（用户漫游在各SGSN漫游的数目） DataOfSubRoamAtPS（漫游用户的主IMSI、MSISDN和所在的SGSN） | RoamAtPSRangeByIMSI（根据IMSI号段查询PS域漫游用户数）         | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSubRoamAtPS（PS域漫游用户数目） CountOfSubRoamAtSGSN（用户漫游在各SGSN漫游的数目） DataOfSubRoamAtPS（漫游用户的主IMSI、MSISDN和所在的SGSN） | RoamAtPSRangeByMSISDN（根据MSISDN号段查询PS域漫游用户数）     | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubRoamAtPS（PS域漫游用户数目） CountOfSubRoamAtSGSN（用户漫游在各SGSN漫游的数目） DataOfSubRoamAtPS（漫游用户的主IMSI、MSISDN和所在的SGSN） | RoamAtPSRangeByHLRSN（根据HLRSN查询PS域漫游用户数）         | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubNotRoamAtCS（CS域未漫游用户数目） DataOfSubNotRoamAtCS（CS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtCS（CS域未漫游总数）                           | -                                      | -                                      |
| CountOfSubNotRoamAtCS（CS域未漫游用户数目） DataOfSubNotRoamAtCS（CS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtCSRangeByIMSI（根据IMSI号段查询CS域未漫游用户数）     | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSubNotRoamAtCS（CS域未漫游用户数目） DataOfSubNotRoamAtCS（CS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtCSRangeByMSISDN（根据MSISDN号段查询CS域未漫游用户数） | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubNotRoamAtCS（CS域未漫游用户数目） DataOfSubNotRoamAtCS（CS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtCSRangeByHLRSN（根据HLRSN查询CS域未漫游用户数）     | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubNotRoamAtPS（PS域未漫游用户数目） DataOfSubNotRoamAtPS（PS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtPS（PS域未漫游总数）                           | -                                      | -                                      |
| CountOfSubNotRoamAtPS（PS域未漫游用户数目） DataOfSubNotRoamAtPS（PS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtPSRangeByIMSI（根据IMSI号段查询PS域未漫游用户数）     | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSubNotRoamAtPS（PS域未漫游用户数目） DataOfSubNotRoamAtPS（PS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtPSRangeByMSISDN（根据MSISDN号段查询PS域未漫游用户数） | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubNotRoamAtPS（PS域未漫游用户数目） DataOfSubNotRoamAtPS（PS域未漫游用户的主IMSI、MSISDN）                                    | NotRoamAtPSRangeByHLRSN（根据HLRSN查询PS域未漫游用户数）     | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfMimsi（多IMSI用户数目） DataOfMimsi（多IMSI用户的主IMSI、MSISDN、多IMSI类型）                                                | AllMimsi （所有多IMSI总数）                            | -                                      | -                                      |
| CountOfMimsi（多IMSI用户数目） DataOfMimsi（多IMSI用户的主IMSI、MSISDN、多IMSI类型）                                                | MimsiRangeByIMSI（根据IMSI号段查询多IMSI用户数）            | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfMimsi（多IMSI用户数目） DataOfMimsi（多IMSI用户的主IMSI、MSISDN、多IMSI类型）                                                | MimsiRangeByHLRSN（根据HLRSN查询多IMSI用户数）            | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubInMWD（短消息中心地址以及对应的用户数目）                                                                                | AllSCAdd （所有短消息中心地址）                            | -                                      | -                                      |
| CountOfEpsSub（EPS用户数目） DataOfEpsSub（EPS用户的IMSI、MSISDN号码）                                                         | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfEpsSub（EPS用户数目） DataOfEpsSub（EPS用户的IMSI、MSISDN号码）                                                         | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfEpsSub（EPS用户数目） DataOfEpsSub（EPS用户的IMSI、MSISDN号码）                                                         | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfEpsSub（EPS用户数目） DataOfEpsSub（EPS用户的IMSI、MSISDN号码）                                                         | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfVoLTESub（VoLTE用户数目）                                                                                       | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfVoLTESub（VoLTE用户数目）                                                                                       | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfVoLTESub（VoLTE用户数目）                                                                                       | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfVoLTESub（VoLTE用户数目）                                                                                       | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfVoWIFISub（VoWIFI用户数目）                                                                                     | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfVoWIFISub（VoWIFI用户数目）                                                                                     | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfVoWIFISub（VoWIFI用户数目）                                                                                     | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfVoWIFISub（VoWIFI用户数目）                                                                                     | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfVoWIFIandVoLTESub（既是VoWIFI用户又是VoLTE用户数目）                                                                  | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfVoWIFIandVoLTESub（既是VoWIFI用户又是VoLTE用户数目）                                                                  | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfVoWIFIandVoLTESub（既是VoWIFI用户又是VoLTE用户数目）                                                                  | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfVoWIFIandVoLTESub（既是VoWIFI用户又是VoLTE用户数目）                                                                  | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSubRoamAtMME（EPS域用户漫游在各MME下漫游的数目）                                                                         | RoamAtMME（MME漫游用户总数）                            | -                                      | -                                      |
| CountOfSubRoamAtMME（EPS域用户漫游在各MME下漫游的数目）                                                                         | RoamAtMMERangeByIMSI（根据IMSI号段查询MME漫游用户数）        | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSubRoamAtMME（EPS域用户漫游在各MME下漫游的数目）                                                                         | RoamAtMMERangeByMSISDN（根据MSISDN号段查询MME漫游用户数）    | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSubRoamAtMME（EPS域用户漫游在各MME下漫游的数目）                                                                         | RoamAtMMERangeByHLRSN（根据HLRSN查询MME漫游用户数）        | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |
| CountOfSASub（SA开户用户数目） DataOfSASub（SA开户用户的主IMSI、MSISDN号码）                                                        | AllSub（所有开户用户）                                  | -                                      | -                                      |
| CountOfSASub（SA开户用户数目） DataOfSASub（SA开户用户的主IMSI、MSISDN号码）                                                        | RangeByIMSI（根据IMSI号段）                           | 起始IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   | 结束IMSI 取值范围：6～15位十进制数字组成的字符串。 默认值：无。   |
| CountOfSASub（SA开户用户数目） DataOfSASub（SA开户用户的主IMSI、MSISDN号码）                                                        | RangeByMSISDN（根据MSISDN号段）                       | 起始MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 | 结束MSISDN 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |
| CountOfSASub（SA开户用户数目） DataOfSASub（SA开户用户的主IMSI、MSISDN号码）                                                        | RangeByHLRSN（根据HLRSN）                           | 起始HLRSN 取值范围：1～255。 默认值：无。             | 结束HLRSN 取值范围：1～255。 默认值：无。             |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释          | 原因分析                      | 处理建议                                      |
|:--------|:---------------|:--------------------------|:------------------------------------------|
| ERR1004 | 无效的参数值         | “起始参数”和“结束参数”的取值与表1的要求不符。 | 根据实际情况，重新输入“起始参数”和“结束参数”的取值，确保其取值符合要求。    |
| ERR1026 | 结束参数应大于/晚于起始参数 | “起始参数”的取值大于或晚于“结束参数”的取值。  | 根据实际情况，重新输入参数，并确保“起始参数”的取值小于或早于“结束参数”的取值。 |