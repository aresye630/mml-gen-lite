# 测试允许访问策略配置（TST ALLOWPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于测试配置的访问授权控制策略。

## 注意事项

- 输入参数中源NF类型，源NF实例标识，源FQDN至少输入一个。
- 输入参数中目标NF类型，目标NF实例标识，目标FQDN至少输入一个。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                               |
|:-------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRCNFTYPE    | 源NF类型    | 可选必选说明：可选参数  参数含义：该参数用于表示访问的源NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无  |
| SRCNFINSTID  | 源NF实例标识  | 可选必选说明：可选参数  参数含义：该参数用于表示访问的源NF实例标识，该参数通过DSP REGNFINSTANCE命令获取。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~40。  默认值：无  配置原则：无                                                                                                                                                                                 |
| SRCFQDN      | 源FQDN    | 可选必选说明：可选参数  参数含义：该参数用于表示访问的源FQDN信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                                                                                                                                                                                           |
| SRCMCC       | 源移动国家码   | 可选必选说明：可选参数  参数含义：该参数用于表示访问的源NF对象所允许访问的移动国家码。  数据来源：全网规划  取值范围：字符串类型，输入长度是3。3位十进制数。  默认值：无  配置原则：无                                                                                                                                                                                                 |
| SRCMNC       | 源移动网号    | 可选必选说明：可选参数  参数含义：该参数用于表示访问的源NF对象所允许访问的移动网号。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是2~3。2位3位十进制数。  默认值：无  配置原则：无                                                                                                                                                                                            |
| TARGETNFTYPE | 目标NF类型   | 可选必选说明：可选参数  参数含义：该参数用于表示访问的目标NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| TARGETINSTID | 目标NF实例标识 | 可选必选说明：可选参数  参数含义：该参数用于表示访问的目标NF实例标识，该参数通过DSP REGNFINSTANCE命令获取。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~40。  默认值：无  配置原则：无                                                                                                                                                                                |
| TARGETFQDN   | 目标FQDN   | 可选必选说明：可选参数  参数含义：该参数用于表示访问的目标FQDN。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                                                                                                                                                                                            |
| DETAILSW     | 调试日志开关   | 可选必选说明：可选参数  参数含义：该参数用于表示详细内容打印开关，开关默认为关闭状态。  数据来源：本端规划 取值范围： DETAILSW_OFF（关闭）DETAILSW_ON（打开）  默认值：无  配置原则：无                                                                                                                                                                                       |

## 使用实例

测试配置的允许访问控制策略：

```
TST ALLOWPLCY: SRCNFTYPE=SMF, TARGETNFTYPE=AMF;
%%TST ALLOWPLCY: SRCNFTYPE=SMF, TARGETNFTYPE=AMF;%%
RETCODE = 0  操作成功

结果如下
------------------------
测试结果  =  {"NfInstanceID":"ff02-1","ServiceInfo":[{"ServiceInstanceID":"service_instance_2","ServiceName":"namf-mt"},{"ServiceInstanceID":"service_instance_3","ServiceName":"namf-loc"}]}
(结果个数  = 1)

---    END
```