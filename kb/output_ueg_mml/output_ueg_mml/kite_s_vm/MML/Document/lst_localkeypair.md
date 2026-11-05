# 查询本地公钥（LST LOCALKEYPAIR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询本地公钥。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                         |
|:--------|:-------|:-------------------------------------------------------------|
| KEYTYPE | 公钥类型   | 可选必选说明：必选参数 参数含义：公钥类型。 数据来源：本端规划 取值范围：枚举类型。 RSA：RSA公钥。 默认值：无 |

#### 使用实例

查询本地公钥：

```
LST LOCALKEYPAIR:KEYTYPE=RSA;
```

```
RETCODE = 0  操作成功

结果如下:
---------
             公钥类型  =  RSA
             公钥名字  =  VNFPOM_SYSTEM_Host
             公钥长度  =  2048
             公钥指纹  =  oAcYnKeTeesfb5k6sVqD5P+7KYurEDPumZwdyHX1MTY
             公钥编码  =  3082010A
  02820101
    00A50D7C 72FEBC88 6699D4F7 FA389FAA 60E91919
    691D3780 36DEBB81 4C4793B2 ACDE5015 BDA3E4D8
    B2CEC230 7805B063 C5F748BE 1B1642A4 14B38EFD
    A0C6A3F5 48EE3490 8C707E41 570CAA75 989DB6A6
    7E2FA0B9 12605171 63557645 E52B2A0E B2A6E98E
    4A22EE15 5376BA61 C46A02A2 20ED4296 0A599E94
    3074EC5B 6A988A34 D7DFB737 15C8B110 88F932F5
    35267D88 B946D1A7 F66D0E17 6443B55C 8DC728FD
    CC82F11B CAB3AC5C 33AB796F F1421934 415F1B30
    B4F8DBCA 64A4140A CD4A1FBA 391CF6E6 835B95A5
    4B9BFD9F 2EE23635 AAA216B6 26130814 D5CCF866
    57BFFB1D 2F35D5DA 57A23561 09911EEB F805EC15
    B09168F3 41B286AB 7D8A3A2A 4AB0EEAE 51
  0203
    010001
    PEM格式的公钥编码  =  ---- BEGIN SSH2 PUBLIC KEY ----
AAAAB3NzaC1yc2EAAAADAQABAAABAQClDXxy/ryIZpnU9/o4n6pg6RkZaR03gDbe
u4FMR5OyrN5QFb2j5NiyzsIweAWwY8X3SL4bFkKkFLOO/aDGo/VI7jSQjHB+QVcM
qnWYnbamfi+guRJgUXFjVXZF5SsqDrKm6Y5KIu4VU3a6YcRqAqIg7UKWClmelDB0
7FtqmIo019+3NxXIsRCI+TL1NSZ9iLlG0af2bQ4XZEO1XI3HKP3MgvEbyrOsXDOr
eW/xQhk0QV8bMLT428pkpBQKzUofujkc9uaDW5WlS5v9ny7iNjWqoha2JhMIFNXM
+GZXv/sdLzXV2leiNWEJkR7r+AXsFbCRaPNBsoarfYo6Kkqw7q5R
---- END SSH2 PUBLIC KEY ----

OpenSSH格式的公钥编码  =  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClDXxy/ryIZpnU9/o4n6pg6RkZaR03gDbeu4FMR5OyrN5QFb2j5NiyzsIweAWwY8X3SL4bFkKkFLOO/aDGo/VI7jSQjHB+QVcMqnWYnbamfi+guRJgUXFjVXZF5SsqDrKm6Y5KIu4VU3a6YcRqAqIg7UKWClmelDB07FtqmIo019+3NxXIsRCI+TL1NSZ9iLlG0af2bQ4XZEO1XI3HKP3MgvEbyrOsXDOreW/xQhk0QV8bMLT428pkpBQKzUofujkc9uaDW5WlS5v9ny7iNjWqoha2JhMIFNXM+GZXv/sdLzXV2leiNWEJkR7r+AXsFbCRaPNBsoarfYo6Kkqw7q5R rsa-key

(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称          | 输出项解释           |
|:---------------|:----------------|
| 公钥名字           | 公钥的名字。          |
| 公钥指纹           | 公钥的指纹。          |
| 公钥编码           | 公钥的编码。          |
| PEM格式的公钥编码     | PEM格式的公钥编码。     |
| OpenSSH格式的公钥编码 | OpenSSH格式的公钥编码。 |
| 公钥类型           | 本地公钥类型。         |
| 公钥长度           | 本地公钥长度。         |