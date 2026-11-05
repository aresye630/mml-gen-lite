# 查询全局IMS互通配置信息（LST CPGLOBALIMS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用于查询全局IMS配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

显示全局IMS配置：

```
%%LST CPGLOBALIMS:;%%
RETCODE = 0  操作成功

全局IMS配置信息
------------------------
                        IMS功能开关  =  使能
                IMS信令空口增强开关  =  使能
                  缺省IPv4 P-CSCF组  =  pcsf1
                  缺省IPv6 P-CSCF组  =  NULL
            发送更新消息速率(个/秒)  =  1000
          缺省IPv4 P-CSCF组域名开关  =  使能
          缺省IPv6 P-CSCF组域名开关  =  不使能
基于UDM的P-CSCF Restoration功能开关  =  不使能
基于UDM的P-CSCF Restoration功能模式  =  PDU会话重激活
基于HSS的P-CSCF Restoration功能开关  =  不使能
基于HSS的P-CSCF Restoration功能模式  =  PDU会话重激活
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                        | 输出项解释                                |
|:-----------------------------|:-------------------------------------|
| IMS功能开关                      | 该参数用于打开或关闭全局IMS功能开关。                 |
| IMS信令空口增强开关                  | 该参数用于设置IMS信令空口增强开关。                  |
| 缺省IPv4 P-CSCF组               | 该参数用于配置缺省IPv4类型的p-cscf组。             |
| 缺省IPv6 P-CSCF组               | 该参数用于配置缺省IPv6类型的p-cscf组。             |
| 发送更新消息速率(个/秒)                | 该参数用于指定整系统更新承载或会话时消息发送的最大速率。         |
| 缺省IPv4 P-CSCF组域名开关           | 该参数用于控制缺省IPv4 P-CSCF组域名是否为空。         |
| 缺省IPv6 P-CSCF组域名开关           | 该参数用于控制缺省IPv6 P-CSCF组域名是否为空。         |
| 基于UDM的P-CSCF Restoration功能开关 | 该参数用于指示基于UDM的P-CSCF Restoration功能开关。 |
| 基于UDM的P-CSCF Restoration功能模式 | 该参数用于指示基于UDM的P-CSCF Restoration功能模式。 |
| 基于HSS的P-CSCF Restoration功能开关 | 该参数用于指示基于HSS的P-CSCF Restoration功能开关。 |
| 基于HSS的P-CSCF Restoration功能模式 | 该参数用于指示基于HSS的P-CSCF Restoration功能模式。 |