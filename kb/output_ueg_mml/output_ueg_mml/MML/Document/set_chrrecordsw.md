# 设置CHR本地存盘开关（SET CHRRECORDSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

设置CHR本地存盘开关。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令初始记录表示默认打开的CHR类型。
- 开启SIP或RTP单据本地存盘会导致性能下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | MSGTYPE                                                                                                                                                                                                                                                                     |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 初始值    | SESS_CRT_FAIL、SESS_DEL_FAIL、SESS_MOD_FAIL、SESS_RPT_FAIL、ASSOC_CRT_FAIL、ASSOC_DEL_FAIL、ASSOC_MOD_FAIL、ASSOC_RPT_FAIL、SIP_CALL_FAIL、TRUNK_SESS_CRT_FAIL、TRUNK_BEAR_CRT_FAIL、TRUNK_ENB_ACT_FAIL、TRUNK_SESS_DEL_FAIL、TRUNK_BEAR_DEL_FAIL、TRUNK_ENB_DEL_FAIL、TRUNK_ENB_NOTI_FAIL |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE | 本地存盘错误类型开关 | 可选必选说明：必选参数 参数含义：该参数用于设置网元相关信令的本地存盘上报开关。 数据来源：本端规划 取值范围：位域说明: SESS_CRT_FAIL：Create Session失败单据。 SESS_DEL_FAIL：Delete Session失败单据。 SESS_MOD_FAIL：Modify Session失败单据。 SESS_RPT_FAIL：Session report失败单据。 ASSOC_CRT_FAIL：偶联建立失败单据。 ASSOC_DEL_FAIL：偶联删除失败单据。 ASSOC_MOD_FAIL：偶联更新失败单据。 ASSOC_RPT_FAIL：耦联报告失败单据。 SIP_CALL_FAIL：SIP呼叫失败单据。 SIP_CALL_SUCC：SIP呼叫成功单据。 RTP_CALL_VOICE_STAT：语音用户RTP音频统计单据。 RTP_CALL_VIDEO_STAT：语音用户RTP视频统计单据。 TRUNK_SESS_CRT_FAIL：宽带集群建立失败单据。 TRUNK_BEAR_CRT_FAIL：宽带集群承载建立失败单据。 TRUNK_ENB_ACT_FAIL：宽带集群承载eNodeB激活失败单据。 TRUNK_SESS_DEL_FAIL：宽带集群删除失败单据。 TRUNK_BEAR_DEL_FAIL：宽带集群承载删除失败单据。 TRUNK_ENB_DEL_FAIL：宽带集群承载eNodeB删除失败单据。 TRUNK_ENB_ACK_FAIL：宽带集群承载eNodeB删除通知失败单据。 SERVER_RTT_STATISTIC：时延统计单据。 SESS_CRT_FAIL：标识Create Session单据。SESS_DEL_FAIL：标识Delete Session单据。SESS_MOD_FAIL：标识Modify Session单据。SESS_RPT_FAIL：标识Session report单据。ASSOC_CRT_FAIL：标识Association Create单据。ASSOC_DEL_FAIL：标识Association Delete单据。ASSOC_MOD_FAIL：标识Association Modify单据。ASSOC_RPT_FAIL：标识Association Report单据。SIP_CALL_FAIL：标识SIP CALL失败单据。SIP_CALL_SUCC：标识SIP CALL成功单据。RTP_CALL_VOICE_STAT：标识语音用户RTP音频统计单据。RTP_CALL_VIDEO_STAT：标识语音用户RTP视频统计单据。TRUNK_SESS_CRT_FAIL：标识宽带集群建立失败单据。TRUNK_BEAR_CRT_FAIL：标识宽带集群承载建立失败单据。TRUNK_ENB_ACT_FAIL：标识宽带集群承载eNodeB激活失败单据。TRUNK_SESS_DEL_FAIL：标识宽带集群删除失败单据。TRUNK_BEAR_DEL_FAIL：标识宽带集群承载删除失败单据。TRUNK_ENB_DEL_FAIL：标识宽带集群承载eNB删除失败单据。TRUNK_ENB_NOTI_FAIL：标识宽带集群承载eNB删除通知失败单据。SERVER_RTT_STATISTIC：时延统计单据。 默认值：无 配置原则：无 |

#### 使用实例

如果要将偶联建立失败和偶联删除失败CHR单据保存在本地，设置本地存盘开关ASSOC\_CRT\_FAIL-1&ASSOC\_DEL\_FAIL-1：

```
SET CHRRECORDSW: MSGTYPE=ASSOC_CRT_FAIL-1&ASSOC_DEL_FAIL-1&ASSOC_MOD_FAIL-0&ASSOC_RPT_FAIL-0&SESS_CRT_FAIL-0&SESS_DEL_FAIL-0&SESS_MOD_FAIL-0&SESS_RPT_FAIL-0&SIP_CALL_FAIL-0&SIP_CALL_SUCC-0&RTP_CALL_VOICE_STAT-0&RTP_CALL_VIDEO_STAT-0&TRUNK_BEAR_CRT_FAIL-0&TRUNK_BEAR_DEL_FAIL-0&TRUNK_ENB_ACT_FAIL-0&TRUNK_ENB_DEL_FAIL-0&TRUNK_ENB_NOTI_FAIL-0&TRUNK_SESS_CRT_FAIL-0&TRUNK_SESS_DEL_FAIL-0;
```