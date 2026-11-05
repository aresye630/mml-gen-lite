# 增加NRF公钥（ADD SBINRFKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## 注意事项

- 该命令执行后立即生效。

- HTTPOAUTHKEY 命令和SBINRFKEY命令存在相同功能，且HTTPOAUTHKEY命令和SBINRFKEY命令不能配置相同的记录，更推荐使用HTTPOAUTHKEY命令。

- 最多可输入128条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                                                     |
|:--------|:--------|:-----------------------------------------------------------------------------------------|
| NRFID   | NRF实例ID | 可选必选说明：必选参数  参数含义：该参数用于指定配置的NRF实例ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无 |
| NRFKEY  | NRF公钥   | 可选必选说明：必选参数  参数含义：该参数用于指定配置的NRF公钥。  数据来源：本端规划  取值范围：任意类型，取值范围是0~2048。  默认值：无  配置原则：无     |
| KEYNAME | 公钥名称    | 可选必选说明：可选参数  参数含义：该参数用于指定配置的公钥名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无    |

## 使用实例

假设运营商需要为NRF实例bf33a517-7789-4637-b675-b3591b0d706b配置公钥，公钥名称为key1，可以用如下命令：

```
ADD SBINRFKEY: NRFID="bf33a517-7789-4637-b675-b3591b0d706b", NRFKEY="-----BEGIN PUBLIC KEY----- MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQA/axE26pXWXesAjcTP/2Tfe4EcF4A 3LuqgpIFzrftiztViq0+5deUvfcxuPIFk+ANVinlAOzgZWpFS0kheI7KJAYA3fOH n5ZTU08AAjau0CoZe9GSPUC4cnSy1nqetiKBW0YpBvhaY5FXnngvfHUHdmkFSVLC S6N+LXoi/dm0Fbo6snE= -----END PUBLIC KEY-----", KEYNAME="key1";
```