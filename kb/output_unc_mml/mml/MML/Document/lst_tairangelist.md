# 查询NF TAI区域信息（LST TAIRANGELIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG、CBC、CBCF**

该命令用于查询NF实例支持的TAI区域信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

运营商A需要查询所有NF实例支持的TAI区域信息。

```
%%LST TAIRANGELIST:;%%
RETCODE = 0  操作成功

结果如下
--------
        NF实例名称  =  SMF_Instance_0
            NF类型  =  NfSMF
      移动国家代码  =  460
          移动网号  =  01
       TAC区域标识  =  0
  绑定的SMFINFO ID  =  null
绑定的NWDAFINFO ID  =  null
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称           | 输出项解释                     |
|:----------------|:--------------------------|
| NF实例名称          | 本参数用于指定NF实例名称。            |
| NF类型            | 本参数用于指定NF类型。              |
| 移动国家代码          | 本参数用于指定移动国家代码。            |
| 移动网号            | 本参数用于指定移动网号。              |
| TAC区域标识         | 本参数用于指定TAC区域标识。           |
| 绑定的SMFINFO ID   | 该参数用于指定绑定的SMFINFOEXT记录。   |
| 绑定的NWDAFINFO ID | 该参数用于指定绑定的NWDAFINFOEXT记录。 |