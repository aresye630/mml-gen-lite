# 显示设备管理诊断信息（DSP DEVDIAGINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示设备管理诊断信息。当设备出现故障时，可以使用该命令查看属性待发送链表、属性变化原因信息、消息统计计数信息、设备属性轮询信息、设备对象信息和属性同步信息配置下发到组件侧信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                     |
|:----------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMPTYPE        | 组件类型   | 可选必选说明：必选参数 参数含义：该参数表示组件类型。 数据来源：本端规划 取值范围：枚举类型。 DEVMA：DEVMA组件，该组件用于收集本资源单元设备属性、运行状态和设备事件数据上报给总控模块，同时执行来自总控模块的各种设备操作。LDEVM：LDEVM组件，该组件用于给APP提供设备属性订阅功能。 默认值：无                            |
| DIAGTYPE        | 诊断信息类型 | 可选必选说明：必选参数 参数含义：该参数表示诊断信息类型。 数据来源：本端规划 取值范围：枚举类型。 NOTIFYLIST：属性待发送链表。ATTRCHGREASON：属性变化原因信息。MSGINFO：消息统计计数信息。DEVPOLLINFO：设备属性轮询信息。DEVOBJINFO：设备对象信息。ATTRSYNINFO：属性同步信息配置下发到组件侧信息。 默认值：无 |
| RUNAME          | RU名称   | 可选必选说明：必选参数 参数含义：该参数表示资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：使用DSP RU查看RU名称。                                                                                   |
| DEVID           | 设备ID   | 可选必选说明：条件必选参数，该参数在“DIAGTYPE”配置为“ATTRCHGREASON”时为必选参数。 参数含义：该参数表示设备ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                 |
| ATTRID          | 属性ID   | 可选必选说明：条件必选参数，该参数在“DIAGTYPE”配置为“ATTRCHGREASON”时为必选参数。 参数含义：该参数表示属性ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                 |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                             |

#### 使用实例

- 显示CSDB\_OM\_RU\_0001的待分发属性链表信息：

  ```
  DSP DEVDIAGINFO:RUNAME="CSDB_OM_RU_0001",COMPTYPE=DEVMA,DIAGTYPE=NOTIFYLIST,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  诊断信息  =  Display devminfo information. Index: 49 
  -----------------------------------------------------------------------------------------------------------------------------------
  QueueType    SubPID      DevId       AttrId      Length      AttrValue(0x)                         SubMod    SendCnt   LastSendTime
  -----------------------------------------------------------------------------------------------------------------------------------
  BatchSub     0xfa0002    0xc         0x172       0xc         01 11 40 00 01 00 00 00 15 00 00 00      6         4         2017/11 14:11:30.006
  BatchSub     0xfa0002    0xd         0x172       0xc         02 11 40 00 01 00 00 00 15 00 00 00      6         4         2017/11 14:11:30.006
  BatchSub     0xfa0002    0xe         0x172       0xc         03 11 40 00 01 00 00 00 15 00 00 00      6         4         2017/11 14:11:30.006
  BatchSub     0xfa0002    0xf         0x172       0xc         00 00 00 00 00 00 00 00 01 00 00 00      6         4         2017/11 14:11:30.006
  (结果个数 = 1)
  ---    END
  ```
- 显示CSDB\_OM\_RU\_0001上属性变化原因信息：

  ```
  DSP DEVDIAGINFO:RUNAME="CSDB_OM_RU_0001",COMPTYPE=DEVMA,DIAGTYPE=ATTRCHGREASON,DEVID="b",ATTRID="13",SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  诊断信息  =  Display devminfo information. Index: 28 
  devID    AttrID    AttrName           value             ChgNum  LastChgTime           R1     R2     R3     R4     R5     R6 
  ------------------------------------------------------------------------------------------------------------------------------------------------
  0xb       0x13      isAvailable       0x1                 2     15-18:32:22.188       29     41     0      0      0      0  
  (结果个数 = 1)
  ---    END
  ```
- 显示CSDB\_OM\_RU\_0001上DEVMA组件的消息统计计数信息：

  ```
  DSP DEVDIAGINFO:RUNAME="CSDB_OM_RU_0001",DIAGTYPE=MSGINFO,COMPTYPE=DEVMA,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  诊断信息  =  Display devminfo information. Index: 20 
  ----------------------------------------------------------------------------------------------------- 
  Global Sync Msg Cnt: 2(send) 0(resend) 0(lost)
  Dev Board Sync Msg Cnt: 0(send) 0(resend) 0(lost)
  Dev Create Sync Msg Cnt: 1(send) 0(resend) 0(lost)
  Dev Remove Sync Msg Cnt: 0(send) 0(resend) 0(lost)
  Dev Pull Sync Msg Cnt: 0(send) 0(resend) 0(lost)
  Attr Notify Sync Msg Cnt: 148(send) 0(resend) 0(lost) 148(recv)
  Attr S2A Sync Msg Cnt: 0(send) 0(resend) 0(lost) 0(recv)
  Attr Set Sync Msg Cnt: 0(send) 0(resend) 0(lost) 0(recv)
  InnerSub Sync Msg Cnt: 0(send) 0(resend)
  Batch Sync Msg Cnt: 14(send) 0(resend)
  ----------------------------------------------------------------------------------------------------- 
  (结果个数 = 1)
  ---    END
  ```
- 显示CSDB\_OM\_RU\_0001上的设备属性轮询信息：

  ```
  DSP DEVDIAGINFO:COMPTYPE=DEVMA,DIAGTYPE=DEVPOLLINFO,RUNAME="CSDB_OM_RU_0001",SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  诊断信息  =  Display devminfo information. Index: 7 
  poll data notify state: success(0)  fail(0) wait(false) notify(false)
  devID       devName        AttrNum 1stAttrId  Asyn RW Dyn SubDev PollCycle Timeout OutPro ErrNum AvTime(us) OutAvWait(ms) State
  -----------------------------------------------------------------------------------------------------------------
  0x2         VM0            1       0xdd       0    R  N   0      1000      132     132    0      51         38             0    
  0x4         eth0           1       0x2d       0    R  N   0      10000     13      13     0      68         35             0    
  0x4         eth0           2       0xc5       0    R  N   0      200       663     662    0      30         43             0    
  0x4         eth0           5       0x2a       0    R  N   0      1000      132     132    0      35         38             0    
  0x4         eth0           2       0x29       0    R  N   0      40        1345    1344   0      39         43             0    
  0x5         eth1           1       0x2d       0    R  N   0      10000     13      13     0      15         35             0    
  0x5         eth1           2       0xc5       0    R  N   0      200       663     662    0      3          43             0    
  0x5         eth1           5       0x2a       0    R  N   0      1000      132     132    0      19         38             0    
  0x5         eth1           2       0x29       0    R  N   0      40        2643    2642   0      34         43             0    
  0x7         loop0          1       0x29       0    R  N   0      40        2643    0      2643   26         0              0    
  0x7         loop0          1       0x2a       0    R  N   0      1000      132     0      132    27         0              0    
  0x7         loop0          1       0x2d       0    R  N   0      10000     13      0      13     32         0              0    
  0x7         loop0          3       0xc5       0    R  N   0      200       663     0      663    30         0              0    
  0x8         eth0:2:1:2     1       0x29       0    R  N   0      40        2643    2643   0      9          43             0    
  0x8         eth0:2:1:2     1       0x2a       0    R  N   0      1000      132     132    0      8          38             0    
  0x8         eth0:2:1:2     1       0x2d       0    R  N   0      10000     13      13     0      13         35             0    
  0x8         eth0:2:1:2     2       0xc5       0    R  N   0      200       663     663    0      4          43             0    
  0x9         eth0:2:1:1     1       0x29       0    R  N   0      40        2643    2643   0      7          43             0    
  0x9         eth0:2:1:1     1       0x2a       0    R  N   0      1000      132     132    0      6          38             0    
  0x9         eth0:2:1:1     1       0x2d       0    R  N   0      10000     13      13     0      8          35             0    
  0x9         eth0:2:1:1     2       0xc5       0    R  N   0      200       663     663    0      3          43             0    
  0xa         eth0:2:1:0     1       0x29       0    R  N   0      40        2643    2643   0      6          43             0    
  0xa         eth0:2:1:0     1       0x2a       0    R  N   0      1000      132     132    0      6          38             0    
  0xa         eth0:2:1:0     1       0x2d       0    R  N   0      10000     13      13     0      9          35             0    
  0xa         eth0:2:1:0     2       0xc5       0    R  N   0      200       663     663    0      3          43             0    
  -------------------------------------------------------------------------------------------------------------------------------
  devID       AttrNum     AttrId0   AttrId1   AttrId2   AttrId3   AttrId4   AttrId5   AttrId6   AttrId7   AttrId8   AttrId9   
  -------------------------------------------------------------------------------------------------------------------------------
  0x4         2           0xc5      0xc6      
  0x4         5           0x2a      0x2c      0x1b8     0x1bc     0x1cb     
  0x4         2           0x29      0x1de     
  0x5         2           0xc5      0xc6      
  0x5         5           0x2a      0x2c      0x1b8     0x1bc     0x1cb     
  0x5         2           0x29      0x1de     
  0x7         3           0xc5      0xc6      0x1d7     
  0x8         2           0xc5      0xc6      
  0x9         2           0xc5      0xc6      
  0xa         2           0xc5      0xc6      
  (结果个数 = 1)
  ---    END
  ```
- 显示CSDB\_OM\_RU\_0001上的设备对象信息：

  ```
  DSP DEVDIAGINFO:COMPTYPE=DEVMA,DIAGTYPE=DEVOBJINFO,RUNAME="CSDB_OM_RU_0001",SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  诊断信息  =  Display devminfo information. Index: 9 
  devID  devName             Position    ObjSt  ChannelID   OwnerPid    OLaSt  OLaEvt  MChLaSt  MChLaEv  BkupSt  MasterMngPID  BkupMngPID    HardType      ModuleID
  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  0x2    VM0                 0x1ffff     1      0xffffffff  0x80fc0012  5      14      0        0        0       0xffffffff    0xffffffff    0x1000000f    0x2     
  0x3    lfe0                0x1ffff     1      0xffffffff  0x80fc0012  1      14      0        0        0       0xffffffff    0xffffffff    0x10000100    0x2     
  0x4    eth0                0x10000     1      0xffffffff  0x80fc0012  1      14      0        0        0       0xffffffff    0xffffffff    0x10000102    0x2     
  0x5    eth1                0x10001     1      0xffffffff  0x80fc0012  1      14      0        0        0       0xffffffff    0xffffffff    0x10000102    0x2     
  0x6    pae                 0x1ffff     1      0xffffffff  0x80fc0012  1      14      0        0        0       0xffffffff    0xffffffff    0x10000103    0x2     
  0x7    loop0               0x1ffff     1      0xffffffff  0x80fc0012  1      14      0        0        0       0xffffffff    0xffffffff    0x10000106    0x2     
  0x8    eth0:2:1:2          0x10000     1      0xffffffff  0x80fc0012  13     16      0        0        0       0xffffffff    0xffffffff    0x10000105    0x2     
  0x9    eth0:2:1:0          0x10000     1      0xffffffff  0x80fc0012  13     16      0        0        0       0xffffffff    0xffffffff    0x10000105    0x2     
  0xa    eth0:2:1:1          0x10000     1      0xffffffff  0x80fc0012  13     16      0        0        0       0xffffffff    0xffffffff    0x10000105    0x2
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 诊断信息    | 用于表示设备诊断信息。 |