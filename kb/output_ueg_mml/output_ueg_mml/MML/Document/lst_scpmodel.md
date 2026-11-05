# 查询业务通信代理模型(LST SCPMODEL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询业务通信代理模型。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询所有业务通信代理模型。

```
LST SCPMODEL:;
```

```
%%LST SCPMODEL:;%%
RETCODE = 0  操作成功 

操作结果如下
------------
网元类型  模型    API前缀  API版本  开关     绑定级别  

CHF       MODELD  NULL     v1       非使能   NFSET    
BSF       MODELD  NULL     v1       非使能   NFSET
SMF       MODELD  NULL     v1       非使能   NFSET  
AMF       MODELD  NULL     v1       非使能   NFSET
VPCF      MODELD  NULL     v1       非使能   NOBINDINGLEVEL  
HPCF      MODELD  NULL     v1       非使能   NOBINDINGLEVEL 
AF        MODELD  NULL     v1       非使能   NFSET  
NWDAF     MODELD  NULL     v1       非使能   NFSET
(结果个数 = 8)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET SCPMODEL**。