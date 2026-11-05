# 查询HLR序列号(LST HLRSN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询虚拟HLR的配置信息：

- 若要查询全部虚拟HLR的配置信息，请不要输入任何参数。
- 若要查询某个虚拟HLR配置的配置信息，请输入“虚拟HLR序列号”。

## 注意事项

在混合组网下，仅用于查询本分区的用户信息。当用户从SP迁移至另一个SP、vSP或vRSP时，用户数统计数据通过凌晨校验后更新，执行本命令才会显示实际的用户数。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                        |
|:-------|:--------|:--------------------------------------------|
| HLRSN  | 虚拟HLRSN | 用于指示系统需要查询哪个虚拟HLR的配置信息；若不输入，则表示全部的虚拟HLR序列号。 |

## 使用实例

1. 查询全部虚拟HLR的配置信息，命令如下：

   ```
   LST HLRSN:;
   ```

   ```
   %%LST HLRSN:;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "HLR Index" "Status" "HLR Number" "CCode" "Max number of subscribers" "Fact number of subscribers" "Status"   "OPC"  "LocalHost" "LocalRealm" "Eps Global Data Update Time" "Max number of EPS subscribers" "Fact number of EPS subscribers" "IMSLOCALHOST" "IMSLOCALREALM" "Max number of IMS subscribers" "Fact number of IMS subscribers" "NFGROUPID" "Max number of 5GS subscribers" "Fact number of 5GS subscribers"
           1           MASTER   86131131     86      <NULL>                      0                            NORMALFUNC <NULL> <NULL>      <NULL>       NULL                          <NULL>                          0                                <NULL>         <NULL>          <NULL>                          0                                <NULL>      <NULL>                          0
           22          MASTER   86131131     86      <NULL>                      0                            NORMALFUNC <NULL> <NULL>      <NULL>       NULL                          <NULL>                          0                                <NULL>         <NULL>          <NULL>                          0                                <NULL>      <NULL>                          0
           34          MASTER   1234         086     <NULL>                      0                            NORMALFUNC <NULL> <NULL>      <NULL>       NULL                          <NULL>                          0                                <NULL>         <NULL>          <NULL>                          0                                <NULL>      <NULL>                          0
           35          MASTER   1234         086     <NULL>                      0                            NORMALFUNC <NULL> <NULL>      <NULL>       NULL                          <NULL>                          0                                <NULL>         <NULL>          100000000                       0                                <NULL>      <NULL>                          0
           36          MASTER   1234         086     <NULL>                      0                            NORMALFUNC <NULL> <NULL>      <NULL>       NULL                          <NULL>                          0                                <NULL>         <NULL>          100000000                       0                                <NULL>      <NULL>                          0

   Total count = 5

   There is together 1 report
   ---    END
   ```
2. 查询“HLRSN”为“1”的虚拟HLR的配置信息，命令如下：

   ```
   LST HLRSN: HLRSN=1;
   ```

   ```
   %%LST HLRSN: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                           STATUS = MASTER
                            HLRNO = 86131131
                            CCODE = 86
                       MAXUSERNUM = NULL
                      FACTUSERNUM = 0
                             ATTR = NORMALFUNC
                              OPC = NULL
                        LOCALHOST = NULL
                       LOCALREALM = NULL
          EPSGLOBALDATAUPDATETIME = NULL
                    MAXEPSUSERNUM = NULL
                   FACTEPSUSERNUM = 0
                     IMSLOCALHOST = NULL
                    IMSLOCALREALM = NULL
                    MAXIMSUSERNUM = NULL
                   FACTIMSUSERNUM = 0
                        NFGROUPID = NULL
   		  MAXSAUSERNUM = NULL
                    FACTSAUSERNUM = 0
   				
   				
   Total count = 20

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。各参数含义请见

**ADD HLRSN**

命令，表1中列出的是未包含在

**ADD HLRSN**

命令参数说明中的输出项。

| 输出项名称                                                | 输出项解释                             |
|:-----------------------------------------------------|:----------------------------------|
| FACTSAUSERNUM                                        | 表示当前HLRSN已有的5GS用户数。               |
| EPSGLOBALDATAUPDATETIME(Eps Global Data Update Time) | 用于返回当前HLRSN中EPS全局数据更新的时间。         |
| FACTEPSUSERNUM(Fact number of EPS subscribers)       | 用于返回当前HLRSN中已有的2G/3G/4G用户数和4G用户数。 |
| FACTIMSUSERNUM(Fact number of IMS subscribers)       | 用于返回当前HLRSN中已有的IMS用户数。            |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                         |
|:--------|:--------|:------------------------|:-----------------------------|
| ERR1004 | 无效的参数值  | 输入的“HLR序列号”参数的值不在取值范围内。 | 请重新输入“HLR序列号”参数的值，确保其在取值范围内。 |