# 设置AMF的SBI接口控制参数（SET AMFSBIINFCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF的SBI接口控制参数，包括location头域及CallbackUri的Schema、重定向使用FQDN构造3gpp-sbi-target-apiroot开关。

若期望AMF向周边网元携带信元location及callbackUri中的Schema可基于对端请求的Schema或所选定的服务Schema动态设置，可通过本命令开启Schema自适应功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCHEMAADAPTSW   | SCHEMAUDMPLCY   | SCHEMAPCFPLCY   | TGTURIUSEFQDN   |
|:----------------|:----------------|:----------------|:----------------|
| OFF             | HTTP_FIRST      | HTTP_FIRST      | OFF             |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                                 | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------|:-------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCHEMAADAPTSW | Schema自适应开关                          | 可选必选说明：可选参数  参数含义：该参数用于控制AMF是否支持Schema自适应功能。  数据来源：全网规划 取值范围： “OFF（关闭）”：关闭“ON（打开）”：打开  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                        |
| SCHEMAUDMPLCY | ModelD模式UDM Schema填充策略               | 可选必选说明：该参数在"SCHEMAADAPTSW"配置为"ON"时为条件可选参数。  参数含义：该参数用于设置ModelD模式下AMF与UDM网元交互时Schema的填充策略。 ModelD模式下，AMF无法感知对端UDM支持的Schema类型，通过本参数可以灵活调整AMF与UDM网元交互时Schema的填充策略。 ModelD模式下，建议AMF与对端UDM的Schema策略均设置一致；若AMF与对端UDM的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与UDM通信。  数据来源：全网规划 取值范围： HTTP_FIRST（HTTP优先）HTTPS_FIRST（HTTPS优先）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。  配置原则：无 |
| SCHEMAPCFPLCY | ModelD模式PCF Schema填充策略               | 可选必选说明：该参数在"SCHEMAADAPTSW"配置为"ON"时为条件可选参数。  参数含义：该参数用于设置ModelD模式下AMF与PCF网元交互时Schema的填充策略。 ModelD模式下，AMF无法感知对端PCF支持的Schema类型，通过本参数可以灵活调整AMF与PCF网元交互时Schema的填充策略。 ModelD模式下，建议AMF与对端PCF的Schema策略均设置一致；若AMF与对端PCF的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与PCF通信。  数据来源：全网规划 取值范围： HTTP_FIRST（HTTP优先）HTTPS_FIRST（HTTPS优先）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。  配置原则：无 |
| TGTURIUSEFQDN | 重定向使用FQDN构造3gpp-sbi-target-apiroot开关 | 可选必选说明：可选参数  参数含义：该参数用来控制AMF没有获取到对端AMF的IP地址时，AMF重定向请求中3gpp-sbi-target-apiroot是否使用FQDN构造。  数据来源：全网规划 取值范围： “OFF（关闭）”：关闭“ON（打开）”：打开  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。  配置原则：  若本AMF仅配置对端AMF的FQDN信息，且需要使用FQDN构造3gpp-sbi-target-apiroot时，将该参数取值设置为"ON(打开)"。                                                                                                                |

## 使用实例

开启Schema自适应功能，执行如下命令：

```
SET AMFSBIINFCTRL:SCHEMAADAPTSW=ON;
```