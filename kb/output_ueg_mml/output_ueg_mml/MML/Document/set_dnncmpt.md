# 设置DNN兼容性控制参数（SET DNNCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF与周边NF交互时的DNN相关控制参数。

## 注意事项

- 该命令执行后立即生效。

- 此命令仅支持整系统控制，无法根据SMF的局向做控制。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HOMEUSRFMT   | LBOUSRFMT   | HRUSRFMT   | AMFHOMEUSRFMT   | AMFLBOUSRFMT   | AMFHRUSRFMT   |
|:-------------|:------------|:-----------|:----------------|:---------------|:--------------|
| NI           | NIANDOI     | NIANDOI    | NI              | NIANDOI        | NIANDOI       |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称              | 参数说明                                                                                                                                                                                                                                                                                                                                      |
|:--------------|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOMEUSRFMT    | 本网用户DNN格式         | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对本网用户，向SMF（包括I-SMF）发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP建议AMF针对本网用户与SMF交互时携带完整的DNN，但具体要视SMF的处理能力决定是否携带完整的DNN。                    |
| LBOUSRFMT     | LBO漫游用户DNN格式      | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对LBO漫游用户，向SMF（包括I-SMF）发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP建议AMF针对LBO漫游用户与SMF交互时携带完整的DNN，但具体要视SMF的处理能力决定是否携带完整的DNN。              |
| HRUSRFMT      | HR漫游用户DNN格式       | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对HR漫游用户，向V-SMF发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP要求AMF针对HR漫游用户与V-SMF交互时必须携带完整的DNN。  HRUSRFMT取值为NI时，只用于测试场景，并且需要SMF支持处理非完整的DNN。 |
| AMFHOMEUSRFMT | AMF间本网用户DNN格式     | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对本网用户向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP建议AMF针对本网用户与新侧AMF交互时携带完整的DNN，但具体要视对端AMF的处理能力决定是否携带完整的DNN。                                                  |
| AMFLBOUSRFMT  | AMF间LBO漫游会话的DNN格式 | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对LBO漫游会话向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP建议AMF针对LBO漫游会话与新侧AMF交互时携带完整的DNN，但具体要视对端AMF的处理能力决定是否携带完整的DNN。                                            |
| AMFHRUSRFMT   | AMF间HR漫游会话DNN格式   | 可选必选说明：可选参数  参数含义：该参数用于标识AMF针对HR漫游会话向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。  数据来源：全网规划 取值范围： “NI（仅网络标识）”：仅网络标识“NIANDOI（完整DNN）”：完整DNN  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNCMPT查询当前参数配置值。  配置原则：  3GPP要求AMF针对HR漫游会话与新侧AMF交互时必须携带完整的DNN。                                                                        |

## 使用实例

设置本网用户与SMF交互时携带完整的DNN，执行如下命令：

```
SET DNNCMPT:HOMEUSRFMT=NIANDOI;
```