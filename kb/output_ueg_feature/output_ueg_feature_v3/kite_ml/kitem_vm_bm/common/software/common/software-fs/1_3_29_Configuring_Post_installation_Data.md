# 安装后配置

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

VNF安装完成后，需要配置部分数据，确保系统正常工作。

## 必备事项

前提条件

已实例化网元。

## 操作步骤

1. 登录UEG OM portal。
2. 请参见《UEG安全配置》，对系统进行安全配置，修改系统默认帐号密码。
3. 在UEG OM portal，选择“监控分析 > 告警管理 > 活动告警”，查看系统是否上报告警“ALM-135301 PaasBroker和FusionStage的通信失败”。

   * 是 => 步骤4。
   * 否 => 步骤5。
4. 处理ALM-135301 PaasBroker和FusionStage的通信失败告警。
5. **仅当**网元已经实例化，且OM操作维护IP（即OM浮动IP）的规划值已被更改时，才需要修改OM操作维护IP地址。示例如下：

   ```
   MOD VIRTUALIP: IPTYPE=IPv4, IPV4ADDR="10.145.27.173", IPV4GW="10.145.27.1", NETMASK="255.255.255.0";
   ```

   执行该命令会导致UEG OM Portal的连接中断。

   此时需要调整本地PC IP，与新的UEG的OM操作维护IP正常通信后，再重新登录UEG OM Portal。

   对于同网段IP，可以使用MOD VIRTUALIP/SET OMIP修改OM IP；对于不同网段的OM IP调整，请联系华为技术支持工程师处理或参考《修改OMU IP指导书》。

版权所有 © 华为技术有限公司
