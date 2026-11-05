# 查询GTP-C功能参数（LST GTPCFUNCPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C功能参数。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令（除FILTERFAULTSW）无效，请使用命令LST GTPPUB配置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询GTP-C功能参数：LST GTPCFUNCPARA:;

```
%%LST GTPCFUNCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                    V1 Echo请求发送开关  =  打开
                V1 Echo请求发送间隔(秒)  =  60
                    V2 Echo请求发送开关  =  打开
                V2 Echo请求发送间隔(秒)  =  60
                 Echo消息的重发间隔(秒)  =  3
                     Echo消息的发送次数  =  5
                           NTSR功能开关  =  关闭
                            PRN功能开关  =  关闭
                          CIOT功能开关  =  关闭
                       路径断去激活开关  =  打开
             路径断后发送心跳消息的次数  =  30
                   本端recovery更新开关  =  打开
                   对端Recovery处理开关  =  关闭
                         本端端口号模式  =  非知名端口号模式
                      UDP校验和检查开关  =  打开
             过滤故障状态的GTPC路径开关  =  打开
Bearer Resource Command使用知名源端口号  =  关闭
  Modify Bearer Command使用知名源端口号  =  关闭
  Delete Bearer Command使用知名源端口号  =  关闭
                      路径数过载门限(%)  =  85
                  路径数过载恢复门限(%)  =  80
                       发送私有信息开关  =  关闭
                       私有信息扩展域ID  =  2011
                               私有信息  =  UNC
              检查GTP扩展头类型个数上限  =  10
              检查GTP扩展头列表个数上限  =  100
              检查GTP扩展头类型长度上限  =  100
                      要求MME携带NTSR标识 = 开启
                         Recovery信元校验开关 = 关闭
               激活应答消息携带NSAPI标识 = 关闭
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                           | 输出项解释                                                                                                                                                                                                                             |
|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V1 Echo请求发送开关                   | 该参数用于指定V1版本的GTP-C路径是否发送Echo请求消息，探测对端通信状态。                                                                                                                                                                                         |
| V1 Echo请求发送间隔                   | 该参数用于指定V1版本的GTP-C路径发送Echo请求消息的时间间隔。                                                                                                                                                                                               |
| V2 Echo请求发送开关                   | 该参数用于指定V2版本路径是否发送Echo请求消息，探测对端通信状态。                                                                                                                                                                                               |
| V2 Echo请求发送间隔                   | 该参数用于指定V2版本的GTP-C路径发送Echo请求消息的时间间隔。                                                                                                                                                                                               |
| Echo消息的重发间隔                     | 该参数用于等待一条Echo响应消息的最大时长，超出时长后重发本Echo请求消息。                                                                                                                                                                                          |
| Echo消息的发送次数                     | 该参数用于指定发送Echo请求消息的最大尝试次数。                                                                                                                                                                                                         |
| NTSR功能开关                        | 该参数用于指定是否支持NTSR（Network Triggered Service Restoration）功能。                                                                                                                                                                         |
| PRN功能开关                         | 该参数用于指定是否支持PRN（PGW Restart Notification）功能。                                                                                                                                                                                       |
| CIOT功能开关                        | 该参数用于指定是否支持CIOT（Cellular Internet Of Things）功能。                                                                                                                                                                                   |
| 路径断去激活开关                        | 该参数用于控制当GTP-C路径故障时是否去激活用户上下文。                                                                                                                                                                                                     |
| 路径断后发送心跳消息的探测周期次数               | 该参数用于控制当GTP-C路径故障后再持续故障多少次探测周期之后才去激活用户上下文。探测周期由SET GTPCFUNCPARA命令的V1EI或者V2EI参数控制。                                                                                                                                                 |
| 本端recovery更新开关                  | 该参数用于控制GTP-C信令消息中是否携带Recovery信元。                                                                                                                                                                                                  |
| 对端Recovery处理开关                  | 该参数用于控制对端Recovery值变化时，是否去激活用户。                                                                                                                                                                                                    |
| 对端Recovery值来源                   | 该参数用于指定对端recovery功能所使用的recovery值来源。                                                                                                                                                                                               |
| 本端端口号模式                         | 该参数用于指定本端端口号分配模式。                                                                                                                                                                                                                 |
| UDP校验和检查开关                      | 开关打开时，支持UDP校验功能，此时发送GTP-C报文需要填写UDP校验和，接收GTP-C报文需要检查UDP校验和，并且校验失败的报文将被丢弃。开关关闭时，不支持UDP校验功能，此时发送GTP-C报文不需要填写UDP校验和，接收GTP-C报文需要检查UDP校验和，并且校验失败的报文将会继续接收，不会被丢弃。                                                                        |
| 过滤故障状态的GTPC路径开关                 | 该参数用于针对DNS解析的IP地址列表，是否根据GTPC路径状态过滤故障状态的对端地址。                                                                                                                                                                                      |
| Bearer Resource Command使用知名源端口号 | 该参数用于控制SGW-C将收到的Bearer Resource Command消息透传给PGW-C时，消息中的源端口号是否为知名端口号。                                                                                                                                                              |
| Modify Bearer Command使用知名源端口号   | 该参数用于控制SGW-C将收到的Modify Bearer Command消息透传给PGW-C时，消息中的源端口号是否为知名端口号。                                                                                                                                                                |
| Delete Bearer Command使用知名源端口号   | 该参数用于控制SGW-C将收到的Delete Bearer Command消息透传给PGW-C时，消息中的源端口号是否为知名端口号。                                                                                                                                                                |
| 路径数过载门限(%)                      | 该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）过载门限，如果当前路径占用比达到或超过此门限值触发告警。                                                                                                                                                                       |
| 路径数过载恢复门限(%)                    | 该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）过载恢复门限，如果在50秒之内当前路径占用比都小于此门限值则恢复告警。                                                                                                                                                                |
| 发送私有信息开关                        | 该参数指示是否发送私有信息，私有信息包含了运营商或设备商定义的信息。                                                                                                                                                                                                |
| 私有信息扩展域ID                       | 该参数指定发送的私有信息的扩展域ID。                                                                                                                                                                                                               |
| 私有信息                            | 该参数指定发送的私有信息。                                                                                                                                                                                                                     |
| 检查GTP扩展头类型个数上限                  | 该参数定义了检查控制面GTP-C扩展头类型个数上限。                                                                                                                                                                                                        |
| 检查GTP扩展头列表个数上限                  | 该参数定义检查用户面GTP-C支持扩展头列表通知长度上限。                                                                                                                                                                                                     |
| 检查GTP扩展头类型长度上限                  | 该参数定义了检查控制面GTP-C扩展头类型长度上限，单位：4字节。                                                                                                                                                                                                 |
| 上下文核查开关                         | 该参数用于控制GTP-C路径从故障到恢复时是否触发上下文核查。                                                                                                                                                                                                   |
| SGW向PGW发送核查消息开关                 | 该参数用于控制GTP-C路径从故障到恢复时是否触发向PGW发送Change Notification Request消息来核查对端上下文是否存在。                                                                                                                                                         |
| 上下文核查消息速率(个/秒)                  | 该参数用于控制向对端发送核查消息的速率。                                                                                                                                                                                                              |
| GGSN/PGW-C Proxy路径Echo请求发送开关    | 该参数用于设置GGSN/PGW-C Proxy路径Echo请求发送开关。                                                                                                                                                                                              |
| 校验Recovery信元开关                  | 该参数用于控制是否校验Echo Request消息中Recovery信元开关。当开关打开时，校验Echo Request消息中Recovery信元，当Echo Request正确携带Recovery信元时，正常响应Echo Response，当Echo Request不携带或携带错误Recovery信元时，不响应Echo Response。当开关关闭时，不校验Echo Request消息中Recovery信元，正常响应Echo Response。 |
| 要求MME携带NTSR标识                   | 该参数用于控制是否要求MME携带NTSR标识。当开关打开时，业务严格按照对端是否携带NTSR Flag判断对端是否支持NTSR功能。当开关关闭时，默认认为对端支持NTSR功能。                                                                                                                                          |
| 是否携带NSAPI字段                     | 该参数用于指定激活应答消息中是否携带NSAPI字段。                                                                                                                                                                                                        |