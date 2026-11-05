# 查询5GC会话管理定时器参数（LST SMTIMER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询5GC会话管理定时器时长和消息重发次数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询5GC会话管理定时器时长和消息重发次数，执行如下命令：

```
%%LST SMTIMER:;%%
RETCODE = 0 操作成功

结果如下
------------------------
	  LADN超时释放时间(秒)  =  60
                     T3591(秒)  =  10
                     N3591(次)  =  3
                     T3593(秒)  =  30
                     T3592(秒)  =  10
                     N3592(次)  =  3
     等待UDM响应定时器时长(秒)  =  10
     等待AMF响应定时器时长(秒)  =  10
   等待I-SMF响应定时器时长(秒)  =  10
   等待H-SMF响应定时器时长(秒)  =  10
EPS Fallback保护定时器时长(秒)  =  5
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                   | 输出项解释                                                                                                                                                                                      |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LADN超时释放时间(秒)           | 该参数用于指定本地数据网络会话超时释放时间，超时后释放会话。                                                                                                                                                             |
| T3591(秒)                | 参数用于指定定时器T3591的时长。SMF发起PDU SESSION MODIFICATION COMMAND消息，如果UE未在T3591定时器时长范围内响应，则SMF重发PDU SESSION MODIFICATION COMMAND消息。                                                                  |
| N3591(次)                | 该参数用于指定SMF重发PDU SESSION MODIFICATION COMMAND消息的次数。当SMF发送PDU SESSION MODIFICATION COMMAND消息后，在T3591定时器时长范围内没有收到UE的响应消息时，SMF会重发PDU SESSION MODIFICATION COMMAND消息，超过N3591不重发。                |
| T3593(秒)                | 该参数用于指定定时器T3593的时长，此定时器控制IPv4 mode3释放旧侧会话的等待时长。超时后，SMF释放对应会话。                                                                                                                              |
| T3592(秒)                | 该参数用于指定定时器T3592的时长。SMF发起PDU SESSION RELEASE COMMAND消息，如果UE未在T3592定时器时长范围内响应，则SMF重发PDU SESSION RELEASE COMMAND消息。                                                                           |
| N3592(次)                | 该参数用于指定SMF重发PDU SESSION RELEASE COMMAND消息的次数。SMF发送PDU SESSION RELEASE COMMAND消息后，在T3592定时器时长范围内没有收到UE的响应消息时，SMF重发PDU SESSION RELEASE COMMAND消息，超过N3592不重发。                                 |
| 等待UDM响应定时器时长(秒)         | 该参数用于指定等待UDM响应的定时器时长。                                                                                                                                                                      |
| 等待AMF响应定时器时长(秒)         | 该参数用于指定等待AMF响应定时器时长。以下场景除外： 寻呼流程中，SMF收到了AMF的Namf_Communication_N1N2MessageTransfer response后，等待AMF的Nsmf_PDUSession_UpdateSMContext request消息时长不受本参数控制，而是通过SET SMCOMMTIMER命令的TPAGING参数进行控制。 |
| 等待I-SMF响应定时器时长(秒)       | 该参数用于指定等待I-SMF响应定时器时长。                                                                                                                                                                     |
| 等待H-SMF响应定时器时长(秒)       | 该参数用于指定等待H-SMF响应定时器时长。                                                                                                                                                                     |
| EPS Fallback保护定时器时长(秒)  | 该参数用于设置EPS Fallback保护定时器时长。5G语音QoS Flow创建触发EPS Fallback流程后启动该定时器，如果定时器超时后，Handover或TAU流程还未启动或还未完成，则SMF指示PCF，语音承载创建失败。                                                                      |
| N11接口等待会话创建响应消息定时器时长（秒） | 该参数用于指定N11接口等待会话创建响应消息定时器时长。                                                                                                                                                               |
| N16接口等待会话创建响应消息定时器时长（秒） | 该参数用于指定N16接口等待会话创建响应消息定时器时长。                                                                                                                                                               |