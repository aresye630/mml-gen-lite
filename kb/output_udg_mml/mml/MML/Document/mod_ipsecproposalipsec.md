# 修改IPsec提议（MOD IPSECPROPOSALIPSEC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

修改配置，可能是不安全算法，影响加解密安全性。

如果修改后的IPSEC提议中的配置与对端规划的IPSEC提议配置不一致，会导致IPSEC SA协商失败。

该命令用于修改IPsec安全提议。

## 注意事项

- 该命令执行后立即生效。

- 该命令中的一些配置可能是不安全的。
- 提议名称格式为“proposal”+“数字”的IPSEC提议（数字区间为80~91，例如proposal80）可以通过软参配置不安全算法MD5、DES、3DES，具体配置方法请参考产品文档相应软参文档。
- 认证算法中Md5、Sha1是不安全的，建议使用Sha2\_256算法。
- AH认证算法不能为空，当选择Unconfigure时，下发Sha2\_256算法。
- 加密算法中DES、3DES、Aes\_128、Aes\_192、Aes\_256是不安全的，建议使用Aes\_gcm\_128算法。
- 当ESP加密算法配置AES\_GCM或AES\_GMAC时，ESP认证算法必须为空。
- 当ESP加密算法不配置AES\_GCM或AES\_GMAC时，认证算法必须不为空。
- 当ESP加密算法配置AES\_GCM或AES\_GMAC时，不能用软参配置算法。
- 国密算法Sm3、Sm4需要设置软参开关才能使用，打开国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;"，关闭国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=0;"。
- 老旧V3单板不支持开启国密算法加速功能。
- 以下算法不支持IKEv1：ESP加密算法: 128位AES-GCM算法、256位AES-GCM算法、128位AES-GMAC算法、NULL。
- IKEv1国密的IPSEC提议仅支持一种配置：IPsec安全协议为ESP，ESP认证算法为SM3，ESP加密算法为SM4，封装模式为隧道模式。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:---------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROPOSALNAME   | Proposal名称 | 可选必选说明：必选参数  参数含义：Proposal名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~15。不区分大小写。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                 |
| IPSECPROTOCOL  | IPsec安全协议  | 可选必选说明：可选参数  参数含义：IPsec协议：AH / ESP / AH-ESP。  数据来源：对端协商 取值范围： “Ah（AH协议）”：AH协议“Esp（ESP协议）”：ESP协议“Ah_esp（AH-ESP协议）”：AH-ESP协议  默认值：无  配置原则：无                                                                                                                                                                                                                                                                               |
| ESPAUTHALGO    | ESP认证算法    | 可选必选说明：该参数在"IPSECPROTOCOL"配置为"Esp"、"Ah_esp"时为条件可选参数。  参数含义：ESP认证算法。  数据来源：对端协商 取值范围： “Md5（Md5算法）”：Md5算法“Sha1（Sha1算法）”：Sha1算法“Sha2_256（Sha2-256算法）”：Sha2-256算法“Sha2_384（Sha2-384算法）”：Sha2-384算法“Sha2_512（Sha2-512算法）”：Sha2-512算法“Null（空）”：空“Unconfigure（未配置）”：未配置“Sm3（Sm3算法）”：Sm3算法  默认值：无  配置原则：无                                                                                                                       |
| ESPENCRYPTALGO | ESP加密算法    | 可选必选说明：该参数在"IPSECPROTOCOL"配置为"Esp"、"Ah_esp"时为条件可选参数。  参数含义：加密算法。  数据来源：对端协商 取值范围： “Des（DES算法）”：DES算法“A3des（3DES算法）”：3DES算法“Aes_128（128位AES算法）”：128位AES算法“Aes_192（192位AES算法）”：192位AES算法“Aes_256（256位AES算法）”：256位AES算法“Unconfigure（未配置）”：未配置“Sm4（SM4算法）”：SM4算法“Aes_gcm_128（128位AES-GCM算法）”：128位AES-GCM算法“Aes_gcm_256（256位AES-GCM算法）”：256位AES-GCM算法“Aes_gmac_128（128位AES-GMAC算法）”：128位AES-GMAC算法“Null（空）”：空  默认值：无  配置原则：无 |
| AHAUTHALGO     | AH认证算法     | 可选必选说明：该参数在"IPSECPROTOCOL"配置为"Ah"、"Ah_esp"时为条件可选参数。  参数含义：认证算法。  数据来源：对端协商 取值范围： “Md5（Md5算法）”：Md5算法“Sha1（Sha1算法）”：Sha1算法“Sha2_256（Sha2-256算法）”：Sha2-256算法“Sha2_384（Sha2-384算法）”：Sha2-384算法“Sha2_512（Sha2-512算法）”：Sha2-512算法“Unconfigure（未配置）”：未配置“Sm3（Sm3算法）”：Sm3算法  默认值：无  配置原则：无                                                                                                                                      |
| ENCAPMODE      | 封装模式       | 可选必选说明：可选参数  参数含义：封装模式。  数据来源：对端协商 取值范围： “Transport（传输模式）”：传输模式“Tunnel（隧道模式）”：隧道模式  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                       |

## 使用实例

修改名称为“asdf2”的IPsec安全提议：

```
MOD IPSECPROPOSALIPSEC:PROPOSALNAME="asdf2",IPSECPROTOCOL=Ah,AHAUTHALGO=Sha2_256,ENCAPMODE=Tunnel;
```