# 查询设备所支持的NETCONF协议能力集（DSP NCSCAPABILITY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询设备所支持的NETCONF协议能力集。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

查询设备所支持的NETCONF协议能力集：

```
DSP NCSCAPABILITY:SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
能力集名称           能力集类型  能力集版本

Base                  public      1.0    
Base                  private     2.0    
Writable-Running      public      1.0    
Candidate             public      1.0    
Confirmed Commit      public      1.0    
Distinct Startup      public      1.0    
Rollback on Error     public      1.0    
Sync                  private     1.0    
Sync                  private     1.1    
Sync                  private     1.2    
Sync                  private     1.3    
Exchange              private     1.0    
Exchange              private     1.1    
Active                private     1.0    
Action                private     1.0    
Action                private     2.0    
Discard Commit        private     1.0    
Execute CLI           private     1.0    
Update                private     1.0    
Commit-Description    private     1.0    
Notification          public      1.0    
Interleave            public      1.0    
Notification          private     2.0    
Sync-config           private     1.0    
(结果个数 = 24)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 能力集名称   | 用于指定能力名称。 |
| 能力集类型   | 用于指定能力类型。 |
| 能力集版本   | 用于指定能力版本。 |