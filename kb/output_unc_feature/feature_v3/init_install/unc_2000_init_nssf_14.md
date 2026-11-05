# NSSF典型配置实例

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

本任务实例实现以下场景配置：

UNC（作为NSSF）与周边NF（本例中包含AMF、SMF、NRF）通过OSPF动态路由绑定动态BFD实现网络互通。

* 网络形态：5G网络
* 网元形态：NSSF
* 路由协议：OSPF动态路由
* 组网IP格式：IPv4组网
* 接入用户：IPv4单栈用户

## 必备事项

前提条件

* 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
* 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）、配置NSSF，本文针对典型的任务场景举例说明整网脚本配置。

数据

可参考各子任务的数据规划准备。

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 关闭自动配置开关。
   1. 查询自动配置开关状态。

      ```
      LST AUTOCONFIG:;
      ```

      如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。
   2. 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

      ```
      DSP OPSASSISTSTATE:;
      ```
   3. 关闭自动配置开关。

      ```
      SET AUTOCONFIG: SWITCHFLAG=FALSE;
      ```
3. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```
4. 配置UNC与对端AMF、SMF、NRF的IP路由数据。
   1. 配置外联口的VPN实例。

      ```
      ADD L3VPNINST: VRFNAME="VRF_SBI";
      ADD VPNINSTAF: VRFNAME="VRF_SBI",AFTYPE=ipv4uni;
      ```
   2. 配置OSPF路由。

      1. 创建OSPF进程。

         ```
         ADD OSPF: PROCID=6, VRFNAME="VRF_SBI", SCHEMAROUID="192.168.35.210", BFDALLINTFFLG=TRUE, LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
         ```
      2. 增加OSPF区域。

         ```
         ADD OSPFAREA: PROCID=6, AREAID="10.0.0.5";
         ```

         如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。
      3. 设置OSPF引入路由类型。

         ```
         ADD OSPFIMPORTROUTE: PROCID=6, TOPOID=0, PROTOCOL=wlr, IMPTCOSTCFG=FALSE, IMPTTAGCFG=FALSE, IMPTTYPECFG=FALSE;
         ```
   3. 配置外联口自动部署模板。

      ```
      ADD AUTOSCALINGSERVICE: SERVICENAME="VRF_SBI_100", VPNNAME="VRF_SBI", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, VNICID=4, VLANID=100, BEGINADDR4="192.168.89.2", ENDADDR4="192.168.89.14", MASKLEN=28, OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="10.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE; 
      ADD AUTOSCALINGSERVICE: SERVICENAME="VRF_SBI_200", VPNNAME="VRF_SBI", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, VNICID=5, VLANID=200, BEGINADDR4="192.168.89.18", ENDADDR4="192.168.89.30", MASKLEN=28, OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="10.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE;
      ```
5. 打开IP路由自动配置开关。

   ```
   SET AUTOCONFIG: SWITCHFLAG=TRUE;
   ```

   从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。
6. 配置NSSF实例信息。
   1. 配置NSSF实例的名称。

      ```
      ADD NFUUID: NFTYPE=NfNSSF, NFINSTANCENAME="NSSF_Instance_0";
      ```
   2. 配置NSSF实例的Profile信息。

      ```
      ADD NFPROFILE: NFINSTANCENAME="NSSF_Instance_0", NFTYPE=NfNSSF, NFSTATUS=Registered;
      ```
   3. 配置NSSF提供的服务实例及其版本信息。

      ```
      ADD NFSERVICE: NFINSTANCENAME="NSSF_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NnssfNsSel; 
      ADD NFSERVICE: NFINSTANCENAME="NSSF_Instance_0", SRVINSTANCEID="Service_Instance_1", SERVICENAME=NnssfNssaiAvai;
      ```

      ```
      ADD NFSERVICEVER: NFINSTANCENAME="NSSF_Instance_0", SRVINSTANCEID="Service_Instance_0", APIFULLVERSION="1.R15.0.0";
      ADD NFSERVICEVER: NFINSTANCENAME="NSSF_Instance_0", SRVINSTANCEID="Service_Instance_1", APIFULLVERSION="1.R15.0.0";
      ```
7. 配置NSSF服务化接口数据。
   1. 增加NSSF服务化接口的IP地址。

      ```
      ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.8", VPNINSTNAME="VRF_SBI", DESC="FOR SBI Server";
      ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.9", VPNINSTNAME="VRF_SBI", DESC="FOR SBI Client";
      ```
   2. 配置Nnssf接口的HTTP信息。

      ```
      ADD HTTPLEGRP: INDEX=3, DESC="NSSF";
      ```

      ```
      ADD HTTPLE: INDEX=5, HTTPLEGRPIDX=3, LETYPE=SERVER, IPTYPE=IPv4, IPV4="172.16.0.8", PORT=8080, VPNNAME="VRF_SBI", TLSFLG=NO, DESC="NSSF Server";
      ADD HTTPLE: INDEX=6, HTTPLEGRPIDX=3, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="172.16.0.9", VPNNAME="VRF_SBI", DESC="NSSF Client";
      ```

      ```
      ADD SBIAPLE: INDEX=3, HTTPLEGRPIDX=3, NFTYPE=NFTypeNSSF, DESCRIPTION="NSSF";
      ```
8. 配置NSSF到NRF的数据。
   1. 配置NRF信息。

      ```
      ADD NRF: NRFINSTANCENAME="NRF_Instance_0", TLS=FALSE, PRIORITY=0;
      ```
   2. 配置NRF的地址信息。

      ```
      ADD NRFADDR: NRFINSTANCENAME="NRF_Instance_0", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="172.16.0.7", PORT=8080;
      ```
   3. 配置NRF协议参数。

      ```
      ADD NRFPARA: NRFINSTANCENAME="NRF_Instance_0", WAITINTERVAL=5, MAXRETRYTIMES=3, LOADCARRYINHB=FALSE, SUBSCRISWITCH=ON, OAUTH2SWITCH=OFF;
      ADD SUBCONDITION: NFTYPE=NfAMF, CONDITION=NfInstanceId-1, REQNOTIFEVENT=NF_REGISTERED-1;
      ADD SUBCONDITION: NFTYPE=NfSMF, CONDITION=NfInstanceId-1, REQNOTIFEVENT=NF_REGISTERED-1;
      ```
   4. 打开NSSF的NF认证功能的开关。

      ```
      SET LICENSESWITCH:LICITEM="LKV2NFANS01",SWITCH=ENABLE;
      ```
   5. 激活NSSF向NRF注册。

      ```
      ACT NFONLINE: NFINSTANCENAME="NSSF_Instance_0";
      ```
9. 配置切片选择数据。
   1. 配置运营商支持的切片信息。

      ```
      ADD CFGSNSSAI: INDEX=1, MCC="123", MNC="03", SST=1, SD="010101", ISACTIVE=TRUE;
      ```
   2. 配置AMF集合支持的切片信息。

      ```
      ADD TACGROUPINNSSF: INDEX=1, TACGROUPNAME="TACGROUP01", TACSTART="290100", TACEND="290110";
      ADD AMFSETID: INDEX=1, SST=1, SD="010101", MCC="123", MNC="03", REGIONID="01", AMFSETID="001", TACGROUPNAME="TACGROUP01";
      ```
10. 配置候选AMF信息。

    ```
    ADD CANDIDATEAMF: INDEX=1, AMFINSTANCEID="bdc3f6f6-69ac-4c06-bfe5-030101000001", MCC="123", MNC="03", REGIONID="01", AMFSETID="001";
    ```
11. 配置AMF订阅NSSF切片可用性服务的有效期时长。

    ```
    SET NSSFSUBTIMER: NFTYPE=AMF, SUBVALIDTIMER=3600;
    ```

版权所有 © 华为技术有限公司
