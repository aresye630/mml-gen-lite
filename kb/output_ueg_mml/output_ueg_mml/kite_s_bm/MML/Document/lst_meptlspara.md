# 查询MEP TLS参数（LST MEPTLSPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查询TLS参数信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                             |
|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------|
| TLSPARANAME | TLS参数名称 | 可选必选说明：可选参数 参数含义：该参数用于指定TLS参数名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：无 |

#### 使用实例

- 查询全部的MEPTLSPARA对象：

  ```
  LST MEPTLSPARA:;
  ```

  ```
  RETCODE = 0 操作成功

  TLS参数
  -------
  TLS参数名称 TLS协议版本 校验对端证书 校验深度 设备证书场景 CA证书场景 TLS算法套件集合

  tls TLSv1.2&TLSv1.3 使能 10 MP1设备证书场景 MP1 CA证书场景 TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  tls1 TLSv1.2&TLSv1.3 使能 10 内部设备证书场景 内部CA证书场景 TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  (结果个数 = 2)

  --- END
  ```
- 查询MEPTLSPARA对象，查询的MEPTLSPARA对象的名称为“tls”：

  ```
  LST MEPTLSPARA: TLSPARANAME="tls";
  ```

  ```
  RETCODE = 0 操作成功

  TLS参数
  -------
  TLS参数名称 = tls
  TLS协议版本 = TLSv1.2&TLSv1.3
  校验对端证书 = 使能
  校验深度 = 10
  设备证书场景 = MP1设备证书场景
  CA证书场景 = MP1 CA证书场景
  TLS算法套件集合 = TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  (结果个数 = 1)

  --- END
  ```

#### 输出结果说明

参见ADD MEPTLSPARA的参数说明。