# 设置NFINFOLIST处理策略（SET NRFNFLSTCTLPLY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于设置NF携带NFINFOLIST注册、更新、发现策略。

当前该命令支持网元类型为SMF，NWDAF，SMF在注册、更新请求中，NfProfile可携带smfInfo以及smfInfoList，其中smfInfoList可包含多条smfInfo。

当网络中NF均支持特性“WSFD-205015 SMF支持多服务区”时，可通过本命令设置SMF注册更新校验策略，从而实现基于位置区域优选SMF。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE   | INFOLSTREGUPD   | PREFERNFINFOSW   | MULINFOONENOTAI   |
|:---------|:----------------|:-----------------|:------------------|
| SMF      | All             | FUNC_ON          | FUNC_ON           |
| NWDAF    | All             | FUNC_OFF         | -                 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                  | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:----------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE          | 网元类型                  | 可选必选说明：必选参数  参数含义：该参数用于表示携带NFINFOLIST注册、更新、发现策略对应的NF类型。  数据来源：全网规划 取值范围： SMF（SMF）NWDAF（NWDAF）  默认值：无。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                      |
| INFOLSTREGUPD   | 携带NFINFOLIST注册更新处理策略  | 可选必选说明：可选参数  参数含义：该参数用于控制NF携带NFINFOLIST向NRF发起注册、更新请求时，NRF针对NF携带NFINFO和NFINFOLIST的校验策略。若NF携带情况不满足本策略，NRF返回400 Bad Request；满足则校验通过。  数据来源：全网规划 取值范围： All（不检验NFINFO或NFINFOLIST的携带情况）MustNfInfo（必须携带NFINFO）NfInfoOrNfInfoList（必须携带NFINFO或NFINFOLIST其中一个）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFNFLSTCTLPLY查询当前参数配置值。  配置原则：  当网络中所有NF都不支持特性“WSFD-205015 SMF支持多服务区”时，建议将参数值设置为All。  当网络中部分NF支持特性“WSFD-205015 SMF支持多服务区”时，建议将参数值设置为MustNfInfo。  当网络中所有NF均支持特性“WSFD-205015 SMF支持多服务区”时，建议将参数值设置为NfInfoOrNfInfoList。 |
| PREFERNFINFOSW  | 服务发现优先匹配NFINFO开关      | 可选必选说明：可选参数  参数含义：该参数用于控制服务发现NF时，若匹配到多个NF，是否优先返回NFINFO满足服务发现条件的NF。开关设置为“FUNC_ON”，服务发现NF时，优先匹配NFINFO满足发现条件的NF；开关设置为“FUNC_OFF”时，服务发现NF时，不区分NFINFO或者NFINFOLIST，两个有一个满足发现条件均可以返回。  数据来源：全网规划 取值范围： FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFNFLSTCTLPLY查询当前参数配置值。  配置原则：  当网络中服务发现发起方不支持特性“WSFD-205015 SMF支持多服务区”，建议打开此开关。  当网元类型为NWDAF时，不可配置此开关。                                                                                                                                           |
| MULINFOONENOTAI | 注册更新多NFINFO部分无TAI处理开关 | 可选必选说明：可选参数  参数含义：该参数用于控制NF向NRF发起注册、更新请求，携带NFINFO和NFINFOLIST时，是否允许该NF的多个NFINFO中有部分NFINFO不携带TAI信息。开关设置为“FUNC_ON”，NRF允许部分NFINFO不携带TAI信息，注册更新请求正常返回；开关设置为“FUNC_OFF”时，NRF不允许部分NFINFO不携带Tai信息，注册更新请求返回400 Bad Request。 若NF向NRF发起注册，更新请求，仅携带单NFINFO或多NFINFO均无TAI时，NRF对于NF携带TAI参数的控制策略可参考SET NRFTAKEPARARULE命令中的NOTAISW参数。  数据来源：全网规划 取值范围： FUNC_ON（打开）FUNC_OFF（关闭）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFNFLSTCTLPLY查询当前参数配置值。  配置原则：  当网元的NFINFO或NFINFOLIST不携带TAI信息，NRF期望服务发现不通配TAI，可关闭此开关。                       |

## 使用实例

运营商需配置携带NFINFOLIST的NF注册、更新、以及服务发现该NF的策略时，若需设置如下策略，

- NRF允许SMF同时携带SMFINFO，SMFINFOLIST注册、更新时，可设置INFOLSTREGUPD为All。
  NRF允许SMF某个SMFINFO不携带TAI注册、更新时，可设置MULINFOONENOTAI为“FUNC\_ON”。
  NF服务发现SMF时，需要NRF优先返回发现参数满足SMFINFO的SMF，可设置PREFERNFINFOSW为“FUNC\_ON”。
  执行命令如下：

  ```
  SET NRFNFLSTCTLPLY: NFTYPE=SMF, INFOLSTREGUPD=All, PREFERNFINFOSW=FUNC_ON, MULINFOONENOTAI=FUNC_ON;
  ```
- NRF允许NWDAF同时携带NWDAFINFO，NWDAFINFOLIST注册、更新时，可设置INFOLSTREGUPD为All。
  执行命令如下：

  ```
  SET NRFNFLSTCTLPLY: NFTYPE=NWDAF, INFOLSTREGUPD=All;
  ```