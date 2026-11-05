# 查询微服务流控策略(LST MSFLOWCTRL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询流控参数配置信息：

- 若需要查询全部流控参数信息，请不要输入任何参数。
- 若需要查询某条流控参数的详细信息，请输入需要查询的参数或参数的组合。

## 注意事项

GBA场景下（仅虚机场景涉及），不支持查询微服务流控策略。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:---------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FCTYPE   | 流控类型   | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个流控类型查询流控参数配置信息。若不输入，表示查询所有流控类型下的配置信息。 取值范围：CPUFC(CPUFC)：表示HLB/AUSF/UDM/ENS的CPU流控。ASSUDRFC(ASSUDRFC)：表示UDM对USCDB的起控协控。ASSUDMFC(ASSUDMFC)：表示HLB对UDM/AUSF的起控协控。SCHEDULEFC(SCHEDULEFC)：表示基于调度的时延流控。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                            |
| FCMSTYPE | 微服务类型  | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个微服务类型查询流控参数配置信息。 取值范围：HLB(HLB)UDM(UDM)AUSF(AUSF)ENS(ENS) 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| FCSWITCH | 流控开关   | 可选必选说明：可选参数 参数含义：用于标识系统按照流控开关是否开启查询流控参数配置信息。 取值范围： OFF(关闭)ON(开启) 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FCITEM   | 流控资源项  | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个流控资源项查询流控参数配置信息。 取值范围： 当“流控类型”取值为“CPUFC(CPUFC)”，“微服务类型”为“HLB(HLB)”、“UDM(UDM)”、“AUSF(AUSF)”或“ENS(ENS)”时，取值范围如下：NODECPU(NODECPU)：表示虚机CPU（裸机POD CPU）。CONTCPU(CONTCPU)：表示容器CPU。PROCCPU(PROCCPU)：表示进程CPU。 默认值：无 当“流控类型”取值为“ASSUDRFC(ASSUDRFC)”，“微服务类型”为“UDM(UDM)”或“AUSF(AUSF)”时，取值范围如下：GDRUFCR(GDRUFCR)：表示全局DRU流控。DRUFCR(DRUFCR)：表示DRU流控。DSUFCR(DSUFCR)：表示DSU流控。DSGFCR(DSGFCR)：表示DSG流控。DBSFCR(DBSFCR)：表示DBS流控。 默认值：无 当“流控类型”取值为“ASSUDMFC(ASSUDMFC)”，“微服务类型”为“HLB(HLB)”时，取值范围如下：UDMFCR(UDMFCR)：表示UDM流控。AUSFFCR(AUSFFCR)：表示AUSF流控。 默认值：无 当“流控类型”取值为“SCHEDULEFC(SCHEDULEFC)”时，取值范围如下：LATENCY(LATENCY)：表示基于调度时延的流控。 默认值：无 配置原则：无 |

## 使用实例

1. 查询所有流控类型下的配置信息：

   ```
   LST MSFLOWCTRL:;
   ```

   ```
   %%LST MSFLOWCTRL:;%%
   RETCODE = 0  操作成功

   操作结果如下：
   ------------------------
   流控类型          微服务类型       流控开关        流控资源项    起控门限     解控门限       消息能力参考值        起控权重  

   CPUFC             HLB              开启            NODECPU       85           75             6000                  20            
   CPUFC             HLB              开启            CONTCPU       85           75             6000                  20            
   CPUFC             HLB              开启            PROCCPU       85           75             6000                  20            
   CPUFC             UDM              开启            NODECPU       85           75             6000                  20            
   CPUFC             UDM              开启            CONTCPU       85           75             6000                  20            
   CPUFC             UDM              开启            PROCCPU       85           75             6000                  20            
   CPUFC             AUSF             开启            NODECPU       85           75             10000                 20            
   CPUFC             AUSF             开启            CONTCPU       85           75             6000                  20            
   CPUFC             AUSF             开启            PROCCPU       85           75             10000                 20   
   CPUFC             ENS              开启            NODECPU       85           75             10000                 20            
   CPUFC             ENS              开启            CONTCPU       85           75             10000                 20            
   CPUFC             ENS              开启            PROCCPU       85           75             10000                 20  
   ASSUDRFC          UDM              开启            GDRUFCR       10           5              6000                  20            
   ASSUDRFC          UDM              开启            DRUFCR        10           5              6000                  20            
   ASSUDRFC          UDM              开启            DSUFCR        10           5              6000                  20            
   ASSUDRFC          UDM              开启            DSGFCR        3            1              6000                  20            
   ASSUDRFC          UDM              开启            DBSFCR        3            1              6000                  20            
   ASSUDRFC          AUSF             开启            GDRUFCR       20           10             6000                  20            
   ASSUDRFC          AUSF             开启            DRUFCR        20           10             6000                  20            
   ASSUDRFC          AUSF             开启            DSUFCR        20           10             6000                  20            
   ASSUDRFC          AUSF             开启            DSGFCR        3            1              6000                  20            
   ASSUDRFC          AUSF             开启            DBSFCR        3            1              6000                  20            
   ASSUDMFC          HLB              开启            UDMFCR        10           5              6000                  20            
   ASSUDMFC          HLB              开启            AUSFFCR       10           5              6000                  20
   SCHEDULEFC        UDM              开启            LATENCY       30           10             6000                  20        
   SCHEDULEFC        AUSF             开启            LATENCY       30           10             10000                 20
   SCHEDULEFC        ENS              开启            LATENCY       30           10             10000                 20
   (结果个数 = 27)

   ---    END
   ```
2. 查询“流控类型”为“CPUFC(CPUFC)”，“微服务类型”为“HLB(HLB)”的配置信息：

   ```
   LST MSFLOWCTRL: FCTYPE=CPUFC, FCMSTYPE=HLB;
   ```

   ```
   %%LST MSFLOWCTRL: FCTYPE=CPUFC, FCMSTYPE=HLB;%%
   RETCODE = 0  操作成功

   操作结果如下:
   ------------------------
   流控类型      微服务类型       流控开关              流控资源项    起控门限   解控门限  消息能力参考值  起控权重  

   CPUFC         HLB              开启                  NODECPU       85         75        6000            20            
   CPUFC         HLB              开启                  CONTCPU       85         75        6000            20            
   CPUFC         HLB              开启                  PROCCPU       85         75        6000            20            
   (结果个数= 3)

   ---    结束
   ```
3. 查询“流控类型”为“ASSUDRFC(ASSUDRFC)”、“微服务类型”为“AUSF(AUSF)”、“流控开关”为“ON(ON)”、“流控资源项”为“DRUFCR(DRUFCR)”的配置信息：

   ```
   LST MSFLOWCTRL: FCTYPE=ASSUDRFC, FCMSTYPE=AUSF, FCSWITCH=ON, FCITEM=DRUFCR;
   ```

   ```
   %%LST MSFLOWCTRL: FCTYPE=ASSUDRFC, FCMSTYPE=AUSF, FCSWITCH=ON, FCITEM=DRUFCR;%%
   RETCODE = 0  操作成功

   操作结果如下：
   ------------------------
                           流控类型  =  ASSUDRFC
                         微服务类型  =  AUSF
                           流控开关  =  开启
                         流控资源项  =  DRUFCR
                           起控门限  =  20
                            解控门限 =  10
                     消息能力参考值  =  6000
                           起控权重  =  20
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD MSFLOWCTRL**命令的参数说明。