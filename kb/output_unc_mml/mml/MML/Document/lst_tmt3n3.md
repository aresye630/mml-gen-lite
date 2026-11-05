# 查询Tm接口消息T3N3参数(LST TMT3N3)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

本命令用于查询Tm接口消息的T3N3参数。

#### 注意事项

- 无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMMSGCFGMODE | Tm接口消息配置模式 | 可选必选说明：可选参数 参数含义：本参数用于选择Tm接口消息配置方式。 数据来源：全网规划 取值范围：“TMMSG_ALL（Tm接口消息全集）”“SPECIAL_TM_MSG（指定Tm接口消息）” 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TMMSG        | Tm接口消息     | 可选必选说明：条件可选参数 前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。 参数含义：Tm接口消息列表。 数据来源：全网规划 取值范围：“ECHO（Echo Request）”“STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”“UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”“TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”“TRK_USR_ATT_REQ（Trunk User Attach Request）”“TRK_USR_DET_REQ（Trunk User Detach Request）”“TRK_USR_HO_REQ（Trunk User Handover Request）”“TRK_USR_HO_NTF（Trunk User Handover Notification）”“TRK_USR_TAU_REQ（Trunk User TAU Request）”“TRK_USR_SR_REQ（Trunk User Service Request）”“NODE_ST_NTF（NE Status Notification）” 默认值 ：无 |

#### 使用实例

1. 查询指定Tm接口消息为Tm接口消息全集的参数配置：

   LST TMT3N3:TMMSGCFGMODE=TMMSG\_ALL ;

   ```
   %%LST TMT3N3:TMMSGCFGMODE=TMMSG_ALL ;%%
   RETCODE = 0  操作成功。

   操作结果如下
   ------------
     指定Tm接口消息  =  Tm接口消息全集         
         Tm接口消息  =  NULL     
      T-RESPONSE(s)  =  1   
   N-REQUEST(times)  =  1

   (结果个数 = 1)

   ---    END
   ```

#### 输出结果说明

参见ADD TMT3N3的参数标识。