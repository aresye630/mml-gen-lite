# 配置SGSN基础数据

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

执行该任务的场景如下：

- 开局
- 扩容

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别              | 参数名称                    | 取值样例     | 获取方法   | 说明                          |
|:----------------|:------------------------|:---------|:-------|:----------------------------|
| SET SYS         | 系统描述（DESC）              | HCGPBER1 | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 系统标识（ID）                | 0        | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 系统名称（NM）                | HCGPBER1 | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 服务描述（SRV）               | prsBER1  | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 移动网号（MNC）               | 00       | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 移动国家码（MCC）              | 460      | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 协议版本（PROVER）            | R4       | 整网规划   | 配置系统基本信息。                   |
| SET SYS         | 核心网标识（CNID）             | 0        | 整网规划   | 配置系统基本信息。                   |
| ADD HPLMN       | 移动国家码（MCC）              | 460      | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 移动网号（MNC）               | 00       | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 国家码（CC）                 | 86       | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 是否允许SM业务（SM）            | YES      | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 最大承载数（MAXSMNUM）         | 7        | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 是否允许SMS业务（SMS）          | NO       | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 协议类型（S5S8TYPE）          | GTP      | 整网规划   | 配置PLMN。                     |
| ADD HPLMN       | 运营商名称（PLMNN）            | noname_1 | 整网规划   | 配置PLMN。                     |
| ADD CONNECTPLMN | 移动国家码（MCC）              | 460      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 移动网号（MNC）               | 00       | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 匹配IMSI（MATCHIMSI）       | 1234     | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 国家码（CC）                 | 860      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 是否允许SM业务（SM）            | YES      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | SMS（是否允许SMS业务）          | YES      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 是否允许纠正短消息中心（SMSCR）      | NO       | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 专属互连PLMN（EXCLUSIVEPLMN） | YES      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |
| ADD CONNECTPLMN | 是否允许紧急呼叫业务（EMCBS）       | YES      | 整网规划   | 配置互联PLMN，用于支持不同PLMN之间的用户漫游。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置系统基本信息。

   ```
   SET SYS: DESC="HCGPBER1", ID=0, NM="HCGPBER1", SRV="prsBER1", MNC="00",MCC="460",  PROVER=R4, CNID=0;
   ```
3. 配置Home PLMN。

   ```
   ADD HPLMN:MCC="460",MNC="00",CC="86",SM=YES,MAXSMNUM=7,SMS=NO,S5S8TYPE=GTP,PLMNN="noname_1";
   ```
4. **可选：**配置互联PLMN，用于支持不同PLMN之间的用户漫游。

   ```
   ADD CONNECTPLMN: MCC="460", MNC="00", MATCHIMSI="1234", CC="860", SM=YES, SMS=YES, SMSCR=NO, EXCLUSIVEPLMN=YES, EMCBS=YES;
   ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 执行以下命令，查询具体配置是否与数据规划表中的值一致。

   - LST SYS
   - LST HPLMN
   - LST CONNECTPLMN