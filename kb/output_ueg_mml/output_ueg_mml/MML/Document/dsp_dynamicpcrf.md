# 显示动态PCRF（DSP DYNAMICPCRF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来查询动态PCRF主机信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称     | 参数说明                                                                                                                                                                        |
|:---------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOSTNAME | PCRF主机名称 | 可选必选说明：可选参数 参数含义：该参数用于表示动态PCRF主机的主机名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。 默认值：无 配置原则： 该参数使用DSP DYNAMICPCRF命令配置生成。不输入此可选参数时，查询所有使用的动态PCRF。在了解对端PCRF的组网配置情况下，输入该参数，查询单个动态PCRF。 |

#### 使用实例

- 查询名为dyn\_pcrf的动态PCRF主机信息：

  ```
  DSP DYNAMICPCRF:HOSTNAME="dyn_pcrf";
  ```

  ```
  RETCODE = 0  Operation Success.

  Dynamic PCRF Information
  ------------------------
  PCRF Host Name  =  dyn_pcrf
      Realm Name  =  huawei
        POD Name  =  uncpod-0
  (Number of results = 1)
  ```
- 查询所有动态PCRF主机信息：

  ```
  DSP DYNAMICPCRF:;
  ```

  ```
  RETCODE = 0  Operation Success.

  Dynamic PCRF Information
  ------------------------
  PCRF Host Name    Realm Name    POD Name 
  dyn_pcrf          huawei        uncpod-0  
  new_pcrf          huawei        uncpod-0  
  (Number of results = 2)
  ```

#### 输出结果说明

| 输出项名称    | 输出项解释                   |
|:---------|:------------------------|
| PCRF主机名称 | 用于表示动态PCRF主机的主机名。       |
| 域名       | 用于表示动态PCRF主机的域名。        |
| POD名称    | 用于表示动态PCRF主机所在的POD资源单元。 |