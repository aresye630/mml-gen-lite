# 查询流过滤器协议绑定关系（LST PROTBINDFLOWF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

此命令用于查询协议与流过滤器绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                        |
|:---------------|:-------|:--------------------------------------------------------------------------------------------|
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数 参数含义：该参数用于指定流过滤器名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询协议与名为testflowfiltername的流过滤器绑定关系：

  ```
  LST PROTBINDFLOWF:FLOWFILTERNAME="testflowfiltername";
  ```

  ```
  RETCODE = 0  操作成功。

  流过滤器协议绑定信息
  --------------------
    流过滤器名称  =  testflowfiltername
        协议名称  =  http
  七层过滤器名字  =  testl7filtername
  (结果个数 = 1)
  ---    END
  ```
- 查询协议与流过滤器所有的绑定关系：

  ```
  LST PROTBINDFLOWF:;
  ```

  ```
  RETCODE = 0  操作成功。

  流过滤器协议绑定信息
  --------------------
  流过滤器名称           协议名称    七层过滤器名字   

  testflowfiltername     http        testl7filtername 
  testflowfiltername2    http        testl7filtername2
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD PROTBINDFLOWF的参数说明。