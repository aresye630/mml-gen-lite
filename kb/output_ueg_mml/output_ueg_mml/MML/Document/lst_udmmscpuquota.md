# 查询UDM 微服务进程CPU配额(LST UDMMSCPUQUOTA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UDM微服务的进程CPU配额。

- 若需要查询所有UDM微服务进程的CPU配额的配置信息，请不要输入任何参数。
- 若需要查询某个UDM微服务的进程CPU配额的配置信息，请输入“服务类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                    |
|:-------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST     | 服务类型   | 可选必选说明：可选参数 参数含义：用于指示系统按照服务类型来查询CPU配额信息；若不输入，则表示查询所有的服务类型对应的CPU配额。 取值范围：UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)EnumService(EnumService) 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有的微服务进程CPU配额的配置信息：

   ```
   LST UDMMSCPUQUOTA:;
   ```

   ```
   %%LST UDMMSCPUQUOTA:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   服务类型            CPU配额  

   UdmAppCtrlService   100      
   NRFClient           100      
   HttpDisCtrlService  100      
   UdmSubService       600      
   UdmAuthService      600 
   EnumService         100          
   (结果个数 = 6)

   ---    END
   ```
2. 查询“服务类型”为“HttpDisCtrlService(HttpDisCtrlService)”的CPU配额的配置信息：

   ```
   LST UDMMSCPUQUOTA: ST=HttpDisCtrlService;
   ```

   ```
   %%LST UDMMSCPUQUOTA: ST=HttpDisCtrlService;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   服务类型  =  HttpDisCtrlService
    CPU配额  =  100
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**SET UDMMSCPUQUOTA**命令的参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 消息解释      | 原因分析           | 处理建议                           |
|-------:|:----------|:---------------|:-------------------------------|
| 100016 | 参数不在指定范围内 | 输入的参数值不在取值范围内。 | 根据参数的取值范围，重新输入参数的取值，确保其取值符合要求。 |