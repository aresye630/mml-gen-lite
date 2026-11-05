# 显示业务资源部署位置(DSP SERRESLOC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询业务资源在整系统各进程上的部署情况。

#### 注意事项

- 该命令执行后立即生效。

- 该命令输入参数(除了业务资源类型)不作为过滤参数，执行该命令后，会查询系统所有保存结果。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERRESTYPE   | 业务资源类型 | 可选必选说明：必选参数 参数含义：该参数用于指定查询的资源类型。 取值范围：“RM_TYPE_USER(USER)”“RM_TYPE_DMLNK(DMLNK)”“RM_TYPE_S1ECMCONN(S1ECMCONN)”“RM_TYPE_S1UCMCONN(S1UCMCONN)”“RM_TYPE_GTPCPATH(GTPCPATH)”“RM_TYPE_GTPUPATH(GTPUPATH)”“RM_TYPE_DNSCONN(DNSCONN)”“RM_TYPE_M3UALNK(M3UALNK)”“RM_TYPE_GTPUPDP(GTPUPDP)”“RM_TYPE_SGSVLRLNK(SGSVLRLNK)”“RM_TYPE_IUUSRCONN(IUUSRCONN)”“RM_TYPE_GBCELL(GBCELL)”“RM_TYPE_GBUSER(GBUSER)”“RM_TYPE_GACONN(GACONN)”“RM_TYPE_NSE(NSE)”“RM_TYPE_LCSAPLNK(LCSAPLNK)”“RM_TYPE_SBCAPLNK(SBCAPLNK)”“RM_TYPE_NGAPLNK(NGAPLNK)” 默认值：无 说明： 目前暂不支持RM_TYPE_LCSAPLNK和RM_TYPE_SBCAPLNK。 |
| RUNAME       | RU名称   | 参数含义：该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 取值范围：0~63位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SPECPROCTYPE | 进程类型   | 参数含义：该参数用于指定查询进程的类型。 取值范围：“SPP(SPP)”“SGP(SGP)”“GBP(GBP)”“LCP(LCP)”“UPP(UPP)”“CDP(CDP)”“OMP(OMP)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SPECPROCID   | 进程序列号  | 参数含义：该参数用于指定查询进程的序列号。 取值范围：0~254 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SERVICETYPE  | 服务名称   | 可选必选说明：必选参数 参数含义：本参数用于指定服务名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。 默认值：无  说明： 该参数可以通过LST VNFC命令查询得到。                                                                                                                                                                                                                                                                                                                                                                                                                 |

#### 使用实例

查询“USER”资源部署情况：DSP SERRESLOC: SERRESTYPE=RM\_TYPE\_USER, SERVICETYPE="USN\_VNFC";

```
%%DSP SERRESLOC:SERRESTYPE=RM_TYPE_USER, SERVICETYPE=USN_VNFC%%
RETCODE = 0  执行成功。

输出结果如下
------------------
        业务资源类型             业务资源逻辑标识       RU名称      进程类型        进程序列号 
        USER                     16                     SPU1        SPP             0                  
        USER                     15                     SPU1        SPP             0                  
        USER                     14                     SPU1        SPP             0                  
        USER                     13                     SPU1        SPP             0                  
        USER                     12                     SPU1        SPP             0                  
        USER                     11                     SPU1        SPP             0                  
        USER                     10                     SPU1        SPP             0                  
        USER                     9                      SPU1        SPP             0                  
        USER                     8                      SPU1        SPP             0                  
        USER                     7                      SPU1        SPP             0                  
        USER                     6                      SPU1        SPP             0                  
        USER                     5                      SPU1        SPP             0                  
        USER                     4                      SPU1        SPP             0                  
        USER                     3                      SPU1        SPP             0                  
        USER                     2                      SPU1        SPP             0                  
        USER                     1                      SPU1        SPP             0                  
        USER                     0                      SPU1        SPP             0                  
        (Number of results = 17)

---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释            |
|:---------|:-----------------|
| 业务资源类型   | 查询的资源类型          |
| 业务资源逻辑标识 | 业务资源逻辑标识         |
| RU名称     | 该参数用于指定SPU资源单元名。 |
| 进程类型     | 资源所在的进程类型        |
| 进程序列号    | 资源所在的进程序列号       |