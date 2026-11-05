# 显示P-GW Back-Off流控状态(DSP PGWBACKOFFSTAT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于显示处于P-GW Back-off流控状态的SPP进程信息。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                         |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定SPU资源单元名称。该参数可以通过DSP RU命令查询。 数据来源：本端规划 取值范围：1～63位字符串 默认值：无                                                                                                                           |
| PROCNO | 进程号    | 可选必选说明：必选参数 参数含义：该参数用于显示业务进程所属的SPP进程序号。 数据来源：本端规划 取值范围：0～20 默认值：无                                                                                                                                            |
| APNNI  | APNNI  | 可选必选说明：可选参数 参数含义：该参数用来设置APNNI信息。 数据来源：本端规划 取值范围：0～62位字符串 默认值：无 配置原则：APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

#### 使用实例

1. 运营商希望查看当前流控任务的状态：

   DSP PGWBACKOFFSTAT: RUNAME="USN\_SP\_RU\_0066", PROCNO=1;

   ```
   %%DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1;%%
   RETCODE = 0  操作成功。

   操作结果如下：
   --------------
   RU名称            进程号     APNNI      

   USN_SP_RU_0066    1          HUAWEI2.COM
   USN_SP_RU_0066    1          HUAWEI3.COM
   (结果个数 = 2)

   ---    END
   ```
2. 运营商希望查看当前“APNNI”为“huawei1.com”的流控任务的状态：

   DSP PGWBACKOFFSTAT: RUNAME="USN\_SP\_RU\_0066", PROCNO=1, APNNI="huawei1.com";

   ```
   %%DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1, APNNI="huawei1.com";%%
   RETCODE = 0  操作成功。

   操作结果如下：
   --------------
   RU名称            进程号     APNNI        PGW Node Name                      P-GW Back-off timer 通过率

   USN_SP_RU_0066    4          HUAWEI1.COM  EPC.MNC03.MCC460.3GPPNETWORK.ORG   31                  50    
   USN_SP_RU_0066    4          HUAWEI1.COM  EPC1.MNC03.MCC460.3GPPNETWORK.ORG  30                  60    
   (结果个数 = 2)

   ---    END
   ```

#### 输出结果说明

| 输出项名称               | 输出项解释                                                |
|:--------------------|:-----------------------------------------------------|
| RU名称                | 该参数用于显示SPP进程所属的资源单元名称。 取值范围：1～63位字符串                 |
| 进程号                 | 该参数用于显示业务进程所属的SPP进程序号。 取值范围：0～20                     |
| APNNI               | 该参数用于显示处于流控状态的APNNI。 取值范围：1～62位字符串                   |
| P-GW Node Name      | 该参数用于显示处于流控状态的P-GW Node Name。 取值范围：1～255位字符串         |
| P-GW Back-off timer | 该参数用于显示处于流控状态的P-GW的Back-off时间。单位：秒 取值范围：0～4294967295 |
| 通过率                 | 该参数用于显示处于流控状态的P-GW当前的信令流程通过率。单位：% 取值范围：0～100         |