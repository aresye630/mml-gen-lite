# 显示流控统计信息(DSP FLOWCTRLSTAT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询流控统计。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                          |
|:------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME      | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定需要查询的SPU资源单元名称。该参数可以通过DSP RU命令查询。 取值范围：1-63位字符串。 默认值：无                                                                                |
| PROCTYPE    | 进程类型   | 可选必选说明：必选参数 参数含义：该参数用于要查询的进程类型。 取值范围：“SPP(SPP)”“SGP(SGP)”“GBP(GBP)”“CDP(CDP)”“UPP(UPP)”“LCP(LCP)” 默认值：无                                                       |
| PROCNO      | 进程号    | 可选必选说明：必选参数 参数含义：该参数用于指定要查询的进程序号。 取值范围：0~20 默认值：无                                                                                                             |
| SERVICETYPE | 服务名称   | 可选必选说明：必选参数 参数含义：本参数用于指定服务名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。 默认值：无  说明： 该参数可以通过LST VNFC命令查询得到。 |

#### 使用实例

查询LINK\_SP\_RU\_0064上0号SGP进程：

DSP FLOWCTRLSTAT: RUNAME="LINK\_SP\_RU\_0064", PROCTYPE=SGP, PROCNO=0, SERVICETYPE="LINK\_VNFC";

```
%%DSP FLOWCTRLSTAT: RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCNO=0, SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

查询结果如下
------------
输出结果  =  	RU CPU:47 	Proc Cpu:36 	WAL_Sig:15000 	PreMsgCount_Sig:0
	WAL_Data:10000 	PreMsgCount_Data:0 	WAL_NS:500 	PreMsgCount_NS:0
--------------------------------------
	msg type                                 self protect pass    self protect reject  queue pass           queue reject
	SCTPADAPT Choose SGP Init Msg            31542                31                   0                    0                   
	SCTPADAPT Choose SGP Tbit Msg            394                  4                    0                    0                   

服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释                                                                                                                                                                                                                                                            |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| msg type | 显示参与流控的消息类型。  说明： 以下类型的消息流控根据流程控制，报文统计结果中self protect与自保流控无关，仅做数字统计。get auth set req(Gr HTR)upd loc req(Gr HTR)get auth set req(Gr softpara)upd loc req(Gr softpara)SCTPADAPT Choose SGP Init MsgSCTPADAPT Choose SGP Tbit Msgauth info req(S6x)upd loc req(S6x) |