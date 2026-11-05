# 查询字段映射关系（LST CDRFIELDTYPE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NCG**

该命令用于查询字段映射关系。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                               |
|:----------|:-------|:-------------------------------------------------------------------------------------------------------------------|
| FIELDNAME | 字段名称   | 可选必选说明：可选参数  参数含义：该参数用于指定字段名称。  数据来源：本端规划 取值范围： RATTYPE（RAT类型）SSCMODE（SSC模式）PDUSESSIONTYPE（PDU会话类型）  默认值：无  配置原则：无 |

## 使用实例

查询字段映射关系：

```
%%LST CDRFIELDTYPE:;%%
RETCODE = 0  操作成功

结果如下
--------
字段名称     RAT类型名称                                 SSC类型名称  PDU类型名称   类型取值  

RAT类型      New Radio                                   SSCMode 1    IPv4          51        
RAT类型      Evolved Universal Terrestrial Radio Access  SSCMode 1    IPv4          6         
RAT类型      Wireless LAN                                SSCMode 1    IPv4          3         
RAT类型      Virtual                                     SSCMode 1    IPv4          7         
RAT类型      GERA                                        SSCMode 1    IPv4          2         
RAT类型      NB IoT                                      SSCMode 1    IPv4          8         
RAT类型      LTE-M                                       SSCMode 1    IPv4          9         
RAT类型      UTRA                                        SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 2    IPv4          2         
SSC模式      New Radio                                   SSCMode 3    IPv4          3         
PDU会话类型  New Radio                                   SSCMode 1    IPv4          1         
PDU会话类型  New Radio                                   SSCMode 1    IPv6          2         
PDU会话类型  New Radio                                   SSCMode 1    IPv4v6        0         
PDU会话类型  New Radio                                   SSCMode 1    Unstructured  3         
PDU会话类型  New Radio                                   SSCMode 1    Ethernet      4         
PDU会话类型  New Radio                                   SSCMode 1    Non-IP        50
RAT类型      NR_REDCAP                                   SSCMode 1    IPv4          58
(结果个数 = 18)
```

## 输出结果说明

| 输出项名称   | 输出项解释           |
|:--------|:----------------|
| 字段名称    | 该参数用于指定字段名称。    |
| RAT类型名称 | 该参数用于指定RAT类型名称。 |
| SSC类型名称 | 该参数用于指定SSC类型名称。 |
| PDU类型名称 | 该参数用于指定PDU类型名称。 |
| 类型取值    | 该参数用于指定类型取值。    |