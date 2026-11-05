# 查询内容分类组绑定关系（LST CONTCATEGBIND）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询内容分类组绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                     |
|:--------------|:---------|:-------------------------------------------------------------------------------------------------------------------------|
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：可选参数 参数含义：该参数用于设置内容过滤策略名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD CFPROFILE命令配置生成。    |
| CONTCATEGNAME | 内容分类组名称  | 可选必选说明：可选参数 参数含义：该参数用于设置内容分类组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD CONTCATEGROUP命令配置生成。 |

#### 使用实例

查询所有的内容分类组绑定关系：

```
LST CONTCATEGBIND:;
```

```
RETCODE = 0  操作成功

内容分类组绑定关系信息
----------------------
内容过滤策略名称  内容分类组名称        动作    缺省重定向名称  TimeRange名称  配置域名称  

cf_profile1       cf_contcategrprange1  丢弃    NULL            NULL           NULL        
cf_profile2       cf_contcategrprange2  转发    NULL            NULL           NULL        
cf_profile3       cf_contcategrprange3  重定向  cf_redirect1    NULL           NULL        
cf_profile4       cf_contcategrprange4  丢弃    NULL            NULL           NULL        
cf_profile5       cf_contcategrprange5  丢弃    NULL            NULL           NULL        
(结果个数 = 5)

---    END
```

#### 输出结果说明

参见ADD CONTCATEGBIND的参数说明。