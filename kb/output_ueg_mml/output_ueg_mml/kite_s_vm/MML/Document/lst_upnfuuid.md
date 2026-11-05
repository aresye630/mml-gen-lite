# 查询NF UUID（LST UPNFUUID）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询NF实例对应的NF实例标识（UUID）。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

运营商A需要查询NF实例生成的UUID信息：

```
LST UPNFUUID:;
```

```
RETCODE = 0  操作成功

NF UUID
-------
NF类型  NF实例名称       NF实例标识                            

NfLMF   LMF_Instance_0   daee87b1-7d01-49ed-830d-d4115fc38675  
NfGMLC  GMLC_Instance_0  639deb4b-b625-4fe8-bb64-d79c4d5a4aaa  
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见ADD UPNFUUID的参数说明。