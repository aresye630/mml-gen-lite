# 查询UP节点定制信元兼容性配置（LST UPCMPTCUSIE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询UP节点定制信元兼容性配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                          |
|:------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| UPFINSTANCE | UPF实例名称 | 可选必选说明：可选参数  参数含义：该参数用于指定UPF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~36。不区分大小写。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IENAME      | 定制信元名称  | 可选必选说明：可选参数  参数含义：该参数用于指定需要定制的信元名称。  数据来源：全网规划 取值范围： EFSEID（扩展F-SEID）PUSERID（私有UserID）  默认值：无  配置原则：无                                         |

## 使用实例

查询UPF实例标识为upf\_instance\_1的Extend F-SEID信元相关配置，执行如下命令：
LST UPCMPTCUSIE:UPFINSTANCE="upf\_instance\_1",IENAME=EFSEID;
2.查询UPF实例标识为upf\_instance\_1的定制信元相关配置，执行如下命令：
LST UPCMPTCUSIE:UPFINSTANCE="upf\_instance\_1";
3.查询所有定制信元相关配置，执行如下命令：
LST UPCMPTCUSIE:;

```
%%LST UPCMPTCUSIE: UPFINSTANCE="upf_instance_1", IENAME=EFSEID;%%
RETCODE = 0  操作成功

结果如下
------------------------
   UPF实例名称  =  upf_instance_1
 定制信元名称   =  Extend F-SEID
定制信元类型值  =  37101
定制信元企业ID  =  2011
(结果个数 = 1)

---    END
2. 
%%LST UPCMPTCUSIE: UPFINSTANCE="upf_instance_1";%%
RETCODE = 0  操作成功

结果如下
------------------------
UPF实例名称        定制信元名称      定制信元类型值  定制信元企业ID  

upf_instance_1     Extend F-SEID     37101           2011                                
upf_instance_1     Private UserID    37001           2000                                
(结果个数 = 2)

---    END

3.
%%LST UPCMPTCUSIE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
UPF实例名称        定制信元名称      定制信元类型值  定制信元企业ID  

upf_instance_1     Extend F-SEID     37101           2011                                
upf_instance_1     Private UserID    37001           2000                                
upf_instance_2     Extend F-SEID     37101           2011                                
upf_instance_2     Private UserID    37102           2011                                
(结果个数 = 4)
---    END
```

## 输出结果说明

| 输出项名称    | 输出项解释             |
|:---------|:------------------|
| UPF实例名称  | 该参数用于指定UPF实例名称。   |
| 定制信元名称   | 该参数用于指定需要定制的信元名称。 |
| 定制信元类型值  | 该参数用于设置定制信元的类型值。  |
| 定制信元企业ID | 该参数用于设置定制信元的企业ID。 |