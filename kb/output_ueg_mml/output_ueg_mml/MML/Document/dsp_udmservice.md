# 查询服务（DSP UDMSERVICE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询各服务信息。

- 若要查询全部服务的配置信息，请不要输入任何参数。
- 若要查询某个服务的配置信息，请输入“服务类型”或其他参数，或者“服务类型”和其他参数的组合。

通过该命令查询后，可实现以下运维能力。

- 根据输出参数“POD名称”：
  - 可以通过CSP命令**DSP POD**查询POD的运行状态。
  - 可以通过CSP命令**RST POD**复位POD。
- 根据输出参数“模块号”，可以通过**DSP MODULE**、**RST MODULE**、**LST MODULE**对融合HLR/HSS模块进行操作。
- 根据输出参数“节点号”，使用putty或其它终端工具：
  - 虚机场景下，登录到网元的OMU VM维护口虚拟机上（若未进行过VM维护口改造，则登录到Paas-om01虚拟机）。

    **说明** 

    - OMU VM维护口登录方式：以mtuser用户通过维护接口IP地址登录到网元的任意一个OMU VM维护口虚拟机上。IP地址获取方法为：执行**DSP NODERES**命令，查询“网口平面”为“ext-om”的IP地址。
    - paas-om01方式：以mtuser用户或者paas用户登录到paas-om01虚拟机（UDM 20.7.1及后续版本禁止使用paas用户登录虚拟机）。
  - 裸机场景下，以mtuser用户登录到网元的Paas-om01节点。
- 根据输出参数“日志IP”，可以过滤集中存储中对应服务的日志。

## 注意事项

- 如果执行**DSP SERVICENAME**命令查询结果中没有对应服务注册信息（注册失败、复位、pod容器重建等场景），命令无法查询对应服务信息。
- 如果网元未部署扩展域功能，则查询“服务类型”为“UdmEru(UdmEru)”的服务信息时，命令无法查询对应服务信息。
- 如果网元未部署扩展域功能，则查询“服务类型”为“UdmAlbService(UdmAlbService)”的服务信息时，命令无法查询对应服务信息。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ST     | 服务类型   | 可选必选说明：可选参数 参数含义：用于标识通过哪种服务类型来查询服务信息，如果不输入该参数，标识查询除UdmEru与UdmAlbService服务之外的所有服务信息。 取值范围： 全部选中全部清空全部灰化UdmAppCtrlService(UdmAppCtrlService)NRFClient(NRFClient)HttpDisCtrlService(HttpDisCtrlService)UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)UdmTcpService(UdmTcpService)UdmHttpService(UdmHttpService)UDRDbbroker(UDRDbbroker)UdmHsf(UdmHsf)UdmBsg(UdmBsg)UdmCcu(UdmCcu)UDRDsg(UDRDsg)UdmEru(UdmEru)UdmAlbService(UdmAlbService)EnumService(EnumService)UdmAcf(UdmAcf)UdmApf(UdmApf) 默认值：无。 配置原则：无。 |
| STATUS | 可用状态   | 可选必选说明：可选参数 参数含义：用于标识通过哪种状态来查询服务信息，如果不输入该参数，标识查询所有状态的服务信息。 取值范围： ReadyNotReady 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

1. 查询所有服务信息。

   ```
   DSP UDMSERVICE:;
   ```

   ```
   %%DSP UDMSERVICE:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   节点号                 Pod名称                          容器                服务号      实例号     SF实例号              模块号  服务类型            主备状态  可用状态  日志IP     标签                                                                                                                                              

   3d10-135-202-248--1a7  udmctrl-pod112-86955fcc84-n6scs  udmappctrlservice   4290481080  4275128    18427475922711034808  NULL    UdmAppCtrlService   主用      正常      NULL       {"HaRole":"Active","ProcessNO":"0"}                                                                                                               
   3d10-135-202-248--24c  udmctrl-pod112-86955fcc84-6hps8  udmappctrlservice   4290481080  4246456    18427475922711006136  NULL    UdmAppCtrlService   备用      正常      NULL       {"HaRole":"Standby","ProcessNO":"0"}                                                                                                              
   3d10-135-202-248--1a7  udmctrl-pod112-86955fcc84-n6scs  nrfclient           4290501565  4275133    18427563905116093373  NULL    NRFClient           主用      正常      NULL       {"HaRole":"Active","NrfcBlockStatus":"False","ProcessNO":"0"}                                                                                     
   3d10-135-202-248--24c  udmctrl-pod112-86955fcc84-6hps8  nrfclient           4290501565  4246461    18427563905116064701  NULL    NRFClient           备用      正常      NULL       {"HaRole":"Standby","NrfcBlockStatus":"False","ProcessNO":"0"}                                                                                    
   3d10-135-202-248--1a7  udmctrl-pod112-86955fcc84-n6scs  httpdisctrlservice  4290497468  4275132    18427546308635081660  NULL    HttpDisCtrlService  主用      正常      NULL       {"HaRole":"Active","ProcessNO":"0","version":"1.0"}                                                                                               
   3d10-135-202-248--24c  udmctrl-pod112-86955fcc84-6hps8  httpdisctrlservice  4290497468  4246460    18427546308635052988  NULL    HttpDisCtrlService  备用      正常      NULL       {"HaRole":"Standby","ProcessNO":"0","version":"1.0"}                                                                                              
   3d10-135-202-248--15c  udmausf-pod112-548944b974-2xpwq  udmsubservice       4290485177  4258745    18427493519192030137  NULL    UdmSubService       NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--1a0  udmausf-pod112-548944b974-6j9z7  udmsubservice       4290485177  4254649    18427493519192026041  NULL    UdmSubService       NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--15c  udmausf-pod112-548944b974-2xpwq  udmauthservice      4290489274  4258746    18427511115673041850  NULL    UdmAuthService      NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--1a0  udmausf-pod112-548944b974-6j9z7  udmauthservice      4290489274  4254650    18427511115673037754  NULL    UdmAuthService      NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--124  hlb-a-pod112-7b78cdfdcf-mxn4l    udmhttpservice      4290505663  4279227    18427581505892076475  NULL    UdmTcpService       NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--1c6  hlb-b-pod112-5cb66b496f-8hrzh    udmhttpservice      4290505663  4209595    18427581505892006843  NULL    UdmTcpService       NULL      正常      NULL       {"ProcessNO":"0"}                                                                                                                                 
   3d10-135-202-248--124  hlb-a-pod112-7b78cdfdcf-mxn4l    udmhttpservice      4290493371  71388091   18427528712221182907  NULL    UdmHttpService      NULL      正常      NULL       {"ClientToken":"32001","LinkStatus":"AllReady","ProcessNO":"1","UdmHttpDead":"false","UdmTcpInstId":"18427581505892076475"}                       
   3d10-135-202-248--1c6  hlb-b-pod112-5cb66b496f-8hrzh    udmhttpservice      4290493371  71318459   18427528712221113275  NULL    UdmHttpService      NULL      正常      NULL       {"ClientToken":"32000","LinkStatus":"AllReady","ProcessNO":"1","UdmHttpDead":"false","UdmTcpInstId":"18427581505892006843"}                       
   3d10-135-202-248--1c6  dbs-b1-pod112-0                  dbbroker            4294598565  4225983    18445160386127756223  23      UDRDbbroker         NULL      正常      NULL       {"AppNodeStatus":"STARTED","FaultCause":"Null","HaHealth":"healthy","InstanceID":"18445160386127756223","LogIp":"8058::289","ModuleNumber":"23"}  
   3d10-135-202-248--124  dbs-a1-pod112-0                  dbbroker            4294598565  4250559    18445160386127780799  21      UDRDbbroker         NULL      正常      NULL       {"AppNodeStatus":"STARTED","FaultCause":"Null","HaHealth":"healthy","InstanceID":"18445160386127780799","LogIp":"8058::286","ModuleNumber":"21"}  
   3d10-135-202-248--124  dbs-a-pod112-0                   dbbroker            4294598565  4238271    18445160386127768511  22      UDRDbbroker         NULL      正常      NULL       {"AppNodeStatus":"STARTED","FaultCause":"Null","HaHealth":"healthy","InstanceID":"18445160386127768511","LogIp":"8058::285","ModuleNumber":"22"}  
   3d10-135-202-248--1c6  dbs-b-pod112-0                   dbbroker            4294598565  4217791    18445160386127748031  24      UDRDbbroker         NULL      正常      NULL       {"AppNodeStatus":"STARTED","FaultCause":"Null","HaHealth":"healthy","InstanceID":"18445160386127748031","LogIp":"8058::287","ModuleNumber":"24"}  
   3d10-135-202-248--1c6  uisu-b-pod112-0                  udmlite             4290517953  138439615  18427634291174304703  214     UdmHsf              NULL      正常      NULL       {"ModuleNumber":"214","ProcessNO":"2"}                                                                                                            
   3d10-135-202-248--124  uisu-a-pod112-0                  udmlite             4290517953  138451903  18427634291174316991  211     UdmHsf              NULL      正常      NULL       {"ModuleNumber":"211","ProcessNO":"2"}                                                                                                            
   3d10-135-202-248--124  uisu-a-pod112-0                  udmlite             4290513856  205560767  18427616694760414143  212     UdmBsg              NULL      正常      NULL       {"ModuleNumber":"212","ProcessNO":"3"}                                                                                                            
   3d10-135-202-248--124  uisu-a-pod112-0                  udmlite             4290513856  272669631  18427616694827523007  213     UdmBsg              NULL      正常      NULL       {"ModuleNumber":"213","ProcessNO":"4"}                                                                                                            
   3d10-135-202-248--1c6  uisu-b-pod112-0                  udmlite             4290513856  205548479  18427616694760401855  215     UdmBsg              NULL      正常      NULL       {"ModuleNumber":"215","ProcessNO":"3"}                                                                                                            
   3d10-135-202-248--1c6  uisu-b-pod112-0                  udmlite             4290513856  272657343  18427616694827510719  216     UdmBsg              NULL      正常      NULL       {"ModuleNumber":"216","ProcessNO":"4"}                                                                                                            
   3d10-135-202-248--1a0  uccu-pod112-0                    udmlite             4290522050  406920128  18427651887923796928  205     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"205","ProcessNO":"6"}                                                                                                            
   3d10-135-202-248--15c  uccu-pod112-1                    udmlite             4290522050  406916032  18427651887923792832  210     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"210","ProcessNO":"6"}                                                                                                            
   3d10-135-202-248--15c  uccu-pod112-1                    udmlite             4290522050  339807168  18427651887856683968  209     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"209","ProcessNO":"5"}                                                                                                            
   3d10-135-202-248--1a0  uccu-pod112-0                    udmlite             4290522050  272702400  18427651887789579200  203     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"203","ProcessNO":"4"}                                                                                                            
   3d10-135-202-248--15c  uccu-pod112-1                    udmlite             4290522050  138480576  18427651887655357376  206     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"206","ProcessNO":"2"}                                                                                                            
   3d10-135-202-248--1a0  uccu-pod112-0                    udmlite             4290522050  138484672  18427651887655361472  201     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"201","ProcessNO":"2","isControlCCU":"True"}                                                                                      
   3d10-135-202-248--15c  uccu-pod112-1                    udmlite             4290522050  205589440  18427651887722466240  207     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"207","ProcessNO":"3"}                                                                                                            
   3d10-135-202-248--1a0  uccu-pod112-0                    udmlite             4290522050  205593536  18427651887722470336  202     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"202","ProcessNO":"3"}                                                                                                            
   3d10-135-202-248--15c  uccu-pod112-1                    udmlite             4290522050  272698304  18427651887789575104  208     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"208","ProcessNO":"4"}                                                                                                            
   3d10-135-202-248--1a0  uccu-pod112-0                    udmlite             4290522050  339811264  18427651887856688064  204     UdmCcu              NULL      正常      NULL       {"ModuleNumber":"204","ProcessNO":"5"}                                                                                                            
   (结果个数 = 34)

   ---    END
   ```
2. 查询“服务类型”为“UdmAppCtrlService”的服务信息。

   ```
   DSP UDMSERVICE: ST=UdmAppCtrlService-1&NRFClient-0&HttpDisCtrlService-0&UdmSubService-0&UdmAuthService-0&UdmTcpService-0&UdmHttpService-0&UDRDbbroker-0&UdmHsf-0&UdmBsg-0&UdmCcu-0&UDRDsg-0&UdmEru-0, STATUS=Ready;
   ```

   ```
   %%DSP UDMSERVICE: ST=UdmAppCtrlService-1&NRFClient-0&HttpDisCtrlService-0&UdmSubService-0&UdmAuthService-0&UdmTcpService-0&UdmHttpService-0&UDRDbbroker-0&UdmHsf-0&UdmBsg-0&UdmCcu-0&UDRDsg-0&UdmEru-0, STATUS=Ready;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   节点号                 Pod名称                          容器               服务号      实例号   SF实例号              模块号  服务类型           主备状态  可用状态  日志IP     标签                                  

   3d10-135-202-248--24c  udmctrl-pod112-86955fcc84-6hps8  udmappctrlservice  4290481080  4246456  18427475922711006136  NULL    UdmAppCtrlService  备用      正常      NULL       {"HaRole":"Standby","ProcessNO":"0"}  
   3d10-135-202-248--1a7  udmctrl-pod112-86955fcc84-n6scs  udmappctrlservice  4290481080  4275128  18427475922711034808  NULL    UdmAppCtrlService  主用      正常      NULL       {"HaRole":"Active","ProcessNO":"0"}   
   (结果个数 = 2)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表1所示。

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 节点号     | 用于返回服务所在节点的IP。                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pod名称   | 用于返回服务所在的Pod名称。                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 容器      | 用于返回服务模块部署所在的容器。 udmappctrlservice：对应的服务为UdmAppCtrlService。nrfclient：对应的服务为NRFClient。httpdisctrlservice：对应的服务为HttpDisCtrlService。udmsubservice：对应的服务为UdmSubService。udmauthservice：对应的服务为UdmAuthService。udmtcpservice：对应的服务为UdmTcpService。udmhttpservice：对应的服务为UdmHttpService。dbbroker：对应的服务为UDRDbbroker。udmlite：对应的服务为UdmHsf、UdmBsg、UdmCcu、UDRDsg、UdmAcf和UdmApf。ueru：对应的服务为UdmEru。UdmAlbService：对应的服务为UdmAlbService。EnumService：对应的服务为EnumService。 |
| 服务号     | 用于返回CSP服务管理中的ServiceId。                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 实例号     | 用于返回CSP服务管理中的InstanceId。                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SF实例号   | 用于返回SDR通信的实例号。                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 模块号     | 用于返回融合HLR/HSS进程模块号。                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 服务类型    | 用于返回服务类型。 UdmAppCtrlServiceNRFClientHttpDisCtrlServiceUdmSubServiceUdmAuthServiceUdmTcpServiceUdmHttpServiceUDRDbbrokerUdmHsfUdmBsgUdmCcuUDRDsgUdmEruUdmAlbServiceUdmAcfUdmApf                                                                                                                                                                                                                                                                     |
| 主备状态    | 用于返回服务的主备状态。 主用备用NULL                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 可用状态    | 用于返回服务的可用状态。 正常：表示服务为可用状态；当DSP MODULE命令中的“可用状态”为“正常”时，表示CCU模块为全局数据加载成功。未就绪：表示服务已启动，此时正处于加载状态，不提供业务功能。NULL：表示不可以提供服务，需要对故障服务进行处理。                                                                                                                                                                                                                                                                                                                   |
| 日志IP    | 用于返回集中存储日志中携带的用于区分不同节点日志的IP。                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 标签      | 用于返回查询出的服务的完整标签。                                                                                                                                                                                                                                                                                                                                                                                                                                   |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|    错误码 | 错误码解释                    | 原因分析                     | 处理建议                                                                                 |
|-------:|:-------------------------|:-------------------------|:-------------------------------------------------------------------------------------|
| 100015 | 参数ST的值无效。                | 输入参数“服务类型”的取值，不符合取值范围要求。 | 根据实际情况，重新输入“服务类型”的取值，确保其取值符合要求。                                                      |
| 100016 | 参数STATUS的值（参数取值）不在指定范围内。 | 输入参数“可用状态”的取值，不符合取值范围要求。 | 根据实际情况，重新输入“可用状态”的取值，确保其取值符合要求。                                                      |
| 360126 | 查询服务信息失败。                | 后台处理错误或调用CSP接口失败。        | 请联系华为技术支持处理。                                                                         |
| 360127 | 查询服务（服务类型）信息失败。          | 提示输入的“服务类型”信息查询失败。       | 当未部署扩展域功能时，执行命令后返回“查询（UdmEru）信息失败”，则需要去勾选参数“服务类型”中的UdmEru服务，并重新执行命令。其余场景请联系华为技术支持处理。 |