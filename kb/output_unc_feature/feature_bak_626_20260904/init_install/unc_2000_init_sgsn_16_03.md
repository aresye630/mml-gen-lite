# 配置2G移动性管理

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

本操作指导介绍在运行网络中配置移动性管理特性的操作过程。

2G移动性管理能使2G MS附着到SGSN，是MS获取网络服务的前提。SGSN对其天然支持。在3G没有完全替代2G时，每台SGSN均需要支持2G移动性管理功能。

系统为移动性管理通用参数提供了默认值，这些默认值为推荐值。用户也可以根据实际网络情况针对部分选项进行调整，使SGSN在本网络中更高效工作。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

数据

| 类别             | 参数名称                     | 取值样例                    | 取值样例.1                  | 获取方法            | 说明              |
|:---------------|:-------------------------|:------------------------|:------------------------|:----------------|:----------------|
| ADD HPLMN      | 移动国家码（MCC）               | 460                     | 460                     | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 移动网号（MNC）                | 00                      | 00                      | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 国家码（CC）                  | 86                      | 86                      | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 是否允许（SM业务SM）             | YES                     | YES                     | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 最大承载数（MAXSMNUM）          | 11                      | 11                      | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 是否允许（SMS业务SMS）           | YES                     | YES                     | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 协议类型（S5S8TYPE）           | GTP                     | GTP                     | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 运营商名称（PLMNN）             | name                    | name                    | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| SET GMM        | T3322（s）（T3322）          | 6                       | 6                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | N3322（times）（N3322）      | 4                       | 4                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | T3350（s）（T3350）          | 6                       | 6                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | N3350（times）（N3350）      | 4                       | 4                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | T3360（s）（T3360）          | 6                       | 6                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | N3360（times）（N3360）      | 4                       | 4                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | T3370（s）（T3370）          | 6                       | 6                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | N3370（times）（N3370）      | 4                       | 4                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | T3313（s）（T3313）          | 6                       | 6                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | N3313（times）（N3313）      | 2                       | 2                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | 重寻呼间隔递增值（s）（PAGINGDELTA） | 0                       | 0                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | 准备定时器（s）（RDYTMR）         | 44                      | 44                      | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | MS可达定时器（min）（MSRCHTMR）   | 54                      | 54                      | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | 保留参数（IMDTCHTMR）          | 58                      | 58                      | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | T3定时器（s）（T3）             | 0                       | 0                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | 优先级（PRT）                 | 0                       | 0                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| SET GMM        | 保留参数2（RDTDELTA）          | 0                       | 0                       | 参见“水平网设LLD文档 ”。 | 配置2G移动性管理定时器参数。 |
| ADD GBAUTHCIPH | IMSI前缀（IMSIPRE）          | 460001                  | 460001                  | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能。      |
| ADD GBAUTHCIPH | 安全策略（SECPLC）             | AUTHANDPROTECTED        | AUTHANDPROTECTED        | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能。      |
| ADD GBAUTHCIPH | 加密算法（CIPHALG）            | GEA_3-1&GEA_2-1&GEA_1-1 | GEA_3-1&GEA_2-1&GEA_1-1 | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能。      |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 增加归属PLMN配置信息。

   ```
   ADD HPLMN: MCC="460", MNC="00", CC="86", SM=YES, MAXSMNUM=11, SMS=YES,S5S8TYPE=GTP, PLMNN="name";
   ```
3. **可选：**配置2G移动性管理定时器参数。

   ```
   SET GMM: T3322=6, N3322=4, T3350=6, N3350=4, T3360=6, N3360=4, T3370=6, N3370=4, T3313=6, N3313=2, PAGINGDELTA=0, RDYTMR=44, PRDTMR=54, MSRCHTMR=58, IMDTCHTMR=0, T3=10, PRT=0, RDTDELTA=0;
   ```
4. **可选：**启用鉴权和加密功能。

   ```
   ADD GBAUTHCIPH: IMSIPRE="460001",SECPLC=AUTHANDPROTECTED, CIPHALG=GEA_3-1&GEA_2-1&GEA_1-1;
   ```