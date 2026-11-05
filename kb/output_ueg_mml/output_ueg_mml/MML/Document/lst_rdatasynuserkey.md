# 查询远端用户数据同步用户密钥文件（LST RDATASYNUSERKEY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询远端用户数据同步服务器用户已加载密钥文件。

#### 注意事项

当查询结果中“密钥状态”显示不是“正常”时，说明密钥文件当前无法正常工作，可能由于文件损坏、格式不支持、私钥文件解密失败等各种可能可能原因，请检查相关文件确认密钥文件可用。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                             |
|:-----------|:-------|:-------------------------------------------------------------------------------------------------|
| SERVERNAME | 服务器名称  | 可选必选说明：可选参数 参数含义：远端用户数据同步服务器名称。 数据来源：本端规划 取值范围：与LST RdataSynServer中的servername保持一致。 默认值：无 配置原则：无 |
| USERNAME   | 用户名称   | 可选必选说明：可选参数 参数含义：用于指定SFTP用户名。 数据来源：对端协商 取值范围：与远端SFTP服务器的用户名保持一致。 默认值：无 配置原则：无                    |
| KEYNAME    | 密钥名称   | 可选必选说明：可选参数 参数含义：用于创建用户加载密钥的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～128。 默认值：无 配置原则：无                  |

#### 使用实例

- 查询远端用户数据同步用户全部已加载密钥文件：

  ```
  LST RDATASYNUSERKEY:;
  ```
- 查询远端用户数据同步用户密钥文件，服务器名称为rdata1，用户名为abc，密钥名称key1密钥文件：

  ```
  LST RDATASYNUSERKEY: SERVERNAME = "sftpserver_ipv41", USERNAME ="shi5";
  ```

  ```
   KEYNAME = "key1";
  RETCODE = 0  操作成功

  远端用户数据同步用户全部已加载密钥文件
  --------------------------------------
  服务器名称  =  sftpserver_ipv41
    用户名称  =  shi5
    密钥名称  =  key1
  公钥文件名  =  rsa_key.pub
  私钥文件名  =  rsa_key
    密钥状态  =  正常
      公钥值  =  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDBvUKOlOgwccJWvFJJA8W81wK27FN+05ZgYIS3dfDOH5djJdq69VJHbdYaaEDY5P42eVEd3KbzOhGa2A+UzHinzV03ncaEq8KUf6ftr111uc7POoeeXMO4fe0WVzKUho7/kGxwZo+vJbs3PCwkv49f9tehSKT6gmJMwTRVLOJ93Pfs1uQxsrixwj9J8bqZ2fA8xnFZTpJhQrc0TOJd+4dhTnWhmHdwDBBpAPII+cHN5Gzy6KgLSSZFUvgKnu3/tHS2Lzi6r6Pc1IN6qyYc1yn+id2RXgFi0cZaGqP5J9F6DU4rcbtgVFpi3CFm9bEMISeaabkdqLHVVW9BfshBUraDhGK3/w2N9Y6UwY/jDidzC4O7t2EYUIQTDJALzKErKF3HIMMPdm2VkHxbf0El0RZL+3TLC4ENXvrvakZ6j0AjDs2gDnpeRU0wkfKIjYrHUQ0iGk5Qkhx+1RtAyQiV881txKr8jGeLsm7vSMiH0VFKl9B2eKTWkdiguaOUBofhnzs= root@localhost.localdomain
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释          |
|:--------|:---------------|
| 服务器名称   | 远端用户数据同步服务器名称。 |
| 用户名称    | 用于指定SFTP用户名。   |
| 密钥名称    | 用于创建用户加载密钥的名称。 |
| 公钥文件名   | 用于指定待加载公钥文件名。  |
| 私钥文件名   | 用于指定待加载私钥文件名。  |
| 密钥状态    | 用于显示密钥状态。      |
| 公钥值     | 公钥值。           |