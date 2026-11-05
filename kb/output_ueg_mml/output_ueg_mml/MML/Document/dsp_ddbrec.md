# 查询DDB记录(DSP DDBREC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于查询DDB记录。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                    |
|:---------|:-------|:----------------------------------------------------------------------------------------|
| RUNAME   | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定要查询的资源单元名称。该参数可以通过DSP RU命令查询。 可选必选说明：可选参数 取值范围：1 ~ 63位字符串 默认值：无 |
| PROCTYPE | 进程类型   | 可选必选说明：必选参数 参数含义：该参数用于要查询的进程类型。 取值范围：“SAP(SAP)”“SRP(SRP)”“OMP(OMP)” 默认值：无               |
| PROCNO   | 进程序列号  | 可选必选说明：必选参数 参数含义：该参数用于指定要查询的进程序号。 取值范围：0~20 默认值：无                                       |
| SQL      | SQL语句  | 可选必选说明：必选参数 参数含义：该参数用于指定查询的sql语句。 取值范围：无 默认值：无                                          |

#### 使用实例

查询资源单元为MCR\_SP\_RU\_0065的0号SAP进程的315号表的所有DDB记录：

DSP DDBREC: RUNAME="MCR\_SP\_RU\_0065", PROCTYPE=SAP, PROCNO=0, SQL="select \* from 315";

```
%%DSP DDBREC: RUNAME="MCR_SP_RU_0065", PROCTYPE=SAP, PROCNO=0, SQL="select * from 315";%%
RETCODE = 0  操作成功。

操作结果如下
--------------
Output  =  ----------CPUID: 2241200376----------
exesql "select * from 315"

	DDBQueryMultiRecordsUnintentionally: Success.
		Get record number: 1. 

		Field 0: 
0
		Field 1: 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
		Field 2: 
01 00 00 00
		Field 3: 
00 00 00 00

(结果个数 = 1)
---    END
```