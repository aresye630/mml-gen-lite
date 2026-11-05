# 查询CSDB的统计信息（DSP DBSTATS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询CSDB的统计信息。

#### 注意事项

针对参数"CSTYPE" （客户端服务端类型）取值为“CLIENT”的查询，存在如下约束：

- 通过命令**DSP DBINSTANCE**查询CSDB子实例信息时， 返回信息中初始容量和总容量为0的不支持查询。
- 通过命令**DSP DBINSTANCE**查询CSDB子实例信息时， 返回信息中初始容量和总容量不为0，但是通过命令**DSP DBPLUGIN**查询CSDB插件信息时，返回信息为“NLS或插件不存在”的不支持查询。
- 通过命令**DSP DBINSTANCE**查询CSDB子实例信息时， 返回信息中初始容量和总容量不为0，且通过命令**DSP DBPLUGIN**能成功查询到CSDB插件信息时，支持查询。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称        | 参数说明                                                                                                                                                                                                                  |
|:-----------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INSTANCEID | 子实例标识       | 可选必选说明：必选参数。 参数含义：该参数用于指定唯一一个子实例，可以通过DSP DBINSTANCE命令查询获取。 数据来源：本端规划 取值范围：1～100。 默认值：无。                                                                                                                               |
| CSTYPE     | 客户端服务端类型    | 可选必选说明：必选参数。 参数含义：该参数用于指定是客户端还是服务端。 数据来源：本端规划 取值范围：“CLIENT”：显示客户端的统计信息。“SERVER”：显示服务端的统计信息。 默认值：无。                                                                                                                    |
| VNFCID     | 虚拟化网络功能组件标识 | 可选必选说明：条件必选参数。 参数含义：该参数用于指定客户端进程所在的VNFC标识，可以通过DSP DBPLUGIN命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“CLIENT”后生效。 数据来源：本端规划 取值范围：0～4294967295。 默认值：无。                                                                              |
| PLUGINID   | 插件标识        | 可选必选说明：条件可选参数。 参数含义：该参数用于指定客户端进程指定的插件标识，可以通过DSP DBPLUGIN命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“CLIENT”后生效。 数据来源：本端规划 取值范围：0～4294967295。 默认值：无。                                                                                |
| RUNAME     | 资源单元名称      | 可选必选说明：条件必选参数。 参数含义：该参数用于指定服务端进程所在的资源单元名称，可以通过LST SERVICERUSTATE命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                          |
| NODETYPE   | 节点类型        | 可选必选说明：条件必选参数。 参数含义：该参数用于指定服务端进程的类型。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：“CONTROL”：显示控制节点（PRP进程）的数据表信息。“STORAGE”：显示存储节点（DNP进程）的数据表信息。 备注：暂不支持节点类型为“CONTROL”的信息表查询操作。 默认值：无。                             |
| NODENO     | 同类进程实例号     | 可选必选说明：条件可选参数。 参数含义：该参数用于指定同类型进程在资源单元内的排序序号，从0开始排序。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：0～63。 默认值：无。 配置原则：如果“节点类型”是“CONTROL”，本参数的值应为“0”。如果“节点类型”是“STORAGE”，本参数的值必须小于STORAGE节点数的最大值。不输入该参数可对指定类型的所有节点生效。 |
| STATSTYPE  | 统计类型        | 可选必选说明：必选参数。 参数含义：该参数用于指定统计类型。 数据来源：本端规划 取值范围： “NODEVISIT”：节点访问数据统计信息。 “COMMONSTATS”：除节点外的其他类型数据统计信息。 默认值：COMMONSTATS。                                                                                                |
| COMMANDSTR | 命令字符串       | 可选必选说明：条件必选参数。 参数含义：该参数用于指定统计类型的命令名称。 前提条件：该参数在“STATSTYPE”参数设置为“COMMONSTATS”后生效。 数据来源：本端规划 取值范围：不超过127个英文字符。 默认值：无。                                                                                                   |

#### 使用实例

查询“子集群标识”为“2”、“客户端服务端类型”为“CLIENT”、“虚拟化网络功能组件标识”为“5”、“插件标识”为“50000052”、“统计类型”为“COMMONSTATS”、“命令字符串”为“dsp\_plugin\_distri 11 0”的统计信息：

`DSP DBSTATS: INSTANCEID=2, CSTYPE=CLIENT, VNFCID=5, PLUGINID=50000052, STATSTYPE=COMMONSTATS, COMMANDSTR="dsp_plugin_statis 11 0";`

```
%%DSP DBSTATS: INSTANCEID=2, CSTYPE=CLIENT, VNFCID=5, PLUGINID=50000052, STATSTYPE=COMMONSTATS, COMMANDSTR="dsp_plugin_distri 11 0";%%
RETCODE = 0  执行成功

操作结果如下 
-------------------------
统计信息  =  nls_id:5, plugin_id:50000052
[dsp_plugin_distri table 11]
max_tuple_num                           61200               
act_tuple_num                           25279               
used_index_num                          25279               
productor_num                           25279               
temp_state_num                          23                  
none_submit_num                         2                   
submitting_num                          56                  
owner_num                               25279               
RecIndex, BlockId, DataFea, PlugId, OwnerStamp, RecStamp, LastVer, CurrVer, SubmitTblId, SubmitIndex, SubmitVer, IsDiviModFlag, DiviModFlag, FirSubmitFlag, GmdbVer
[5]: [204, 305, 50000052, 1515481757004, 1215, 4185, 4185, 4294967295][4294967295, 4185, 0, 0, 1, 72057594037927960]
[12]: [777, 312, 50000052, 1515481757014, 1215, 4184, 4184, 4294967295][4294967295, 4184, 0, 0, 1, 72057594037927960]
[14]: [628, 314, 50000052, 1515481757014, 1215, 3261, 3261, 4294967295][4294967295, 3261, 1, 0, 1, 72057594037927965]
[15]: [212, 315, 50000052, 1515481757014, 1215, 3073, 3073, 4294967295][4294967295, 3073, 1, 0, 1, 72057594037927965]
[21]: [607, 301, 50000052, 1515481757004, 1215, 3112, 3112, 4294967295][4294967295, 3112, 0, 0, 1, 72057594037927962]
[25]: [199, 305, 50000052, 1515481757004, 1215, 3163, 3163, 4294967295][4294967295, 3163, 1, 0, 1, 72057594037927965]
[31]: [537, 311, 50000052, 1515481757014, 1215, 4184, 4184, 4294967295][4294967295, 4184, 0, 0, 1, 72057594037927960]
[34]: [1001, 314, 50000052, 1515481757014, 1215, 3154, 3154, 4294967295][4294967295, 3154, 1, 0, 1, 72057594037927963]
[40]: [688, 300, 50000052, 1515481757004, 1215, 3528, 3528, 4294967295][4294967295, 3528, 1, 0, 1, 72057594037927964]
[41]: [124, 301, 50000052, 1515481757004, 1215, 2982, 2982, 4294967295][4294967295, 2982, 1, 0, 1, 72057594037927962]

(Number of results = 1)
---    END
```

查询“子集群标识”为“2”、“客户端服务端类型”为“SERVER”、“资源单元名称”为“CSDB\_SD\_RU\_0064”、“节点类型”为“STORAGE”、“统计类型”为“COMMONSTATS”、“命令字符串”为“GMDB V$CLUSTER”的所有节点的统计信息：

`DSP DBSTATS: INSTANCEID=2, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=STORAGE, STATSTYPE=COMMONSTATS, COMMANDSTR="GMDB V$CLUSTER";`

```
%%DSP DBSTATS: INSTANCEID=2, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=STORAGE, STATSTYPE=COMMONSTATS, COMMANDSTR="GMDB V$CLUSTER";%%
RETCODE = 0  执行成功

操作结果如下 
-------------------------
Statistics  =  {
    "NODE_TYPE": "coordinator",
    "NODE_ID": 0,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=14,csi=267518307,role=0",
    "WAN_LOCATOR": null,
    "STATE": "LEADER",
    "AFFINITY": ""
}{
    "NODE_TYPE": "coordinator",
    "NODE_ID": 1,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=11,csi=267518110,role=0",
    "WAN_LOCATOR": null,
    "STATE": "FOLLOWER",
    "AFFINITY": ""
}{
    "NODE_TYPE": "coordinator",
    "NODE_ID": 2,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=8,csi=267518100,role=0",
    "WAN_LOCATOR": null,
    "STATE": "FOLLOWER",
    "AFFINITY": ""
}{
    "NODE_TYPE": "coordinator",
    "NODE_ID": 3,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=5,csi=267518324,role=0",
    "WAN_LOCATOR": null,
    "STATE": "FOLLOWER",
    "AFFINITY": ""
}{
    "NODE_TYPE": "data node",
    "NODE_ID": 0,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=7,csi=267387024,role=1",
    "WAN_LOCATOR": "net+cslb:dc=1,nls=3,serv=5,token=1",
    "STATE": "NORMAL",
    "AFFINITY": "64"
}{
    "NODE_TYPE": "data node",
    "NODE_ID": 1,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=4,csi=267387248,role=1",
    "WAN_LOCATOR": "net+cslb:dc=1,nls=3,serv=5,token=0",
    "STATE": "NORMAL",
    "AFFINITY": "65"
}{
    "NODE_TYPE": "data node",
    "NODE_ID": 2,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=13,csi=267387231,role=1",
    "WAN_LOCATOR": "net+cslb:dc=1,nls=3,serv=5,token=3",
    "STATE": "NORMAL",
    "AFFINITY": "67"
}{
    "NODE_TYPE": "data node",
    "NODE_ID": 3,
    "VERSION": 1,
    "LOCATOR": "net:nls=3,node=10,csi=267387034,role=1",
    "WAN_LOCATOR": "net+cslb:dc=1,nls=3,serv=5,token=2",
    "STATE": "NORMAL",
    "AFFINITY": "66"
}
(Number of results = 1)
---    END

查询“子集群标识”为“7”、“客户端服务端类型”为“SERVER”、“资源单元名称”为“CSDB_OM_RU_0001”、“节点类型”为“STORAGE”、“统计类型”为“COMMONSTATS”、“命令字符串”为“dsp_trans_info”的所有子实例的数据转换状态信息：
DSP DBSTATS: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_OM_RU_0001", NODETYPE=STORAGE, STATSTYPE=COMMONSTATS, COMMANDSTR="dsp_trans_info";
%%DSP DBSTATS: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_OM_RU_0001", NODETYPE=STORAGE, STATSTYPE=COMMONSTATS, COMMANDSTR="dsp_trans_info";%%
RETCODE = 0  执行成功

操作结果如下 
-------------------------
Statistics  =  
instance 7: trans finished
instance 8: trans finished
(Number of results = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                             |
|:--------|:--------------------------------------------------|
| 统计信息    | 统计信息，例如，插件侧提交次数、远程查询次数，服务侧推送次数等。 取值范围：不超过1023个字符。 |