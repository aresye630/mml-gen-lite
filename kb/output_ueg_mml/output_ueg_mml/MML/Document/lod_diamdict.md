# 加载Diameter字典（LOD DIAMDICT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

**须知** 

本命令属于高危命令，加载Diameter字典可能会导致UNC各Diameter应用对外接口呈现的变化，此时一般需要对端网元做同步的升级适配，否则可能造成业务异常。

该命令用于加载Diameter字典文件。

#### 注意事项

- 该命令执行后立即生效。
- 可以通过ADD DIAMDICTPATH/MOD DIAMDICTPATH命令设置字典加载路径，通过LST DIAMDICTPATH命令查询字典加载路径。
- 执行命令前请确保对应目录下保存了Diameter控制文件，如果控制文件不齐全会导致字典加载失败。
- 该命令执行后UNC需要一段时间检查及同步字典文件数据。请在命令执行成功10-20s后，使用DSP DIAMDICTSTAT命令查看UNC当前加载字典路径是否修改。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                            |
|:---------------|:-------|:--------------------------------------------------------------------------------|
| DICTFILESELECT | 字典文件选择 | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter字典类型。 数据来源：本端规划 取值范围：枚举类型。 ALL：全部。 默认值：无 配置原则：无 |

#### 使用实例

配置UNC的Gy应用使用用户定制的第一套Diameter字典文件：

```
MOD DIAMDICTPATH: APPLICATION=GY,DICTNO=1,DICTPATH=CUSTOM1;
LOD DIAMDICT:DICTFILESELECT=ALL;
```