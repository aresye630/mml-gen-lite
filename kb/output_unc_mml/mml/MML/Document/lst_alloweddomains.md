# 查询允许访问的域名（LST ALLOWEDDOMAINS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询指定NF类型/NF实例允许访问的FQDN。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                   |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------------------------|
| OBJNAME | 授权对象名称 | 可选必选说明：可选参数  参数含义：该参数表示设置访问授权控制的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。  默认值：无  配置原则：无 |

## 使用实例

- 查询所有对象允许访问的FQDN：

  ```
  LST ALLOWEDDOMAINS:;
  %%LST ALLOWEDDOMAINS:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  授权对象名称  允许访问该对象的FQDN                               记录状态    

  objname001    huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org  添加未提交  
  objname002    huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org  添加未提交  
  objname003    huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org  添加未提交  
  (结果个数 = 3)
  ```
- 查询对象为objname001允许访问的FQDN：

  ```
  LST ALLOWEDDOMAINS: OBJNAME="objname001";
  %%LST ALLOWEDDOMAINS: OBJNAME="objname001";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          授权对象名称  =  objname001
  允许访问该对象的FQDN  =  huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org
              记录状态  =  添加未提交
  (结果个数 = 1)
  ```

## 输出结果说明

| 输出项名称        | 输出项解释                                                |
|:-------------|:-----------------------------------------------------|
| 授权对象名称       | 该参数表示设置访问授权控制的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。    |
| 允许访问该对象的FQDN | 该参数表示指定的NF对象所允许访问的FQDN，该参数可以通过DSP REGNFINSTANCE命令获取。 |
| 记录状态         | 该参数用于表示数据记录的提交状态。                                    |