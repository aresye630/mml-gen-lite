# 查询HTTPOauth公钥（LST HTTPOAUTHKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询NF认证所需的公钥信息。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                                |
|:---------|:--------|:------------------------------------------------------------------------------------------------------------------------------------|
| AUTSCENE | 认证场景    | 可选必选说明：可选参数  参数含义：该参数用于指定OAuth授权及认证的使用场景。  数据来源：本端规划 取值范围： “NFSERV_ACCESS（NF服务接入认证）”：NF服务接入认证  默认值：无  配置原则：无                        |
| AUZSVRID | 授权服务器标识 | 可选必选说明：可选参数  参数含义：该参数用于指定OAuth令牌授权服务器ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                        |
| PUBKEYID | 公钥标识    | 可选必选说明：可选参数  参数含义：该参数用于指定验证OAuth令牌的公钥标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~128。大小写敏感。  默认值：无  配置原则：  当使用消息中身份令牌的公钥ID，查找公钥进行校验时，配置该参数。 |

## 使用实例

若运营商想查询配置的NRF公钥信息，可以用如下命令：

```
%%LST HTTPOAUTHKEY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     Index  =  1
  AUTSCENE  =  NFService Access
  AUZSVRID  =  bf33a517-7789-4637-b675-b3591b0d706b
  PUBKEYID  =  NULL
    PUBKEY  =  -----BEGIN PUBLIC KEY----- MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQA/axE26pXWXesAjcTP/2Tfe4EcF4A 3LuqgpIFzrftiztViq0+5deUvfcxuPIFk+ANVinlAOzgZWpFS0kheI7KJAYA3fOH n5ZTU08AAjau0CoZe9GSPUC4cnSy1nqetiKBW0YpBvhaY5FXnngvfHUHdmkFSVLC S6N+LXoi/dm0Fbo6snE= -----END PUBLIC KEY-----
PUBKEYNAME  =  key1
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                   |
|:--------|:------------------------|
| 索引      | 该参数用于指定表项索引。            |
| 认证场景    | 该参数用于指定OAuth授权及认证的使用场景。 |
| 授权服务器标识 | 该参数用于指定OAuth令牌授权服务器ID。  |
| 公钥标识    | 该参数用于指定验证OAuth令牌的公钥标识。  |
| 公钥内容    | 该参数用于指定验证OAuth令牌的公钥内容。  |
| 公钥名称    | 该参数用于指定OAuth令牌的公钥名称。    |