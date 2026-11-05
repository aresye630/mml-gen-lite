# 显示计费数据统计信息（DSP CHGDATASTAT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

用来查询计费数据统计信息，比如预定义URR流量上报信息、UserProfile安装次数、整体转发和计费流量差异比例信息、缺省费率流量增量信息、子协议Top30的流量增量信息、预定义规则Top20的匹配次数增量信息、URR Top20的流量增量信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                |
|:----------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STATTYPE        | 统计类型            | 可选必选说明：必选参数 参数含义：该参数用于指定要显示计费数据的统计类型。 数据来源：本端规划 取值范围：ENUM。 UPINSTALL：查询UserProfile安装次数。URRVOLUME：查询URR流量统计信息。WHOLE_VOLUME_CONDITION：整体转发和计费流量差异比例信息。TOPN_URR_VOLUME：URR流量增量Top20信息。RULE_MATCH_NUM：预定义PCC规则Top20的匹配次数增量信息。PROTOCOL_VOLUME：协议Top30的流量增量信息。DEFAULT_URR_VOLUME：缺省费率流量增量信息。 默认值：无 配置原则：无 |
| URRID           | URRID(Predef)   | 可选必选说明：条件可选参数 前提条件：该参数在“STATTYPE”配置为“URRVOLUME”时为可选参数。 参数含义：用于指示URR标识（预定义）。 数据来源：本端规划 取值范围：整数类型，取值范围为0～2147483646。 默认值：无 配置原则：无                                                                                                                                                                     |
| USERPROFILENAME | UserProfileName | 可选必选说明：条件可选参数 前提条件：该参数在“STATTYPE”配置为“UPINSTALL”时为可选参数。 参数含义：该参数用于指定用户模板名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1~63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                              |
| DATETYPE        | 周期类型            | 可选必选说明：条件可选参数 前提条件：该参数在“STATTYPE”配置为“DEFAULT_URR_VOLUME”、“PROTOCOL_VOLUME”、“RULE_MATCH_NUM”、“TOPN_URR_VOLUME” 或 “WHOLE_VOLUME_CONDITION”时为可选参数。 参数含义：该参数用于指定要显示计费数据的查询周期，支持按天查近七天数据或按月查近期6个月数据。 数据来源：本端规划 取值范围：ENUM。 DAY：天。MONTH：月。 默认值：无 配置原则：无                                                    |

#### 使用实例

- 查询URR流量统计数据：

  ```
  %%DSP CHGDATASTAT: STATTYPE=URRVOLUME;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  Charging Data Statistics
  ------------------------
  Result                                                                                                                

  URRID      ReportVolume(Total)  ReportVolume(Today)  ReportVolume(YesterDay)  ReportVolume(The Day Before Yesterday)  
  1          3000                   2970               2940                     2910                                    
  2          4000                   3980               3960                     3940                                                                        
  (Number of results = 3)

  ---    END
  ```
- 查询UserProfile安装次数信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=UPINSTALL;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  UserProfile Installation Count
  ------------------------------
                              UserProfileName  =  up
                            InstallCnt(Total)  =  1
                            InstallCnt(Today)  =  1
                        InstallCnt(Yesterday)  =  0
         InstallCnt(The Day Before Yesterday)  =  0
  (Number of results = 1)

  ---    END
  ```
- 查询协议Top30的流量增量信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=PROTOCOL_VOLUME, DATETYPE=DAY;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  Protocol Volume Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top30 Protocol Volume Information:
  Last 1Day:
  No.  ProtocolName                    Volume
  1    http                            360

  (Number of results = 1)
  ```
- 查询整体转发和计费流量差异比例信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=WHOLE_VOLUME_CONDITION, DATETYPE=DAY;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  whole volume condition
  ----------------------
  Result  =  

  ssgpod-0:
  Lost ratio type     Last 1Day           
  uplinkvolume        0.000%(100/100)              
  dnlinkvolume        0.000%(100/100)              
  uplinkpktnum        0.000%(1/1)              
  dnlinkpktnum        0.000%(1/1)              

  (Number of results = 1)

  ---    END
  ```
- 查询预定义规则Top20的匹配次数增量信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=RULE_MATCH_NUM, DATETYPE=DAY;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  Rule Match Num Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top20 Rule Match Num Information:
  Last 1Day:
  No.  RuleName                                                          RuleMatchNum
  1    rule1                                                             360

  (Number of results = 1)
  ```
- 查询URR Top20的流量增量信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=TOPN_URR_VOLUME, DATETYPE=DAY;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  Top20 URR Volume Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top20 URR Volume Information:
  Last 1Day:
  No.  URRID       Volume
  1    1           1360

  (Number of results = 1)
  ```
- 查询缺省费率流量增量信息：

  ```
  %%DSP CHGDATASTAT: STATTYPE=DEFAULT_URR_VOLUME, DATETYPE=DAY;
  ```

  ```
  %%
  RETCODE = 0  Operation succeeded

  Default URR Volume Statistics
  --------------------------
  Result  =  
  ssgpod-0:
  Volume Type     Last 1Day
  uplink          482
  dnlink          1440

  (Number of results = 1)
  ```

#### 输出结果说明

| 输出项名称                                  | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserProfileName                        | 用于指定用户模板名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| InstallCnt(Total)                      | UserProfile安装次数累计值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| InstallCnt(Today)                      | 今天安装次数增量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| InstallCnt(Yesterday)                  | 昨天安装次数增量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| InstallCnt(The Day Before Yesterday)   | 前天安装次数增量。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| URRID(Predef)                          | 用于指示URR标识（预定义）。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ReportVolume(Total)                    | URR流量累计值，单位为字节。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ReportVolume(Today)                    | 今天流量增量，单位为字节。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ReportVolume(Yesterday)                | 昨天流量增量，单位为字节。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ReportVolume(The Day Before Yesterday) | 前天流量增量，单位为字节。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Result                                 | 查询参数STATTYPE为DEFAULT_URR_VOLUME，查询结果为过去7天或过去6个月的缺省费率流量增量数据。查询参数STATTYPE为PROTOCOL_VOLUME，查询结果为过去7天或过去6个月的协议流量增量的Top30信息。查询参数STATTYPE为RULE_MATCH_NUM，查询结果为过去7天或过去6个月的预定义规则命中次数增量的Top20信息。查询参数STATTYPE为TOPN_URR_VOLUME，查询结果为过去7天或过去6个月的URR流量增量Top20信息。查询参数STATTYPE为WHOLE_VOLUME_CONDITION，查询结果为过去7天或过去6个月转发与计费报文流量和报文数的差异比例，单位为百分比。以上行报文流量为例，显示形式为“上行报文数差异比例(上行计费报文数增量/上行转发报文数增量)”。比例计算公式为：（1）流量差异百分比(%)=(转发报文流量-计费报文流量)/转发报文流量；（2）报文数差异百分比(%)=(转发报文数-计费报文数)/转发报文数。使用实例中，Last 1Day显示为昨日的数据，不含当天已过去时间段的数据。以上数据不足7天，按实际天数显示。Last 1Mth显示为上个月的统计数据，不包含当月已过去时间段的数据。以上数据不足6个月，按实际月数显示。 |