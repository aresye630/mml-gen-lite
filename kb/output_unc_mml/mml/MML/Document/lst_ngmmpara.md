# 查询5G MM协议参数（LST NGMMPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查看5G模式性移动性管理参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询5G MM参数，执行如下命令：

```
%%LST NGMMPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                          T3522(s)  =  6
                      N3522(times)  =  4
                          T3550(s)  =  6
                      N3550(times)  =  4
                          T3560(s)  =  6
                      N3560(times)  =  4
                          T3570(s)  =  6
                      N3570(times)  =  4
                        T3512(min)  =  54
                        T3502(min)  =  12
                          T3513(s)  =  6
                      N3513(times)  =  2
                          T3555(s)  =  6
                      N3555(times)  =  4
               重寻呼间隔递增值(s)  =  0
            高优先级业务的T3513(s)  =  2
        高优先级业务的N3513(times)  =  4
 高优先级业务的重寻呼间隔递增值(s)  =  0
               移动可达定时器(min)  =  58
   不可达用户隐式去注册定时器(min)  =  60
                        GUTI重分配  =  初始注册&移动性注册
               GUTI重分配定时器(h)  =  0
             Handover准备定时器(s)  =  10
         源侧Handover完成定时器(s)  =  10
       目标侧Handover完成定时器(s)  =  10
                       T3定时器(s)  =  10
         测试用GUTI重分配定时器(m)  =  0
         切换流程资源释放定时器(s)  =  2
             GUTI重分配最大间隔(h)  =  0
   用户去注册后签约数据保留时间(h)  =  24
等待gNodeB上下文释放完成定时器 (s)  =  4
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                  | 输出项解释                                                                                                                                                                                                                                               |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T3522(s)               | 该定时器用于控制AMF发起去注册流程后等待UE响应的时长。该定时器在AMF发送Deregistration Request消息时启动，在收到Deregistration Accept消息时停止；超时后AMF会重发Deregistration Request消息。                                                                                                                 |
| N3522(times)           | 该参数用于指定当AMF发起去注册流程后没有收到UE的响应消息时，重发Deregistration Request消息的次数。                                                                                                                                                                                      |
| T3550(s)               | 该定时器用于控制AMF发起初始注册或移动性注册更新后等待UE响应的时长。该定时器在AMF发送Registration Accept启动，在收到Registration Complete时停止；超时后AMF将重发Registration Accept消息。                                                                                                                     |
| N3550(times)           | 该参数用于指定在用户初始注册或移动性注册更新流程中没有收到UE的响应消息，AMF重复发送Registration Accept消息的次数。                                                                                                                                                                               |
| T3560(s)               | 该定时器用于控制AMF发起鉴权或密钥协商流程后等待UE响应的时长。该定时器在AMF发送Authentication Request或Security Mode Command消息时启动，在收到Authentication Response或Security Mode Complete消息时停止；超时后，AMF将重发Authentication Request或Security Mode Command消息。                                       |
| N3560(times)           | 该参数用于指定在AMF发起鉴权或密钥协商流程后没有收到UE的响应消息时，重发Authentication Request或Security Mode Command消息的次数。                                                                                                                                                            |
| T3570(s)               | 该定时器用于控制AMF发起身份识别流程后等待UE响应的时长。该定时器在AMF发送Identity Request消息时启动，在收到Identity Response消息时停止；超时后，AMF将重发Identity Request消息。                                                                                                                               |
| N3570(times)           | 该参数用于指定当AMF发起身份识别流程后没有收到UE的响应消息时，重发Identity Request消息的次数。                                                                                                                                                                                           |
| T3512(min)             | 该定时器用于控制UE自动发起周期性注册更新流程的时间间隔。当UE状态从CM-CONNECTED变为CM-IDLE时启动该定时器；超时后，UE发起周期性注册更新流程。当系统存在ADD NGPRDREGTIMEDNN配置记录时，该命令中的T3512优先级高于本命令的T3512。 若用户签约数据中subsRegTimer取值不为0且小于移动可达定时器（RCHTMR）时，则使用subsRegTimer信元取值，否则使用该参数配置值。                              |
| T3502(min)             | 该定时器用于注册失败场景下，控制UE重新发起注册请求的时间间隔，注册类型包括初始注册、移动性注册更新和周期性注册更新。                                                                                                                                                                                         |
| T3513(s)               | 该定时器用于控制AMF发起寻呼流程后等待UE响应的时长。该定时器在AMF发送Paging Request消息时启动，在收到Service Request或Registration Request消息时停止；超时后，AMF重发Paging Request消息。                                                                                                                   |
| N3513(times)           | 该参数用于指定AMF发起寻呼流程后没有收到UE的响应消息，重发Paging Request消息的次数。                                                                                                                                                                                                 |
| T3555(s)               | 该定时器用于控制AMF发起配置更新流程后等待UE响应的时长。该定时器在AMF发送Configuration Update Command启动，在收到Configuration Update Complete时停止；超时后AMF将重发Configuration Update Command消息。                                                                                                 |
| N3555(times)           | 该参数用于指定在用户配置更新流程中没有收到UE的响应消息，AMF重复发送Configuration Update Command消息的次数。                                                                                                                                                                              |
| 重寻呼间隔递增值(s)            | 该参数用于指定AMF发起寻呼流程后没有收到UE响应消息，重发Paging Request消息的间隔递增时间值。                                                                                                                                                                                             |
| 高优先级业务的T3513(s)        | 该定时器用于控制AMF发起高优先级业务（VoLTE紧急呼叫、VoLTE普通语音业务）的寻呼流程后等待UE响应的时长。该定时器在AMF发送Paging Request消息时启动，在收到Service Request或Registration Request消息时停止；超时后，AMF重发Paging Request消息。                                                                                     |
| 高优先级业务的N3513(times)    | 该参数用于指定当AMF发起高优先级业务（VoLTE紧急呼叫、VoLTE普通语音业务）的寻呼流程后没有收到UE的响应消息，重发Paging Request消息的次数。                                                                                                                                                                  |
| 高优先级业务的重寻呼间隔递增值(s)     | 该参数用于指定AMF发起高优先级业务（VoLTE紧急呼叫、VoLTE普通语音业务）的寻呼流程后没有收到UE响应消息，重发Paging Request消息的间隔递增时间值。                                                                                                                                                               |
| 移动可达定时器(min)           | 该定时器用于监测UE是否发起周期性注册更新流程。该定时器在UE的NAS信令连接释放时启动，在NAS信令连接建立时停止；超时后，如果UE还没有发起周期性注册更新流程，则启动不可达用户隐式去注册定时器（IMDTCHTMR）。当系统存在ADD NGPRDREGTIMEDNN配置记录时，该命令中的RCHTMR优先级高于本命令的RCHTMR。                                                                             |
| 不可达用户隐式去注册定时器(min)     | 该定时器用于指定移动可达定时器超时后，AMF保持UE信息的时长。移动可达定时器超时后，可认为用户脱离了网络覆盖范围，但无法明确脱离时间，所以AMF不能立即隐式去注册用户，只启动不可达用户隐式去注册定时器。该定时器启动期间，AMF拒绝网络侧对UE的寻呼。如果在不可达用户隐式去注册定时器超时时UE仍未接入网络，那么AMF隐式去注册该UE。                                                                            |
| GUTI重分配                | 该参数用来指定在注册和网络侧触发的服务请求流程时，是否重分配5G-GUTI。                                                                                                                                                                                                              |
| GUTI重分配定时器(h)          | 该定时器用于控制5G-GUTI重分配时长。当UE进入CM-CONNECT态时启动定时器，如果用户一直处于CM-CONNECT态并且持续时间超过本参数指定时长，那么AMF将执行5G-GUTI重分配流程；如果UE切换到CM-IDLE态，则停止该定时器，等用户下次进入CM-CONNECT态再重新启动该定时器。                                                                                            |
| Handover准备定时器(s)       | 该定时器用于控制在Handover准备阶段，AMF在向目标NG-RAN发送Handover Request消息后等待Handover Request Ack消息的时长。该定时器在向目标NG-RAN发送Handover Request消息后启动，在收到目标NG-RAN的Handover Request Ack消息后停止；超时后，AMF向源NG-RAN发送Handover Preparation Failure消息。                                    |
| 源侧Handover完成定时器(s)     | 该定时器用于控制Handover流程中，在以下场景会触发HOCMPSRCTMR定时器： 源AMF向源NG-RAN发送Handover Command时启动，在收到目标AMF调用Namf_Communication_N2InfoNotify服务操作后停止； AMF向NG-RAN发送Handover Command时启动，在收到MME的Relocation Complete Notification消息后停止； 超时后，AMF将释放UE信息。                       |
| 目标侧Handover完成定时器(s)    | 该定时器用于控制目标AMF切换完成的时间。该定时器在目标AMF调用源AMF的Namf_Communication_CreateUEContext Response服务操作后启动，在收到目标NG-RAN的Handover Notify消息后停止；超时后，目标AMF将释放用户信息。                                                                                                         |
| T3定时器(s)               | 该参数用于指定T3定时器时长。在以下场景中会触发T3定时器： UE从5GS到EPS的互操作流程中，老侧AMF向新侧MME发送上下文响应（Context Response）消息时； Inter AMF注册流程中，老侧AMF向新侧AMF发送RegistrationStatusUpdateResponse消息时； 当T3定时器超时时，将删除相应的老侧数据及承载资源。                                                               |
| 测试用GUTI重分配定时器(m)       | 该参数描述的是内部测试用的5G-GUTI重新分配的定时器参数对应值。                                                                                                                                                                                                                  |
| 切换流程资源释放定时器(s)         | 此参数用于指定HOT3定时器时长。在以下场景中会触发HOT3定时器： Inter HO中源侧AMF收到Namf_Communication_CreateUEContext Response服务调用时； Inter HO中目标侧AMF收到Namf_Communication_N2InfoNotify ACK服务调用，并且之前已在新侧UPF创建间接承载时； Intra HO中AMF收到Handover Notify消息时； 当HOT3定时器超时时，AMF将删除相应的源侧数据及承载资源。 |
| GUTI重分配最大间隔(h)         | 该参数用于指定5G-GUTI重分配最大间隔。                                                                                                                                                                                                                              |
| 用户去注册后签约数据保留时间(h)      | 该参数用于指定UE去注册后其签约数据在AMF上的保存时长。该定时器在UE去注册后启动，在UE注册后停止；超时后，AMF将删除UE的签约数据。                                                                                                                                                                              |
| 等待gNodeB上下文释放完成定时器 (s) | 此参数用于指定AMF发起UE上下文释放后等待gNodeB完成的定时器时长。该定时器在AMF发送UE Context Release Command消息时启动，在收到UE Context Release Complete消息时停止；超时后，AMF将用户设置为CM-IDLE态。 在由NG-RAN触发的AN Release流程和由MML命令（RMV USRN2CONN）触发的AN Release流程中，该参数不生效，保持系统默认时长。                            |