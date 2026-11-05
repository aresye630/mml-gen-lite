# 查询DNAI粒度的UPF选择策略（LST DNAIUPSELPLY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询DNAI粒度的UPF选择策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                               |
|:-------|:---------|:---------------------------------------------------------------------------------------------------|
| DNAI   | 数据网络访问标识 | 可选必选说明：可选参数  参数含义：该参数用于指定数据网络访问标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。  默认值：无  配置原则：无 |

## 使用实例

查询DNAI为huawei.com的UPF选择策略：
2.查询所有DNAI粒度的UPF选择策略：

```
%%LST DNAIUPSELPLY: DNAI="huawei.com";%%
RETCODE = 0  Operation succeeded

The result is as follows
--------
                                  Data Network Access Identifier  =  huawei.com
Shared UPF Preferential Selection Switch in Traffic Distribution  =  INHERIT
                             Priority-based UPF Selection Switch  =  INHERIT
                                 Load-based UPF Selection Switch  =  INHERIT
(Number of results = 1)

---    END
```

## 输出结果说明

| 输出项名称          | 输出项解释                                                      |
|:---------------|:-----------------------------------------------------------|
| 数据网络访问标识       | 该参数用于指定数据网络访问标识。                                           |
| 分流场景下共享UPF优选开关 | 该参数用于该DNAI下SMF在分流场景下是否优选共享UPF。该优选策略属于合一优先选择，生效顺位与合一优先选择相同。 |
| 基于优先级优选UPF开关   | 该参数用于指示该DNAI下SMF基于优先级选择UPF的功能是否开启。                         |
| 基于负载优选UPF开关    | 该参数用于指示该DNAI下SMF是否打开基于UPF负载信息进行UPF优选的功能。                   |