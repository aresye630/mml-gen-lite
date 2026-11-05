# 显示LDP的Listen Socket信息（DSP LDPSSMGLSSOCK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示LDP的Listen Socket信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                            |
|:--------|:-----------|:--------------------------------------------------------------------------------|
| VRFNAME | VPN实例名称    | 可选必选说明：可选参数 参数含义：该参数用于表示VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ |
| PEERID  | 对等体的LSR ID | 可选必选说明：可选参数 参数含义：该参数用于表示对等体的LSR ID。 数据来源：对端协商 取值范围：IPv4地址类型。 默认值：无              |

#### 使用实例

显示LDP的Listen Socket信息：

```
DSP LDPSSMGLSSOCK:VRFNAME="_public_";
```

```
RETCODE = 0  操作成功。

结果如下
--------
            VPN实例名称  =  _public_
         对等体的LSR ID  =  10.10.10.10
  LDP分配给Socket的编号  =  12
  Socket分配给LDP的编号  =  12
    LDP TCP连接的源地址  =  10.10.10.3
  LDP TCP连接的目的地址  =  10.10.10.10
   TCP Socket创建的状态  =  Socket创建成功
           KeyChain状态  =  未设置Socket选项
                MD5状态  =  未设置Socket选项
               GTSM状态  =  未设置Socket选项
       Socket的备份状态  =  空闲状态
       Socket的备份类型  =  备份类型无效
       Socket备份版本号  =  0
LDP分布式整数形式的编号  =  0
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称           | 输出项解释                                                                                                                                      |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| VPN实例名称         | 用于表示VPN实例名称。                                                                                                                               |
| 对等体的LSR ID      | 用于表示对等体的LSR ID。                                                                                                                            |
| LDP分配给Socket的编号 | 用于表示LDP分配给Socket的编号。                                                                                                                       |
| Socket分配给LDP的编号 | 用于表示Socket分配给LDP的编号。                                                                                                                       |
| LDP TCP连接的源地址   | 用于表示LDP TCP连接的源地址。                                                                                                                         |
| LDP TCP连接的目的地址  | 用于表示LDP TCP连接的目的地址。                                                                                                                        |
| TCP Socket创建的状态 | 该参数用于表示TCP Socket创建的状态，包括： 空闲状态。创建Socket。Socket已回复了创建。打开Socket的发送消息的管道。已收到发送消息管道打开的回复。备份Socket的创建到备组件。Socket创建成功。备份Socket的删除到备组件。删除Socket。 |
| KeyChain状态      | 该参数用于表示KeyChain状态，包括： 未设置Socket选项。创建设置Socket选项。正在设置Socket选项。设置Socket选项成功。清除设置的Socket选项。                                                    |
| MD5状态           | 该参数用于表示MD5状态，包括： 未设置Socket选项。创建设置Socket选项。正在设置Socket选项。设置Socket选项成功。清除设置的Socket选项。                                                         |
| GTSM状态          | 该参数用于表示GTSM状态，包括： 未设置Socket选项。创建设置Socket选项。正在设置Socket选项。设置Socket选项成功。清除设置的Socket选项。                                                        |
| Socket的备份状态     | 该参数用于表示Socket的备份状态标识，包括： 空闲状态。备组件创建Socket。备组件Socket创建成功。备组件关闭Socket。备组件删除Socket。备组件打开Socket的发送消息的管道。                                       |
| Socket的备份类型     | 该参数用于表示Socket的备份类型标识，包括： 备份类型无效。通过批量备份将Socket备份到备组件。通过实时备份将Socket备份到备组件。                                                                   |
| Socket备份版本号     | 用于表示Socket备份版本号。                                                                                                                           |
| LDP分布式整数形式的编号   | 用于表示LDP分布式整数形式的编号。                                                                                                                         |