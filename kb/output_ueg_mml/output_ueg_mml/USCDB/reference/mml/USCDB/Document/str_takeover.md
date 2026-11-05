# 启动容灾接管(STR TAKEOVER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，该命令会影响主用局和容灾局之间的数据处理流程。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于手工启动容灾接管。

## 注意事项

- 如果接管方模块号最小的DSG重启，接管状态变为非接管状态，接管方从接管态退出，如需接管，可通过执行本命令启动容灾接管。
- 该命令不允许进行批操作。

## 参数说明

| 参数标识   | 参数名称         | 参数说明                                                                                                                                                         |
|:-------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RLOCID | 远端Location标识 | 用于指定需要接管的远端Location，该参数须在对接的远端USCDB网元中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。 取值范围：1～512 默认值：无。                                                             |
| CT     | Cluster类型    | 用于指定需要接管的Cluster类型。 取值范围：DRU(DRU)DSU(DSU) 默认值：无。                                                                                                             |
| CID    | Cluster标识    | 仅当本命令中的“Cluster类型”参数值为“DSU”时该参数有效，用于指定需要接管的Cluster。该参数是通过ADD CLUSTER定义后在此引用。 取值范围：1～4096 默认值：无。 说明：当不设定参数“Cluster标识”的值时，表示接管指定“远端Location标识”中的所有DSU CLuster。 |

## 使用实例

手动容灾倒换，“远端Location标识”为“1”、“Cluster类型”为“DSU”、“Cluster标识”为“512”：

```
STR TAKEOVER: RLOCID=1, CT=DSU, CID=512;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                       | 原因分析                                                                                                                         | 处理建议                                                                                                                                                                                                                                     |
|-------:|:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   1710 | 无可用模块。                                      | 所有DSU模块全部异常。                                                                                                                 | 请参见产品手册的“模块故障”进行处理。                                                                                                                                                                                                                      |
|   1819 | 部分模块异常。                                     | 部分DSU模块异常。                                                                                                                   | 请按照如下方式排查： 执行DSP CLUSTER查看哪些预期启动接管的Cluster仍未接管。执行DSP NODE查看是否有异常的DSU节点。                                                                                                                                                                  |
|   2117 | Master节点不存在。                                | 不存在Master节点。                                                                                                                 | 请按照如下方式排查： 执行DSP CLUSTER查看哪些预期启动接管的Cluster仍未接管。执行DSP NODE检查对应DSU的节点状态。若DSU模块故障，请参见产品手册的“模块故障”进行处理。                                                                                                                                       |
| 260234 | 输入的DSU Cluster ID不存在。                       | 输入的参数“Cluster标识”在本Location中不存在。                                                                                              | 请执行LST CLUSTER命令查询本地Cluster标识，请重新执行本命令，确保输入的“Cluster标识”在本Location中存在。                                                                                                                                                                    |
| 260367 | 不允许接管Redundancy属性Cluster。                   | 输入参数“远端Location标识”中的指定“Cluster标识”为Redundancy属性。                                                                              | 通过执行DSP CLUSTER命令确认输入的“远端location标识”中的“Cluster标识”是否为Redundancy属性。                                                                                                                                                                        |
| 302002 | 参数RLID指定的远端location标识与本地location标识重复。       | 输入的参数“远端Location标识”与本地Location标识重复。                                                                                          | 请执行LST LOCATION命令查询本地Location标识，请重新执行本命令输入“远端location标识”参数，确保与查询中的不一致。                                                                                                                                                                   |
| 302003 | 远端location不存在。                              | 输入的参数“远端Location标识”不存在，必须先配置远端Location。                                                                                      | 通过ADD RLOCATION命令先配置远端Location，再在本命令中引用。                                                                                                                                                                                                 |
| 331001 | 操作失败。                                       | 失败的可能原因有： “Cluster类型”取值为“DRU”时，DSG模块异常。“Cluster类型”取值为“DSU”时，DSU节点异常。指定的“远端Location标识”在本局中不存在容灾关系的Cluster。链路异常，无法确认指定远端的容灾关系。 | 请按照如下方式排查： 执行DSP CLUSTER查看哪些预期启动接管的Cluster仍未接管。检查对应节点状态。“Cluster类型”取值为“DSU”时，执行DSP NODE检查对应DSU的节点状态。“Cluster类型”取值为“DRU”时，在“CSP MML命令”界面执行DSP MODULE检查对应DSG模块的状态。 若DSU/DSG模块故障，请参见产品手册的“模块故障”进行处理。 执行DSP DSGSCTP检查指定“location标识”的承载网是否正常。 |
| 331002 | 部分操作失败。                                     | 部分DSG/DSU成功启动接管，部分DSG/DSU因为某种错误未能启动接管。                                                                                       | 请按照如下方式排查： 执行DSP CLUSTER查看哪些预期启动接管的Cluster仍未接管。检查对应节点状态。“Cluster类型”取值为“DSU”时，执行DSP NODE检查对应DSU的节点状态。“Cluster类型”取值为“DRU”时，在“CSP MML命令”界面执行DSP MODULE检查对应DSG模块的状态。 若DSU/DSG模块故障，请参见产品手册的“模块故障”进行处理。 执行DSP DSGSCTP检查指定“location标识”的承载网是否正常。 |
| 331004 | 部分操作超时。                                     | 部分DSG/DSU模块未返回响应。                                                                                                            | 请查看是否有异常的DSU节点。 “Cluster类型”取值为“DSU”时，执行DSP NODE查看是否有异常的DSU节点。“Cluster类型”取值为“DRU”时，在“CSP MML命令”界面执行DSP MODULE查看是否有异常的DSG模块。若DSU/DSG模块故障，请参见产品手册的“模块故障”进行处理。                                                                               |
| 337102 | 非A-A组网，不支持执行此命令。                            | STR TAKEOVER命令仅支持A-A组网。                                                                                                      | 非A-A组网，不支持STR TAKEOVER命令，可通过LST INSP命令查询参数“AAMODESWITCH”值，确认当前是否是A-A组网。                                                                                                                                                                  |
| 337103 | 指定的Location在本局不存在容灾关系的Cluster。              | 输入的参数“远端location标识”在本局不存在容灾关系的Cluster。                                                                                       | 通过DSP CLUSTER命令查询输入的参数“远端location标识”在本局是否存在容灾关系的Cluster。                                                                                                                                                                                 |
| 337104 | 指定Location已经被接管。                            | 输入的参数“远端location标识”中所有的Cluster已经为接管状态。                                                                                       | 通过DSP CLUSTER确认指定“远端location标识”中的所有Cluster是否已经被接管。                                                                                                                                                                                       |
| 337105 | 指定DRU或DSU Cluster在本Location中不为Redundancy属性。 | 输入的参数“Cluster类型”指定的DRU或DSU Cluster在本Location中不为容灾属性。                                                                         | 通过DSP CLUSTER命令查询输入的参数“Cluster类型”指定的DRU或DSU Cluster在本Location中是否为容灾属性。                                                                                                                                                                   |
| 337106 | 指定DRU或DSU Cluster已经被接管。                     | 输入的参数“Cluster类型”指定的DRU或DSU Cluster已经为接管状态。                                                                                   | 通过DSP CLUSTER确认输入的参数“Cluster类型”指定的Cluster是否已经被接管。                                                                                                                                                                                        |