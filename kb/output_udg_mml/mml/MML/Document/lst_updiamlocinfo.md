# 查询Diameter本端信息（LST UPDIAMLOCINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

此命令用来查询Diameter本端信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                 |
|:---------|:-------|:-------------------------------------------------------------------------------------|
| HOSTNAME | 本端主机名  | 可选必选说明：可选参数 参数含义：该参数用于指定本端主机名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格。 默认值：无 配置原则：无 |

#### 使用实例

查询HOSTNAME为“test”的Diameter本端信息：

```
LST UPDIAMLOCINFO: HOSTNAME="test";
```

```
RETCODE = 0  操作成功
Diameter本端主机信息
--------------------
                     本端主机名  =  test
                       本端域名  =  test
                       产品名称  =  product
                Vendor-Id AVP值  =  0
        Firmware-Revision AVP值  =  1
    Origin-State-Id AVP使能开关  =  不使能
Supported-Vendor-Id AVP使能开关  =  不使能
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见ADD UPDIAMLOCINFO的参数说明。