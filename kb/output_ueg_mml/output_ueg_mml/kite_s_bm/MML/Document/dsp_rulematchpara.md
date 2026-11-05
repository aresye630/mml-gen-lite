# 显示规则匹配报文信息构造状态（DSP RULEMATCHPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于显示规则匹配报文信息构造状态。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                     |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------|
| PACKETSOURCE | 报文信息来源 | 可选必选说明：可选参数 参数含义：规则匹配时选择的报文信息来源。 数据来源：本端规划 取值范围： USER_DEFINED：表示选择规则匹配时使用的报文信息为自定义。 默认值：无 配置原则：指定报文信息来源。 |

#### 使用实例

显示规则匹配报文信息构造状态：

```
DSP RULEMATCHPARA: PACKETSOURCE=USER_DEFINED;
```

```
RETCODE = 0  Operation succeeded

The Status Of Packet Information Construction Required For Rule Matching
------------------------------------------------------------------------
                       Source of The Packet Information  =  user defined
Status Of Rule Matching Packet Information Construction  =  done
(Number of results = 1)

---    END
```

#### 输出结果说明

| 输出项名称        | 输出项解释           |
|:-------------|:----------------|
| 报文信息来源       | 规则匹配时选择的报文信息来源。 |
| 规则匹配报文信息构造状态 | 表示规则匹配报文信息构造状态。 |