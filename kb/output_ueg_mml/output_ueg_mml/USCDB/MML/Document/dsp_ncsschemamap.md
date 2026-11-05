# 显示应用模型间模型映射关联关系（DSP NCSSCHEMAMAP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示应用模型间模型映射关联关系。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| FAILFLAG        | 失败标志位  | 可选必选说明：可选参数 参数含义：失败标志位。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无                                      |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

- 显示应用模型间模型映射关联关系：

  ```
  DSP NCSSCHEMAMAP:SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  文件名称             映射关系        对象类型              命名空间                                           父亲路径信息                                     孩子路径                         源模式映射           数据模型关系资源文件路径

  vrp_schema_map.xml   child-table     配置类型          http://www.huawei.com/netconf/vrp                  /l3vpn/l3vpncomm/l3vpnInstances/l3vpnInstance    /ifm_l3vpn_map/l3vpnIfs          l2_schema_map        .../reslink/schema
  vrp_schema_map.xml   child-table     查询类型          http://www.huawei.com/netconf/vrp                  /l3vpn/l3vpncomm/l3vpnInstances/l3vpnInstance    /ifm_l3vpn_map/l3vpnIfs          l2_schema_map        .../reslink/schema
  (结果个数 = 2)
  ---    END
  ```
- 显示加载失败的应用模型间模型映射关联关系：

  ```
  DSP NCSSCHEMAMAP:FAILFLAG=TRUE,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  文件名称              映射关系        对象类型              命名空间                                           父亲路径信息                                    孩子路径                               源模式映射               错误信息                                                 数据模型关系资源文件路径

  vrp_schema_map.xml    sub-service     配置类型          http://www.huawei.com/netconf/vrp                  /directrt                                       /eumpu_directrt_map/directrtvlink      l2_schema_map            Child application not found                              .../reslink/schema
  vrp_schema_map.xml    sub-service     查询类型          http://www.huawei.com/netconf/vrp                  /directrt                                       /eumpu_directrt_map/directrtvlink      l2_schema_map            Child application not found                              .../reslink/schema
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称        | 输出项解释                |
|:-------------|:---------------------|
| 文件名称         | Schema Map文件的名称。     |
| 映射关系         | Schema Map的映射关系。     |
| 对象类型         | Schema Map的对象的类型。    |
| 命名空间         | Schema Map的名字空间。     |
| 父亲路径信息       | Schema Map的父节点xPath。 |
| 孩子路径         | Schema Map的子节点xPath。 |
| 源模式映射        | Schema Map的来源子系统。    |
| 错误信息         | Schema Map加载失败的错误信息。 |
| 数据模型关系资源文件路径 | Schema Map的资源文件相对路径。 |