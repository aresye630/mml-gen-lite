# 查询服务发现网元实例信息(LST UDMDISCNFPROF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询服务发现网元实例数据。

- 若需要查询所有网元实例的信息，不输入任何参数。
- 若需要查询某个网元实例的详细信息，请输入“网元实例名称”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                   |
|:----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSNAME | 网元实例名称 | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个网元实例名称来查询网元实例信息数据；若不输入，则表示所有网元实例名称的网元实例信息。 取值范围：长度不超过32的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无。 配置原则：无。                                                                                      |
| NFINSID   | 网元实例标识 | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个网元实例标识来查询网元实例信息数据；若不输入，则表示所有网元实例标识的网元实例信息。 取值范围：有效的UUIDv4格式，只允许输入0～9，a～f，A～F，“-”。 UUIDv4格式为“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，例如：4947a69a-f61b-4bc1-b9da-47c9c5d14b64。 默认值：无。 配置原则：无。 |
| NFTYPE    | 网元类型   | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个网元类型来查询网元实例信息数据；若不输入，则表示所有网元类型的网元实例信息。 取值范围：UDR(统一数据存储库)AMF(接入和移动性管理功能)SCP(服务通信代理)SEPP(安全边缘保护代理)SMF(会话管理功能) 默认值：无。 配置原则：无。                                                                |

## 使用实例

1. 查询所有用于服务发现的网元实例信息：

   ```
   LST UDMDISCNFPROF:;
   ```

   ```
   %%LST UDMDISCNFPROF:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   网元实例名称  网元实例标识                          网元类型              网元实例信息

   amf           22222222-2222-2222-2222-222222222222  接入和移动性管理功能  {"ipv4Addresses":["192.168.91.105"],"nfInstanceId":"22222222-2222-2222-2222-222222222222","nfServiceList":{"4947a32a-f61b-4bc1-b9da-47c9c8690001":{"fqdn":"s906.huawei.com","ipEndPoints":[{"ipv4Address":"192.168.91.105","port":8020,"transport":"TCP"}],"nfServiceStatus":"REGISTERED","scheme":"http","serviceInstanceId":"4947a32a-f61b-4bc1-b9da-47c9c8690001","serviceName":"namf-mt","versions":[{"apiFullVersion":"v1","apiVersionInUri":"v1"}]}},"nfStatus":"REGISTERED","nfType":"AMF"}  
   udr           11111111-1111-1111-1111-111111111111  统一数据存储库        {"ipv4Addresses":["192.168.91.105"],"nfInstanceId":"11111111-1111-1111-1111-111111111111","nfServices":[{"nfServiceStatus":"REGISTERED","scheme":"http","serviceInstanceId":"4947a32a-f61b-4bc1-b9da-47c9c8690001","serviceName":"nudm-sdm","versions":[{"apiFullVersion":"v1","apiVersionInUri":"v1"}]}],"nfStatus":"REGISTERED","nfType":"UDR"}                                                                                                                                                    
   (结果个数 = 2)

   ---    END
   ```
2. 查询“网元实例名称”为“amf”的网元实例信息：

   ```
   LST UDMDISCNFPROF: NFINSNAME="amf";
   ```

   ```
   %%LST UDMDISCNFPROF: NFINSNAME="amf";%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   网元实例名称  =  amf
   网元实例标识  =  22222222-2222-2222-2222-222222222222
       网元类型  =  接入和移动性管理功能
   网元实例信息  =  {"ipv4Addresses":["192.168.91.105"],"nfInstanceId":"22222222-2222-2222-2222-222222222222","nfServiceList":{"4947a32a-f61b-4bc1-b9da-47c9c8690001":{"fqdn":"s906.huawei.com","ipEndPoints":[{"ipv4Address":"192.168.91.105","port":8020,"transport":"TCP"}],"nfServiceStatus":"REGISTERED","scheme":"http","serviceInstanceId":"4947a32a-f61b-4bc1-b9da-47c9c8690001","serviceName":"namf-mt","versions":[{"apiFullVersion":"v1","apiVersionInUri":"v1"}]}},"nfStatus":"REGISTERED","nfType":"AMF"}
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD UDMDISCNFPROF**命令的参数说明。