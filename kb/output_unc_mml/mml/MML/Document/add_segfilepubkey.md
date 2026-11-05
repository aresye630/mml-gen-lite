# 增加号段配置文件的签名验证公钥（ADD SEGFILEPUBKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于在NRF上新增号段配置文件的签名验证公钥。

当使用号段文件导入到NRF这种方式来配置号段数据前，为了保证文件完整性安全，需要给号段文件配置签名验证公钥。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                 |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------|
| KEYNAME | 公钥名称   | 可选必选说明：必选参数  参数含义：该参数用于表示在NRF上配置的号段配置文件的签名验证公钥名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。  默认值：无  配置原则：无 |
| KEYINFO | 公钥信息   | 可选必选说明：必选参数  参数含义：该参数用于表示在NRF上配置的公钥内容。  数据来源：本端规划  取值范围：任意类型，取值范围是0~4096。  默认值：无  配置原则：无             |

## 使用实例

新增号段配置文件的签名验证公钥，公钥名称为keyname001。

```
ADD SEGFILEPUBKEY: KEYNAME="keyname001", KEYINFO="-----BEGIN PUBLIC KEY-----#MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsog/61GMt1h6iePkMilD#L7PUuZ41aI8swe/aJAUMlDORsGkoOvkUxRZitBccUr/5yThXb1el5TSUpibGCbEj#YWJmpPSbTQzOQUKTYHwB3Ex23Qo5C3ByeN9HgzUKZMghNeHw5IUIKU/9PKp34bVX#/If2u4q+bPrGqFZ7Uqf/HM2eD8LR2POVSgyngNDCKt5MI5DVx4Kj5JmdaZHmJppD#/72qzxLXdJGH79z3M/Z2MtJ7jp4ZEi+MtOnyqx7Tvrm3A/9bWRghDCLUjxKzHvbi#NTVrf8QDpO2J1FkMmsTBsLJAHyA+rCB11J9OFCObF5HaS6ZqKrOz/FD/mAsLZZi7#gwIDAQAB#-----END PUBLIC KEY-----#";
```