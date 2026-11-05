# 查询SA指纹识别协议（LST SUPPFINGERIDEN）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于显示系统支持的SA指纹识别功能的协议。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示系统支持的所有SA指纹识别功能的协议：

```
LST SUPPFINGERIDEN:;
```

```
RETCODE = 0  操作成功。

支持SA指纹识别协议信息
----------------------
应用子协议名称            应用协议名称

a000dn_data               a000dn       
dolphintunnel             dolphintunnel
facebook_http_video       facebook     
facebook_messenger_im     facebook     
facebook_nonhttp_video    facebook     
facebook_others           facebook     
tor                       tor          
(结果个数 = 7)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                   |
|:--------|:------------------------|
| 应用子协议名称 | 用于显示支持SA指纹识别功能的应用子协议名称。 |
| 应用协议名称  | 用于显示支持SA指纹识别功能的应用协议名称。  |