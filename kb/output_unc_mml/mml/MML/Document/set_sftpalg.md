# 设置SFTP协议算法（SET SFTPALG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于设置SFTP协议是否使用兼容性算法。

**须知** 

如果将“SFTP协议算法开关”设置为“ON（开启兼容算法）”，系统会使用兼容算法，请谨慎处理。

## 注意事项

使用**SET SFTPALG**关闭兼容算法后为保证业务连续性，不会将之前建立的SFTP链接关闭，建议用户重新建立SFTP链接，保证系统安全。

| 算法类型   | 交互算法类型   | 算法                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 不兼容算法  | 密钥交换算法   | curve25519-sha256@libssh.org、 curve25519-sha256、curve448-sha512、 ecdh-sha2-nistp521、ecdh-sha2-nistp384、 ecdh-sha2-nistp256、diffie-hellman-group-exchange-sha256、diffie-hellman-group18-sha512、diffie-hellman-group17-sha512、diffie-hellman-group16-sha512、 diffie-hellman-group15-sha512、diffie-hellman-group14-sha256                                                                                                                    |
| 不兼容算法  | 主机加密算法   | aes256-gcm@openssh.com、aes256-ctr、chacha20-poly1305@openssh.com、aes192-ctr、aes128-gcm@openssh.com、aes128-ctr                                                                                                                                                                                                                                                                                                                              |
| 不兼容算法  | MAC算法    | hmac-sha2-512-etm@openssh.com、hmac-sha2-512、hmac-sha2-256-etm@openssh.com、hmac-sha2-256                                                                                                                                                                                                                                                                                                                                                   |
| 不兼容算法  | 主机密钥算法   | ssh-ed25519-cert-v01@openssh.com、ggssh-ed25519、sk-ssh-ed25519@openssh.com、sk-ecdsa-sha2-nistp256@openssh.com、rsa-sha2-512-cert-v01@openssh.com、rsa-sha2-512、rsa-sha2-256-cert-v01@openssh.com、rsa-sha2-256、ecdsa-sha2-nistp521-cert-v01@openssh.com、nistp521、ecdsa-sha2-nistp384-cert-v01@openssh.com、nistp384、ecdsa-sha2-nistp256-cert-v01@openssh.com、nistp256                                                                          |
| 兼容算法   | 密钥交换算法   | curve25519-sha256@libssh.org、curve25519-sha256、curve448-sha512、ecdh-sha2-nistp521、ecdh-sha2-nistp384、ecdh-sha2-nistp256、diffie-hellman-group-exchange-sha256、diffie-hellman-group18-sha512、diffie-hellman-group17-sha512、diffie-hellman-group16-sha512、 diffie-hellman-group15-sha512、diffie-hellman-group14-sha256、diffie-hellman-group-exchange-sha1、diffie-hellman-group14-sha1、diffie-hellman-group1-sha1                             |
| 兼容算法   | 主机加密算法   | aes256-gcm@openssh.com、aes256-ctr、aes192-ctr、aes128-gcm@openssh.com、aes128-ctr、chacha20-poly1305@openssh.com、aes256-cbc、aes192-cbc、aes128-cbc、arcfour256、arcfour128、blowfish-cbc、3des-cbc                                                                                                                                                                                                                                                 |
| 兼容算法   | MAC算法    | hmac-sha2-512-etm@openssh.com、hmac-sha2-512、hmac-sha2-256-etm@openssh.com、hmac-sha2-256、hmac-sha1-etm@openssh.com、hmac-sha1、hmac-sha1-96、hmac-md5-96、hmac-md5                                                                                                                                                                                                                                                                             |
| 兼容算法   | 主机密钥算法   | ssh-ed25519-cert-v01@openssh.com、ssh-ed25519、sk-ssh-ed25519@openssh.com、sk-ecdsa-sha2-nistp256@openssh.com、rsa-sha2-512-cert-v01@openssh.com、rsa-sha2-512、rsa-sha2-256-cert-v01@openssh.com、rsa-sha2-256、ecdsa-sha2-nistp521-cert-v01@openssh.com、nistp521、ecdsa-sha2-nistp384-cert-v01@openssh.com、nistp384、 ecdsa-sha2-nistp256-cert-v01@openssh.com、nistp256、ssh-rsa、ssh-rsa-cert-v01@openssh.com、ssh-dss-cert-v01@openssh.com、ssh-dss |

## 参数说明

| 参数标识          | 参数名称       | 参数说明                                                                    |
|:--------------|:-----------|:------------------------------------------------------------------------|
| SFTPALGSWITCH | SFTP协议算法开关 | 可选必选说明：必选参数。 参数含义：SFTP协议算法开关 取值范围： ON（开启兼容算法）OFF（关闭兼容算法） 默认值：无。 配置原则：无。 |

## 使用实例

设置“SFTP协议算法开关”为“ON（开启兼容算法）”。

```
%%SET SFTPALG: SFTPALGSWITCH=ON;%%
RETCODE = 0  操作成功

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

|    错误码 | 错误码解释   | 原因分析   | 处理建议       |
|-------:|:--------|:-------|:-----------|
| 102201 | 数据库处理失败 | 内部错误。  | 请联系华为技术支持。 |
| 102200 | MML处理失败 | 内部错误。  | 请联系华为技术支持。 |

## 参考信息

无。