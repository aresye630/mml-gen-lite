# 修改局向流控配置(MOD MFLOWCTRL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会导致系统异常，需联系华为技术支持确认后再执行。

该命令为配置类命令，修改一个局向流控配置。

## 注意事项

无。

## 参数说明

| 参数ID          | 参数名称          | 参数描述                                                                                                                                                                                                                                                                                |
|:--------------|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCRFID        | PCRF实体ID      | 用于标识PCRF实体，该参数必须先由ADD PCRF命令定义，然后才能在此处索引。 取值范围：1 默认值：无。                                                                                                                                                                                                                             |
| PEERTYPE      | PCRF对端实体类型    | 用于标识PCRF对端实体类型。 取值说明： PCEFDRAAFTDF 默认值：无。                                                                                                                                                                                                                                           |
| PEERID        | PCRF对端实体ID    | 用于标识PCRF对端实体，该参数必须先由ADD PPCEF、ADD PEER或者ADD PAF命令定义，然后才能在此处索引。 取值范围：0～1023 默认值：无。                                                                                                                                                                                                   |
| INTERFACETYPE | 接口类型          | 用于标识PCRF对端接口类型。仅当“PCRF对端实体类型”取值为“DRA”时，可配置此参数。 取值说明： GxRx 默认值：无。                                                                                                                                                                                                                    |
| FLOWCTRL      | 流量控制开关        | 用于设定是否进行局向流控。 如下情况可以配置此参数：“PCRF对端实体类型”配置为“PCEF”、“AF”或“TDF”。“PCRF对端实体类型”配置为“DRA”且配置了“接口类型”。 取值说明： OFF(关闭流控)ON(打开流控) 默认值：OFF。                                                                                                                                                         |
| CCRINUM       | 每秒最大CCR_I消息数量 | 用于设定每秒该局向在每个DLB上允许通过的最大CCR_I消息数量，超过此数量的CCR_I消息将被丢弃。 当“流量控制开关”设置为“ON(打开流控)”且满足如下其中一种配置时，才可以配置此参数。“PCRF对端实体类型”为“PCEF”。“接口类型”为“Gx”。 取值范围：0～1000000 默认值：无。                                                                                                                              |
| CCRUNUM       | 每秒最大CCR_U消息数量 | 用于设定每秒该局向在每个DLB上允许通过的最大CCR_U消息数量，超过此数量的CCR_U消息将被丢弃。 当“流量控制开关”设置为“ON(打开流控)”且满足如下其中一种配置时，才可以配置此参数。“PCRF对端实体类型”为“PCEF”或“TDF”。“接口类型”为“Gx”。 取值范围：0～1000000 默认值：无。                                                                                                                        |
| CCRTNUM       | 每秒最大CCR_T消息数量 | 用于设定每秒该局向在每个DLB上允许通过的最大CCR_T消息数量，超过此数量的CCR_T消息将被丢弃。 当“流量控制开关”设置为“ON(打开流控)”且满足如下其中一种配置时，才可以配置此参数。“PCRF对端实体类型”为“PCEF”或“TDF”。“接口类型”为“Gx”。 取值范围：0～1000000 默认值：无。                                                                                                                        |
| AARINUM       | 每秒最大AAR-I消息数量 | 用于设定每秒该局向在每个DLB上允许通过的最大AAR_I消息数量，超过此数量的AAR_I消息将被丢弃。 当“流量控制开关”设置为“ON(打开流控)”且满足如下其中一种配置时，才可以配置此参数。“PCRF对端实体类型”为“AF”。“接口类型”为“Rx”。 取值范围：0～1000000 默认值：无。  说明： Rx接口消息流控时，Rx-Request-Type AVP取值为“PCSCF_RESTORATION (2)”的AAR消息和Rx-Request-Type AVP取值为“INITIAL_REQUEST (0)”的AAR_I消息为同样的优先级。 |

## 使用实例

1. 修改一个局向流控配置。“PCRF实体ID”为“1”，“PCRF对端实体类型”为“PCEF”,“PCRF对端实体ID”为“0”，“流量控制开关”为“关闭流控”。

   ```
   MOD MFLOWCTRL: PCRFID=1, PEERTYPE=PCEF, PEERID=0, FLOWCTRL=OFF;
   ```
2. 修改一个局向流控配置。“PCRF实体ID”为“1”，“PCRF对端实体类型”为“PCEF”,“PCRF对端实体ID”为“1”，“流量控制开关”为“打开流控”，“每秒最大CCR\_I消息数量”为“800”，“每秒最大CCR\_U消息数量”为“800”，“每秒最大CCR\_T消息数量”为“800”。

   ```
   MOD MFLOWCTRL: PCRFID=1, PEERTYPE=PCEF, PEERID=1, FLOWCTRL=ON, CCRINUM=800, CCRUNUM=800, CCRTNUM=800;
   ```

   **说明** 

   开始局向流控时 ，会把所有流量平均分配给所有配置为Enable的链路。假如配置局向流控的最大CCR\_Initial消息数a为800，最大CCR\_Update消息数b为800，最大CCR\_Termination消息数c为800，该对端设备的链路所关联的DLB数量d为2。

   - 如果对端设备对PCRF的链路使用模式为主备模式，则最大CCR\_Initial，CCR\_Update，CCR\_Termination消息数分别为a，b，c，例如：

     ```
     MOD MFLOWCTRL: PCRFID=1, PEERTYPE=PCEF, PEERID=1, FLOWCTRL=ON, CCRINUM=800, CCRUNUM=800, CCRTNUM=800;
     ```
   - 如果对端设备对PCRF的链路使用模式为负载均衡模式，则最大CCR\_Initial，CCR\_Update，CCR\_Termination消息数分别为a/d，b/d，c/d，例如：

     ```
     MOD MFLOWCTRL: PCRFID=1, PEERTYPE=PCEF, PEERID=1, FLOWCTRL=ON, CCRINUM=400, CCRUNUM=400, CCRTNUM=400;
     ```
3. 修改一个局向流控配置。“PCRF实体ID”为“1”，“PCRF对端实体类型”为“AF”，“PCRF对端实体ID”为“1”，“流量控制开关”为“打开流控”，“每秒最大AAR-I消息数量”为“800”。

   ```
   MOD MFLOWCTRL: PCRFID=1, PEERTYPE=AF, PEERID=1, FLOWCTRL=ON, AARINUM=800;
   ```
4. 修改一个局向流控配置。“PCRF实体ID”为“1”，“PCRF对端实体类型”为“DRA”，“接口类型”为“Rx”，“PCRF对端实体ID”为“1”，“流量控制开关”为“打开流控”，“每秒最大AAR-I消息数量”为“800”。

   ```
   MOD MFLOWCTRL: PCRFID=1, PEERTYPE=DRA, INTERFACETYPE=Rx, PEERID=1, FLOWCTRL=ON, AARINUM=800;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

## 参考信息

无。