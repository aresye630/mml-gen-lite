# 显示进程内线程信息（DSP PROCTHREAD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示进程内的线程信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                                                 |
|:----------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME          | RU名称   | 可选必选说明：必选参数 参数含义：用于说明RU的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则： 只能填写实际存在的资源单元或资源名称。当本命令在VNFP上使用时，需要先使用DSP RES查到“资源名称”，然后将“资源名称”的取值配置到本参数。当本命令在VNFC上使用时，需要先使用DSP RU查到“RU名称”，然后将“RU名称”的取值配置到本参数。 |
| PROCID          | 进程ID   | 可选必选说明：可选参数 参数含义：用于说明进程的编号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                                                                                                                             |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                                                         |

#### 使用实例

显示进程内线程信息：

```
DSP PROCTHREAD:RUNAME="VNODE_CSLB_VNFC_OMU_0001",PROCID=3,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
--------
RU名称                     进程ID    进程名称    线程ID             线程名称           组件绑定标识    CPU绑定标识    CPU使用率（%）    线程绑定标识       操作系统线程ID
                                                                                                                                                          
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675839457088    main thread        Bind            all            0                 Free               2332
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674943219456    DefSch0400         Free            all            0                 Free               2333
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674943084288    DefSch0500         Free            all            0                 Free               2334
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674499208960    ADMAPPDB2          Free            all            0                 Free               2335
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674499073792    DefSch0600         Free            all            0                 Free               2336
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959193856    ADMAPPDB1          Free            all            0                 Free               2337
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959464192    ADMSESS7           Free            all            0                 Free               2338
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959329024    ADMAPPDB0          Free            all            0                 Free               2339
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959599360    ADMSESS6           Free            all            0                 Free               2340
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959734528    ADMSESS5           Free            all            0                 Free               2344
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674498410240    PRFB               Free            all            0                 Free               2342
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674473301760    DbMemCheck         Free            all            0                 Free               2343
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673706329856    FileSync           Free            all            0                 Free               2344
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673705142016    DirMaintain        Free            all            0                 Free               2345
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673705006848    PRFG               Free            all            0                 Free               2346
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674473436928    PRFF               Free            all            0                 Free               2347
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673713182464    PfbCfgMsg          Free            all            0                 Free               2348
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675681208064    PfSB               Free            all            0                 Free               2349
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674498275072    PfSC               Free            all            0                 Free               2350
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673717327616    measureMsgProc     Free            all            0                 Free               2351
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673704871680    PfGRep             Free            all            0                 Free               2352
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674959869696    ADMSESS4           Free            all            0                 Free               2353
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675211548416    ADMSESS2           Free            all            0                 Free               2354
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675837556480    IPC0000            Free            all            0                 Free               2355
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675702134528    DefSch0200         Free            all            0                 Free               2356
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675701999360    MsgAllocCheck      Free            all            0                 Free               2357
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675697116928    DefSch0900         Free            all            0                 Free               2358
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675838199552    DMS_TIPC_SEND      Free            all            0                 Free               2359
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675838265088    VCLK               Free            0              0                 Free               2360
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675838232320    TICK               Free            all            0                 Free               2361
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675838400256    BOX_Out            Free            all            0                 Free               2362
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674960004864    ADMSESS3           Free            all            0                 Free               2372
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675681613568    DefSch0100         Free            all            0                 Free               2373
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675681343232    DefSch0300         Free            all            0                 Free               2374
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675211818752    ADMSESS0           Free            all            0                 Free               2375
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675211683584    ADMSESS1           Free            all            0                 Free               2376
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675681478400    DefSch0101         Free            all            0                 Free               2377
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674534381312    AppThread          Free            all            0                 Free               2378
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675211953920    DefSch0700         Free            all            0                 Free               2379
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140674978445056    RPM_Listen         Bind            all            0                 Free               2380
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140675212089088    DefSch0800         Free            all            0                 Free               2381
VNODE_CSLB_VNFC_OMU_0001    3         CFG         140673704736512    CliGetThreadCpu    Free            all            0                 Free               2382
(结果个数 = 42)
---    END
```

#### 输出结果说明

| 输出项名称     | 输出项解释                  |
|:----------|:-----------------------|
| RU名称      | 用于说明RU的名称。             |
| 进程ID      | 用于说明进程的编号。             |
| 进程名称      | 用于说明进程的名称。             |
| 线程ID      | 用于说明进程内线程的编号。          |
| 线程名称      | 用于说明进程内线程的名称。          |
| 组件绑定标识    | 用于说明进程内线程的组件绑定情况。      |
| CPU绑定标识   | 用于说明进程内线程的CPU绑定情况。     |
| CPU使用率（%） | 用于说明进程内线程的CPU使用率，单位：%。 |
| 线程绑定标识    | 用于说明进程内线程绑定情况。         |
| 操作系统线程ID  | 用于说明进程内操作系统线程的编号。      |