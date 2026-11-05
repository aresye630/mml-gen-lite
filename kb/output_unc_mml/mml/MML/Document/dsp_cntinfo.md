# 查询容器部署信息（DSP CNTINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统中的容器部署信息。

## 注意事项

无。

## 参数说明

| 参数标识               | 参数名称   | 参数说明                                                                                                                                        |
|:-------------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| CNTINFO_MEID       | 网元ID   | 可选必选说明：可选参数。 参数含义：当前需要查询的网元ID；若不输入，则表示查询所有。 取值范围：整数类型，取值范围0~65535。 默认值：无。 配置原则：无。                                                           |
| CNTINFO_QUERY_TYPE | 查询类型   | 可选必选说明：可选参数。 参数含义：用于指示系统当前的查询类型；若不输入，则表示查询所有。 取值范围： byContainerType(容器类型)byNode(节点名称) 默认值：无。 配置原则：无。                                        |
| CNTINFO_CNT_TYPE   | 容器类型   | 可选必选说明：该参数在“查询类型”取值为“byContainerType(容器类型)”时为必选参数。 参数含义：用于指示系统按照容器类型查询部署信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP CNTINFO命令查询容器类型。 |
| CNTINFO_NODE_NAME  | 节点名称   | 可选必选说明：该参数在“查询类型”取值为“byNode(节点名称)”时为必选参数。 参数含义：用于指示系统按照节点名称查询部署信息。 取值范围：字符串类型，字符串长度范围为2~256个字符。 默认值：无。 配置原则：通过DSP CNTINFO命令查询节点名称。          |

## 使用实例

1. 按照节点名称查询容器部署信息

```
%%DSP CNTINFO: CNTINFO_MEID=0, CNTINFO_QUERY_TYPE=byNode, CNTINFO_NODE_NAME="xxxx";%% 
RETCODE = 0  执行成功    
网元ID  容器类型              节点名称         Pod名称                           容器ID                                                                                  
0       cspopsagent-software  xxxx             cspopsagent-jtfnh                 nodeName:xxxx/podName:cspopsagent-jtfnh/containerType:cspopsagent-software   
0       NULL                  xxxx             cspagentmanager-74bcd589f4-czs72  nodeName:xxxx/podName:cspagentmanager-74bcd589f4-czs72/containerType:        
0       kafka-software        xxxx             kafka-30074789-1                  nodeName:xxxx/podName:kafka-30074789-1/containerType:kafka-software          
(结果个数 = 3)  
---    END
```

2. 按照容器类型查询容器部署信息

```
%%DSP CNTINFO: CNTINFO_MEID=0, CNTINFO_QUERY_TYPE=byContainerType, CNTINFO_CNT_TYPE="cspopsagent-software";%% 
RETCODE = 0  执行成功      
网元ID    =  0 
容器类型  =  cspopsagent-software 
节点名称  =  xxxx  
Pod名称   =  cspopsagent-jtfnh   
容器ID    =  nodeName:xxxx/podName:cspopsagent-jtfnh/containerType:cspopsagent-software 
(结果个数 = 1)  
---    END
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明表1 输出项说明所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

| 输出项名称   | 输出项解释          |
|:--------|:---------------|
| 网元ID    | 容器所在网元ID，即应用ID |
| 容器类型    | 容器的类型          |
| 节点名称    | 容器所在的节点名称      |
| Pod名称   | 容器所在的Pod名称     |
| 容器ID    | 容器的唯一标识ID      |

|   错误码 | 消息解释             | 原因分析                   | 处理建议           |
|------:|:-----------------|:-----------------------|:---------------|
| 20002 | 查询mk失败           | ModuleKeeper服务故障或网络异常。 | 重试或联系华为技术支持处理。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。           | 修改查询条件后重试。     |