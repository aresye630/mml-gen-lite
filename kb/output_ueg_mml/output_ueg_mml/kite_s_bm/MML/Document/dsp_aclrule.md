# 查询ACL规则配置（DSP ACLRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查看黑白名单规则配置信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                              |
|:--------|:-------|:------------------------------------------------------------------------------------------------------------------|
| APPNAME | 应用名称   | 可选必选说明：必选参数 参数含义：指定Application名称，可以通过DSP APPLICATIONINFO查出所有的应用名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |
| MEPID   | MEP ID | 可选必选说明：可选参数 参数含义：指定MEP ID，可以通过DSP APPLICATIONINFO查出所有的MEP ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无      |

#### 使用实例

查询指定应用名称的ACL Rule配置的详细信息，app名称为"app2"：

```
DSP ACLRULE: APPNAME="appName02";
```

```
RETCODE = 0 操作成功

ACL规则配置
----------------------
MEP ID  Application Name  ACL Type  UE Tag  UE ID Type  UE ID Value     

NULL    appName02         BLACK     UeTag1  SUPI        46001012377777       
NULL    appName02         BLACK     UeTag2  GPSI        15858586969666  
(结果个数 = 2)

---    END
```

#### 输出结果说明

| 输出项名称            | 输出项解释           |
|:-----------------|:----------------|
| Application Name | 应用名称。           |
| APP Instance ID  | 实例号。            |
| ACL Type         | 黑白名单种类。         |
| UE ID Type       | 该参数用于指定UE ID类型。 |
| UE Tag           | 指定UE的标签。        |
| UE ID Value      | 该参数用于指定UE ID值。  |