# 显示断言信息（DSP RESASSERTINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示当前系统中存在的断言信息。

当业务处理异常时，可执行该命令查看当前系统中是否存在断言信息，方便定位问题。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                          |
|:-------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESOURCENAME | 资源名称       | 可选必选说明：可选参数 参数含义：该参数用于表示节点名称或容器名称。通过DSP RES命令可以查询资源信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示所有资源的信息。使用DSP RES查看资源名称。                                               |
| SHOWNUM      | 要查询的数据最大个数 | 可选必选说明：可选参数 参数含义：该参数用于表示每个资源能够显示的最大记录量。 数据来源：本端规划 取值范围：整数类型，取值范围为1～100。 默认值：20 配置原则：当不输入时，若是某个资源的实际数据量达到此参数的默认值，则显示的数据量为此参数默认值，否则按实际数据量显示。当输入某个值时，若是某个资源的实际数据量达到此参数值，则显示的数据量为此参数值，否则按实际数据量显示。 |
| BEGININDEX   | 记录起始位置     | 可选必选说明：可选参数 参数含义：该参数用于表示每个资源从第几条记录开始显示。 数据来源：本端规划 取值范围：整数类型，取值范围为0～99。 默认值：无 配置原则：当不输入时，从最新的数据开始显示，否则从指定的起始数据索引开始显示。                                                                          |
| ISVERBOSE    | 是否查询详细信息   | 可选必选说明：可选参数 参数含义：该参数用于表示是否显示详细信息。 数据来源：本端规划 取值范围：枚举类型。 NO：否。YES：是。 默认值：NO                                                                                                                     |

#### 使用实例

显示所有详细的断言信息：

```
DSP RESASSERTINFO: ISVERBOSE=YES;
```

```
RETCODE = 0  操作成功

结果如下:
--------
资源名称    断言发生时间           进程ID    进程名称            文件名        行号        附加信息   Fenix版本                     Dopra版本                      补丁版本          调用栈
OMU1        2016-04-15 10:19:01    1011      APPLocation10001    abc.c         32        NULL       FENIXV100R005C00B090          DOPRA SSP V300R002C50SPC070    V100R005MOD000    
liblocbase.so(VRP_Assert+0x75) [0x00007f77d866d2c5] 
compa.so(SSITP_Set_Compa_Triggerassertion+0x29) [0x00007f77d5261a59] 
libssitp.so(SSITP_Action_SetTestData+0x4f4) [0x00007f77d4bf9bc6] 
libssitp.so(SSITP_CFG_ParseActAtom+0x168) [0x00007f77d4bfbca4] 
libssitp.so(SSITP_CFG_ReceiveSmpActMsg+0x101) [0x00007f77d4bfbaa5] 
libssitp.so(SSITP_RECV_ProcSMPAppCfgiMsg+0xae) [0x00007f77d4bffe3f] 
libssitp.so(SSITP_COM_ReceiveMsg+0x140) [0x00007f77d4bffa34] 
libdefault.so(RTF_MsgProcessCbk+0x101) [0x00007f77dd6fc7a1] 
libdefault.so(rtfScmMessageSchedule+0x24d) [0x00007f77dd6fb7bd] 
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x00007f77dd6fc55a] 
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x00007f77dd6f8b6a] 
libdefault.so(tskAllTaskEntry+0x15f) [0x00007f77dd50deff]
OMU2        2016-04-15 10:18:50    1010      APPLocation10001    abc.c         32       NULL        FENIXV100R005C00B090          DOPRA SSP V300R002C50SPC070    V100R005MOD000    
liblocbase.so(VRP_Assert+0x75) [0x00007f9990c062c5]
compa.so(SSITP_Set_Compa_Triggerassertion+0x29) [0x00007f998d7faa59] 
libssitp.so(SSITP_Action_SetTestData+0x4f4) [0x00007f998d192bc6] 
libssitp.so(SSITP_CFG_ParseActAtom+0x168) [0x00007f998d194ca4] 
libssitp.so(SSITP_CFG_ReceiveSmpActMsg+0x101) [0x00007f998d194aa5] 
libssitp.so(SSITP_RECV_ProcSMPAppCfgiMsg+0xae) [0x00007f998d198e3f] 
libssitp.so(SSITP_COM_ReceiveMsg+0x140) [0x00007f998d198a34] 
libdefault.so(RTF_MsgProcessCbk+0x101) [0x00007f9995c957a1] 
libdefault.so(rtfScmMessageSchedule+0x24d) [0x00007f9995c947bd] 
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x00007f9995c9555a] 
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x00007f9995c91b6a] 
libdefault.so(tskAllTaskEntry+0x15f) [0x00007f9995aa6eff] 
(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                              |
|:--------|:-----------------------------------|
| 资源名称    | 用于表示节点名称或容器名称。通过DSP RES命令可以查询资源信息。 |
| 断言发生时间  | 用于表示断言发生的时间。                       |
| 进程ID    | 用于表示进程ID。                          |
| 进程名称    | 用于表示进程名称。                          |
| 文件名     | 用于表示文件名。                           |
| 行号      | 用于表示行号。                            |
| 附加信息    | 用于表示断言附加信息。                        |
| Fenix版本 | 用于表示FENIX版本。                       |
| Dopra版本 | 用于表示DOPRA版本。                       |
| 补丁版本    | 用于表示补丁版本。                          |
| 调用栈     | 用于表示调用栈信息。                         |