# 查询多Serving Plmn增强功能（LST MULTISRVPLMNEN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询多Serving Plmn增强功能参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询多Serving Plmn增强功能参数，执行如下命令：

```
%%LST MULTISRVPLMNEN;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
 支持多Serving Plmn功能增强  =  支持
     移动性流程增强处理策略  =  支持
         AMF设备信息通知SMF  =  支持
           AMF设备GUAMI索引  =  256
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称               | 输出项解释                                                                                                                                     |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| 支持多Serving Plmn功能增强 | 该参数用于控制AMF是否支持对AMF内Serving Plmn改变的移动性管理流程增强处理。                                                                                            |
| 移动性流程增强处理策略         | 该参数用于控制对AMF内部Serving Plmn改变的移动性管理流程的处理策略。 当参数取值“拒绝”时，注册流程拒绝原因值受SET NGMMPROCTRL命令SRVPLMNCHGREG参数控制。                                        |
| AMF设备信息通知SMF        | 该参数用于控制在AMF内Serving Plmn改变的移动性管理流程中，AMF在向SMF发送的Nsmf_PDUSession_UpdateSMContext Request消息中是否携带AMF设备信息（包括servingNfId、guami、servingNetwork）。 |
| AMF设备GUAMI索引        | 该参数用于控制AMF在向UDM发送Nudm_UECM_RegistrationAMF3GppAccess Request消息时，通过该参数指定的GUAMI填充guami信元。如果不指定GUAMI索引，默认使用用户所在Serving PLMN对应的GUAMI。         |