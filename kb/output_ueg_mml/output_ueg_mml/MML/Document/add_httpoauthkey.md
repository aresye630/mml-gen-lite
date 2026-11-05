# 增加HTTPOauth密钥（ADD HTTPOAUTHKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## 注意事项

- 该命令执行后立即生效。

- 如果NF服务消费者发送的OAuth令牌中携带了公钥标识，但NF服务提供者没有配置该公钥标识的公钥，而配置了无公钥标识的公钥，则使用无公钥标识的公钥进行校验。
- HTTPOAUTHKEY 命令和SBINRFKEY命令存在相同功能，且HTTPOAUTHKEY命令和SBINRFKEY命令不能配置相同的记录，更推荐使用HTTPOAUTHKEY命令。

- 最多可输入128条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称    | 参数说明                                                                                                                                |
|:-----------|:--------|:------------------------------------------------------------------------------------------------------------------------------------|
| INDEX      | 索引      | 可选必选说明：必选参数  参数含义：该参数用于指定表项索引。  数据来源：本端规划  取值范围：整数类型，取值范围是1~128。  默认值：无  配置原则：无                                                     |
| AUTSCENE   | 认证场景    | 可选必选说明：必选参数  参数含义：该参数用于指定OAuth授权及认证的使用场景。  数据来源：本端规划 取值范围： “NFSERV_ACCESS（NF服务接入认证）”：NF服务接入认证  默认值：无  配置原则：无                        |
| AUZSVRID   | 授权服务器标识 | 可选必选说明：必选参数  参数含义：该参数用于指定OAuth令牌授权服务器ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                        |
| PUBKEYID   | 公钥标识    | 可选必选说明：可选参数  参数含义：该参数用于指定验证OAuth令牌的公钥标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~128。大小写敏感。  默认值：无  配置原则：  当使用消息中身份令牌的密钥ID，查找公钥进行校验时，配置该参数。 |
| PUBKEY     | 公钥内容    | 可选必选说明：必选参数  参数含义：该参数用于指定验证OAuth令牌的公钥内容。  数据来源：全网规划  取值范围：任意类型，取值范围是0~1024。  默认值：无  配置原则：无                                          |
| PUBKEYNAME | 公钥名称    | 可选必选说明：可选参数  参数含义：该参数用于指定OAuth令牌的公钥名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                          |

## 使用实例

假设运营商需要为授权服务器bf33a517-7789-4637-b675-b3591b0d706b配置公钥，公钥名称为key1，可以用如下命令：

```
ADD HTTPOAUTHKEY: INDEX=1, AUTSCENE=NFSERV_ACCESS, AUZSVRID="bf33a517-7789-4637-b675-b3591b0d706b", PUBKEY="-----BEGIN PUBLIC KEY----- MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQA/axE26pXWXesAjcTP/2Tfe4EcF4A 3LuqgpIFzrftiztViq0+5deUvfcxuPIFk+ANVinlAOzgZWpFS0kheI7KJAYA3fOH n5ZTU08AAjau0CoZe9GSPUC4cnSy1nqetiKBW0YpBvhaY5FXnngvfHUHdmkFSVLC S6N+LXoi/dm0Fbo6snE= -----END PUBLIC KEY-----", PUBKEYNAME="key1";
```