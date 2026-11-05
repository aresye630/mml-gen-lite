# 查询AMF的SBI接口控制参数（LST AMFSBIINFCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF的SBI接口控制参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询AMF的SBI接口控制参数，执行如下命令：

```
%%LST AMFSBIINFCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                             Schema自适应开关  =  关闭
                 ModelD模式UDM Schema填充策略  =  HTTP优先
                 ModelD模式PCF Schema填充策略  =  HTTP优先
重定向使用FQDN构造3gpp-sbi-target-apiroot开关  =  打开
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                                | 输出项解释                                                                                                                                                                                                               |
|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schema自适应开关                          | 该参数用于控制AMF是否支持Schema自适应功能。                                                                                                                                                                                          |
| ModelD模式UDM Schema填充策略               | 该参数用于设置ModelD模式下AMF与UDM网元交互时Schema的填充策略。 ModelD模式下，AMF无法感知对端UDM支持的Schema类型，通过本参数可以灵活调整AMF与UDM网元交互时Schema的填充策略。 ModelD模式下，建议AMF与对端UDM的Schema策略均设置一致；若AMF与对端UDM的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与UDM通信。 |
| ModelD模式PCF Schema填充策略               | 该参数用于设置ModelD模式下AMF与PCF网元交互时Schema的填充策略。 ModelD模式下，AMF无法感知对端PCF支持的Schema类型，通过本参数可以灵活调整AMF与PCF网元交互时Schema的填充策略。 ModelD模式下，建议AMF与对端PCF的Schema策略均设置一致；若AMF与对端PCF的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与PCF通信。 |
| 重定向使用FQDN构造3gpp-sbi-target-apiroot开关 | 该参数用来控制AMF没有获取到对端AMF的IP地址时，AMF重定向请求中3gpp-sbi-target-apiroot是否使用FQDN构造。                                                                                                                                              |