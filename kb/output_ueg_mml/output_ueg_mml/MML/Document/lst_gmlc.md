# 查询GMLC配置(LST GMLC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

此命令用于查询GMLC配置。

#### 注意事项

- 此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称    | 参数说明                                                  |
|:-------|:--------|:------------------------------------------------------|
| GMLCID | GMLC 标识 | 可选必选说明：可选参数 参数含义：该参数用于指定要查询的GMLC标识。 取值范围：0～639 默认值 ：无 |

#### 使用实例

查询GMLC参数设置：

LST GMLC:;

```
%%LST GMLC:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 GMLC 标识  GMLC IP地址类型  GMLC IP地址  GMLC 号码        GMLC 主机名                                GMLC所属MCC  GMLC所属MNC    接口类型      支持定位信息

 1          IPv4             10.10.10.15  861390123456789  example.com                                 123          01             Lg            E-UTRAN Cell Identifier & Cell Portion ID & Civic Address & Barometric Pressure & Velocity Estimate & Additional Positioning Data
 2          IPv4             10.10.10.16  861390123456780  example.com                                123          01             SLg           E-UTRAN Cell Identifier & Cell Portion ID & Civic Address & Barometric Pressure & Velocity Estimate & Additional Positioning Data
(结果个数 = 2)
---    END
```

#### 输出结果说明

参见**ADD GMLC**的参数说明。