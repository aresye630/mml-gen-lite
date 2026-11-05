# 设置I-UPF选择失败处理方式（SET IUPFSELFAIL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于配置当SMF/I-SMF在Service Request流程中选择I-UPF失败时的处理方式。如果处理方式为保留会话，则SMF/I-SMF保持该会话，并通知AMF拒绝该PDU会话的用户面连接建立请求；如果处理方式为释放会话，则SMF/I-SMF，先通知AMF拒绝该PDU会话的用户面建立请求，然后发送Namf\_Communication\_N1N2MessageTransfer Req消息并内置NAS删除消息（即PDU Session Release Command消息）来释放UE会话。其中，NAS删除消息中携带的释放原因值，通过本配置命令中的RELCAUSE字段来指定。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH   | FAILPROC        | RELCAUSE        |
|:---------|:----------------|:----------------|
| DISABLE  | RELEASE_SESSION | NETWORK_FAILURE |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识     | 参数名称           | 参数说明                                                                                                                                                                                                                                               |
|:---------|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SWITCH   | 开关             | 可选必选说明：必选参数  参数含义：该参数用于表示是否开启I-UPF选择失败处理功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。  配置原则：  当SWITCH = DISABLE时，保持产品原有实现，当前实现为会话删除。                                                                                                         |
| FAILPROC | 失败处理方式         | 可选必选说明：该参数在"SWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定SMF/I-SMF在Service Request流程中选择I-UPF失败时的处理方式。  数据来源：本端规划 取值范围： RELEASE_SESSION（释放会话）KEEP_SESSION（保留会话）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IUPFSELFAIL查询当前参数配置值。  配置原则：无                  |
| RELCAUSE | 释放会话时携带的NAS原因值 | 可选必选说明：该参数在"FAILPROC"配置为"RELEASE_SESSION"时为条件必选参数。  参数含义：该参数用于指定I-UPF选择失败并需要释放PDU会话时所携带的NAS原因值。  数据来源：全网规划 取值范围： NETWORK_FAILURE（#38 网络侧失败）REACTIVATION_REQUEST（#39 请求重新激活）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IUPFSELFAIL查询当前参数配置值。  配置原则：无 |

## 使用实例

当SMF/I-SMF在Service Request流程中选择I-UPF失败时，如果处理方式为保留会话，可以执行如下命令：

```
SET IUPFSELFAIL: SWITCH=ENABLE, FAILPROC=KEEP_SESSION;
```