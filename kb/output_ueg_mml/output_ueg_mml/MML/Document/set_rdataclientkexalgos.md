# 设置数据同步客户端支持的密钥交换算法（SET RDATACLIENTKEXALGOS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于设置数据同步客户端支持的密钥交换算法。在登陆远端数据同步服务器时，本地客户端和对端服务器协商密钥交互算法。协商会选择服务器和客户端都支持的算法，优先级以客户端算法列表为准，算法列表中排列在前的优先级高。如果服务器和客户端没有相同的算法，则协商失败。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 可选参数至少配置一个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | CURVE25519_SHA256   | CURVE25519_SHA256_LIBSSH   | DH_GROUP_EXCHANGE_SHA256   | ECDH_SHA2_NISTP256   | ECDH_SHA2_NISTP384   | ECDH_SHA2_NISTP521   |
|:-------|:--------------------|:---------------------------|:---------------------------|:---------------------|:---------------------|:---------------------|
| 初始值    | True                | True                       | True                       | False                | False                | False                |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识                     | 参数名称                                       | 参数说明                                                                                                                                                                                                         |
|:-------------------------|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CURVE25519_SHA256        | curve25519-sha256密钥交换算法                    | 可选必选说明：可选参数 参数含义：本参数用于指定curve25519-sha256密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启curve25519-sha256密钥交换算法 false:关闭curve25519-sha256密钥交换算法。 默认值：无 配置原则：无                                                          |
| CURVE25519_SHA256_LIBSSH | curve25519-sha256@libssh.org密钥交换算法         | 可选必选说明：可选参数 参数含义：本参数用于指定curve25519-sha256@libssh.org密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启curve25519-sha256@libssh.org密钥交换算法 false:关闭curve25519-sha256@libssh.org密钥交换算法。 默认值：无 配置原则：无                         |
| DH_GROUP_EXCHANGE_SHA256 | diffie-hellman-group-exchange-sha256密钥交换算法 | 可选必选说明：可选参数 参数含义：本参数用于指定diffie-hellman-group-exchange-sha256密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启diffie-hellman-group-exchange-sha256密钥交换算法 false:关闭diffie-hellman-group-exchange-sha256密钥交换算法。 默认值：无 配置原则：无 |
| ECDH_SHA2_NISTP256       | ecdh-sha2-nistp256密钥交换算法                   | 可选必选说明：可选参数 参数含义：本参数用于指定ecdh-sha2-nistp256密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启ecdh-sha2-nistp256密钥交换算法 false:关闭ecdh-sha2-nistp256密钥交换算法。 默认值：无 配置原则：无                                                       |
| ECDH_SHA2_NISTP384       | ecdh-sha2-nistp384密钥交换算法                   | 可选必选说明：可选参数 参数含义：本参数用于指定ecdh-sha2-nistp384密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启ecdh-sha2-nistp384密钥交换算法 false:关闭ecdh-sha2-nistp384密钥交换算法。 默认值：无 配置原则：无                                                       |
| ECDH_SHA2_NISTP521       | ecdh-sha2-nistp521密钥交换算法                   | 可选必选说明：可选参数 参数含义：本参数用于指定ecdh-sha2-nistp521密钥交换算法的开启或者关闭。 数据来源：本端规划 取值范围：true:开启ecdh-sha2-nistp521密钥交换算法 false:关闭ecdh-sha2-nistp521密钥交换算法。 默认值：无 配置原则：无                                                       |

#### 使用实例

设置数据同步客户端支持的密钥交换算法，开启CURVE25519\_SHA256、CURVE25519\_SHA256\_LIBSSH、DH\_GROUP\_EXCHANGE\_SHA256、ECDH\_SHA2\_NISTP256、ECDH\_SHA2\_NISTP384、ECDH\_SHA2\_NISTP521密钥交换算法：

```
SET RDATACLIENTKEXALGOS: CURVE25519_SHA256=TRUE, CURVE25519_SHA256_LIBSSH=TRUE, DH_GROUP_EXCHANGE_SHA256= TRUE, ECDH_SHA2_NISTP256=TRUE, ECDH_SHA2_NISTP384=TRUE, ECDH_SHA2_NISTP521= TRUE;
```