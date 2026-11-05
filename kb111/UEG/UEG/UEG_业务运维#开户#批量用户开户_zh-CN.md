---
id: ''
name: 批量用户开户
ne_type: UEG
type: feature
description: 对批量用户执行开户操作。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 基础运维操作（风筝S，虚机容器）","业务运维","开户","批量用户开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
对批量用户执行开户操作。

## 必备事项
前提条件

* 开站已成功。
* 已登录 OM Portal。
* 操作员拥有系统管理员权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 选择“应用配置 > 业务运维”，在左侧导航栏中选择“开户”-> "用户批量开户"，进入“用户批量开户”界面。

### 2 单击导出按钮导出开户数据文件模板。

### **图1** 模板导出

### 3 填充批量用户模板数据，最大规格为2000条用户数据，并保存文件。

### **表1** 批量用户开户模板参数

### | 参数名 | 参数含义 | 参数取值 |

### | --- | --- | --- |

### | No | 标识序号。 | 整数类型，取值范围: 1~2000。上传文件中唯一。 |

### | imsi | 用户的IMSI号码。 | 6～15位的十进制数字。由MCC+MNC+MIN/MSIN组成。 |

### | msisdn | 用户的MSISDN号码。 | 1～15位十进制数字组成的字符串。由CC+NDC+SN组成。 |

### | kivalue | KI值。 | 32位的十六进制格式字符组成的字符串，不需要以“0x”开头，只能包含数字和字母（A-F和a-f）。 |

### | k2sno | K2序列号 | 获取序列号方式：  * 执行2，查询或添加成功的K2序列号值为1。 * 登录PGW，选择“UDM业务管理视图”，执行命令LST K2: HLRSN=1;，获取所有可使用的序列号。 |

### | authmode | 鉴权模式 | 取值有：1和2。1表示OPCVALUE，2表示OPID。 |

### | opcvalue | OPC值。 | authmode值为1时必填。32位的十六进制格式字符组成的字符串，不需要以“0x”开头，只能包含数字和字母（A-F和a-f）。 |

### | opid | OP序列号 | authmode值为2时必填。  获取序列号方式：  * 执行3，查询OP序列号。 |

### | amfsno | AMF序列号 | 获取序列号方式：  * 执行4，查询或添加成功的AMF序列号值为10001。 * 登录PGW，选择“UDM业务管理视图”，执行命令LST AMF: HLRSN=1;，获取所有可使用的序列号。 |

### | maxupbandwidth | 上行最大带宽，单位kbit/s。 | 整数类型，取值范围: 1~4294967295。 |

### | maxdownbandwidth | 下行最大带宽，单位kbit/s。 | 整数类型，取值范围: 1~4294967295。 |

### | addind | PDP/PDN地址标识 | 取值有：STATIC和DYNAMIC。 |

### | pdpadd | PDP/PDN地址 | IPv4地址。仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”时该参数有效，不填写此地址时需填写0。 |

### | pdpaddv6 | PDP/PDN地址 | IPv6地址。仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”时该参数有效，不填写此地址时需填写0。 |

### | tpl4gID | 4G模板ID | 至少填写一个4g或5g模板名称，不填写模板则填写0。登录PGW，选择“UDM业务管理视图”，执行命令LST EPSQOSTPL: HLRSN=1;，获取所有可使用的模板ID。 |

### | tpl5gID | 5G模板ID | 至少填写一个4g或5g模板名称，不填写模板则填写0。登录PGW，选择“UDM业务管理视图”，执行命令LST NGSUSERTPL: HLRSN=1;，获取所有可使用的模板ID。 |

### | DNN | 数据网名称 | 仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”并且选择“5G模板”时该参数有效。取值范围：1～64位的字符串，只允许输入字母、数字、“-”、“\_”、“.”和“\*”。 |

### | sliceType | SST（Slice/Service Type） | 仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”并且选择“5G模板”时该参数有效。整数类型，取值范围: 0~255。 |

### | sliceId | SD（Slice Differentiator） | 仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”并且选择“5G模板”时该参数有效。固定长度为3字节的十六进制字符串。 |

### | DNNQOSTPLID | DNN模板 | 仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”并且选择“5G模板”时该参数有效。  获取模板id方式：  * 执行5.c，查询模板id。 |

### | EPS\_QOSTPLID | EPS模板 | 仅当本命令中的“PDP/PDN地址标识”参数为“STATIC”并且选择”4G模板”时该参数有效。  获取模板id方式：  * 执行5.a，查询模板id。 |

### 如果KIVALUE和OPCVALUE为纯数字，且使用Excel编辑CSV文件时请设置对应单元格格式为文本格式。

### 批量用户数据中，IMSI和MSISDN全局唯一。如果存在重复的IMSI或MSISDN，仅第一个用户会开户成功，后续相同IMSI或者MSISDN的用户将开户失败。

### 2000条用户数据在10分钟内下发完毕。

### 4 选择开户数据文件并导入。

### **图2** 开户数据导入

### 5 根据提示输入开销户接入账号“用户名”和“密码”，并点击提交。

### 6 可能存在部分用户开户成功的情况，根据结果输出的提示信息可以获取开户失败的IMSI信息，按照开户数据文件中的用户顺序，该IMSI之前的用户（不包括该IMSI）均已开户成功，该IMSI用户开户失败，该IMSI之后的用户（不包括该IMSI）均未执行开户操作。

