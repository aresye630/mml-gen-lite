# 查询OMU信息(DSP OMU)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于请求系统显示OMU的状态、资源信息。

当CSP应用于NFV模式并启用了扩展OMU功能时，本命令会同时显示扩展OMU的状态、资源信息。

## 注意事项

- HA（High Availability）模式下，当备端的状态为未知或宕机时，显示的备端的启动时间为无效值。
- 对所有资源状态进行查询，需要的时间较长，因此资源信息中的资源状态是上次监控资源时保存的状态，与资源的实际状态不一定相同。
- 系统会根据业务调整资源配置，本命令根据系统实际配置的资源显示，示例仅供参考。
- 若系统处于升级观察期，Pod的位置无法刷新，可能会造成Pod的“位置描述”字段显示不准确。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                  |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RES    | 资源显示状态 | 可选必选说明：必选参数。 参数含义：用于标识查询OMU信息时资源显示状态的分类。 取值范围： “SIMPLE(简单的OMU信息)”：查询简单的OMU信息。“DETAIL(详细的OMU信息)”：查询详细的OMU信息。“UPGDETAIL(升级场景的OMU信息)”：查询升级场景的OMU信息。“CHKDETAIL(安装场景的OMU信息)”：查询安装场景的OMU信息。 默认值：“DETAIL(详细的OMU信息)”。 配置原则：无。 |

## 使用实例

- 查询OMU信息（HA模式，OMU部署在节点上），执行下面的命令：

  ```
  DSP OMU:;
  ```

  ```
  %%DSP OMU: RES=DETAIL;%%
  RETCODE = 0  操作成功

  OMU基本信息 -- HA模式
  ---------------------
    节点      版本                   OMU状态  Pod名称    位置描述       开始运行时间
   cgplite-0  CGP V200R021C00B060  主用     cgplite-0  10.11.159.168  2020-05-28 14:48:09+08:00
   cgplite-1  CGP V200R021C00B060  备用     cgplite-1  10.12.150.241  2020-05-28 14:48:09+08:00
  (结果个数 = 2)

  资源信息
  --------
   节点       资源名      资源类型  资源状态

   cgplite-0  bkm         进程      已激活  
   cgplite-0  cgpbroker   进程      已激活  
   cgplite-0  cm          进程      已激活  
   cgplite-0  dcm         进程      已激活  
   cgplite-0  deploy      进程      已激活  
   cgplite-0  devlog      进程      已激活  
   cgplite-0  fm          进程      已激活  
   cgplite-0  imap        进程      已激活
   cgplite-0  keyfile     进程      已激活
   cgplite-0  kpi         进程      已激活
   cgplite-0  load        进程      已激活  
   cgplite-0  logzip      进程      已激活  
   cgplite-0  mit         进程      已激活  
   cgplite-0  mm          进程      已激活  
   cgplite-0  mmlserver   进程      已激活  
   cgplite-0  mt          进程      已激活  
   cgplite-0  mt0         进程      已激活
   cgplite-0  omufile     进程      已激活 
   cgplite-0  pm          进程      已激活  
   cgplite-0  prm_server  进程      已激活
   cgplite-0  rcm         进程      已激活  
   cgplite-0  rsm         进程      已激活 
   cgplite-0  scheduler   进程      已激活  
   cgplite-0  security    进程      已激活  
   cgplite-0  sync        进程      已激活
   cgplite-0  ua          进程      已激活 
   cgplite-0  utility     进程      已激活  
   cgplite-0  db          数据库    已激活  
   cgplite-0  dbfile      数据库    已激活  
   cgplite-0  dbha        数据库    已激活  
   cgplite-0  cron        系统服务  已激活  
   cgplite-0  sftp        系统服务  已激活
   cgplite-0  base        网络      已激活   
   cgplite-0  fabric1     网络      已激活  
   cgplite-0  fabric2     网络      已激活
   cgplite-0  paas_nic    网络      已激活  
   cgplite-1  bkm         进程      未激活  
   cgplite-1  cgpbroker   进程      未激活  
   cgplite-1  cm          进程      未激活  
   cgplite-1  dcm         进程      未激活  
   cgplite-1  deploy      进程      未激活  
   cgplite-1  devlog      进程      未激活  
   cgplite-1  fm          进程      未激活  
   cgplite-1  imap        进程      已激活
   cgplite-1  keyfile     进程      已激活
   cgplite-1  kpi         进程      未激活
   cgplite-1  load        进程      未激活  
   cgplite-1  logzip      进程      未激活  
   cgplite-1  mit         进程      未激活  
   cgplite-1  mm          进程      未激活  
   cgplite-1  mmlserver   进程      未激活  
   cgplite-1  mt          进程      未激活  
   cgplite-1  mt0         进程      未激活 
   cgplite-1  omufile     进程      已激活 
   cgplite-1  pm          进程      未激活  
   cgplite-1  prm_server  进程      未激活
   cgplite-1  rcm         进程      未激活  
   cgplite-1  rsm         进程      未激活 
   cgplite-1  scheduler   进程      未激活  
   cgplite-1  security    进程      未激活  
   cgplite-1  sync        进程      未激活
   cgplite-1  ua          进程      未激活  
   cgplite-1  utility     进程      未激活  
   cgplite-1  db          数据库    已激活  
   cgplite-1  dbfile      数据库    已激活  
   cgplite-1  dbha        数据库    未激活  
   cgplite-1  cron        系统服务  已激活  
   cgplite-1  sftp        系统服务  已激活 
   cgplite-1  base        网络      已激活   
   cgplite-1  fabric1     网络      已激活  
   cgplite-1  fabric2     网络      已激活
   cgplite-1  paas_nic    网络      已激活  
  (结果个数 = 72)

  ---    END
  ```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 资源名     | 用于返回OMU的资源名称，该参数是资源的唯一标识，各资源的名称都不相同。 OMU的服务进程包括以下几种： “bkm” “cgpbroker”“cm” “dcm” “deploy” “devlog” “fm” “imap” “keyfile”“kpi”“load” “logzip” “mit” “mm” “mmlserver” “mt” “mt0” “omufile”“pm” “prm_server” “rcm”“rsm”“scheduler” “security” “sync” “ua” “utility” 数据库资源类型如下： “dbha” “db” “dbfile” Linux的系统服务类型包括以下几种： “cron” “sftp” 网络类型包括以下几种： “base” “fabric1” “fabric2” “paas_nic”                                                |
| 资源类型    | 用于返回OMU管理的资源所属的类型。 “进程”：OMU的服务进程。此类资源只会在主OMU上启动 “数据库”：数据库类型。 “系统服务”：Linux的系统服务类型。OMU运行中需要使用的系统服务，由OMU负责管理。此类资源根据OMU的需求，在主备OMU上分别启动。 “网络”：网络类型。主要是网口和光纤。此类资源在主备OMU上都需要启动。                                                                                                                                                                                                                                                            |
| 资源状态    | 用于返回资源当前的运行状态。 “已激活”：表示该资源成功激活。“未激活”：表示该资源未激活。“正在激活”：是一种中间态，表示该资源正在进行激活操作。“正在去激活”：是一种中间态，表示该资源正在进行去激活操作。“异常”：表示该资源的状态异常。如：需要去激活的资源处于激活状态。“故障”：表示该资源状态异常后无法修复。“未知”：表示该资源的状态无法得到。如：监控超时。                                                                                                                                                                                                                                              |
| OMU状态   | 用于返回OMU当前的状态。 “初始化”：表示系统正在进行初始化，未确定主备。“正在激活”：表示系统正在激活OMU正常运行所需要的服务或者资源，激活完成后，OMU就变成主用状态。“主用”：主用状态。“请求去激活”：处于主用状态的OMU发现本端有关键资源异常，则请求对端进行倒换检查。如果检查通过，则本端降备，否则本端回滚到主用状态。“同意对方去激活”：处于备用状态的OMU接收到主用OMU的“请求去激活”请求后，进行倒换检查（例如本机网络资源是否正常等），如果检查通过，则进入“同意对方去激活”状态。对端进入备用状态后，本端升主。“正在去激活”：原主用状态的OMU正在去激活本机的所有资源，操作完成后，此OMU的状态迁移到备用状态。“备用”：备用状态。“未知”：由于主备OMU通信异常，导致主用OMU无法获取对端状态，则将对端置为未知状态。一段时间后（默认5分钟）若仍无法获取对端状态，则将对端状态置为宕机状态。“宕机”：参见未知状态说明。 |
| 节点      | 用于返回CGPLite容器所在节点信息。                                                                                                                                                                                                                                                                                                                                                                                                                |
| 版本      | 用于返回CGPlite容器的版本信息。                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Pod名称   | 用于返回CGPLite容器的主机名。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 位置描述    | 用于返回CGPLite容器的位置信息。                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 开始运行时间  | 用于返回CGPLite容器开始运行时间。                                                                                                                                                                                                                                                                                                                                                                                                                |