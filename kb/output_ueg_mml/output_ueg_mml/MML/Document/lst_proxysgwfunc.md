# 查询Proxy SGW功能参数（LST PROXYSGWFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C**

该命令用于查询Proxy S-GW特性的功能参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询Proxy S-GW特性的功能参数：

```
%%LST PROXYSGWFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           查询类型  =  IMSI优先
           控制类型  =  拒绝
           解析方式  =  本地配置优先
       是否允许4切2  =  使能
    透传NSA流量开关  =  使能
透传5GSIWKI标志开关  =  使能
 透传5GCNRI标志开关  =  使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称         | 输出项解释                                                                   |
|:--------------|:------------------------------------------------------------------------|
| 查询类型          | 该参数用于控制Proxy SGW特性中根据本地配置查找归属地PGW地址时的查询类型。                              |
| 控制类型          | 该参数用于控制Proxy SGW特性接入列表功能中IMSI和MSISDN同时匹配时是否允许接入。                        |
| 解析方式          | 该参数用于控制Proxy SGW获取归属地PGW地址的方式。                                          |
| 是否允许4切2       | 该参数用于控制UNC作为Proxy SGW-C时，是否允许用户从4G切换到2G。                                |
| 透传NSA流量开关     | 该参数用于控制UNC作为Proxy SGW-C时，是否允许透传Secondary RAT Usage Data Report信元给PGW-C。 |
| 透传5GSIWKI标志开关 | 该参数用于控制作为Proxy SGW-C时，是否允许透传5GS Interworking Indication标志给PGW-C。        |
| 透传5GCNRI标志开关  | 该参数用于控制作为Proxy SGW-C时，是否允许透传5GC Not Restricted Indication标志给PGW-C。      |