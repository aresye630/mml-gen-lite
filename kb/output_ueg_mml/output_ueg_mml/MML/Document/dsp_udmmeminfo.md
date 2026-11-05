# 显示UDM进程内存占用信息(DSP UDMMEMINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UDM进程内存占用信息。

- 若要查询所有服务的进程内存占用信息，请不要输入任何参数。
- 若要查询某个服务的进程内存占用信息，请输入“服务类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                            |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST     | 服务类型   | 可选必选说明：条件可选参数。 参数含义：用于指示系统按照哪个服务类型来查询UDM进程内存占用信息。若不输入，则表示查询所有服务的进程内存占用信息。 取值范围： 全部选中全部清空全部灰化UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UdmAlbService(UdmAlbService)EnumService(EnumService) 默认值：无 配置原则：无 |

## 使用实例

1. 查询所有服务的进程内存占用信息：

   ```
   DSP UDMMEMINFO:;
   ```

   ```
   %%DSP UDMMEMINFO:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   节点号           Pod名称                         SF实例号              分配的内存(MB)  内存占用率(百分比)  

   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13510349538880825641  148             24                  
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13510349538881874029  192             32                  
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13511200354722296972  257             16                  
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13510938086839336060  271             45                  
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13510475226803781472  215             26                  
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13510475226804826220  181             22                  
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13511785702931210911  127             1                   
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13513264034969462591  652             4                   
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13512346118852882027  228             4                   
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13512346118853929567  265             5                   
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13510938086840377710  189             31                  
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13511785702930166871  127             1                   
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13513264034968418043  652             4                   
   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13511200354723346826  255             16                  
   (结果个数 = 14)

   ---    END
   ```
2. 查询“服务类型”为“UdmHttpService(UdmHttpService)”的进程内存占用信息：

   ```
   DSP UDMMEMINFO: ST=UdmAppCtrlService-0&NRFClient-0&HttpDisCtrlService-0&UdmSubService-0&UdmAuthService-0&UdmTcpService-0&UdmHttpService-1&UdmAlbService-0&EnumService-0;
   ```

   ```
   %%DSP UDMMEMINFO: ST=UdmAppCtrlService-0&NRFClient-0&HttpDisCtrlService-0&UdmSubService-0&UdmAuthService-0&UdmTcpService-0&UdmHttpService-1&UdmAlbService-0&EnumService-0;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   节点号           Pod名称                         SF实例号              分配的内存(MB)  内存占用率(百分比)  

   192.168.239.181  udmall-pod217-575979d69b-q5qpb  13513264034969462591  652             4                   
   192.168.239.248  udmall-pod217-575979d69b-mtzrq  13513264034968418043  652             4                   
   (结果个数 = 2)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1所示。

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| 节点号        | 用于返回服务所在节点的IP。  |
| Pod名称      | 用于返回服务所在的Pod名称。 |
| SF实例号      | 用于返回SDR通信的实例号。  |
| 分配的内存(MB)  | 用于返回服务占用的内存。    |
| 内存占用率(百分比) | 用于返回服务的内存占用率。   |