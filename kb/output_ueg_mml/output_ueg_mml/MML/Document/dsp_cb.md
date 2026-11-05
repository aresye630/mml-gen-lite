# 显示CB表(DSP CB)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询控制表的占用情况。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                           |
|:-------|:-------|:-----------------------------------------------------------------------------------------------|
| RUNAME | RU名称   | 可选必选说明：必选参数 该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 取值范围：0~63 位字符串 默认值：无                            |
| SPPNO  | 进程号    | 可选必选说明：必选参数 参数含义：该参数用于设置需要查询的SPP进程的进程号。 取值范围：0~20 默认值：无                                        |
| PIDNO  | PID号   | 可选必选说明：必选参数 参数含义：该参数用于指定功能子模块号。 取值范围：“MM(MM)”“SM(SM)”“UDM(UDM)” 默认值：无  说明： 参数取值“UDM(UDM)”为保留值。 |
| FR     | 强制释放Cb | 可选必选说明：可选参数 参数含义：该参数用于强制释放指定的CB。 取值范围：“NO(否)”“YES(是)” 默认值：“NO(否)”。  说明： 强制释放可能会打断该CB关联用户的当前流程。 |

#### 使用实例

查询控制表的占用情况：

DSP CB: RUNAME="USN\_SP\_RU\_0066", SPPNO=0, PIDNO=MM;

```
%%DSP CB: RUNAME="USN_SP_RU_0066", SPPNO=0, PIDNO=MM;%%
RETCODE = 0 执行成功。
 
查询结果如下
-----------
                RU名称  =  USN_SP_RU_0066
                进程号  =  0
                 PID号  =  MM
           使用中的CB数 =  0
         最大使用的CB数 =  6000
       MM_DEREGISTERED  =  0
         MM_REGISTIDLE  =  0
        MM_REGISTCONNT  =  0
             MM_ATTACH  =  0
          MM_UE_DETACH  =  0
          MM_CN_DETACH  =  0
         MM_S1_RELEASE  =  0
        MM_SERVICE_REQ  =  0
             MM_PAGING  =  0
      MM_INTRA_TAU_NEW  =  0
      MM_INTRA_TAU_OLD  =  0
      MM_INTER_TAU_NEW  =  0
      MM_INTER_TAU_OLD  =  0
              MM_GUARD  =  0
MM_PATHSWITCH_HANDOVER  =  0
 MM_INTRA_HANDOVER_NEW  =  0
 MM_INTRA_HANDOVER_OLD  =  0
 MM_INTER_HANDOVER_NEW  =  0
 MM_INTER_HANDOVER_OLD  =  0
       MM_GUTI_REALLOC  =  0
         MM_IU_RELEASE  =  0
          MM_INTRA_RAU  =  0
      MM_INTER_RAU_NEW  =  0
      MM_INTER_RAU_OLD  =  0
   MM_INTRA_SRNS_RELOC  =  0
    MM_INTER_RELOC_NEW  =  0
    MM_INTER_RELOC_OLD  =  0
          MM_UECTX_MOD  =  0
            MM_COM_SEC  =  0
        MM_PTMSI_RELOC  =  0
(结果个数 = 1)
 
--- END
```

#### 输出结果说明

| 输出项名称                              | 输出项解释                                            |
|:-----------------------------------|:-------------------------------------------------|
| RU名称                               | 查询所在的SPP进程的SPU资源单元名。                             |
| 进程号                                | 查询所在的SPP进程的进程号。                                  |
| PID号                               | 查询的功能子模块号。                                       |
| 使用的CB数                             | 使用中的CB数                                          |
| 最大使用的CB数                           | 最大使用的CB数                                         |
| MM_DEREGISTERED                    | 用户处于分离状态的CB数                                     |
| MM_REGISTIDLE                      | 用户处于无信令连接的稳定态的CB数                                |
| MM_REGISTCONNT                     | 用户处于有信令连接的稳定态的CB数                                |
| MM_ATTACH                          | 用户处于MM_ATTACH状态的CB数                              |
| MM_UE_DETACH                       | 用户处于MM_UE_DETACH状态CB数                            |
| MM_CN_DETACH                       | 用户处于MM_CN_DETACH状态CB数                            |
| MM_S1_RELEASE                      | 用户处于MM_S1_RELEASE状态CB数                           |
| MM_SERVICE_REQ                     | 用户处于MM_SERVICE_REQ状态CB数                          |
| MM_PAGING                          | 用户处于MM_PAGING状态CB数                               |
| MM_INTRA_TAU_NEW                   | 用户处于MM_INTRA_TAU_NEW状态CB数                        |
| MM_INTRA_TAU_OLD                   | 用户处于MM_INTRA_TAU_OLD状态CB数                        |
| MM_INTER_TAU_NEW                   | 用户处于MM_INTER_TAU_NEW状态CB数                        |
| MM_INTER_TAU_OLD                   | 用户处于MM_INTER_TAU_OLD状态CB数                        |
| MM_GUARD                           | 用户处于MM_GUARD状态CB数                                |
| MM_PATHSWITCH_HANDOVER             | 用户处于MM_PATHSWITCH_HANDOVER状态CB数                  |
| MM_INTRA_HANDOVER_NEW              | 用户处于MM_INTRA_HANDOVER_NEW状态CB数                   |
| MM_INTRA_HANDOVER_OLD              | 用户处于MM_INTRA_HANDOVER_OLD状态CB数                   |
| MM_INTER_HANDOVER_NEW              | 用户处于MM_INTER_HANDOVER_NEW状态CB数                   |
| MM_INTER_HANDOVER_OLD              | 用户处于MM_INTER_HANDOVER_OLD状态CB数                   |
| MM_GUTI_REALLOC                    | 用户处于MM_GUTI_REALLOC状态CB数                         |
| Max USER CB Number                 | 最大使用的User CB数                                    |
| UsedUserCbNumber                   | 最大使用中的User CB数                                   |
| UsedMultiCbNumber                  | 最大使用中的Multi CB数                                  |
| UsedPdpCbNumber                    | 最大使用中的Pdp CB数                                    |
| E_GUSM_USER_IDLE                   | User CB处于E_GUSM_USER_IDLE状态CB数                   |
| E_GUSM_USER_PENDING                | User CB处于E_GUSM_USER_PENDING状态CB数                |
| E_GUSM_USER_DETACH                 | User CB处于E_GUSM_USER_DETACH状态CB数                 |
| E_GUSM_USER_IU_RELEASE             | User CB处于E_GUSM_USER_IU_RELEASE状态CB数             |
| E_GUSM_USER_SERVICE_REQUEST        | User CB处于E_GUSM_USER_SERVICE_REQUEST状态CB数        |
| E_GUSM_USER_GGSN_ACT_PDP           | User CB处于E_GUSM_USER_GGSN_ACT_PDP状态CB数           |
| E_GUSM_USER_RAU_NEW                | User CB处于E_GUSM_USER_RAU_NEW状态CB数                |
| E_GUSM_USER_RAU_OLD                | User CB处于E_GUSM_USER_RAU_OLD状态CB数                |
| E_GUSM_USER_HO_NEW                 | User CB处于E_GUSM_USER_HO_NEW状态CB数                 |
| E_GUSM_USER_HO_OLD                 | User CB处于E_GUSM_USER_HO_OLD状态CB数                 |
| E_GUSM_USER_SUSPEND                | User CB处于E_GUSM_USER_SUSPEND状态CB数                |
| E_GUSM_USER_FSM_STATE_BUTT         | User CB处于E_GUSM_USER_FSM_STATE_BUTT状态CB数         |
| E_SM_USER_IDLE                     | User CB处于E_SM_USER_IDLE状态CB数                     |
| E_SM_USER_PENDING                  | User CB处于E_SM_USER_PENDING状态CB数                  |
| E_SM_USER_S1_ATTACH                | User CB处于E_SM_USER_S1_ATTACH状态CB数                |
| E_SM_USER_S1_DETACH                | User CB处于E_SM_USER_S1_DETACH状态CB数                |
| E_SM_USER_INTRA_TRAU_NEW           | User CB处于E_SM_USER_INTRA_TRAU_NEW状态CB数           |
| E_SM_USER_INTRA_TRAU_OLD           | User CB处于E_SM_USER_INTRA_TRAU_OLD状态CB数           |
| E_SM_USER_INTER_TRAU_NEW           | User CB处于E_SM_USER_INTER_TRAU_NEW状态CB数           |
| E_SM_USER_INTER_TRAU_OLD           | User CB处于E_SM_USER_INTER_TRAU_OLD状态CB数           |
| E_SM_USER_X2_HO_NEW                | User CB处于E_SM_USER_X2_HO_NEW状态CB数                |
| E_SM_USER_X2_HO_OLD                | User CB处于E_SM_USER_X2_HO_OLD状态CB数                |
| E_SM_USER_INTRA_S1_HO_NEW          | User CB处于E_SM_USER_INTRA_S1_HO_NEW状态CB数          |
| E_SM_USER_INTRA_S1_HO_OLD          | User CB处于E_SM_USER_INTRA_S1_HO_OLD状态CB数          |
| E_SM_USER_INTER_S1_HO_NEW          | User CB处于E_SM_USER_INTER_S1_HO_NEW状态CB数          |
| E_SM_USER_INTER_S1_HO_OLD          | User CB处于E_SM_USER_INTER_S1_HO_OLD状态CB数          |
| E_SM_USER_S1_RELEASE               | User CB处于E_SM_USER_S1_RELEASE状态CB数               |
| E_SM_USER_UE_INIT_SERVICE_REQUEST  | User CB处于E_SM_USER_UE_INIT_SERVICE_REQUEST状态CB数  |
| E_SM_USER_NET_INIT_SERVICE_REQUEST | User CB处于E_SM_USER_NET_INIT_SERVICE_REQUEST状态CB数 |
| E_SM_USER_HSS_INIT_MOD             | User CB处于E_SM_USER_HSS_INIT_MOD状态CB数             |
| E_SM_USER_FSM_STATE_BUTT           | User CB处于E_SM_USER_FSM_STATE_BUTT状态CB数           |
| MM_PTMSI_RELOC                     | User CB处于MM_PTMSI_RELOC状态CB数                     |