# 查询IMSI和Pod绑定关系（LST IMSIBINDPOD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询IMSI和POD的绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI   | IMSI   | 可选必选说明：可选参数 参数含义：用户的IMSI信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无 |

#### 使用实例

- 显示指定IMSI与POD的绑定关系：

  ```
  LST IMSIBINDPOD: IMSI="123456782";
  ```

  ```
  RETCODE = 0  Operation succeeded

  The imsi Pod binding information
  --------------------------------
      IMSI  =  123456782
  Pod Name  =  ssgpod-0
  (Number of results = 1)
  ```
- 查询整机IMSI与POD的绑定关系：

  ```
  LST IMSIBINDPOD:;
  ```

  ```
  RETCODE = 0  Operation succeeded

  The imsi Pod binding information
  --------------------------------
  IMSI       Pod Name             

  123456781  ssgpod-0
  123456782  ssgpod-0
  123456789  ssgpod-0
  (Number of results = 3)
  ```

#### 输出结果说明

参见ADD IMSIBINDPOD的参数说明。