# 显示Gresm资源信息（DSP GRESMRESINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示本设备上APP使用的Gresm资源信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                    |
|:----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------|
| APPPID    | APP ID | 可选必选说明：必选参数 参数含义：该参数用于表示APP ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                      |
| RESTYPE   | 资源类型   | 可选必选说明：必选参数 参数含义：该参数用于表示资源类型包括label、iid。 数据来源：本端规划 取值范围：枚举类型。 label：标签。iid：直连ID。DPOOL：资源池。SLABEL：静态标签。BLABEL：块标签。 默认值：无                 |
| RESSTATUS | 资源状态   | 可选必选说明：必选参数 参数含义：该参数用于表示资源状态包括normal、once-error、twice-error。 数据来源：本端规划 取值范围：枚举类型。 normal：Normal。once-error：一次错误。twice-error：两次错误。 默认值：无 |

#### 使用实例

显示指定的APP资源使用信息：

```
DSP GRESMRESINFO:APPPID="6F4655", RESTYPE=iid, RESSTATUS=normal;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
APP ID      资源类型    资源状态    资源ID

0x6f4655    直连ID      Normal      7
0x6f4655    直连ID      Normal      92
0x6f4655    直连ID      Normal      91
0x6f4655    直连ID      Normal      90
0x6f4655    直连ID      Normal      89
0x6f4655    直连ID      Normal      88
0x6f4655    直连ID      Normal      87
0x6f4655    直连ID      Normal      86
0x6f4655    直连ID      Normal      85
0x6f4655    直连ID      Normal      84
0x6f4655    直连ID      Normal      45
0x6f4655    直连ID      Normal      43
0x6f4655    直连ID      Normal      12
0x6f4655    直连ID      Normal      11
0x6f4655    直连ID      Normal      10
0x6f4655    直连ID      Normal      9
0x6f4655    直连ID      Normal      8
(结果个数 = 17)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                    |
|:--------|:-----------------------------------------|
| APP ID  | 用于表示APP ID。                              |
| 资源类型    | 用于表示资源类型包括label、iid。                     |
| 资源状态    | 用于表示资源状态包括normal、once-error、twice-error。 |
| 资源ID    | 用于表示资源ID。                                |