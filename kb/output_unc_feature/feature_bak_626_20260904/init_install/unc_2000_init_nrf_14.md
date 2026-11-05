# NRF典型配置实例

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

本任务实例实现以下场景配置：

UNC（作为NRF）与周边NF（本例中包含AMF、SMF、NSSF）通过OSPF动态路由绑定动态BFD实现网络互通。

- 网络形态：5G网络
- 网元形态：NRF
- 路由协议：OSPF动态路由
- 组网IP格式：IPv4组网
- 接入用户：IPv4单栈用户

## 必备事项

前提条件

- 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
- 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）、配置NRF，本文针对典型的任务场景举例说明整网脚本配置。

数据

可参考各子任务的数据规划准备。

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 关闭IP路由自动配置开关。
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
4. 配置UNC与对端AMF、SMF、NSSF的IP路由数据。
   1. 配置外联口的VPN实例。

      ```
      ADD L3VPNINST: VRFNAME="VRF_SBI";
      ADD VPNINSTAF: VRFNAME="VRF_SBI", AFTYPE=ipv4uni;
      ```
   2. 配置OSPF路由。

      1. 创建OSPF进程。

         ```
         ADD OSPF: PROCID=6,VRFNAME="VRF_SBI", SCHEMAROUID="192.168.35.210", BFDALLINTFFLG=TRUE, LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
         ```
      2. 增加OSPF区域。

         ```
         ADD OSPFAREA: PROCID=6, AREAID="10.0.0.5";
         ```

         **说明** 

         如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。
      3. 设置OSPF引入路由类型。

         ```
         ADD OSPFIMPORTROUTE: PROCID=6, TOPOID=0, PROTOCOL=wlr, IMPTCOSTCFG=FALSE, IMPTTAGCFG=FALSE, IMPTTYPECFG=FALSE;
         ```
   3. 配置外联口自动部署模板。

      ```
      ADD AUTOSCALINGSERVICE: SERVICENAME="VRF_SBI_100", VPNNAME="VRF_SBI", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, VNICID=4, VLANID=100, BEGINADDR4="192.168.79.2", ENDADDR4="192.168.89.14", MASKLEN=28, OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="10.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE; 
      ADD AUTOSCALINGSERVICE: SERVICENAME="VRF_SBI_200", VPNNAME="VRF_SBI", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, VNICID=5, VLANID=200, BEGINADDR4="192.168.79.18", ENDADDR4="192.168.79.30", MASKLEN=28, OSPFENABLE=TRUE, OSPFPROCID=6, OSPFAREAID="10.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE;
      ```
5. 打开IP路由自动配置开关。

   ```
   SET AUTOCONFIG: SWITCHFLAG=TRUE;
   ```

   **说明** 

   从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。
6. 配置NRF基础数据。
   1. 配置运营商信息、运营商签约用户的Home PLMN。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。

      ```
      ADD NGMNO: NOID=0, FULLNAME="Operator A", SHORTNAME="OA";
      ```

      ```
      ADD NGHPLMN: NOID=0, MCC="123", MNC="03";
      ```
   2. 打开NRF基本功能、NF发现的License。

      ```
      SET LICENSESWITCH: LICITEM="LKV2NFBNR01", SWITCH=ENABLE;
      SET LICENSESWITCH: LICITEM="LKV2NFDNR01", SWITCH=ENABLE;
      ```
   3. 配置NRF实例信息。

      ```
      ADD NFUUID: NFTYPE=NfNRF, NFINSTANCENAME="NRF_INSTANCE_0";
      ```
7. 配置NRF服务化接口数据。
   1. 增加NRF服务化接口的IP地址。

      ```
      ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.7", VPNINSTNAME="VRF_SBI", DESC="FOR SBI Server";
      ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="172.16.0.8", VPNINSTNAME="VRF_SBI", DESC="FOR SBI Client";
      ```
   2. 配置Nnrf接口的HTTP信息。

      ```
      ADD HTTPLEGRP: INDEX=3, DESC="NRF";
      ```

      ```
      ADD HTTPLE: INDEX=5, HTTPLEGRPIDX=3, LETYPE=SERVER, IPTYPE=IPv4, IPV4="172.16.0.7", PORT=8080, VPNNAME="VRF_SBI"", TLSFLG=NO, DESC="NRF Server";
      ADD HTTPLE: INDEX=6, HTTPLEGRPIDX=3, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="172.16.0.8", VPNNAME="VRF_SBI"", DESC="NRF Client";
      ```

      ```
      ADD SBIAPLE: INDEX=3, HTTPLEGRPIDX=3, NFTYPE=NFTypeNRF, DESCRIPTION="NRF";
      ```
8. 打开NF Token管理及NF认证的License。为指定的NF添加Token有效期。

   ```
   SET LICENSESWITCH:LICITEM="LKV2NFANR01",SWITCH=ENABLE;
   ADD TOKENEXP: SCFGTYPE=BYNFTYPE, NFTYPE=AMF, EXPTIME=180;
   ```
9. 修改NRF定时器。

   ```
   SET NRFTIMER: NFTYPE=AMF, HBTIMES=3, HEARTBEATTIMER=10, DISCVALIDTIMER=86400, SUBVALIDTIMER=86400;
   SET NRFTIMER: NFTYPE=SMF, HBTIMES=3, HEARTBEATTIMER=10, DISCVALIDTIMER=86400, SUBVALIDTIMER=86400;
   SET NRFTIMER: NFTYPE=NSSF, HBTIMES=3, HEARTBEATTIMER=10, DISCVALIDTIMER=86400, SUBVALIDTIMER=86400;
   ```