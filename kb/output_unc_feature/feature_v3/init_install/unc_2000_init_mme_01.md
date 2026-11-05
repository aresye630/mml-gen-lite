# 配置MME基础数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

执行该任务的场景如下：

* 开局
* 扩容

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET SYS** | 系统描述（DESC） | HCGPBER1 | 整网规划 | 配置系统基本信息。 |
|  | 系统标识（ID） | 0 |  |  |
|  | 系统名称（NM） | HCGPBER1 |  |  |
|  | 服务描述（SRV） | prsBER1 |  |  |
|  | 移动网号（MNC） | 00 |  |  |
|  | 移动国家码（MCC） | 123 |  |  |
|  | 协议版本（PROVER） | R4 |  |  |
|  | 核心网标识（CNID） | 0 |  |  |
| **ADD HPLMN** | 移动国家码（MCC） | 123 |  | 配置PLMN。 |
|  | 移动网号（MNC） | 00 |  |  |
|  | 国家码（CC） | 86 |  |  |
|  | 是否允许SM业务（SM） | YES |  |  |
|  | 最大承载数（MAXSMNUM） | 7 |  |  |
|  | 是否允许SMS业务（SMS） | NO |  |  |
|  | 协议类型（S5S8TYPE） | GTP |  |  |
|  | 运营商名称（PLMNN） | noname\_1 |  |  |
| **ADD CONNECTPLMN** | 移动国家码（MCC） | 123 |  | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
|  | 移动网号（MNC） | 00 |  |  |
|  | 匹配IMSI（MATCHIMSI） | 1234 |  |  |
|  | 国家码（CC） | 860 |  |  |
|  | 是否允许SM业务（SM） | YES |  |  |
|  | SMS（是否允许SMS业务） | YES |  |  |
|  | 是否允许纠正短消息中心（SMSCR） | NO |  |  |
|  | 专属互连PLMN（EXCLUSIVEPLMN） | YES |  |  |
|  | 是否允许紧急呼叫业务（EMCBS） | TES |  |  |
| **ADD MMEID** | 移动国家码（MCC） | 123 |  | 配置MMEID。 |
|  | 移动网号（MNC） | 00 |  |  |
|  | MME组识别码（MMEGI） | 8001 |  |  |
|  | MME编码（起始值）（MMEC） | 01 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置系统基本信息。

   ```
   SET SYS: DESC="HCGPBER1", ID=0, NM="HCGPBER1", SRV="prsBER1", MNC="00",MCC="123",  PROVER=R4, CNID=0;
   ```
3. 配置Home PLMN。

   ```
   ADD HPLMN:MCC="123",MNC="00",CC="86",SM=YES,MAXSMNUM=7,SMS=NO,S5S8TYPE=GTP,PLMNN="noname_1";
   ```
4. **可选：**配置互联PLMN，用于支持不同PLMN之间的用户漫游。

   ```
   ADD CONNECTPLMN: MCC="123", MNC="00", MATCHIMSI="1234", CC="860", SM=YES, SMS=YES, SMSCR=NO, EXCLUSIVEPLMN=YES, EMCBS=YES;
   ```
5. 配置MMEID。

   ```
   ADD MMEID:MCC="123",MNC="00",MMEGI="8001",MMEC="01";
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 执行以下命令，查询具体配置是否与数据规划表中的值一致。

   * LST SYS
   * LST HPLMN
   * LST CONNECTPLMN
   * LST MMEID

版权所有 © 华为技术有限公司
