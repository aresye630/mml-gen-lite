# 增加服务发现网元实例信息(ADD UDMDISCNFPROF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于增加一个静态服务发现网元实例信息。

UDM根据该命令配置网元静态实例信息，当UDM需要服务发现时可根据配置直接从本地服务发现网元信息。

## 注意事项

- 系统中增加服务发现网元实例信息的最大记录数不能超过最大1024条。
- 执行本命令新增SCP/SEPP链路时，如果**DSP UDMHTTPLNK**命令在客户端模式下查询的结果中已经存在相同对端IP地址和对端端口号且对端网元类型为非SCP/SEPP的链路，先确认对端是否存在IP冲突，如果存在，需要先解决IP冲突问题，再执行**RMV HTTPLINK**命令删除该非SCP/SEPP链路。删除链路后执行本命令新增SCP/SEPP链路，操作完成后新建链路1分钟左右生效。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSNAME    | 网元实例名称 | 可选必选说明：必选参数 参数含义：用于标识一个服务发现网元实例的名称。 取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无。 配置原则：该参数全局唯一，不能重复。                                                                                                                                                                                                                                                                                                                                                           |
| NFINSID      | 网元实例标识 | 可选必选说明：必选参数 参数含义：用于标识服务发现网元实例在系统中的序号。 取值范围：有效的UUIDv4格式，只允许输入0～9，a～f，A～F，“-”。 UUIDv4格式为“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，例如：4947a69a-f61b-4bc1-b9da-47c9c5d14b64。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                               |
| NFTYPE       | 网元类型   | 可选必选说明：必选参数 参数含义：用于标识该服务发现网元实例的类型。 取值范围：UDR(统一数据存储库)AMF(接入和移动性管理功能)SCP(服务通信代理)SEPP(安全边缘保护代理)SMF(会话管理功能) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                             |
| LOCALNFINSID | 本端网元实例 | 可选必选说明：条件必选参数 参数含义：用于标识SCP或SEPP网元对应的本端网元实例标识（即网元实例在系统中的序号）。 取值范围：长度不超过1024的字符串。 默认值：无。 配置原则： 仅当本命令中的“网元类型”参数取值为“SCP(服务通信代理)”或“SEPP(安全边缘保护代理)”时，该参数有效。在配置该参数前，请确认该服务发现本端网元实例可以通过LST UDMNFSRV查询到，且“网元类型”为“UDM(统一数据管理)”。如果需要配置多个实例标识，多个实例标识需要用英文逗号分隔开，例如“4947a32a-f61b-4bc1-b9da-47c9c8690001,4947a32a-f61b-4bc1-b9da-47c9c8690002”。                                                                                                                                  |
| NFPROFILE    | 网元实例信息 | 可选必选说明：必选参数 参数含义：用于标识服务发现网元实例的详细信息，该参数为JSON格式。 取值范围：长度不超过8000的字符串。 默认值：无。 配置原则：参考网元实例信息配置中信元“网元实例信息”的格式。 其中nfInstanceID、nfType两个参数必须和ADD UDMDISCNFPROF命令的“网元实例标识”、“网元类型”一致。nfServiceList、nfServices两个参数必填其中一个，但是当“网元类型”参数取值为“SCP(服务通信代理)”或“SEPP(安全边缘保护代理)”时，nfServiceList、nfServices两个参数可不填。nfInstanceId、nfType、nfStatus为必填参数，fqdn、ipv4Addresses、ipv6Addresses三个参数必填其中一个。如果nfStatus未配置，则认为对端网元状态不正常。当需要增加SCP网元实例信息时，scpInfo参数必须配置。当需要增加SEPP网元实例信息时，seppInfo参数必须配置。 |

## 使用实例

1. 在开局场景下配置信令数据时，增加一个服务发现网元实例信息。“网元实例名称”为“udr”，“网元实例标识”为“11111111-1111-1111-1111-111111111111”，“网元类型”为“UDR（统一数据存储库）”，“网元实例信息”为“{"nfServices":[{"serviceInstanceId":"4947a32a-f61b-4bc1-b9da-47c9c8690001","serviceName":"nudm-sdm","versions":[{"apiFullVersion":"v1","apiVersionInUri":"v1"}],"scheme":"http","nfServiceStatus":"REGISTERED"}],"nfInstanceId":"11111111-1111-1111-1111-111111111111","nfType":"UDR","nfStatus":"REGISTERED","ipv4Addresses":["192.168.91.105"]}”;

   ```
   ADD UDMDISCNFPROF: NFINSNAME="udr", NFINSID="11111111-1111-1111-1111-111111111111", NFTYPE=UDR, NFPROFILE="{\"nfServices\":[{\"serviceInstanceId\":\"4947a32a-f61b-4bc1-b9da-47c9c8690001\",\"serviceName\":\"nudm-sdm\",\"versions\":[{\"apiFullVersion\":\"v1\",\"apiVersionInUri\":\"v1\"}],\"scheme\":\"http\",\"nfServiceStatus\":\"REGISTERED\"}],\"nfInstanceId\":\"11111111-1111-1111-1111-111111111111\",\"nfType\":\"UDR\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"192.168.91.105\"]}";
   ```
2. 在开局场景下配置信令数据时，增加一个服务发现网元实例信息。“网元实例名称”为“amf”，“网元实例标识”为“22222222-2222-2222-2222-222222222222”，“网元类型”为“AMF(接入和移动性管理功能)”，“网元实例信息”为“{"nfServiceList":{"4947a32a-f61b-4bc1-b9da-47c9c8690001":{"serviceInstanceId":"4947a32a-f61b-4bc1-b9da-47c9c8690001","serviceName":"nudm-sdm","versions":[{"apiVersionInUri":"v1","apiFullVersion":"v1"}],"scheme":"http","nfServiceStatus":"REGISTERED","fqdn":"s906.huawei.com","ipEndPoints":[{"port":8020,"ipv4Address":"192.168.91.105","transport":"TCP"}]}},"nfInstanceId":"22222222-2222-2222-2222-222222222222","nfType":"AMF","nfStatus":"REGISTERED","ipv4Addresses":["192.168.91.105"]}”;

   ```
   ADD UDMDISCNFPROF: NFINSNAME="amf", NFINSID="22222222-2222-2222-2222-222222222222", NFTYPE=AMF, NFPROFILE="{\"nfServiceList\":{\"4947a32a-f61b-4bc1-b9da-47c9c8690001\":{\"serviceInstanceId\":\"4947a32a-f61b-4bc1-b9da-47c9c8690001\",\"serviceName\":\"namf-mt\",\"versions\":[{\"apiVersionInUri\":\"v1\",\"apiFullVersion\":\"v1\"}],\"scheme\":\"http\",\"nfServiceStatus\":\"REGISTERED\",\"fqdn\":\"s906.huawei.com\",\"ipEndPoints\":[{\"port\":8020,\"ipv4Address\":\"192.168.91.105\",\"transport\":\"TCP\"}]}},\"nfInstanceId\":\"22222222-2222-2222-2222-222222222222\",\"nfType\":\"AMF\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"192.168.91.105\"]}";
   ```
3. 在开局场景下配置信令数据时，增加一个服务发现网元实例信息。“网元实例名称”为“scp”，“网元实例标识”为“33333333-3333-3333-3333-333333333333”，“网元类型”为“SCP(服务通信代理)”，“本端网元实例”为“4947a32a-f61b-4bc1-b9da-47c9c8690001”，“网元实例信息”为“{"nfInstanceId" :"33333333-3333-3333-3333-333333333333","scpInfo":{"scpDomainInfoList":{"11111":{"scpFqdn":"huawei1.com","scpIpEndPoints":[{"ipv4Address":"192.168.91.105","ipv6Address":"2001:db8::11","port":8020,"transport":"TCP"}]}}},"nfStatus":"REGISTERED","fqdn" : "huawei.com","nfType":"SCP"}”;

   ```
   ADD UDMDISCNFPROF: NFINSNAME="scp", NFINSID="33333333-3333-3333-3333-333333333333", NFTYPE=SCP, LOCALNFINSID="4947a32a-f61b-4bc1-b9da-47c9c8690001", NFPROFILE="{\"nfInstanceId\" :\"33333333-3333-3333-3333-333333333333\",\"scpInfo\":{\"scpDomainInfoList\":{\"11111\":{\"scpFqdn\":\"huawei1.com\",\"scpIpEndPoints\":[{\"ipv4Address\":\"192.168.91.105\",\"ipv6Address\":\"2001:db8::11\", \"port\":8020,\"transport\":\"TCP\"}]}}},\"nfStatus\":\"REGISTERED\",\"fqdn\" : \"huawei.com\",\"nfType\":\"SCP\"}";
   ```
4. 支持国际漫游场景时，增加一个服务发现网元实例信息。“网元实例名称”为“sepp”，“网元实例标识”为“44444444-4444-4444-4444-444444444444”，“网元类型”为“SEPP(安全边缘保护代理)”，“本端网元实例”为“4947a32a-f61b-4bc1-b9da-47c9c8690002”，“网元实例信息”为“{"ipv4Addresses":["192.168.91.105","192.168.91.15"],"nfInstanceId":"44444444-4444-4444-4444-444444444444","nfStatus":"REGISTERED","nfType":"SEPP","seppInfo":{"remotePlmnList":[{"mcc":"460","mnc":"94"}],"seppPorts":{"http":6060}}}”;

   ```
   ADD UDMDISCNFPROF: NFINSNAME="sepp", NFINSID="44444444-4444-4444-4444-444444444444", NFTYPE=SEPP, LOCALNFINSID="4947a32a-f61b-4bc1-b9da-47c9c8690002", NFPROFILE="{\"ipv4Addresses\":[\"192.168.91.105\",\"192.168.91.15\"],\"nfInstanceId\":\"44444444-4444-4444-4444-444444444444\",\"nfStatus\":\"REGISTERED\",\"nfType\":\"SEPP\",\"seppInfo\":{\"remotePlmnList\":[{\"mcc\":\"460\",\"mnc\":\"94\"}],\"seppPorts\":{\"http\":6060}}}";
   ```
5. 在开局场景下配置信令数据时，增加一个服务发现网元实例信息。“网元实例名称”为“smf”，“网元实例标识”为“00001111-1111-2222-3333-111122223333”，“网元类型”为“SMF(会话管理功能)”，“网元实例信息”为“{"ipv4Addresses":["192.168.91.105"],"nfInstanceId":"00001111-1111-2222-3333-111122223333","nfServices":[{"fqdn":"huawei111.com","ipEndPoints":[{"ipv4Address":"192.168.91.105","port":8020}],"nfServiceStatus":"REGISTERED","scheme":"http","serviceInstanceId":"00001111-1111-2222-3333-111122223333","versions":[{"apiVersionInUri":"v1","apiFullVersion":"21.1.0"}]}],"nfStatus":"REGISTERED","nfType":"SMF"}”;

   ```
   ADD UDMDISCNFPROF: NFINSNAME="smf", NFINSID="00001111-1111-2222-3333-111122223333", NFTYPE=SMF, NFPROFILE="{\"ipv4Addresses\":[\"192.168.91.105\"],\"nfInstanceId\":\"00001111-1111-2222-3333-111122223333\",\"nfServices\":[{\"fqdn\":\"huawei111.com\",\"ipEndPoints\":[{\"ipv4Address\":\"192.168.91.105\",\"port\":8020}],\"nfServiceStatus\":\"REGISTERED\",\"scheme\":\"http\",\"serviceInstanceId\":\"00001111-1111-2222-3333-111122223333\",\"versions\":[{\"apiVersionInUri\":\"v1\",\"apiFullVersion\":\"21.1.0\"}]}],\"nfStatus\":\"REGISTERED\",\"nfType\":\"SMF\"}";
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                             | 原因分析                                                                | 处理建议                                                                                                       |
|-------:|:----------------------------------|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| 360041 | 参数值不合法                            | 错误提示中携带的参数值不合法或“网元实例标识”和“网元类型”与“网元实例信息”中携带的对应字段不一致。                 | 修改错误提示中携带的参数后重新运行命令，参考参数说明中对应参数的格式。                                                                        |
| 360042 | 参数值已存在                            | 错误提示中携带的参数值已存在。                                                     | 修改已存在的参数确保与已有参数不同。                                                                                         |
| 360184 | LOCALNFINSID未在NFTYPE为UDM的NFSRV中配置 | 在配置“本端网元实例”参数前，需要确认该网元实例已通过ADD UDMNFSRV命令参数“网元类型”为“UDM(统一数据管理)”时添加。 | 根据实际情况，重新输入参数，确保满足以下条件： 请确认该服务发现本端网元实例已通过ADD UDMNFSRV命令参数“网元类型”为“UDM(统一数据管理)”时添加，对应的网元实例可通过LST UDMNFSRV查询。 |