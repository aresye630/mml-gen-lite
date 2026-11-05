# LCS全局属性（SET LCSGLBATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令用于配置LCS的全局属性。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令执行后只对新激活用户生效。
- LCSSVCASSNSW开关配置为ENABLE后，当本框LMF服务故障后，会导致定位失败。
- ISOLATEAMFSW开关配置为ENABLE后，当AMF失败次数达到参数CONFAILLOCREQ的配置值时，会隔离该AMF。
- 当AMFFAULTRETCODE或者LMFFAULTRETCODE配置为307时，需要执行SET LCSREDIRECTGMLC命令配置重定向IP地址，否则GMLC会给LCS Client返回503。
- 执行SET LCSGLBATTR命令时，需要至少输入一个参数；否则，命令执行失败。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | LCSSVCASSNSW   | ISOLATEAMFSW   |   CONFAILLOCREQ |   FAILRETRYINT | AMFFAULTRETCODE         | LMFFAULTRETCODE         |   RETRYINTTIME |
|:-------|:---------------|:---------------|----------------:|---------------:|:------------------------|:------------------------|---------------:|
| 初始值    | DISABLE        | DISABLE        |               5 |             30 | SERVICE_UNAVAILABLE_503 | SERVICE_UNAVAILABLE_503 |             10 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                                                            |
|:----------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LCSSVCASSNSW    | LCS服务联动开关    | 可选必选说明：可选参数 参数含义：该参数用于配置LCS的GMLC服务是否感知本框LMF服务状态。配置为使能时，如果本设备内LMF服务全部故障，则本设备不能处理单次定位请求以及周期定位订阅请求消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                      |
| ISOLATEAMFSW    | 隔离AMF功能开关    | 可选必选说明：可选参数 参数含义：该参数用于设置是否使能隔离AMF功能。 数据来源：本端规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                    |
| CONFAILLOCREQ   | 定位请求连续失败次数   | 可选必选说明：条件可选参数 前提条件：该参数在“ISOLATEAMFSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置连续定位失败多少次触发隔离AMF的功能。 数据来源：本端规划 取值范围：整数类型，取值范围为3~200。 默认值：无 配置原则：无                                                           |
| FAILRETRYINT    | 故障重试间隔（秒）    | 可选必选说明：条件可选参数 前提条件：该参数在“ISOLATEAMFSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置隔离AMF后，GMLC再次给AMF发送定位请求的间隔时长。 数据来源：本端规划 取值范围：整数类型，取值范围为5~600，单位为秒。 默认值：无 配置原则：无                                             |
| AMFFAULTRETCODE | 隔离AMF定位失败返回码 | 可选必选说明：条件可选参数 前提条件：该参数在“ISOLATEAMFSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置隔离AMF后GMLC给LCS Client发送的失败返回码。 数据来源：本端规划 取值范围： SERVICE_UNAVAILABLE_503：服务不可用。TEMPORARY_REDIRECT_307：重定向。 默认值：无 配置原则：无       |
| LMFFAULTRETCODE | LMF故障返回码     | 可选必选说明：条件可选参数 前提条件：该参数在“LCSSVCASSNSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置检测到本框内LMF故障后GMLC给LCS Client发送的失败返回码。 数据来源：本端规划 取值范围： SERVICE_UNAVAILABLE_503：服务不可用。TEMPORARY_REDIRECT_307：重定向。 默认值：无 配置原则：无 |
| RETRYINTTIME    | 重试间隔次数       | 可选必选说明：条件可选参数 前提条件：该参数在“ISOLATEAMFSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于设置隔离AMF后，GMLC再次给AMF发送定位请求的间隔次数。 数据来源：本端规划 取值范围：整数类型，取值范围为5~200。 默认值：无 配置原则：无                                                  |

#### 使用实例

配置LCS的全局属性：

```
SET LCSGLBATTR: LCSSVCASSNSW=ENABLE, ISOLATEAMFSW=ENABLE, CONFAILLOCREQ=3, FAILRETRYINT=30, AMFFAULTRETCODE=TEMPORARY_REDIRECT_307, LMFFAULTRETCODE=TEMPORARY_REDIRECT_307, RETRYINTTIME=10;
```