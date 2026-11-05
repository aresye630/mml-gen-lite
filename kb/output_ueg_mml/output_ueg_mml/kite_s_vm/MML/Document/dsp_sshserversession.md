# 显示SSH服务端会话信息（DSP SSHSERVERSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

本命令用于显示SSH服务器session信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

无。

#### 使用实例

显示SSH服务器session信息：

```
DSP SSHSERVERSESSION:;
```

```
RETCODE = 0 操作成功

结果如下
------------------------
  SSH服务端的会话号  =  1
    SSH服务端的索引  =  VTY 0
            SSH版本  =  2.0
          SSH用户名  =  admin
       会话重试次数  =  1
       Ctos加密算法  =  aes256-ctr
       Stoc加密算法  =  aes256-ctr
      Ctos HMAC算法  =  hmac-sha2-256
      Stoc HMAC算法  =  hmac-sha2-256
       Ctos压缩算法  =  none
       Stoc压缩算法  =  none
           交换算法  =  diffie-hellman-group-exchange-sha256
     会话的密钥类型  =  DSA
         服务端类型  =  stelnet
           认证类型  =  密码
         服务端端口  =  6000
         客户端端口  =  1936
       服务端IP地址  =  192.168.2.3
       客户端IP地址  =  192.168.2.5
        VPN实例名称  =  __mpp_vpn_outer__
           空闲时间  =  00:00:00
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称       | 输出项解释        |
|:------------|:-------------|
| SSH服务端的会话号  | SSH服务端的会话号。  |
| SSH服务端的索引   | SSH服务端的索引。   |
| SSH版本       | SSH版本。       |
| SSH用户名      | SSH用户名。      |
| 会话重试次数      | 会话重试次数。      |
| Ctos加密算法    | Ctos加密算法。    |
| Stoc加密算法    | Stoc加密算法。    |
| Ctos HMAC算法 | Ctos HMAC算法。 |
| Stoc HMAC算法 | Stoc HMAC算法。 |
| Ctos压缩算法    | Ctos压缩算法。    |
| Stoc压缩算法    | Stoc压缩算法。    |
| 交换算法        | 交换算法。        |
| 会话的密钥类型     | 会话的密钥类型。     |
| 服务端类型       | 服务端类型。       |
| 认证类型        | 认证类型。        |
| 服务端端口       | 服务端端口。       |
| 客户端端口       | 客户端端口。       |
| 服务端IP地址     | 服务端IP地址。     |
| 客户端IP地址     | 客户端IP地址。     |
| VPN实例名称     | VPN实例名称。     |
| 空闲时间        | 空闲时间。        |