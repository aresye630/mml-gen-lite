# 查询HTTP服务存储的接口DSCP信息（LST HTTPINTFDSCP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用来查看逻辑接口对外发送IP包时携带的DSCP值。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

若查看逻辑接口对外发送IP包时携带的DSCP值，则可以使用如下命令：

```
%%LST HTTPINTFDSCP:;%%
RETCODE = 0  操作成功

结果如下
--------
NF类型      DSCP值  

NFTypeNRF   46      
NFTypeAMF   46      
NFTypeSMF   46      
NFTypeSMSF  46      
NFTypeNSSF  46      
NFTypeCHF   46      
(结果个数 = 6)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                 |
|:--------|:----------------------|
| NF类型    | 该参数用于指定逻辑接口DSCP的NF类型。 |
| DSCP值   | 该参数用于指定设置的DSCP值。      |