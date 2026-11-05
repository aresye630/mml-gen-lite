# 查询FEI消息统计（DSP SFEMSGSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询FEI消息统计。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| RUNAME | 资源单元名称 | 可选必选说明：必选参数 参数含义：指定系统中有效的资源单元。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

查询FEI消息统计：

```
DSP SFEMSGSTC:RUNAME="VNODE_VNRS_VNFC_IPU_0065";
```

```
RETCODE = 0  操作成功。

结果如下
--------
组件ID        子接口                  消息类型    接收消息数量    发送消息数量

0x80cc000d    SMP_SUB_INTF_APPCFGI     3           1               0
0x7a0012      CTL_SUB_INTF_IFMI        1           1               0
0x6a0011      FEI_CTL_SUB_INTF_RMI     35          0               2
0x6a0011      CTL_SUB_INTF_FEII        1           1               0
0x6a0011      CTL_SUB_INTF_FESI        35          2               0
0x80030070    SSP_SUB_INTF_HA          8           1               0
0x80030070    SSP_SUB_INTF_CSHELPER    1           1               0
(结果个数 = 7)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 组件ID    | 与FEI通信的组件ID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 子接口     | 与FEI通信的子接口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 消息类型    | SMP_SUB_INTF_APPCFGI{0 MSG_APPCFGI_UPDATE_CFG，1 MSG_APPCFGI_UPDATE_INNERCFG，3 MSG_APPCFGI_QUERY}；CTL_SUB_INTF_IFMI{1 MSG_IFMI_COLLECT_SERVICE，4 MSG_IFMI_COLLECT_DATA，10 MSG_IFMI_REAL_UPDATE，13 MSG_IFMI_REGISTER}；CTL_SUB_INTF_FEII{1 MSG_FEII_REGISTER，4 MSG_FEII_TABLE_BATCH，5 MSG_FEII_SMOOTH_REQUEST，6 MSG_FEII_TABLE_BATCH_BEGIN，7 MSG_FEII_TABLE_BATCH_END，10 MSG_FEII_INDICATION，24 MSG_FEII_NOTIFY_SMSTATE，26 MSG_FEII_SERVICE_STATE_NOTIFY，27 MSG_FEII_QUERY_SMOOTH_STATE}；CTL_SUB_INTF_FESI{31 MSG_FESI_REGISTER，35 MSG_FESI_SERVICE_STATE_NOTIFY}；SSP_SUB_INTF_HA{8 MSG_HA_START_WORK，16 MSG_HA_PARTNER_STATUS}；SSP_SUB_INTF_CSHELPER{1 MSG_SIO_CREATE_PIPE，2 MSG_SIO_DELETE_PIPE，3 MSG_SIO_RESUME_PIPE}。 |
| 接收消息数量  | FEI接收消息数量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 发送消息数量  | FEI发送消息数量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |