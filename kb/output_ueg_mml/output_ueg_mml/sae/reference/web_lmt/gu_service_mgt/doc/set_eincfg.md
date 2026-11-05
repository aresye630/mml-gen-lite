# 设置增强智能业务(SET EINCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于设置增强智能业务配置。

## 注意事项

- 如果OPERTYPE=ADD，参数EINTYPE、EINBEGIN和EINEND是必选，EINEND值大于等于EINBEGIN。
- “PrePaidCtr1的业务键+100”的范围应包含在PrePaid的业务键范围中，因为PrePaidCtr1用户下发PPS TSK时，使用“PrePaidCtr1用户签约的TSK+100”下发。
- 当EINTYPE为PrePaid，PrePaidCtr1，PrePaidCtr2，PostPaid，PrePaidFix，QosCheck时，每种用户类型最多能加999条智能业务记录。
- 当EINTYPE为VMCC时，只能加1条智能业务记录。

## 参数说明

| 参数标识     | 参数名称     | 参数说明                                                                                                                                                                                 |
|:---------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPERTYPE | 操作类型     | 操作类型。取值如下： ADD：增加一条记录。 RMV：删除已有记录。                                                                                                                                                   |
| EINTYPE  | 增强智能业务类型 | 增强智能业务类型。取值如下： PrePaid：预付费用户配置选项。 PrePaidCtr1：VPN Control 1用户配置选项。 PrePaidCtr2：VPN Control 2用户配置选项。 PostPaid：后付费用户配置选项。 VMCC：VMCC配置选项。 PrePaidFix：预付费固定用户配置选项。 QosCheck：Qos检测用户配置选项。 |
| EINBEGIN | 起始业务键    | 仅当本命令中的“操作类型”参数为“ADD”或“RMV”时该参数有效。用于标识增强智能业务起始业务键。 取值范围：1～999 默认值：无。                                                                                                                 |
| EINEND   | 终止业务键    | 仅当本命令中的“操作类型”参数为“ADD”时该参数有效。用于标识增强智能业务终止业务键。 取值范围：1～999 默认值：无。                                                                                                                       |

## 使用实例

在［增强智能配置表］中增加一条记录，设置起始业务键为900，终止业务键为919，该增强智能业务类型为PrePaid。命令如下：

SET EINCFG: OPERTYPE=ADD, EINTYPE=PrePaid, EINBEGIN=900, EINEND=919;