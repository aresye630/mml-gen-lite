# 查询ACS与APP数据差异信息(DSP ACSAPPDATADIFF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询ACS与其他微服务侧差异数据信息。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                               |
|:------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| INFOLEVEL   | 信息级别   | 可选必选说明：必选参数 参数含义：用于指定查询差异数据的信息级别。 取值范围：枚举类型。 Service(服务)：服务级差异。Instance(实例)：实例级差异。Table(表)：表级差异。 默认值：无。 配置原则：无。                                    |
| SERVICENAME | 服务名称   | 可选必选说明：当参数“信息级别(INFOLEVEL)”选择“Instance(实例)”或“Table(表)”时，该参数为必选参数。 参数含义：查询差异数据的微服务名称，可以使用DSP ACSSYNCINFO查询获得该参数。 取值范围：长度范围1~255的字符串。 默认值：无。 配置原则：无。 |
| INSTANCEID  | 实例ID   | 可选必选说明：当参数“信息级别(INFOLEVEL)”选择“Table(表)”时，该参数为必选参数。 参数含义：查询差异数据的微服务实例ID，可以使用DSP ACSSYNCINFO查询获得该参数。 取值范围：长度范围1~255的字符串。 默认值：无。 配置原则：无。              |
| TABLENAME   | 表名称    | 可选必选说明：可选参数。 参数含义：查询差异数据的表名称。 取值范围：长度范围1~16的字符串。 默认值：无。 配置原则：无。                                                                                    |

## 使用实例

- 查询“信息级别”为“Service”的差异信息：

```
DSP ACSAPPDATADIFF: INFOLEVEL=Service;
```

```
%%DSP ACSAPPDATADIFF: INFOLEVEL=Service;%%
RETCODE = 0  操作成功

操作结果如下
------------
服务名称         检查结果    

TestGoServerNOS  配置不一致  
TestforGoCM      检查失败    
(结果个数 = 2)

---    END
```

- 查询“信息级别”为“Instance”，“服务名称”为“TestGoServerNOS”的差异信息：

```
DSP ACSAPPDATADIFF: INFOLEVEL=Instance, SERVICENAME="TestGoServerNOS";
```

```
%%DSP ACSAPPDATADIFF: INFOLEVEL=Instance, SERVICENAME="TestGoServerNOS";%%
RETCODE = 0  操作成功

操作结果如下
------------
服务名称  =  TestGoServerNOS
  实例ID  =  goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType
检查结果  =  配置不一致
(结果个数 = 1)

---    END
```

- 查询“信息级别”为“Table”，“服务名称”为“TestGoServerNOS”，“实例ID”为“goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233\_\_cType”的差异信息：

```
DSP ACSAPPDATADIFF: INFOLEVEL=Table, SERVICENAME="TestGoServerNOS", INSTANCEID="goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType";
```

```
%%DSP ACSAPPDATADIFF: INFOLEVEL=Table, SERVICENAME="TestGoServerNOS", INSTANCEID="goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType";%%
RETCODE = 0  操作成功

操作结果如下
------------
服务名称         实例ID                                                 表名称        检查结果    

TestGoServerNOS  goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType  TsdkLabel1    配置不一致  
TestGoServerNOS  goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType  TsdkforSPS10  配置不一致  
TestGoServerNOS  goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType  TsdkforSPS6   配置不一致  
TestGoServerNOS  goservernos-10-pod-676bcfcb7-pdwrn172-16-0-233__cType  TsdkforSPS9   配置不一致  
(结果个数 = 4)

---    END
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如下表所示。

| 输出项名称   | 输出项解释                                                                                         |
|:--------|:----------------------------------------------------------------------------------------------|
| 服务名称    | 微服务名称。                                                                                        |
| 实例ID    | 微服务实例ID。                                                                                      |
| 表名称     | 配置表名称。                                                                                        |
| 检查结果    | 微服务的数据检查结果状态，有如下2种状态： 配置不一致。表示ACS服务和业务微服务配置数据不一致。检查失败。表示ACS服务和业务微服务进行配置检查时，由于系统内部原因，未能进行检查操作。 |

## 参考信息

无。