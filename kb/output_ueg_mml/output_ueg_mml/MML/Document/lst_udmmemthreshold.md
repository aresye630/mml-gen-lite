# 查询UDM服务内存告警阈值(LST UDMMEMTHRESHOLD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UDM服务内存告警阈值。

- 若需要查询所有配置的UDM服务内存告警阈值配置信息，请不要输入任何参数。
- 若需要查询某个UDM服务内存告警阈值配置信息，请输入“服务类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST     | 服务类型   | 可选必选说明：可选参数 参数含义：用于指定系统按照哪个服务类型查询UDM服务内存告警阈值；若不输入，则表示查询所有的UDM服务内存告警阈值。 取值范围： UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmSubServiceIWF(UdmSubServiceIWF)UdmAuthService(UdmAuthService)UdmAlbService(UdmAlbService)EnumService(EnumService) 默认值：无 配置原则：无 |

## 使用实例

1. 查询所有的UDM服务内存告警阈值配置信息：

   ```
   LST UDMMEMTHRESHOLD:;
   ```

   ```
   %%LST UDMMEMTHRESHOLD:;%%
   RETCODE = 0  操作成功

   服务类型            内存阈值  

   UdmTcpService       1024
   UdmHttpService      2048
   UdmAppCtrlService   800
   NRFClient           2048
   HttpDisCtrlService  900
   UdmSubService       4608
   UdmSubServiceIWF    4608
   UdmAuthService      1536
   UdmAlbService       2048
   EnumService         1536
   (结果个数 = 10)

   ---    END
   ```
2. 查询“服务类型”参数为“UdmTcpService(UdmTcpService)”的配置信息：

   ```
   LST UDMMEMTHRESHOLD: ST=UdmTcpService;
   ```

   ```
   %%LST UDMMEMTHRESHOLD: ST=UdmTcpService;%%
   RETCODE = 0  操作成功

   服务类型  =  UdmTcpService
   内存阈值  =  1024
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**MOD UDMMEMTHRESHOLD**命令的参数。