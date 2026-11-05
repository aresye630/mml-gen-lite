# 查询OSPFv3链接状态数据库（DSP OSPFV3LSDB）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示OSPFv3的链路状态数据库LSDB信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称      | 参数说明                                                                     |
|:-------|:----------|:-------------------------------------------------------------------------|
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数 参数含义：OSPFv3进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 |

#### 使用实例

显示设备OSPFv3进程号为1的所有链路状态数据库信息：

```
DSP OSPFV3LSDB: PROCID=1;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
    OSPFv3进程号  =  1
  本地路由器标识  =  10.1.1.1
  Router-LSA数量  =  2
 Network-LSA数量  =  1
 Summary-LSA数量  =  0
    ASBR LSA数量  =  0
   类型7 LSA数量  =  0
     ASE-LSA数量  =  0
    Link LSA数量  =  2
   Grace LSA数量  =  0
     未知LSA数量  =  0
内部区域前缀计数  =  1
   RiLinkLSA总数  =  0
   RiAreaLSA总数  =  0
     RiASLSA总数  =  0
        总的数量  =  6
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释          |
|:--------------|:---------------|
| OSPFv3进程号     | OSPFv3进程号。     |
| 本地路由器标识       | 本地路由器标识。       |
| Router-LSA数量  | Router-LSA数量。  |
| Network-LSA数量 | Network-LSA数量。 |
| Summary-LSA数量 | Summary-LSA数量。 |
| ASBR LSA数量    | ASBR LSA数量。    |
| 类型7 LSA数量     | 类型7 LSA数量。     |
| ASE-LSA数量     | ASE-LSA数量。     |
| Link LSA数量    | Link LSA数量。    |
| Grace LSA数量   | Grace LSA数量。   |
| 未知LSA数量       | 未知LSA数量。       |
| 内部区域前缀计数      | 内部区域前缀计数。      |
| RiLinkLSA总数   | RiLinkLSA总数。   |
| RiAreaLSA总数   | RiAreaLSA总数。   |
| RiASLSA总数     | RiASLSA总数。     |
| 总的数量          | 总的数量。          |