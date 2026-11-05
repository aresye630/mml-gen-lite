# 查询DCI消息优先级(LST DBMSGPRIORITY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询DCI消息优先级：

- 若需要查询全部DCI消息优先级的配置信息，请不要输入任何参数。
- 若需要查询某些DCI消息优先级的配置信息，请输入“业务消息”参数或“DCI访问优先级”参数或这两个参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                 |
|:-----------|:---------|:-----------------------------------------------------|
| MSGTYPE    | 业务消息     | 用于指示系统按照哪种业务消息来查询DCI消息优先级信息；若不输入，则表示所有的业务消息。         |
| DBPRIORITY | DCI访问优先级 | 用于指示系统按照哪种DCI访问优先级来查询DCI消息优先级信息；若不输入，则表示所有的DCI访问优先级。 |

## 使用实例

1. 查询所有DCI消息优先级的配置信息。

   ```
   LST DBMSGPRIORITY:;
   ```

   ```
   %%LST DBMSGPRIORITY:;%%
   RETCODE = 0  操作成功
   查询结果如下
   ------------
    业务消息                    应用类型  DCI访问优先级          
    AIR                         S6a/S6d   DCI_NORMAL_PRIORITY_MSG
    ULR                         S6a/S6d   DCI_HIGH_PRIORITY_MSG  
    SEND_ROUTING_INFO_FOR_GPRS  MAP       DCI_LOWEST_PRIORITY_MSG
    UPDATE_GPRS_LOCATION        MAP       DCI_HIGH_PRIORITY_MSG  
    UPDATE_LOCATION             MAP       DCI_HIGH_PRIORITY_MSG  
    PROVIDE_SUBSCRIBER_INFO     MAP       DCI_HIGH_PRIORITY_MSG  
    INSERT_SUBSCRIBER_DATA      MAP       DCI_HIGH_PRIORITY_MSG  
    CANCEL_LOCATION             MAP       DCI_HIGH_PRIORITY_MSG  
    SEND_PARAMETERS             MAP       DCI_LOWEST_PRIORITY_MSG
    SEND_AUTHENTICATION_INFO    MAP       DCI_NORMAL_PRIORITY_MSG
    SEND_ROUTING_INFORMATION    MAP       DCI_NORMAL_PRIORITY_MSG
    SEND_ROUTING_INFO_FOR_LCS   MAP       DCI_LOWEST_PRIORITY_MSG
    SEND_ROUTING_INFO_FOR_SM    MAP       DCI_LOWEST_PRIORITY_MSG
    AAR                         AAA       DCI_NORMAL_PRIORITY_MSG
    DER                         AAA       DCI_LOW_PRIORITY_MSG   
    RTR                         AAA       DCI_HIGH_PRIORITY_MSG  
    PPR                         AAA       DCI_HIGH_PRIORITY_MSG  
    STR                         AAA       DCI_NORMAL_PRIORITY_MSG
   (结果个数 = 18)
   ---    END
   ```
2. 查询“业务消息”为“SEND\_PARAMETERS”的DCI消息优先级的配置信息。

   ```
   LST DBMSGPRIORITY: MSGTYPE=SEND_PARAMETERS;
   ```

   ```
   %%LST DBMSGPRIORITY: MSGTYPE=SEND_PARAMETERS;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
        业务消息  =  SEND_PARAMETERS
        应用类型  =  MAP
   DCI访问优先级  =  DCI_LOWEST_PRIORITY_MSG
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**SET DBMSGPRIORITY**

命令的参数说明，表1列出的是未包含在

**SET DBMSGPRIORITY**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                                                                                                      |
|:--------|:---------------------------------------------------------------------------------------------------------------------------|
| 应用类型    | 用于返回查询消息所属的应用类型：S6a/S6d：查询的消息属于Diameter协议S6a/S6d接口应用层消息。MAP：查询的消息属于MAP协议应用层消息。AAA：查询的消息属于Diameter协议S6b、SWm及STa/SWa接口应用层消息。 |