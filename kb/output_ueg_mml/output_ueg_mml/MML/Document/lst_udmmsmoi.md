# 查询UDM微服务进程测量对象(LST UDMMSMOI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询微服务进程测量对象。

- 若要查询所有微服务进程测量对象，请不要输入任何参数。
- 若要查询某个微服务进程测量对象，请输入“服务类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST     | 服务类型   | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个服务类型查询对应的微服务进程测量对象；若不输入，则表示所有的服务类型。 取值范围： UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UdmAlbService(UdmAlbService)EnumService(EnumService) 默认值：无 配置原则：无 |

## 使用实例

1. 查询所有微服务进程测量对象：

   ```
   LST UDMMSMOI:;
   ```

   ```
   %%LST UDMMSMOI:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   服务类型              节点ID              POD名称                          服务实例ID            

   UdmAppCtrlService     172.16.239.192      udmctrl-pod439-6f4df87bc4-ghl9b  11661818249158462009  
   NRFClient             172.20.239.75       udmctrl-pod439-6f4df87bc4-ghl9b  11660859578098258637  
   HttpDisCtrlService    172.16.239.151      udmctrl-pod439-6f4df87bc4-ghl9b  11659702251915710741  
   UdmSubService         172.19.239.84       udmausf-pod439-6f4df87bc4-gh19b  11664080344008760812  
   UdmAuthService        172.21.239.11       udmausf-pod439-6f4df87bc4-gh19b  11662671676340046768  
   UdmTcpService         172.19.239.71       hlb-a-pod439-6f95f7cbf4-k47v7    11663530850187870750  
   UdmHttpService        172.30.239.150      hlb-a-pod439-6f95f7cbf4-k47v7    11664156133001665406  
   (结果个数 = 7)

   ---    END
   ```
2. 查询“服务类型”为“UdmTcpService” 的微服务进程测量对象：

   ```
   LST UDMMSMOI: ST=UdmTcpService;
   ```

   ```
   %%LST UDMMSMOI: ST=UdmTcpService;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
     服务类型  =  UdmTcpService
       节点ID  =  172.19.239.71
      POD名称  =  hlb-a-pod439-6f95f7cbf4-k47v7
   服务实例ID  =  11663530850187870750
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。各参数含义如表1所示。

| 输出项名称   | 输出项解释            |
|:--------|:-----------------|
| 服务类型    | 用于返回测量对象所属的服务类型。 |
| 节点ID    | 用于返回节点ID。        |
| POD名称   | 用于返回POD名称。       |
| 服务实例ID  | 用于返回测量对象的服务实例号。  |