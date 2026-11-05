# 发送CSDB的软件调试命令(STR DBSFTD)

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令为专家维护命令，用于向主机发送软件调试命令。

#### 注意事项

- 该命令需要慎重使用，必须在华为技术支持人员的指导下操作。
- 不同的模块有不同的软调名称，不同的软调名称也有不同的参数，如果软调名称和参数输入不准确，不会出现错误提示。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称        | 参数说明                                                                                                                                                                                                                  |
|:-----------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INSTANCEID | 子实例标识       | 可选必选说明：必选参数。 参数含义：该参数用于指定唯一一个子实例，可以通过DSP DBINSTANCE命令查询获取。 数据来源：本端规划 取值范围：1～100。 默认值：无。                                                                                                                               |
| CSTYPE     | 客户端服务端类型    | 可选必选说明：必选参数。 参数含义：该参数用于指定是客户端还是服务端。 数据来源：本端规划 取值范围：“CLIENT”：向客户端发送软调命令。“SERVER”：向服务端发送软调命令。 默认值：无。                                                                                                                    |
| VNFCID     | 虚拟化网络功能组件标识 | 可选必选说明：条件必选参数。 参数含义：该参数用于指定客户端进程所在的VNFC标识，可以通过DSP DBPLUGIN命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“CLIENT”后生效。 数据来源：本端规划 取值范围：0～4294967295。 默认值：无。                                                                              |
| PLUGINID   | 插件标识        | 可选必选说明：条件可选参数。 参数含义：该参数用于指定客户端进程指定的插件标识，可以通过DSP DBPLUGIN命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“CLIENT”后生效。 数据来源：本端规划 取值范围：0～4294967295。 默认值：无。                                                                                |
| RUNAME     | 资源单元名称      | 可选必选说明：条件必选参数。 参数含义：该参数用于指定服务端进程所在的资源单元名称，可以通过LST SERVICERUSTATE命令查询获取。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                          |
| NODETYPE   | 节点类型        | 可选必选说明：条件必选参数。 参数含义：该参数用于指定服务端进程的类型。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：“CONTROL”：向控制节点（PRP进程）发送软调命令。“STORAGE”：向存储节点（DNP进程）发送软调命令。 默认值：无。                                                              |
| NODENO     | 同类进程实例号     | 可选必选说明：条件可选参数。 参数含义：该参数用于指定同类型进程在资源单元内的排序序号，从0开始排序。 前提条件：该参数在“CSTYPE”参数设置为“SERVER”后生效。 数据来源：本端规划 取值范围：0～63。 默认值：无。 配置原则：如果“节点类型”是“CONTROL”，本参数的值应为“0”。如果“节点类型”是“STORAGE”，本参数的值必须小于STORAGE节点数的最大值。不输入该参数可对指定类型的所有节点生效。 |
| SFNAME     | 软件调试名称      | 可选必选说明：必选参数。 参数含义：该参数用于指定软调函数的名称。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                                                                                                   |
| PARA1      | 参数1         | 可选必选说明：可选参数。 参数含义：该参数用于指定软件调试命令下发的参数1。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                                                                                              |
| PARA2      | 参数2         | 可选必选说明：可选参数。 参数含义：该参数用于指定软件调试命令下发的参数2。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                                                                                              |
| PARA3      | 参数3         | 可选必选说明：可选参数。 参数含义：该参数用于指定软件调试命令下发的参数3。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                                                                                              |
| PARA4      | 参数4         | 可选必选说明：可选参数。 参数含义：该参数用于指定软件调试命令下发的参数4。 数据来源：本端规划 取值范围：不超过63个英文字符。 默认值：无。                                                                                                                                              |

#### 使用实例

目前可执行的软调函数：

1. CSDB插件快速恢复数据：

   该软调用来触发CSDB插件向服务侧快速恢复生产者数据。该软调函数入参说明：
   - “软件调试名称”固定为“QUICK\_RECOVERY”。
   - “参数1”、“参数2”、“参数3”、“参数4”为空。

   以恢复子实例8的生产者数据举例：`STR DBSFTD: INSTANCEID=8, CSTYPE=CLIENT, VNFCID=4, SFNAME="QUICK_RECOVERY";`
2. 设置内存申请类型：

   该软调用来设置GMDB内存申请类型。该软调函数入参说明：
   - “软件调试名称”固定为“SET\_MALLOC\_TYPE”。
   - “参数1”为申请内存类型。0表示使用jemalloc的内存管理，0为默认值。1表示使用jemalloc并带内存泄漏检查的内存管理。2表示使用适配的内存管理。
   - “参数2”、“参数3”、“参数4”为空。

   以设置GMDB内存申请类型为jemalloc并带内存泄漏检查的内存管理举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SET_MALLOC_TYPE", PARA1="1";`
3. 显示进程状态信息：

   该软调用来显示进程状态信息。该软调函数入参说明：
   - “软件调试名称”固定为“PROCSTATUS”。
   - “参数1”、“参数2”、“参数3”、“参数4”为空。

   以查询子实例7的实例的进程状态信息举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="PROCSTATUS";`
4. 清除流控信息表状态统计：

   该软调用来把流控信息表状态统计项清零。该软调函数入参说明：
   - “软件调试名称”固定为“FLOWCTRL\_STATS\_CLEAR”。
   - “参数1”、“参数2”、“参数3”、“参数4”为空。

   以清除子实例7的实例流控信息表状态统计举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="FLOWCTRL_STATS_CLEAR";`
5. 设置允许超过流控阈值的最大次数：

   该软调用来设置允许超过流控阈值的最大次数。该软调函数入参说明：
   - “软件调试名称”固定为“FLOWCTRL\_SET\_MAX\_CYC”。
   - “参数1”为设置流控允许超过阈值的最大次数。
   - “参数2”、“参数3”、“参数4”为空。

   以子实例ID为7的实例允许超过流控阈值最大次数为10举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="FLOWCTRL_SET_MAX_CYC",PARA1="10";`
6. 配置插件侧和服务侧核查开关：

   该软调用来设置插件侧和服务侧核查开关。该软调函数入参说明：
   - “软件调试名称”固定为“PLUGIN\_CHECK\_SWITCH”。
   - “参数1”为核查类型。0为插件侧快速核查。1为插件侧慢速核查。2为服务侧核查消息开关。3为三个同时控制。
   - “参数2”为核查开关状态。0为关闭。其他值为打开。
   - “参数3”、“参数4”为空。

   以配置子实例7的实例设置插件侧慢速核查开关为关闭举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="PLUGIN_CHECK_SWITCH",PARA1="1",PARA2="0";`
7. 设置检查函数执行开关：

   该软调用来设置检查函数执行开关。该软调函数入参说明：
   - “软件调试名称”固定为“PLUGIN\_CHECK\_FUNC\_EXE”。
   - “参数1”为设置对象类型。0为设置检查开关。1为设置最大执行时间。
   - “参数2”为核查开关状态。设置检查开关时0为关闭，其他值为打开。设置最大执行时间时单位为秒。
   - “参数3”、“参数4”为空。

   以配置子实例7的实例设置检查开关为关闭举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="PLUGIN_CHECK_FUNC_EXE",PARA1="0",PARA2="0";`
8. 设置插件侧输出PID开关：

   该软调用来设置插件侧是否需要输出PID。该软调函数入参说明：
   - “软件调试名称”固定为“PLUGIN\_PRINT\_PID”。
   - “参数1”为插件PID输出开关。0为不输出。1为输出。
   - “参数2”、“参数3”、“参数4”为空。

   以配置子实例7的实例设置PID输出开关为关闭举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="PLUGIN_PRINT_PID",PARA1="0";`
9. 设置插件侧数据面日志打印开关：

   该软调用来设置插件侧是否需要输出数据面日志。该软调函数入参说明：
   - “软件调试名称”固定为“PLUGIN\_SMART\_LOG”。
   - “参数1”为数据面日志输出开关。0为不输出。1为输出。
   - “参数2”、“参数3”、“参数4”为空。

   以配置子实例7的实例设置数据面日志输出开关为关闭举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="PLUGIN_SMART_LOG",PARA1="0";`
10. SRVO服务状态核查：

    该软调用来手工触发一次SRVO的服务状态核查。该软调函数入参说明：
    - “软件调试名称”固定为“SERVICE\_RESUME”。
    - “参数1”为子实例ID。
    - “参数2”、“参数3”、“参数4”为空。

    以触发子实例7的实例的SRVO服务状态核查举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SERVICE_RESUME", PARA1="7";`
11. 修改服务侧副本个数：

    该软调用来修改服务侧副本个数。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_SET\_REP”。
    - “参数1”为集群ID。
    - “参数2”为副本个数。
    - “参数3”、“参数4”为空。

    以子实例7集群ID为1的实例配置副本个数为2举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_REP", PARA1="1", PARA2="2";`
12. 触发反亲和性修复：

    该软调用来触发反亲和性修复。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_ANTI\_AFFINITY\_REPAIR”。
    - “参数1”、“参数2”、“参数3”、“参数4”为空。

    以配置子实例7的实例触发反亲和性修复举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_ANTI_AFFINITY_REPAIR";`
13. 设置数据均衡模式：

    该软调用来设置数据均衡模式。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_SET\_GMDB\_DATA\_REBALANCE”。
    - “参数1”为集群ID。
    - “参数2”为数据均衡模式。“RU\_ID”表示设置当前集群为RU\_ID数据均衡模式。“HOST\_ID”表示设置当前集群为HOST\_ID数据均衡模式。
    - “参数3”、“参数4”为空。

    以配置子实例7集群ID为1的实例RU\_ID数据均衡模式举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_GMDB_DATA_REBALANCE", PARA1="1", PARA2="RU_ID";`
14. 修改墓碑表字段值：

    该软调用来设置墓碑表中延迟删除启动与关闭和延迟删除时间字段的值。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_SET\_GMDB\_CONFIG\_TABLE\_TOMBSTONE”。
    - “参数1”为集群ID。
    - “参数2”为TombstoneTable表的字段修改值。取值格式为“table:<table\_id>;flag:<delay\_delete\_flag>;time:<delay\_delete\_time>”。
      - table\_id指定表id，对所有表操作可使用all。
      - delay\_delete\_flag指定是否开启延迟删除功能，0为关闭，1为开启。可缺省，表示维持原值不变。
      - delay\_delete\_time设置延迟删除时间，单位为秒，范围0~31536000。可缺省，表示维持原值不变。
    - “参数3”、“参数4”为空。

    以配置子实例7集群ID为1的实例开启表id为1000的数据表延迟删除功能举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_GMDB_CONFIG_TABLE_TOMBSTONE", PARA1="1", PARA2="table:<1000>;flag:<1>;";`
15. 持久化参数配置：

    该软调用来配置持久化参数。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_SET\_PERSIST\_PARA”。
    - “参数1”为集群ID。
    - “参数2”为持久化参数类型。
    - “参数3”为持久化参数值。
    - “参数4”为空。

    以配置子实例7集群ID为1持久化参数类型为PERSIST\_HLV\_SCAN\_NUM且扫描数为100的实例举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_PERSIST_PARA", PARA1="1", PARA2="PERSIST_HLV_SCAN_NUM",PARA3="100";`
16. CSDB修改集群ID构造模式：

    该软调用来修改双活容灾场景下集群ID构造模式。该软调函数入参说明：
    - “软件调试名称”固定为“SM\_SET\_TRANSVERSION”。
    - “参数1”为控制参数，取值范围为0~1，模式0采用BIT方式构造集群ID；模式1采用偏移量方式构造集群ID。
    - “参数2”、“参数3”、“参数4”为空。

    以使用BIT方式构造ClusterId举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_TRANSVERSION", PARA1="0";`

    以使用偏移量方式构造ClusterId举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_SD_RU_0064", NODETYPE=CONTROL, SFNAME="SM_SET_TRANSVERSION", PARA1="1";`
17. 导出实例表定义信息：

    该软调用来导出实例的表定义信息。该软调函数入参说明：
    - “软件调试名称”固定为“OUTPUT\_TBL\_DEF”。
    - “参数1”、“参数3”、“参数4”为空。
    - “参数2”为表版本类型，取值为“old”表示低版本，取值为“new”表示高版本。

    以导出子实例7低版本表定义举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_OM_RU_0001", NODETYPE=STORAGE, SFNAME="OUTPUT_TBL_DEF", PARA2="old";`
18. 读取低版本表定义信息：

    该软调用来读取低版本表定义信息。该软调函数入参说明：
    - “软件调试名称”固定为“SET\_LOW\_TBL”。
    - “参数2”、“参数3”、“参数4”为空。
    - “参数1”固定为“file”。

    以子实例7读取低版本表定义信息举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_OM_RU_0001", NODETYPE=STORAGE, SFNAME="SET_LOW_TBL", PARA1="file";`
19. 设置表数据版本转换：

    该软调用来设置表数据版本转换。该软调函数入参说明：
    - “软件调试名称”固定为“SET\_TBL\_TRANS”。
    - “参数2”、“参数3”、“参数4”为空。
    - “参数1”为表数据转换目标版本类型，取值为“low”表示低版本，取值为“high”表示高版本。

    以将子实例7表数据从低版本转换成高版本举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=SERVER, RUNAME="CSDB_OM_RU_0001", NODETYPE=STORAGE, SFNAME="SET_TBL_TRANS", PARA1="high";`
20. 清理CSDB提交队列：

    该软调用来清理CSDB的提交队列。该软调参数入参说明：

    - “软件调试名称”固定为“PLUGIN\_RESET\_QUEUE”。
    - “参数1”、“参数2”、“参数3”、“参数4”为空。

    以清理子实例7的DB提交队列举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="PLUGIN_RESET_QUEUE";`
21. 设置扫描步骤：

    该软调用来设置扫描步骤。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_TRANS\_TIME\_STEP”。
    - “参数1”为设置的扫描步骤。如果step小于CSDB\_TRANSPORT\_DEFAULT\_DIVIDE\_STEP未流控的普通插件扫描提交Step，或大于CSDB\_TRANSPORT\_MAX\_DIVIDE\_STEP插件最大提交Step，则打印错误信息。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7的扫描步骤为20举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_TRANS_TIME_STEP", PARA1="20";`
22. 设置数据恢复模式：

    该软调用来设置数据恢复的模式。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_RECOVERY\_MODE”。
    - “参数1”用于设置数据恢复最大速率的模式。0表示以原始速率恢复，1表示限制最大速率恢复，2表示速率按照分区恢复，当取值大于等于3时打印错误日志。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7的数据恢复模式为限制最大速率恢复举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_RECOVERY_MODE", PARA1="1";`
23. 设置数据恢复最大速率：

    该软调用来设置数据恢复的最大速率。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_RECOVERY\_RATE”。
    - “参数1”用于设置数据恢复的最大速率。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7的数据恢复最大速率为1000举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_RECOVERY_RATE", PARA1="1000";`
24. 设置是否启动丢包反压流控机制：

    该软调用来设置是否启动丢包流控机制。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_CTRL”。
    - “参数1”用于设置是否启动丢包流控机制。1表示启动流控机制，传入设置扫描步骤函数的实参为CSDB\_TRANSPORT\_QUICK\_DIVIDE\_STEP轻量插件和流控的普通插件扫描提交step；否则为不启动流控，传入设置扫描步骤函数的实参为CSDB\_TRANSPORT\_DEFAULT\_DIVIDE\_STEP未流控的普通插件扫描提交step。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7启动丢包反压流控机制举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_CTRL", PARA1="1";`
25. 设置单分区60秒发送最大/默认/最小消息数：

    该软调用来在启动丢包流控机制时，设置单分区60秒发送的最大/默认/最小消息数。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_DIV\_SUBMIT\_RATE”。
    - “参数1”为单分区60秒发送最大消息数，当小于默认消息数时打印错误信息。
    - “参数2”为单分区60秒发送默认消息数，当小于最小消息数时打印错误信息。
    - “参数3”为单分区60秒发送最小消息数。
    - “参数4”为空。

    以设置子实例7的单分区60秒发送的最大消息数为1200，默认消息数为120，最小消息数为10举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_DIV_SUBMIT_RATE", PARA1="1200", PARA2="120", PARA3="10";`
26. 设置队列过载阈值：

    该软调用来在启动丢包流控机制时，设置队列过载阈值。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_QUEUE\_THRESHOLD”。
    - “参数1”为单分区队列过载阈值，当大于PLUGIN\_DIV\_QUEUE\_MAX\_NUM\_THRES单分区队列过载最大操作个数时打印错误信息。
    - “参数2”为所有分区队列过载阈值百分比，当大于PLUGIN\_ALL\_QUEUE\_MAX\_PERCENT\_THRES所有分区队列过载最大阈值时打印错误信息。
    - “参数3”、“参数4”为空。

    以设置子实例7的单分区队列过载阈值为50，整队列过载阈值百分比为80举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_QUEUE_THRESHOLD", PARA1="50", PARA2="80";`
27. 设置丢包率：

    该软调用来在启动丢包流控机制时，设置丢包率。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_LOSS\_THRESHOLD”。
    - “参数1”为丢包率，当大于PLUGIN\_PERCENT\_100时打印错误信息。
    - “参数2”为丢包数量。
    - “参数3”、“参数4”为空。

    以设置子实例7的丢包率为80，丢包数量为5举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_LOSS_THRESHOLD",PARA1="80", PARA2="5";`
28. 设置丢包处理策略：

    该软调用来在启动丢包流控机制时，设置丢包处理策略。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_LOSS\_POLICY”。
    - “参数1”为丢包场景下窗口打压等级1，表示丢包场景下触发丢包流控后每秒调小窗口值，当小于窗口打压等级2时打印错误信息。
    - “参数2”为丢包场景下窗口打压等级2。
    - “参数3”、“参数4”为空。

    以设置子实例7的丢包场景下触发丢包流控后每秒调小的窗口打压等级1为20，窗口打压等级2为10举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_LOSS_POLICY", PARA1="20", PARA2="10";`
29. 设置不丢包处理策略：

    该软调用来在启动丢包流控机制时，设置不丢包处理策略。该软调参数入参说明：

    - “软件调试名称”固定为“SET\_PACKET\_NORMAL\_POLICY”。
    - “参数1”为非丢包场景下窗口调大等级1，表示非丢包场景下触发丢包流控后每秒调大窗口值，当小于窗口调大等级2时打印错误信息。
    - “参数2”为非丢包场景下窗口调大等级2。
    - “参数3”、“参数4”为空。

    以设置子实例7的非丢包场景下触发丢包流控后每秒调大的窗口调大等级1为20，窗口调大等级2为10举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="SET_PACKET_NORMAL_POLICY", PARA1="20", PARA2="10";`
30. 插件设置带宽压缩开关：

    该软调用来设置是否启动带宽压缩机制。该软调参数入参说明：

    - “软件调试名称”固定为“BANDWIDTH\_COMPRESS”。
    - “参数1”用于设置是否启动带宽压缩机制。0表示使用对外API接口配置值，1表示使用lz4压缩算法压缩，2表示使用zstd压缩算法压缩，3表示关闭带宽压缩功能。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7开启带宽压缩功能并使用lz4进行压缩举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="BANDWIDTH", PARA1="1";`
31. 插件设置带宽压缩阈值：

    该软调用来在启动带宽压缩机制时，设置带宽压缩消息的最小长度。该软调参数入参说明：

    - “软件调试名称”固定为“COMPRESS\_MSG\_SIZE”。
    - “参数1”用于设置带宽压缩消息的最小长度，单位字节，即超过该阈值的消息才进行压缩，低于该阈值的消息不进行压缩。
    - “参数2”、“参数3”、“参数4”为空。

    以设置子实例7的带宽压缩阈值为8000字节举例：`STR DBSFTD: INSTANCEID=7, CSTYPE=CLIENT, VNFCID=999, SFNAME="COMPRESS_MSG_SIZE", PARA1="8000";`