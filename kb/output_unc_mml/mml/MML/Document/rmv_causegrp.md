# 删除原因值映射组配置(RMV CAUSEGRP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

此命令用于删除一个原因值映射组配置记录。

#### 注意事项

- 此命令执行后立即生效。
- 当删除一个原因值映射组时，一定确保在GMMPROCTRL、PMMPROCTRL、EMMPROCTRL、EMMPROCTRLIMSI、GBSMPROCTRL、IUSMPROCTRL、S1SMPROCTRL和CAUSEMAP命令中无引用该ID记录，否则执行删除时系统提示CAUSEGRPID已被某个协议参数值使用，然后中断删除操作。建议通过查询命令确认在哪里使用CAUSEGRPID并删除那一条记录，再执行此删除命令。
- 当软参“BYTE\_EX\_B86”BIT5、“BYTE\_EX\_B86”BIT6、“BYTE\_EX\_B86”BIT7、“BYTE\_EX\_B86”BIT8、“BYTE\_EX\_B87”BIT1、“BYTE\_EX\_B87”BIT2中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                          |
|:-----------|:-------|:----------------------------------------------|
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数 参数含义：待删除的原因值组标识。 取值范围：1～127 默认值：无 |

#### 使用实例

当CAUSEGRPID值为126的原因值组标识未被任何协议使用时，删除CAUSEGRPID（原因值组标识）为126的原因值映射组记录：

RMV CAUSEGRP: CAUSEGRPID=126;