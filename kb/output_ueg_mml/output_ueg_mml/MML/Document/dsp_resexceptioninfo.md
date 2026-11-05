# 显示异常信息（DSP RESEXCEPTIONINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示当前系统中存在的异常信息。

当业务处理异常时，可执行该命令查看当前系统中是否存在异常信息，方便定位问题。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                         |
|:-------------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESOURCENAME | 资源名称       | 可选必选说明：可选参数 参数含义：该参数用于表示资源名称。通过DSP RES命令可以查询资源信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示所有资源的信息。                                                                   |
| ISVERBOSE    | 是否查询详细信息   | 可选必选说明：可选参数 参数含义：该参数用于表示是否显示详细信息。 数据来源：本端规划 取值范围：枚举类型。 NO：否。YES：是。 默认值：NO                                                                                                                    |
| SHOWNUM      | 要查询的数据最大个数 | 可选必选说明：可选参数 参数含义：该参数用于表示每个资源能够显示的最大记录量。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20。 默认值：20 配置原则：当不输入时，若是某个资源的实际数据量达到此参数的默认值，则显示的数据量为此参数默认值，否则按实际数据量显示。当输入某个值时，若是某个资源的实际数据量达到此参数值，则显示的数据量为此参数值，否则按实际数据量显示。 |
| BEGININDEX   | 记录起始位置     | 可选必选说明：可选参数 参数含义：该参数用于表示每个资源从第几条记录开始显示。 数据来源：本端规划 取值范围：整数类型，取值范围为0～19。 默认值：无 配置原则：当不输入时，从最新的数据开始显示，否则从指定的起始数据索引开始显示。                                                                         |

#### 使用实例

显示所有异常的详细信息：

```
DSP RESEXCEPTIONINFO: ISVERBOSE=YES;
```

```
RETCODE = 0  操作成功

结果如下:
--------
异常类型ID    异常子类型ID    异常名称    资源名称    进程ID    进程名称            异常发生时间           CPU Tick时间高8位    CPU Tick时间低8位    Fenix版本                     Dopra版本                      补丁版本          调用栈              寄存器信息                                                  转储栈
11            1               SIGSEGV     OMU1        1011      APPLocation10001    2016-04-15 10:11:33    0x0000083e           0xf3c2329b           FENIXV100R005C00B090          DOPRA SSP V300R002C50SPC070    V100R005MOD000    
liblocbase.so(SSP_ProcSigGetStack+0xdd) [0x7f94ae101fcd]
liblocbase.so(SSP_ProcSigFunc+0x1db) [0x7f94ae104f0b]
libdefault.so(sigcapHandler+0xb5) [0x7f94b2f60325]
libdefault.so(patchIllInsHandler+0x5b) [0x7f94b2fef73b]
libpthread.so.0(+0xf130) [0x7f94b4517130]
compa.so(COMPA_TriggerExceptionMsgHandler+0x22) [0x7f9490724122]
libdefault.so(RTF_MsgProcessCbk+0x101) [0x7f94b31907a1]
libdefault.so(rtfScmMessageSchedule+0x24d) [0x7f94b318f7bd]
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x7f94b31905]
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x7f94b318cb6a]
libdefault.so(tskAllTaskEntry+0x15f) [0x7f94b2fa1eff]
libpthread.so.0(+0x7df5) [0x7f94b450fdf5]
libc.so.6(clone+0x6d) [0x7f94b3c0860d]    
RAX:0000000000000000; RBX:00007f94ac794980
RCX:00007f94b3bffd83; RDX:0000000000000000
RSI:0000000000000000; RDI:0000000000000002
RBP:00007f94ac187c20; RSP:00007f94ac187c10
R8:00007f94ac187be0; R9:0000000000005c2a
R10:0000000000000000; R11:0000000000000246
R12:00007f94ac187cf0; R13:00007f94adb502c8
R14:0000000000000001; R15:00007f94adb897e0
RIP:00007f9490724122; EFLAGS:0000000000010246
CS:0000000000000033; CR2:0000000000000001
FS:0000000000000000; GS:0000000000000000
ERR:0000000000000006; TRAPNO:000000000000000e    
Dump stack(total 1536Bytes, 16Bytes/line):
0x00007f94ac187a10: 70 7a 18 ac 94 7f 00 00 00 00 00 00 00 00 00 00
0x00007f94ac187a20: 28 7b 18 ac 94 7f 00 00 2c 7b 18 ac 94 7f 00 00
0x00007f94ac187a30: 0d 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00
0x00007f94ac187a40: 80 7a 18 ac 94 7f 00 00 9c 7b 00 b3 94 7f 00 00
0x00007f94ac187a50: 68 7a 18 ac 94 7f 00 00 6c 7a 18 ac 94 7f 00 00
0x00007f94ac187a60: 7c df 55 b3 94 7f 00 00 00 00 00 00 bc 08 00 00
11            1               SIGSEGV     OMU2        1010      APPLocation10001    2016-04-15 10:11:22    0x0000081e                 0xf3c2339b     FENIXV100R005C00B090          DOPRA SSP V300R002C50SPC070    V100R005MOD000    
liblocbase.so(SSP_ProcSigGetStack+0xdd) [0x7f5208e6dfcd]
liblocbase.so(SSP_ProcSigFunc+0x1db) [0x7f5208e70f0b]
libdefault.so(sigcapHandler+0xb5) [0x7f520dccc325]
libdefault.so(patchIllInsHandler+0x5b) [0x7f520dd5b73b]
libpthread.so.0(+0xf130) [0x7f520f283130]
compa.so(COMPA_TriggerExceptionMsgHandler+0x22) [0x7f5205a3b122]
libdefault.so(RTF_MsgProcessCbk+0x101) [0x7f520defc7a1]
libdefault.so(rtfScmMessageSchedule+0x24d) [0x7f520defb7bd]
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x7f520defc5]
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x7f520def8b6a]
libdefault.so(tskAllTaskEntry+0x15f) [0x7f520dd0deff]
libpthread.so.0(+0x7df5) [0x7f520f27bdf5]
libc.so.6(clone+0x6d) [0x7f520e97460d]    
RAX:0000000000000000; RBX:00007f5207500980
RCX:00007f520e96bd83; RDX:0000000000000000
RSI:0000000000000000; RDI:0000000000000002
RBP:00007f5205604c20; RSP:00007f5205604c10
R8:00007f5205604be0; R9:0000000000004e16
R10:0000000000000000; R11:0000000000000246
R12:00007f5205604cf0; R13:00007f52088bc2c8
R14:0000000000000001; R15:00007f52088f57e0
RIP:00007f5205a3b122; EFLAGS:0000000000010246
CS:0000000000000033; CR2:0000000000000001
FS:0000000000000000; GS:0000000000000000
ERR:0000000000000006; TRAPNO:000000000000000e    
Dump stack(total 1536Bytes, 16Bytes/line):
0x00007f5205604a10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x00007f5205604a20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x00007f5205604a30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x00007f5205604a40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x00007f5205604a50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x00007f5205604a60: 00 00 00 00 00 00 00 00 c9 d4 69 0f 52 7f 00 00
(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释                         |
|:--------------|:------------------------------|
| 异常类型ID        | 用于表示信号类型号。                    |
| 异常子类型ID       | 用于表示信号子类型号。                   |
| 异常名称          | 用于表示异常名称。                     |
| 资源名称          | 用于表示资源名称。通过DSP RES命令可以查询资源信息。 |
| 进程ID          | 用于表示进程ID。                     |
| 进程名称          | 用于表示进程名称。                     |
| 异常发生时间        | 用于表示异常发生的时间。                  |
| CPU Tick时间高8位 | 用于表示CPU TICK时间的高八位。           |
| CPU Tick时间低8位 | 用于表示CPU TICK时间的低八位。           |
| Fenix版本       | 用于表示FENIX版本。                  |
| Dopra版本       | 用于表示DOPRA版本。                  |
| 补丁版本          | 用于表示补丁版本。                     |
| 调用栈           | 用于表示调用栈信息。                    |
| 寄存器信息         | 用于表示寄存器信息。                    |
| 转储栈           | 用于表示转储栈信息。                    |