# 查询计费CDR参数（LST CHGCDR）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询计费CDR参数的配置，包括各种话单内容配置选项、SGSN节点标识等。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询计费CDR参数的配置信息：

LST CHGCDR:;

```
%%LST CHGCDR:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                           M-CDR选项   =  SERVED_IMEI & SGSN_ADDR & MS_NETWORK_CAPABILITY & RAC & LAC & CI & CHANGE_OF_LOCATION & DURATION & DIAGNOSTICS & NODE_ID & SERVED_MSISDN & SYSTEM_TYPE & CC_SELECT_MODE & CELL_PLMN_ID
                        S-SMO-CDR选项  =  SERVED_IMEI & SERVED_MSISDN & MS_NETWORK_CAPABILITY & SC & RECORDING_ENTITY & LAC & RAC & CI & NODE_ID & SYSTEM_TYPE & DEST_NUM & CC_SELECT_MODE
                        S-SMT-CDR选项  =  SERVED_IMEI & SERVED_MSISDN & MS_NETWORK_CAPABILITY & SC & RECORDING_ENTITY & LAC & RAC & CI & NODE_ID & SYSTEM_TYPE & CC_SELECT_MODE
                            S-CDR选项  =  NETWORK_INITIATED_PDP & SERVED_IMEI & SGSN_ADDR & MS_NETWORK_CAPABILITY & RAC & LAC & CI & APNNI & PDP_TYPE & SERVED_PDP_ADDR & LIST_OF_TDV & DIAGNOSTICS & NODE_ID & APN_SELECT_MODE & APNOI & SERVED_MSISDN & SYSTEM_TYPE & RNC_UDV & CC_SELECT_MODE & DAF & RECORD_EXTENTIONS & IMSI_UNAUTHENTICATED_FLAG & USER_CSG_INFORMATION & SERVED_PDP_ADDR_EXT
                       LCS-MT-CDR选项  =  SERVED_MSISDN & SGSN_ADDR & MEASUREMENT_DURATION & LOCATION & RAC & LOCATION_ESTIMATE & NODE_ID & CC_SELECT_MODE & SYSTEM_TYPE & LCS_CAUSE
                       LCS-MO-CDR选项  =  SERVED_MSISDN & SGSN_ADDR & LCS_PRIOPITY & MEASUREMENT_DURATION & LOCATION & RAC & LOCATION_ESTIMATE & NODE_ID & CC_SELECT_MODE & SYSTEM_TYPE
                       LCS-NI-CDR选项  =  SGSN_ADDR & SERVED_IMEI & MEASUREMENT_DURATION & LOCATION & RAC & LOCATION_ESTIMATE & NODE_ID & CC_SELECT_MODE & SYSTEM_TYPE
                         SGSN节点标识  =  InvalidNodeID                
                 本地用户缺省计费属性  =  普通计费
                 拜访用户缺省计费属性  =  普通计费
                 漫游用户缺省计费属性  =  普通计费
                   缺省非本地用户类型  =  漫游用户
                   配置本地话单序列号  =  有
                     忽略签约计费属性  =  NULL
                     丢失话单告警门限  =  20000
                       话单关闭原因值  =  正常释放
                      PLMN ID控制策略  =  IMSI中的PLMN ID
                       PLMNCG范围扩展  =  允许非PLMNCG
                     强制生成话单方式  =  不强制生成话单
                     强制生成话单时间  =  00:00:00
                          保持请求QoS  =  否
              话单填写PLMN ID选择策略  =  位置信息中的PLMN ID
              话单发送PLMN ID选择策略  =  位置信息中的PLMN ID
 MOCN中Non-supporting UE的PLMN获取策略 = 服务PLMN
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考**SET CHGCDR**命令参数说明。