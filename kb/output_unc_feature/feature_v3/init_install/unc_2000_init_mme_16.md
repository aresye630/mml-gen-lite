# 配置移动性管理

* 操作场景
* 必备事项
* 操作步骤
* 验证方法

## 操作场景

本操作指导介绍在运行网络中配置移动性管理特性的操作过程。

移动性管理功能EMM（EPS Mobility Management）用来控制UE（User Equipment）在LTE/EPC的接入及跟踪UE当前的位置信息，即UE当前所在的TA(Tracking Area)/TA List、当前所在的MME（Mobilit Management Entity）等信息。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

数据

系统为移动性管理通用参数提供了默认值，这些默认值为推荐值。用户也可以根据实际网络情况针对部分选项进行调整，使MME在本网络中更高效工作。

本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****SET EMM**** | T3422（s）（T3422） | 6 | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令  当使用NB-IoT业务时，需通过****SET NBEMM****来配置移动性管理。 |
|  | N3422（times）（N3422） | 4 |  |  |
|  | T3450（s）（T3450） | 6 |  |  |
|  | N3450（times）（N3450） | 4 |  |  |
|  | T3460（s）（T3460） | 6 |  |  |
|  | N3460（times）（N3460） | 4 |  |  |
|  | T3470（s）（T3470） | 6 |  |  |
|  | N3470（times）（N3470） | 4 |  |  |
|  | T3412（min）（T3412） | 54 |  |  |
|  | T3402（min）（T3402） | 12 |  |  |
|  | T3413（s）（T3413） | 6 |  |  |
|  | N3413（times）（N3413） | 2 |  |  |
|  | 重寻呼间隔递增值（s）（PAGINGDELTA） | 0 |  |  |
|  | 移动可达定时器（min）（RCHTMR） | 58 |  |  |
|  | GUTI重分配定时器（h）（GUTITMR） | 0 |  |  |
|  | Attach或TAU中重分配GUTI（GUTIREALLOC） | YES |  |  |
|  | Handover准备定时器（s）（HOPRETMR） | 10 |  |  |
|  | 源侧Handover完成定时器（s）（HOCMPSRCTMR） | 10 |  |  |
|  | 目标侧Handover完成定时器（s）（HOCMPTGTTMR） | 10 |  |  |
|  | T3定时器（s）（T3） | 10 |  |  |
| ****ADD TALST**** | TA List标号（TALISTID） | 1 |  | 增加跟踪区域码列表。 |
|  | TAI（TAI） | 46001000010 |  |  |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. **可选：**设置移动性管理EMM（EPS Mobility Management）参数。

   ```
   SET EMM:T3422=6,N3422=4,T3450=6,N3450=4,T3460=6,N3460=4,T3470=6,N3470=4,T3412=54,T3402=12,T3413=6,N3413=2,PAGINGDELTA=0,RCHTMR=58,GUTITMR=0,GUTIREALLOC=YES,HOPRETMR=10,HOCMPSRCTMR=10,HOCMPTGTTMR=10,T3=10;
   ```
3. 增加跟踪区域码列表。

   ```
   ADD TALST:TALISTID=1,TAI="4600100010";
   ```

## 验证方法

用户成功附着到网络。

1. 进入“MML命令行-UNC”窗口。
2. 执行****LST EMM****命令，查询当前EMM参数配置表中的信息。

   ```
   %%LST EMM:;%% 
   RETCODE = 0  操作成功。  

   操作结果如下 
   ------------                          
                            T3422（s）  =  6                      
                        N3422（times）  =  4                         
                            T3450（s）  =  6                      
                        N3450（times）  =  4                         
                            T3460（s）  =  6                      
                        N3460（times）  =  4                          
                            T3470（s）  =  6                      
                        N3470（times）  =  4                        
                          T3412（min）  =  54                        
                          T3402（min）  =  12                          
                            T3413（s）  =  6                      
                        N3413（times）  =  2               
                 重寻呼间隔递增值（s）  =  0            
              高优先级业务的T3413（s）  =  2        
          高优先级业务的N3413（times）  =  4 
   高优先级业务的重寻呼间隔递增值（s）  =  0               
                 移动可达定时器（min）  =  58     
       不可达用户隐式分离定时器（min）  =  0               
                 GUTI重分配定时器（h）  =  0            
               Attach或TAU中重分配GUTI  =  重分配GUTI            
               Handover准备定时器（s）  =  10         
           源侧Handover完成定时器（s）  =  10      
         目标侧Handover完成定时器（s）  =  10                       
                         T3定时器（s）  =  10         
           测试用GUTI重分配定时器（m）  =  0         
           切换流程资源释放定时器（s）  =  10            
               GUTI重分配最大间隔（h）  =  0 
   (结果个数 = 1) 
   ---    END
   ```
3. 执行****LST TALST****命令，查询跟踪区列表和在该跟踪区列表中的跟踪区。

   * 查看所有跟踪区列表和与其对应的跟踪区：

     ```
     %%LST TALST:;%% 
     RETCODE = 0  操作成功。  

     结果如下 
     --------------  
     TA List 标号  TAI         描述   
     0             308015101   AREA1  
     0             308015102   AREA2  
     1             308015103   AREA3  
     2             4600100010  noname 
     (结果个数 = 4)
      ---    END
     ```
   * 查看包含跟踪区标识为308015101的跟踪区列表：

     ```
     %%LST TALST: TAI="308015101";%% 
     RETCODE = 0  操作成功。  

     结果如下 
     -------------- 
     TA List 标号  =  0          
     TAI  =  308015101         
     述  =  AREA1 
     (结果个数 = 1) 
     ---    END
     ```
4. 执行**DSP COMMMCTX**命令查询用户的MM上下文。

   **DSP COMMMCTX**: QUERYOPT=BYIMSI, IMSI=IMSI;

   预期结果：用户处于ECM CONNECTED状态。用户当前所在的TA区域码标识正确。

版权所有 © 华为技术有限公司
