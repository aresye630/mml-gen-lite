# 启动eNodeB跟踪区信息同步任务（STR ENBTASYN）

- 命令功能
- 操作场景
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：MME**

该命令用于启动eNodeB跟踪区信息同步任务，可以根据输入参数选择所有eNodeB、以进程为单位或者以eNodeB为单位的同步任务。

#### 操作场景

- 当MME和TSN上的eNodeB跟踪区信息不一致时，操作人员可以执行此命令进行强制同步。
- 选择所有eNodeB选项时，MME触发Start eNodeB TA Information Update Request流程，清除TSN中保存的eNodeB和TA的对应关系，等收到TSN的Start eNodeB TA Information Update Response后，MME再通过Update eNodeB TA Information Request发送全量的eNodeB TA Relationship List。
- 选择以进程为单位或者以eNodeB为单位时，MME通过Update eNodeB TA Information Request发送某部分或某个eNodeB TA Relationship List。

#### 注意事项

- 在Tm接口链路正常的情况下使用。

- 正常情况下不要执行，只有在TSN侧需要MME重新上报时才需要执行。
- 此命令执行后立即生效。

#### 本地用户权限

manage-ug;system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                         |
|:-------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENBTASYNTYPE | TA同步类型   | 可选必选说明：必选参数 参数含义：该参数用于指定同步任务的类型。 取值范围： “ALL（全部eNodeB）”：表示将让所有eNodeB重新上报跟踪区信息。“SPEACIAL_PROCESS（指定SGP进程）”：表示让指定SGP进程上关联的eNodeB重新上报跟踪区信息。“ENODEBID（指定eNodeB ID）”：表示让指定eNodeB重新上报跟踪区信息。 默认值：ALL |
| RUNAME       | RU名称     | 可选必选说明：条件必选参数 参数含义：该参数用于指定需要同步eNodeB跟踪区信息的资源单元名称。该参数可以通过DSP RU命令查询。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“SPEACIAL_PROCESS（指定SGP进程）”值后生效。 取值范围：1~63位字符串 默认值：无                                 |
| PROCID       | 进程号      | 可选必选说明：条件必选参数 参数含义：该参数用于指定需要同步eNodeB跟踪区信息的SGP进程的进程号。该参数可以通过DSP PROCESSLINK命令查询，选取结果中的“相同进程类型的索引”列。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“SPEACIAL_PROCESS（指定SGP进程）”值后生效。 取值范围：0~20 默认值：无      |
| MCC          | 移动国家码    | 可选必选说明：条件必选参数 参数含义：该参数用于指定待同步的eNodeB对应的移动国家代码。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。 数据来源：整网规划 取值范围：位数为3的十进制数字 默认值：无                                             |
| MNC          | 移动网号     | 可选必选说明：条件必选参数 参数含义：该参数用于指定待同步的eNodeB对应的移动网号。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。 数据来源：整网规划 取值范围：2位或者3位十进制数字 默认值：无                                              |
| ENBTYPE      | eNodeB类型 | 可选必选说明：条件必选参数 参数含义：待同步的eNodeB的类型。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。 取值范围： “HOME_ENB(HOME_ENB)”：28位长的eNodeB。“MACRO_ENB(MACRO_ENB)”：20位长的eNodeB。 默认值：无         |
| ENBID        | eNodeB标识 | 可选必选说明：条件必选参数 参数含义：待同步的eNodeB ID。该参数可以通过DSP S1APLNK命令查询。 前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。 取值范围：0~268435455 默认值：无                                            |

#### 使用实例

1. 启动所有eNodeB重新上报跟踪区信息：

   STR ENBTASYN: ENBTASYNTYPE=ALL;
2. 启动进程号为0的SGP进程关联的eNodeB重新上报跟踪区信息：

   STR ENBTASYN: ENBTASYNTYPE=SPEACIAL\_PROCESS, RUNAME="USN\_SP\_RU\_0064", PROCID=0;
3. 启动移动国家代码为460，移动网号为00，标识为1104的eNodeB重新上报跟踪区信息：

   STR ENBTASYN: ENBTASYNTYPE=ENODEB\_ID, MCC="460", MNC="00", ENBTYPE=MACRO\_ENB, ENBID=1104;