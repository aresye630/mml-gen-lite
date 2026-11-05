# 配置3G移动性管理

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

本操作指导介绍在运行网络中配置移动性管理特性的操作过程。

3G移动性管理能使3G MS附着到SGSN，是MS获取网络服务的前提。在网络中存在3G MS时，每台SGSN均需要支持3G移动性管理功能。

系统为移动性管理通用参数提供了默认值，这些默认值为推荐值。用户也可以根据实际网络情况针对部分选项进行调整，使SGSN在本网络中更高效工作。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

数据

| 类别             | 参数名称                         | 取值样例                          | 取值样例.1                        | 获取方法            | 说明              |
|:---------------|:-----------------------------|:------------------------------|:------------------------------|:----------------|:----------------|
| ADD IUPAGING   | 位置区标识（LAI）                   | 460000001                     | 460000001                     | 参见“水平网设LLD文档 ”。 | 增加3G寻呼数据。       |
| ADD IUPAGING   | 路由区编码（RAC）                   | 01                            | 01                            | 参见“水平网设LLD文档 ”。 | 增加3G寻呼数据。       |
| ADD IUPAGING   | RNC索引（RNCINDEX）              | 0                             | 0                             | 参见“水平网设LLD文档 ”。 | 增加3G寻呼数据。       |
| ADD HPLMN      | 移动国家码（MCC）                   | 460                           | 460                           | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 移动网号（MNC）                    | 00                            | 00                            | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 国家码（CC）                      | 68                            | 68                            | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 是否允许（SM业务SM）                 | YES                           | YES                           | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 最大承载数（MAXSMNUM）              | 11                            | 11                            | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 是否允许（SMS业务SMS）               | YES                           | YES                           | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 协议类型（S5S8TYPE）               | GTP                           | GTP                           | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| ADD HPLMN      | 运营商名称（PLMNN）                 | name                          | name                          | 参见“水平网设LLD文档 ”。 | 增加归属PLMN配置信息。   |
| SET PMM        | T3322（s）（T3322）              | 6                             | 6                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | N3322（times）（N3322）          | 4                             | 4                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | T3350（s）（T3350）              | 6                             | 6                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | N3350（times）（N3350）          | 4                             | 4                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | T3360（s）（T3360）              | 6                             | 6                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | N3360（times）（N3360）          | 4                             | 4                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | T3370（s）（T3370）              | 6                             | 6                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | N3370（times）（N3370）          | 4                             | 4                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | T3313（s）（T3313）              | 5                             | 5                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | N3313（times）（N3313）          | 4                             | 4                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 重寻呼间隔递增值（s）（PAGINGDELTA）     | 10                            | 10                            | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 周期路由更新定时器（min）（PRDTMR）       | 2                             | 2                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | MS可达定时器（min）（MSRCHTMR）       | 2                             | 2                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 保留参数（IMDTCHTMR）              | 0                             | 0                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 重定位资源分配定时器（s）（RLCTMR）        | 10                            | 10                            | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 旧侧重定位完成定时器（s）（RLCOLD）        | 10                            | 10                            | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 新侧重定位完成定时器（s）（RLCNEW）        | 10                            | 10                            | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | T3定时器（s）（T3）                 | 10                            | 10                            | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| SET PMM        | 释放非活动Iu连接定时器（min）（RELIUTIME） | 5                             | 5                             | 参见“水平网设LLD文档 ”。 | 配置3G移动性管理定时器参数。 |
| ADD IUAUTHCIPH | IMSI前缀（IMSIPRE）              | 460001                        | 460001                        | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能       |
| ADD IUAUTHCIPH | 安全策略（SECPLC）                 | AUTHANDPROTECTED              | AUTHANDPROTECTED              | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能       |
| ADD IUAUTHCIPH | 加密算法（CIPHALG）                | UEA1-1&UEA2-1&NO_ENCRYPTION-1 | UEA1-1&UEA2-1&NO_ENCRYPTION-1 | 参见“水平网设LLD文档 ”。 | 启用鉴权和加密功能       |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 增加3G寻呼数据。

   ```
   ADD IUPAGING:LAI="460000001",RAC="01",RNCINDEX=0;
   ```
3. 增加归属PLMN配置信息。

   ```
   ADD HPLMN: MCC="460", MNC="00", CC="86", SM=YES, MAXSMNUM=11, SMS=YES, S5S8TYPE=GTP, PLMNN="name";
   ```
4. **可选：**配置3G移动性管理定时器参数。

   ```
   SET PMM: T3322=6, N3322=4, T3350=6, N3350=4, T3360=6, N3360=4, T3370=6, N3370=4, T3313=5, N3313=4,PAGINGDELTA=10, PRDTMR=2,MSRCHTMR=2,IMDTCHTMR=0,RLCTMR=10,RLCOLD=10,RLCNEW=10,T3=10,RELIUTIME=5;
   ```
5. **可选：**启用鉴权和加密功能

   ```
   ADD IUAUTHCIPH: IMSIPRE="460001", SECPLC=AUTHANDPROTECTED, CIPHALG=UEA1-1&UEA2-1&NO_ENCRYPTION-1;
   ```