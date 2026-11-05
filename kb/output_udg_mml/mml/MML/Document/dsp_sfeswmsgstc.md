# 查询FEISW消息统计（DSP SFESWMSGSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询FEISW消息统计。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| RUNAME | 资源单元名称 | 可选必选说明：必选参数 参数含义：指定系统中有效的资源单元。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

查询FEISW消息统计：

```
DSP SFESWMSGSTC: RUNAME="VNRS_IPCTRL_EX_RU_0201";
```

```
RETCODE = 0  操作成功。

结果如下
--------
组件ID        子接口                   消息类型    接收消息数量    发送消息数量    IID类型            

0x808c00b4    SSP_SUB_INTF_HA          8           1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          9           1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          11          1               0               VOS_IID_MAX        
0x808c00b4    SSP_SUB_INTF_HA          16          20              0               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    1           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    2           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    3           2               2               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_FEISWHAI    5           74              74              VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FEII        1           1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        3           29              0               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FEII        5           1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        6           1               2               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        7           1               2               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        4           2               0               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FEII        26          1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        2           6               6               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        6           0               65              VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        7           0               2               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        18          1               1               VOS_IID_MAX        
0x6a0025      CTL_SUB_INTF_FESI        19          1               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        31          2               1               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_FESI        35          1               1               VOS_IID_MAX        
0x8c0026      SMP_SUB_INTF_APPCFGI     3           1               0               VOS_IID_MAX        
0x8c0026      SMP_SUB_INTF_APPCFGI     2           1               0               VOS_IID_MAX        
0x808c00b4    CTL_SUB_INTF_JOBI        1           11              11              VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      8           61              0               VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      7           40              40              VOS_IID_MAX        
0x8c0026      CTL_SUB_INTF_LDEVMI      10          33              0               VOS_IID_MAX        
0x808c00b4    SUB_INTF_MAX             0           4657            0               VOS_IID_TMR_TIMEOUT
(结果个数 = 29)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 组件ID    | 与FEISW通信的组件ID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 子接口     | 与FEISW通信的子接口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 消息类型    | SSP_SUB_INTF_HA{8 MSG_HA_START_WORK，11 MSG_HA_NEW_BACKUP，16 MSG_HA_PARTNER_STATUS}；CTL_SUB_INTF_FEISWHAI{1 MSG_FEISWHAI_BACKUP_BEGIN，2 MSG_FEISWHAI_BACKUP_DATA，3 MSG_FEISWHAI_BACKUP_END，4 MSG_FEISWHAI_BACKUP_REQUEST，5 MSG_FEISWHAI_REAL_BACKUP_DATA，6 MSG_FEISWHAI_NOTIFY_ERROR}；CTL_SUB_INTF_FEII{1 MSG_FEII_REGISTER，3 MSG_FEII_TABLE，4 MSG_FEII_TABLE_BATCH，5 MSG_FEII_SMOOTH_REQUEST，6 MSG_FEII_TABLE_BATCH_BEGIN，7 MSG_FEII_TABLE_BATCH_END，26 MSG_FEII_SERVICE_STATE_NOTIFY}；CTL_SUB_INTF_FESI{2 MSG_FESI_SUBSCRIBE_TABLE，6 MSG_FESI_UPDATE_TABLE，7 MSG_FESI_BATCH_UPDATE_TABLE，18 MSG_FESI_BATCH_UPDATE_BEGIN，19 MSG_FESI_BATCH_UPDATE_END，31 MSG_FESI_REGISTER，35 MSG_FESI_SERVICE_STATE_NOTIFY}；SMP_SUB_INTF_APPCFGI{0 ENUM_MSG_APPCFGI_UPDATE_CFG，3 ENUM_MSG_APPCFGI_QUERY}；CTL_SUB_INTF_JOBI{1 MSG_JOBI_JOBMSG}；CTL_SUB_INTF_LDEVMI{7 MSG_PDEVMI_DEVICE_EVENT_NOTIFY，10 MSG_PDEVMI_SUBSCRIBE_RESULT}。 |
| 接收消息数量  | FEISW接收消息数量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 发送消息数量  | FEISW发送消息数量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IID类型   | 消息的IID类型。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |