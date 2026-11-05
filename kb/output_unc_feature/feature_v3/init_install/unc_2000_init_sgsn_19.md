# 配置到PCU的数据

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

当运营商在部署分组交换网，新增BSC或SGSN时，在配置完成SGSN到BSC的路由数据后，可通过配置Gb接口数据建立SGSN到BSC的逻辑连接。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。

数据

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD SERVICEIP**** | IP版本（IPVERSION） | IPv4 | 参见“水平网设LLD文档 ”。 | 增加业务IP。 |
|  | 业务IPv4地址（SERVICEIPV4） | 10.10.80.130、10.10.80.131、10.10.80.130、10.10.80.141 |  |  |
|  | VPN实例名称（VPNINSTNAME） | VRF\_Access |  |  |
| ****ADD NSE**** | NSE连接方向（OTHERNODE） | PCU1 |  | 配置NSE链路数据。 |
|  | SGSN索引（SGSNINDEX） | 0 |  |  |
|  | NSE标识（NSEI） | 2740 |  |  |
|  | BSS编号（BSSID） | 2740 |  |  |
|  | 是否支持PFC（PFC） | YES |  |  |
|  | 是否支持SPID（SPID） | NO |  |  |
| ****ADD GBIPLOCENDPT**** | NSE标识（NSEI） | 2740 |  |  |
|  | IP地址类型（IPT） | IPV4 |  |  |
|  | 本端IPv4地址（LIPV4） | 10.10.80.130 |  |  |
|  | 本端UDP端口号（LUP） | 12740 |  |  |
|  | vpn名称（VPNNAME） | VRF\_Access |  |  |
| ****ADD GBIPRMTENDPT**** | IP地址类型（IPT） | IPV4 |  |  |
|  | 对端IPv4地址（RIPV4） | 10.10.10.1 |  |  |
|  | 对端UDP端口号（RUP） | 2704 |  |  |
|  | NSE标识（NSEI） | 2740 |  |  |
| ****SET GB**** | 启用Gb动态over IP自动配置功能（AUTO） | YES |  |  |
| ****ADD GBEPPOOL**** | IP类型 （IPTYPE） | IPV4 |  |  |
|  | IPv4地址 （IPV4） | 10.10.80.130 |  |  |
|  | vpn名称（VPNNAME） | VRF\_Access |  |  |
|  | 组号（GROUPID） | 1 |  |  |
| ****SET GBLOCPORTRGE**** | 起始端口号 （PORTBGN） | 1024 |  |  |
|  | 结束端口号 （PORTEND） | 10000 |  |  |
|  | 起始预置端口（BEGINPRECFGPORT） | 2000 |  |  |
|  | 描述信息 （DESC） | DEFAULT |  |  |
| ****SET BSSGP**** | BSSID与NSEI的对应关系（BSSIDRULE） | NSEI |  |  |
| ****ADD GBNSECFGPARA**** | 模板索引（PARAINDEX） | 1 |  |  |
|  | 本端端点个数 （EPNUM） | ONE |  |  |
| ****ADD GBNSEGRP**** | 关联索引（GRPINDEX） | 1 |  |  |
|  | 起始NSEI （NSEIBGN） | 2740 |  |  |
|  | 结束NSEI （NSEIEND） | 2740 |  |  |
|  | 关联的NSE属性模板索引 （PARAINDEX） | 1 |  |  |
| ****ADD BSSIDFORNSEI**** | 起始NSE标识 （NSEI） | 2740 |  |  |
|  | BSSID与NSEI的对应关系（BSSIDRULE） | NSEI\_MAP\_SPECIFIC\_BSSID |  |  |
|  | BSS标识 （BSSID） | 200 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置Gb接口业务IP。

   ```
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.80.130", VPNINSTNAME="VRF_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.10.80.131", VPNINSTNAME="VRF_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.33.80.140", VPNINSTNAME="VRF_Access";
   ADD SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="10.33.80.141", VPNINSTNAME="VRF_Access";
   ```
3. 配置NSE链路数据。

   * 静态配置
     1. 配置到每个PCU的NSE，IP承载的NSE配置类型为静态配置。

        ```
        ADD NSE: OTHERNODE="PCU1", SGSNINDEX=0, NSEI=2740, BSSID=2740, PFC=YES, SPID=NO;
        ADD NSE: OTHERNODE="PCU2", SGSNINDEX=0, NSEI=2750, BSSID=2750, PFC=YES, SPID=NO;
        ```
     2. 配置不同NSE下的本端端点。

        ```
        ADD GBIPLOCENDPT:NSEI=2740,IPT=IPV4,LIPV4="10.10.80.130",LUP=12740,VPNNAME="VRF_Access";
        ADD GBIPLOCENDPT:NSEI=2740,IPT=IPV4,LIPV4="10.10.80.131",LUP=12740,VPNNAME="VRF_Access";
        ADD GBIPLOCENDPT:NSEI=2750,IPT=IPV4,LIPV4="10.33.80.140",LUP=12750,VPNNAME="VRF_Access";
        ADD GBIPLOCENDPT:NSEI=2750,IPT=IPV4,LIPV4="10.33.80.141",LUP=12750,VPNNAME="VRF_Access";
        ```
     3. 配置对端端点。

        ```
        ADD GBIPRMTENDPT: IPT=IPV4, RIPV4="10.10.10.1", RUP=2704, NSEI=2740;
        ADD GBIPRMTENDPT: IPT=IPV4, RIPV4="10.10.11.1", RUP=2704, NSEI=2740;
        ADD GBIPRMTENDPT: IPT=IPV4, RIPV4="10.10.12.1", RUP=2705, NSEI=2750;
        ADD GBIPRMTENDPT: IPT=IPV4, RIPV4="10.10.13.1", RUP=2705, NSEI=2750;
        ```
   * 动态自动配置。
     1. 打开自动配置开关。

        ```
        SET GB: AUTO=YES;
        ```
     2. 添加IP地址到GB地址池。

        ```
        ADD GBEPPOOL: IPTYPE=IPV4, IPV4="10.10.80.130", VPNNAME="VRF_Access", GROUPID=1;
        ADD GBEPPOOL: IPTYPE=IPV4, IPV4="10.10.80.131", VPNNAME="VRF_Access", GROUPID=1;
        ADD GBEPPOOL: IPTYPE=IPV4, IPV4="10.33.80.140", VPNNAME="VRF_Access", GROUPID=2;
        ADD GBEPPOOL: IPTYPE=IPV4, IPV4="10.33.80.141", VPNNAME="VRF_Access", GROUPID=2;
        ```
     3. 配置本端端点端口范围，端口范围内的端口必须可用。起始预置端口(起始预置端口)用于指定动态流程上报的预配置端口，进行动态流程协商时发送使用，配置时预置端口范围需在对端配置的端口范围内。

        ```
        SET GBLOCPORTRGE: PORTBGN=1024, PORTEND=10000, BEGINPRECFGPORT=2000, DESC="DEFAULT";
        ```
     4. 配置全局动态NSE与BSSID对应关系。

        ```
        SET BSSGP: BSSIDRULE=NSEI;
        ```
     5. 配置NSE属性模板，指定NSE的属性时，需要与对端网元协商，保持RIM/PFC/INR/LCS/CBL等参数与对端网元能力的一致性，否则小区上报失败。

        ```
        ADD GBNSECFGPARA: PARAINDEX=1, EPNUM=ONE;
        ADD GBNSECFGPARA: PARAINDEX=2, EPNUM=TWO;
        ```
     6. 关联NSE到NSE属性模板。

        ```
        ADD GBNSEGRP: GRPINDEX=1, NSEIBGN=2740, NSEIEND=2740, PARAINDEX=1;
        ADD GBNSEGRP: GRPINDEX=2, NSEIBGN=2750, NSEIEND=2750, PARAINDEX=2;
        ```
     7. 配置NSEI和BSSID的对应关系。

        ```
        ADD BSSIDFORNSEI: NSEI=2740, BSSIDRULE=NSEI_MAP_SPECIFIC_BSSID, BSSID=200;
        ```

## 验证方法

1. 进入“MML命令行-UNC”窗口。
2. 当Gb接口采用动态自动配置时，检查NSE状态。

   **DSP NSE**

   * **预期结果：**有NSE信息上报。

     ```
     %%DSP NSE: NSEIFLTP=EQUAL, BNSEI=11002;%%
     RETCODE = 0  操作成功。

     操作结果如下
     -------------------------
                            RU名称  =  USN_VSU1
                            进程号  =  0
                           NSE标识  =  11002
                           BSS编号  =  11002
               FLUSH监控定时器(ms)  =  0
                       是否支持PFC  =  否(BSS侧不支持,SGSN侧不支持)
                       是否支持CBL  =  否(BSS侧不支持,SGSN侧不支持)
                       是否支持INR  =  否(BSS侧不支持,SGSN侧不支持)
                       是否支持LCS  =  否(BSS侧不支持,SGSN侧不支持)
                       是否支持RIM  =  否(BSS侧不支持,SGSN侧不支持)
                   是否携带ARP信元  =  否
         是否携带RA Capability信元  =  否
                   是否支持Gb-Flex  =  否
              是否支持特殊业务类型  =  否
                  BSS支持的Qos版本  =  R99
                      是否支持MOCN  =  否(BSS侧不支持,SGSN侧不支持)
                      是否支持SPID  =  否
     (结果个数 = 1)
     ---    END
     ```
   * **异常结果：**无NSE信息上报。

     异常处理:

     1. 在BSC侧ping IP地址，检查IP地址是否可达。

        + IP地址不可达，根据实际排查端到端路由配置。
        + IP地址可达，转2.b。
     2. 在BSC侧查看预配置端口IP和端口号是否和SGSN侧配置一致。

        + BSC侧和SGSN侧配置不一致，修改配置为一致。
        + BSC侧和SGSN侧配置一致，请联系华为技术支持。
3. 检查SGSN到指定BSS的NSVC链路状态是否正常。

   **DSP IPNSVC**

   * **预期结果：**“NSVC 状态”字段为“可操作”。

     ```
     %%DSP IPNSVC:;%%
     RETCODE = 0  操作成功。

     操作结果如下
     ------------
     NSVC标识        NSE标识     RU名称  进程号   IP地址类型   本地IP地址       本端UDP端口号    对端IP地址     对端UDP端口号    NSVC状态

     9216           11001       USN_VSU1    1         IPv4      192.168.14.19     1043         10.126.13.1    11102           可操作
     10243          11002       USN_VSU1    1         IPv4      192.168.14.20     1045         10.126.13.1    11102           可操作
     11266          11002       USN_VSU1    1         IPv4      192.168.14.19     1045         10.126.13.1    11102           可操作
     8193           11001       USN_VSU1    1         IPv4      192.168.14.20     1043         10.126.13.1    11102           可操作
     链路总数  =  3
     (结果个数 = 4)

     ---    END
     ```
   * **异常结果：**“NSVC 状态”字段为“不可操作”。

     异常处理参见ALM-80640 IP NS-VC链路故障。
4. 检查SGSN与指定PCU协商的NSE实体状态是否正常。

   **DSP SIGBVC**

   * **预期结果：**“SIG实体状态”字段为“正常”。

     ```
     %%DSP SIGBVC: OUTPUTTYPE=MULTI_SIGBVC, RUNAME="USN_VSU1";%% 
     RETCODE = 0  操作成功。
     输出结果如下
     --------------
       RU名称    NSE标识       SIG实体状态
     USN_VSU1   11802         等待NS层状态正常
     USN_VSU1   11801         等待NS层状态正常
     (结果个数 = 2)   
     ---    END
     ```
   * **异常结果：**“SIG实体状态”字段为非“正常”。

     异常处理过程参见BSSGP层功能实体创建失败。
5. 检查指定BSS上报的小区状态是否正常。

   **LST CELL**

   参数“OUTPUTTYPE”（输出类型）固定选择“SCREEN”（报告输出）。

   * **预期结果：**可以查到指定小区信息，并且“PTP实体状态”字段为“正常状态”。

     ```
     %%LST CELL: OUTPUTTYPE=SCREEN;%%
     RETCODE = 0  操作成功。

     操作结果如下
     --------------

     小区号                                  NSE标识   小区所在RU名称       小区所在进程号              BVCI     NSE所在RU名称    NSE所在进程号             是否支持PFC      是否支持CB    是否支持INR           是否支持LCS                                 是否支持RIM                                是否支持PFCFCE                              PTP实体状态        

     123054804041026(123-05-18436-4-4134)    14804     USN_SP_RU_0067         0                          1026    USN_SP_RU_0067        1                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034803031025(123-03-18435-3-4133)    14804     USN_SP_RU_0067         1                          1025    USN_SP_RU_0067        1                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034802021024(123-03-18434-2-4132)    14804     USN_SP_RU_0066         4                          1024    USN_SP_RU_0067        1                         是            是            是            否(BSS侧不支持,SGSN侧不支持)       否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                      NS故障 
     123034801011027(123-03-18433-1-4135)    14804     USN_SP_RU_0067         3                          1027    USN_SP_RU_0067        1                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034801011011(123-03-18433-1-4113)    14801     USN_SP_RU_0066         4                          1011    USN_SP_RU_0066        0                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034811081018(123-03-18449-8-4120)    14801     USN_SP_RU_0067         3                          1018    USN_SP_RU_0066        0                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034801021013(123-03-18433-2-4115)    14801     USN_SP_RU_0067         0                          1013    USN_SP_RU_0066        0                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034801011012(123-03-18433-1-4114)    14801     USN_SP_RU_0067         1                          1012    USN_SP_RU_0066        0                         是            是            是            否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                否(BSS侧不支持,SGSN侧不支持)                       NS故障 
     123034801011017(123-03-18433-1-4119)    14802     USN_SP_RU_0066         3                          1017    USN_SP_RU_0066        1                         是            是            是            否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                         NS故障 
     123054804041016(123-05-18436-4-4118)    14802     USN_SP_RU_0066         2                          1016    USN_SP_RU_0066        1                         是            是            是            否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                         NS故障 
     123034803031015(123-03-18435-3-4117)    14802     USN_SP_RU_0066         0                          1015    USN_SP_RU_0066        1                         是            是            是            否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                         NS故障 
     123034802021014(123-03-18434-2-4116)    14802     USN_SP_RU_0066         1                          1014    USN_SP_RU_0066        1                         是            是            是            否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                  否(BSS侧支持,SGSN侧不支持)                         NS故障 
     (结果个数 = 12)
     --- END
     ```
   * **异常结果：**
     + “PTP实体状态”字段为“等待复位响应”、“等待写DDB响应”或“等待板间迁移响应”：等待几分钟后，重新查询小区状态。
     + “PTP实体状态”字段为“闭塞状态”：处理过程参见小区闭塞。

   * 对于“2G寻呼表”，其配置方法和原理与“3G寻呼表”存在差异，除了通过**LST CELL**检查指定BSS上报小区是否正常还需要通过**LST GBPAGING**查询2G寻呼表格中的数据配置。
   * 实际使用过程中，通过**LST GBPAGING**命令查询出的“2G寻呼表”可能存在冗余数据。如果发现2G寻呼表表格和小区信息中有冗余数据时，可以通过下面过程进行处理:

     通过信令实体管理中的**RST SIGBVC**命令复位SigBvc信令实体，使BSS和SGSN两端同步初始化信令实体的相关上下文，使系统根据当前网络来重新构建“2G寻呼表”。

     执行**RST SIGBVC**命令，位于该SigBvc信令实体下的所有小区将全部丢失，只有当PCU侧重新发起小区创建流程才能恢复小区信息，而SGSN侧涉及相关小区的信息也将全部丢失并重新构建。小区的重新上报正常情况下在10毫秒级，这段时间内将会造成SigBvc信令实体下的分组业务发生“瞬断”，因此上面的操作需要选择业务空闲时段操作。
6. 进行业务测试。

   进行业务拨测前，需要受限完成SGSN与HLR、GGSN的对接。

   1. 创建用户跟踪。

      参数选择如下：

      * IMSI/MSISDN/IMEI：被跟踪用户的IMSI、MSISDN或者IMEI。
      * 其它参数：选择默认值。
   2. 创建Gb接口L3跟踪。

      参数选择如下：

      * Ru名称：资源单元的名称。
      * NSEI号：NSE号码，条件必选参数，跟踪SIG管理消息时此参数必选。对于整个Gb接口跟踪，参数输入时，NSE号码和小区号码两者必选一项。
      * 小区号：小区号码，条件必选参数，跟踪PTP消息时此参数必须。 对于整个Gb接口跟踪，参数输入时，NSE号码和小区号码两者必选一项。
      * 其它参数：选择默认值。
   3. 用户在测试PCU下开机附着。
   4. 查看跟踪信息。

      * **预期结果：**可以观察到正常的附着消息流程，并且手机向SGSN下发Attach Request消息，SGSN向手机下发Attach Accept消息，指示附着成功。

        此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。该功能提供了假名化的处理方式。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护，例如在U2020上将假名化开关打开、处理完毕后将保存跟踪记录的文件夹进行删除等。
      * **异常结果：**用户附着失败。
   5. 查询用户MM上下文。

      **DSP COMMMCTX**

      * **预期结果：**可以查询到用户的MM上下文，并且状态为3G状态。
      * **异常结果：**查询不到用户的MM上下文。
   6. 用户用手机浏览网页。
   7. 查看跟踪信息。
      * **预期结果：**可以观察到正常的激活消息流程，并且SGSN向手机下发ACTIVATE\_PDP\_CONTEXT\_ACCEPT消息，指示激活成功。
      * **异常结果：**用户激活失败。
   8. 查询用户PDP上下文。

      **DSP SMCTX**

      * **预期结果：**可以查询到用户的PDP上下文。
      * **异常结果：**查询不到用户的PDP上下文。

版权所有 © 华为技术有限公司
