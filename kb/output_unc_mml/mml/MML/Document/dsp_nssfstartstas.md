# 显示NSSF开工状态（DSP NSSFSTARTSTAS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NSSF**

查询NSSF微服务的开工状态。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询所有NSSF微服务的开工状态：

```
%%DSP NSSFSTARTSTAS:;%%
RETCODE = 0  执行成功

结果如下
------------------------
微服务类型         功能实体名称                                            开工状态        

NSSF               nssf/cellcore/cell-service-NssfExecSvc                  状态正常 
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet2   状态正常  
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet3   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet4   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet5   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet0   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet1   状态正常
NSSF               ctrl/cellcore/cell-service-NssfCtrlSvc                  状态正常
(结果个数 = 8)
```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                                             |
|:--------|:------------------------------------------------------------------------------------------------------------------|
| 微服务类型   | 该参数表示微服务类型。 取值说明： NSSF（NSSF）                                                                                      |
| 功能实体名称  | 该参数表示对应微服务的功能实体名称。                                                                                                |
| 开工状态    | 该参数表示对应微服务功能实体的开工状态。开工状态完全正常经历三个阶段分别为阶段一、阶段二、阶段三，阶段三完成后开工状态为正常状态。 取值说明： OK（状态正常）STAGE1（阶段一）STAGE2（阶段二）STAGE3（阶段三） |