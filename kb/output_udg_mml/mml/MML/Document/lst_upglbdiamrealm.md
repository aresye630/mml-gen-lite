# 查询全局Diameter域（LST UPGLBDIAMREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询全局Diameter域。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                             |
|:------------|:-----------|:-----------------------------------------------------------------------------------------------------------------|
| APPLICATION | Diameter应用 | 可选必选说明：可选参数 参数含义：该参数用于指定全局Diameter域所属的Diameter应用。 数据来源：全网规划 取值范围：枚举类型。 SWM：SWM接口应用。 默认值：无 配置原则：根据实际应用场景选择对应的枚举值。 |

#### 使用实例

- 查询全局Diameter域与SWM应用的绑定关系：

  ```
  LST UPGLBDIAMREALM: APPLICATION=SWM;
  ```

  ```
  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```
- 查询所有全局Diameter域的绑定关系：

  ```
  LST UPGLBDIAMREALM:;
  ```

  ```
  RETCODE = 0  操作成功
  全局Diameter域名
  ----------------
                    Diameter应用  =  SWM
     根据IMSI构造归属地Realm开关  =  不使能
                    Diameter域名  =  test.huawei.com
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

参见ADD UPGLBDIAMREALM的参数说明。