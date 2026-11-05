# 查询S1接口均衡操作信息(DSP S1BALANCEINFO)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

此命令用于查询系统中指定SGP进程上的eNodeB数目或系统中总的eNodeB数目。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                         |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYSCE | 查询场景   | 可选必选说明：可选参数 参数含义：该参数用于指定eNodeB均衡信息查询场景。 数据来源：本端规划 取值范围： “DISTRIBUTED(分布查询)”：用于查询相应SGP进程上的eNodeB数目。如果用户只指定RU名称，则查询指定RU所有SGP进程的eNodeB数目；如果用户不指定任何查询条件，则查询系统中所有SGP进程的eNodeB数目。“TOTAL(总数查询)”：用于查询系统总的eNodeB数目。 默认值：“TOTAL(总数查询)” |
| RUNAME   | RU名称   | 可选必选说明：条件可选参数 参数含义：该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 前置条件：该参数在“查询场景”为“DISTRIBUTED(分布查询)”时才生效。 数据来源：本端规划 取值范围：0~63 位字符串 默认值：无                                                                                                |
| PRON     | 进程号    | 可选必选说明：条件可选参数 参数含义：该参数用于指定到eNodeB的S1链路所在的SGP进程的进程号。 前置条件：该参数在“查询场景”为“DISTRIBUTED(分布查询)”时才生效。 数据来源：本端规划 取值范围：0~20 默认值：无  说明： 如果输入进程号，必须输入RU名称。                                                                                |

#### 使用实例

1. 查询系统所有eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=TOTAL;

   ```
   %%DSP S1BALANCEINFO: QUERYSCE=TOTAL;%%
   RETCODE = 0  操作成功。

   操作结果如下
   --------------
   总的eNodeB数目  =  0
   (结果个数 = 1)
   ---    END
   ```
2. 查询USN\_VSU1 0号SGP进程的eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN\_VSU1", PRON=0;

   ```
   %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1", PRON=0;%%
   RETCODE = 0  操作成功。

   操作结果如下
   -------------------------
             RU名称   =  USN_VSU1
              进程号  =  0
          eNodeB个数  =  0
   (结果个数 = 1)
   ---    END
   ```
3. 查询USN\_VSU1上的所有SGP进程的eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN\_VSU1";

   ```
   %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1";%%
   RETCODE = 0  操作成功。

   操作结果如下
   -------------------------
   RU名称      进程号         eNodeB个数 
   USN_VSU1    0              0                 
   USN_VSU1    3              0                 
   USN_VSU1    2              0                 
   USN_VSU1    1              0                 
   仍有后续报告输出
   ---    END
   ```

   ```
   %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1";%%
   RETCODE = 0  操作成功。

   操作结果如下
   ------------
   总的eNodeB数目  =  0
   (结果个数 = 5)
   共有2个报告
   ---    END
   ```

#### 输出结果说明

| 输出项名称      | 输出项解释                                                       |
|:-----------|:------------------------------------------------------------|
| RU名称       | 参数含义：当“查询场景”为“DISTRIBUTED(分布查询)”时，用于描述SGP进程所在的RU名称。         |
| 进程号        | 参数含义：当“查询场景”为“DISTRIBUTED(分布查询)”时，用于描述SGP进程的进程号。            |
| eNodeB个数   | 参数含义：当“查询场景”为“DISTRIBUTED(分布查询)”时，用于描述当前查询的SGP进程上的eNodeB数目。 |
| 总的eNodeB数目 | 参数含义：用于描述当前命令查询出来的eNodeB总数。                                 |