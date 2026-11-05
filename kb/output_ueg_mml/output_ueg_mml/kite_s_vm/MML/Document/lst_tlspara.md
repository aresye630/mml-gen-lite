# 查询TLS参数（LST TLSPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

开启服务化接口的TLS协议时，需要配置详细的TLS上下文参数，该命令用于查询一组TLS参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------|
| INDEX  | 索引     | 可选必选说明：可选参数  参数含义：该参数用于指定TLS参数索引。  数据来源：本端规划  取值范围：整数类型，取值范围是1~128。  默认值：无  配置原则：  与ADD HTTPLE中配置的TLS参数索引保持一致。 |

## 使用实例

- 若运营商想查询索引为1的TLS参数配置信息，可以用如下命令；

  ```
  %%LST TLSPARA: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
              索引  =  1
          HTTP模式  =  服务端模式
  是否验证对端证书  =  开启校验对端证书
          校验深度  =  0
          协议版本  =  传输层安全性协议版本v1.2&传输层安全性协议版本v1.3
      加密套件集合  =  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256
        CA证书场景  =  2
      设备证书场景  =  1
       CRL是否开启  =  开启吊销证书列表
              描述  =  NULL
      域名校验开关  =  关闭校验对端证书
        IP校验开关  =  关闭校验对端证书
       SNI校验开关  =  关闭SNI校验
          认证模式  =  证书认证
  预共享密钥组索引  =  0
    域名校验全匹配  =  关闭域名检验全匹配
  (结果个数 = 1)

  ---    END
  ```
- 若运营商想查询所有的TLS参数配置信息，可以用如下命令；

  ```
  %%LST TLSPARA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  索引  HTTP模式    是否验证对端证书  校验深度  协议版本                                           加密套件集合                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            CA证书场景  设备证书场景  CRL是否开启       描述  域名校验开关      IP校验开关        SNI校验开关  认证模式  预共享密钥组索引  域名校验全匹配      

  1     服务端模式  开启校验对端证书  0         传输层安全性协议版本v1.2&传输层安全性协议版本v1.3  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256  2           1             开启吊销证书列表  NULL  关闭校验对端证书  关闭校验对端证书  关闭SNI校验  证书认证  0                 关闭域名检验全匹配  
  2     客户端模式  开启校验对端证书  0         传输层安全性协议版本v1.2&传输层安全性协议版本v1.3  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256  2           1             开启吊销证书列表  NULL  关闭校验对端证书  关闭校验对端证书  关闭SNI校验  证书认证  0                 关闭域名检验全匹配  
  (结果个数 = 2)

  ---    END
  ```

## 输出结果说明

| 输出项名称    | 输出项解释                                                                      |
|:---------|:---------------------------------------------------------------------------|
| 索引       | 该参数用于指定TLS参数索引。                                                            |
| HTTP模式   | 该参数用于指定开启服务化接口的TLS协议时的HTTP模式，HTTP模式指客户端模式或服务端模式的区分。                        |
| 是否验证对端证书 | 该参数用于指定是否验证对端证书。                                                           |
| 校验深度     | 该参数用于指定校验深度。                                                               |
| 协议版本     | 该参数用于指定协议版本。                                                               |
| 加密套件集合   | 该参数用于指定加密套件集合。                                                             |
| CA证书场景   | 该参数用于CA证书场景。                                                               |
| 设备证书场景   | 该参数用于设备证书场景。                                                               |
| CRL是否开启  | 该参数用于指定开启服务化接口的TLS协议时是否开启吊销证书列表。                                           |
| 描述       | 该参数用于指定TLS上下文描述。                                                           |
| 域名校验开关   | 该参数用于指定在证书校验阶段是否校验对端域名。开启域名校验时，将校验对端证书中的域名与实际域名是否一致，如果不一致则HTTPS建链失败。       |
| IP校验开关   | 该参数用于指定在证书校验阶段是否校验对端IP地址。开启IP校验后，将校验对端证书中的IP地址与实际IP地址是否一致，如果不一致则HTTPS建链失败。 |
| SNI校验开关  | 该参数用于控制是否使用SNI验证证书中的域名。如果开启了该功能，当使用SNI匹配证书的域名失败后，建链失败。                     |
| 认证模式     | 该参数用于指定身份认证方式。                                                             |
| 预共享密钥组索引 | 在身份认证模式为预共享密钥时，该参数用于指定关联的预共享密钥组索引。                                         |
| 域名校验全匹配  | 该参数用于指定检验证书域名时是否全匹配。                                                       |