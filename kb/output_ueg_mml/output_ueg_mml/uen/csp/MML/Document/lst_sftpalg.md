# 查询SFTP协议算法(LST SFTPALG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

查询SFTP协议算法开关。

## 注意事项

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

无。

## 使用实例

查询SFTP协议算法开关

```
%%LST SFTPALG:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
SFTP协议算法开关  =  关闭兼容算法
(结果个数 = 1)

---    END
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表2所示。

命令执行失败则返回相应的错误，参见表3 错误码列表；命令执行异常，请联系技术支持处理。

| 输出项名称      | 输出项解释          |
|:-----------|:---------------|
| SFTP协议算法开关 | SFTP协议算法开关的状态。 |

|    错误码 | 错误码解释   | 原因分析   | 处理建议       |
|-------:|:--------|:-------|:-----------|
| 102201 | 数据库处理失败 | 内部错误。  | 请联系华为技术支持。 |
| 102200 | MML处理失败 | 内部错误。  | 请联系华为技术支持。 |

## 参考信息

无。