# 查询BSF索引和IP Domain的关联关系（LST NRFIPDOMAINREL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询已配置的BSF索引和IP Domain的关联关系。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称        | 参数说明                                                                                                                                                                      |
|:---------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSFINDEX | BSF索引       | 可选必选说明：可选参数  参数含义：该参数用于描述BSF路由实例信息的索引值。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：  该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。                          |
| IPDOMAIN | IP Domain标识 | 可选必选说明：可选参数  参数含义：当SET NRFFUNCSW命令中的IPDOMAINSW开关开启时，该参数用于表示IP Domain后缀；当IPDOMAINSW开关关闭时，该参数用于表示IP Domain标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。该参数不区分大小写。  默认值：无  配置原则：无 |

## 使用实例

- 查询所有已配置的BSF索引和IP Domain的关联关系信息：

  ```
  LST NRFIPDOMAINREL:;
  %%LST NRFIPDOMAINREL:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  BSF索引 IP Doamin标识
  1       Huawei
  2       Huawei
  (结果个数 = 2)
  ```
- 查询BSF索引为1，IP Domain标识为Huawei关联关系信息：

  ```
  LST NRFIPDOMAINREL:  BSFINDEX=1, IPDOMAIN="Huawei";
  %%LST NRFIPDOMAINREL:  BSFINDEX=1, IPDOMAIN="Huawei";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        BSF索引 = 1
  IP Doamin标识 = Huawei
  (结果个数 = 1)
  ```

## 输出结果说明

| 输出项名称       | 输出项解释                                                                                     |
|:------------|:------------------------------------------------------------------------------------------|
| BSF索引       | 该参数用于描述BSF路由实例信息的索引值。                                                                     |
| IP Domain标识 | 当SET NRFFUNCSW命令中的IPDOMAINSW开关开启时，该参数用于表示IP Domain后缀；当IPDOMAINSW开关关闭时，该参数用于表示IP Domain标识。 |