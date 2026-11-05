# 查询会话管理接口IP传输类型（LST SMIPTRANSTYPE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询会话管理接口IP传输类型。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询会话管理接口IP传输类型：

```
%%LST SMIPTRANSTYPE:;%%
RETCODE = 0  操作成功

结果如下
--------
       SGW S11控制面接口IP类型  =  根据对端能力选择IP类型
        SGW S1用户面接口IP类型  =  IPv4优先
        SGW S5控制面接口IP类型  =  IPv6优先
        SGW S5用户面接口IP类型  =  IPv4优先
        SGW S8控制面接口IP类型  =  IPv4优先
        SGW S8用户面接口IP类型  =  IPv4优先
        PGW S5控制面接口IP类型  =  根据对端能力选择IP类型
        PGW S5用户面接口IP类型  =  根据对端能力选择IP类型
        PGW S8控制面接口IP类型  =  IPv4优先
        PGW S8用户面接口IP类型  =  IPv4优先
              UPF N3接口IP类型  =  使用双栈
            I-UPF N9接口IP类型  =  使用双栈
I-UPF home routed N9接口IP类型  =  IPv4优先
           H-UPF N9A接口IP类型  =  IPv4优先
           V-UPF N9C接口IP类型  =  IPv4优先
             UPF N9A接口IP类型  =  IPv4优先
           I-UPF N9C接口IP类型  =  IPv4优先
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SGW S11控制面接口IP类型           | 该参数用于指定SGW S11控制面接口IP类型。 对端IP是MME S11控制面地址，当SGW收到MME的Create Session Request消息，消息中携带Sender F-TEID for Control Plane信元指示MME S11控制面地址，SGW向MME返回Create Session Response消息时通过Sender F-TEID for Control Plane信元指定SGW S11控制面接口IP类型。                                                                                                                                                                                                                                                                                                                                                         |
| SGW S1用户面接口IP类型            | 该参数用于指定SGW S1用户面接口（或SGW S11用户面接口）IP类型。 对端IP是eNodeB S1用户面地址，当SGW收到MME的Create Session Request/Modify Bearer Request消息，消息中携带S1-U eNodeB F-TEID信元指示eNodeB S1用户面地址，SGW向MME返回Create Session Response/Modify Bearer Response消息时通过S1-U SGW F-TEID信元指定SGW S1用户面接口IP类型（或通过S11-U SGW F-TEID信元指定SGW S11用户面接口IP类型）。 当SGW向eNodeB发送Create Bearer Request消息通过S1-U SGW F-TEID信元指定SGW S1用户面接口IP类型。 当SGW向MME返回Create Indirect Data Forwarding Tunnel Response消息通过S1-U SGW F-TEID for DL data forwarding/S1-U SGW F-TEID for UL data forwarding信元指定SGW S1用户面接口IP类型。                                      |
| SGW S5控制面接口IP类型            | 该参数用于指定SGW S5控制面接口IP类型。 对端IP是PGW S5控制面地址，当SGW收到MME的Create Session Request消息，消息中携带PGW S5/S8 Address for Control Plane or PMIP信元指示PGW S5控制面地址。SGW向PGW发送Create Session Request消息通过Sender F-TEID for Control Plane信元指定SGW S5控制面接口IP类型。 当SGW改变，SGW向PGW发送Modify Bearer Request消息通过Sender F-TEID for Control Plane信元指定SGW S5控制面接口IP类型。                                                                                                                                                                                                                                                      |
| SGW S5用户面接口IP类型            | 该参数用于指定SGW S5用户面接口IP类型。 对端IP是PGW S5用户面地址，当SGW向PGW发送Create Session Request/Modify Bearer Request/Create Bearer Request消息通过S5/S8-U SGW F-TEID信元指定SGW S5用户面接口IP类型。 当SGW向MME发送Create Indirect Data Forwarding Tunnel Response消息通过SGW F-TEID for DL data forwarding/SGW F-TEID for UL data forwarding信元指定SGW S5用户面接口IP类型。                                                                                                                                                                                                                                                                 |
| SGW S8控制面接口IP类型            | 该参数用于指定SGW S8控制面接口IP类型。 对端IP是PGW S8控制面地址，当SGW收到MME的Create Session Request消息，消息中携带PGW S5/S8 Address for Control Plane or PMIP信元指示PGW S8控制面地址，SGW向PGW发送Create Session Request消息通过Sender F-TEID for Control Plane信元指定SGW S8控制面接口IP类型。 当SGW改变，SGW向PGW发送Modify Bearer Request消息通过Sender F-TEID for Control Plane信元指定SGW S8控制面接口IP类型。                                                                                                                                                                                                                                                      |
| SGW S8用户面接口IP类型            | 该参数用于指定SGW S8用户面接口IP类型。 对端IP是PGW S8用户面地址，当SGW向PGW发送Create Session Request/Modify Bearer Request/Create Bearer Request消息通过S5/S8-U SGW F-TEID信元指定SGW S8用户面接口IP类型。 当SGW向MME发送Create Indirect Data Forwarding Tunnel Response消息通过SGW F-TEID for DL data forwarding/SGW F-TEID for UL data forwarding信元指定SGW S8用户面接口IP类型。                                                                                                                                                                                                                                                                 |
| PGW S5控制面接口IP类型            | 该参数用于指定PGW S5控制面接口（或GGSN Gn控制面接口）IP类型。对于GGSN，只有控制面和用户面的决策结果都为双栈时，最终响应消息中控制面和用户面携带双栈地址；否则控制面和用户面均携带单栈地址。 对端IP是SGW S5控制面地址（或SGSN Gn控制面地址），当PGW收到SGW的Create Session Request消息，消息中携带Sender F-TEID for Control Plane信元指示SGW S5控制面地址，PGW向SGW发送Create Session Response消息通过Sender F-TEID for Control Plane信元指定PGW S5控制面接口IP类型。 当GGSN收到SGSN的Create PDP Context Request消息后，GGSN向SGSN发送Create PDP Context Response消息通过GGSN Address for Control Plane和Alternative GGSN Address for Control Plane信元指定GGSN Gn控制面接口IP类型。                                                                            |
| PGW S5用户面接口IP类型            | 该参数用于指定PGW S5用户面接口（或GGSN Gn用户面接口、锚点UPF的非漫游或Local Breakout的N9接口）IP类型。对于GGSN，只有控制面和用户面的决策结果都为双栈时，最终响应消息中控制面和用户面携带双栈地址；否则控制面和用户面均携带单栈地址。 对端IP是SGW S5用户面地址（或SGSN Gn用户面接口），当PGW收到SGW的Create Session Request消息，消息中携带S5/S8-U SGW F-TEID信元指示SGW S5用户面地址，PGW向SGW发送Create Session Response消息通过S5/S8-U PGW F-TEID信元指定PGW S5用户面接口IP类型。 当PGW向SGW发送Create Bearer Request消息通过S5/8-U PGW F-TEID信元指定PGW S5用户面接口IP类型。 当GGSN收到SGSN的Create PDP Context Request消息后，GGSN向SGSN发送Create PDP Context Response消息通过GGSN Address for user traffic和Alternative GGSN Address for user traffic信元指定GGSN Gn用户面接口IP类型。 |
| PGW S8控制面接口IP类型            | 该参数用于指定PGW S8控制面接口（或GGSN Gp控制面接口）IP类型。对于GGSN，只有控制面和用户面的决策结果都为双栈时，最终响应消息中控制面和用户面携带双栈地址；否则控制面和用户面均携带单栈地址。 对端IP是SGW S8控制面地址（或SGSN Gp控制面地址），当PGW收到SGW的Create Session Request消息，消息中携带Sender F-TEID for Control Plane信元指示SGW S8控制面地址，PGW向SGW发送Create Session Response消息通过Sender F-TEID for Control Plane信元指定PGW S8控制面接口IP类型。 当GGSN收到SGSN的Create PDP Context Request消息后，GGSN向SGSN发送Create PDP Context Response消息通过GGSN Address for Control Plane和Alternative GGSN Address for Control Plane信元指定GGSN Gp控制面接口IP类型。                                                                            |
| PGW S8用户面接口IP类型            | 该参数用于指定PGW S8用户面接口（或GGSN Gp用户面接口、锚点UPF在home routed形态的N9接口）IP类型。对于GGSN，只有控制面和用户面的决策结果都为双栈时，最终响应消息中控制面和用户面携带双栈地址；否则控制面和用户面均携带单栈地址。 对端IP是SGW S8用户面地址（或SGSN Gp用户面接口），当PGW收到SGW的Create Session Request消息，消息中携带S5/S8-U SGW F-TEID信元指示SGW S8用户面地址，PGW向SGW发送Create Session Response消息通过S5/S8-U PGW F-TEID信元指定PGW S8用户面接口IP类型。 PGW向SGW发送Create Bearer Request消息通过S5/8-U PGW F-TEID信元指定PGW S8用户面接口IP类型。 当GGSN收到SGSN的Create PDP Context Request消息后，GGSN向SGSN发送Create PDP Context Response消息通过GGSN Address for user traffic和Alternative GGSN Address for user traffic信元指定GGSN Gp用户面接口IP类型。       |
| UPF N3接口IP类型               | 该参数用于指定UPF或I-UPF的N3接口IP类型。 对端IP是指gNodeB N3用户面地址，SMF通过Namf_Communication_N1N2MessageTransfer Request / Nsmf_PDUSession_UpdateSMContext Response消息中携带的N2 SM Information中的CN Tunnel Info指示UPF N3用户面地址， AMF会通过Nsmf_PDUSession_UpdateSMContext Request消息中携带的N2 SM Information中的AN Tunnel Info指示gNodeB N3用户面地址。                                                                                                                                                                                                                                                                            |
| I-UPF N9接口IP类型             | 该参数用于指定I-UPF在非漫游或Local breakout形态下N9接口IP类型。 对端IP是指锚点UPF N9用户面地址，SMF通过N4 Session Establishment Request消息中携带锚点UPF N9用户面地址，并在N4 PFCP Session Modification Request消息中携带I-UPF N9用户面地址。                                                                                                                                                                                                                                                                                                                                                                                                    |
| I-UPF home routed N9接口IP类型 | 该参数用于指定I-UPF在home routed形态下N9接口IP类型。 对端IP是指归属地UPF N9用户面地址，拜访地SMF通过Nsmf_PDUSession_Create Request消息携带拜访地UPF N9用户面给归属地SMF；归属地SMF通过Nsmf_PDUSession_Create Response消息携带归属地UPF N9用户面地址给拜访地SMF，并通过N4 PFCP Session Modification Request消息携带给拜访地UPF。                                                                                                                                                                                                                                                                                                                                         |
| H-UPF N9A接口IP类型            | 该参数用于指定归属地UPF的N9a接口IP类型。 对端IP是指拜访地UPF或Proxy UPF N9c用户面地址，拜访地SMF通过Nsmf_PDUSession_Create Request消息携带拜访地UPF或Proxy UPF N9c用户面地址给归属地SMF，并通过N4 PFCP Session Modification Request消息携带给归属地UPF。                                                                                                                                                                                                                                                                                                                                                                                              |
| V-UPF N9C接口IP类型            | 该参数用于指定拜访地UPF的N9c接口IP类型。 对端IP是指归属地UPF或Proxy UPF N9a用户面地址，归属地SMF通过Nsmf_PDUSession_Create Response消息携带归属地UPF或Proxy UPF N9a用户面地址给拜访地SMF，并通过N4 PFCP Session Modification Request消息携带给拜访地UPF。                                                                                                                                                                                                                                                                                                                                                                                             |
| UPF N9A接口IP类型              | 该参数用于指定UPF在非漫游形态下N9a接口IP类型。 对端IP是指I-UPF N9c用户面地址，SMF通过N4 PFCP Session Modification Request消息携带I-UPF N9c用户面地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| I-UPF N9C接口IP类型            | 该参数用于指定I-UPF在非漫游形态下N9c接口IP类型。 对端IP是指锚点UPF N9用户面地址，SMF通过N4 Session Establishment Request消息中携带锚点UPF N9用户面地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |