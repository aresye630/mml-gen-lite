# 显示SFE Fast-ping报文统计信息（DSP SFEFASTPINGPKTSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示SFE fast-ping报文统计信息。

#### 注意事项

- 只有在打开了ping快回使能开关后，才会对ping快回报文进行统计计数。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| RUNAME | RU名称   | 可选必选说明：可选参数 参数含义：资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。区分大小写。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

- 显示指定RU的fast-ping报文统计信息：

  ```
  DSP SFEFASTPINGPKTSTC:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```

  ```
  RETCODE = 0  操作成功。                                                 
                                                                                  
  结果如下                                                       
  -------------------------                                                       
  RU名称                      报文类型         报文数量
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回应答     15   
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回请求    15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回应答    15                         
  (结果个数 = 4)                                                         
  ---    END
  ```
- 显示所有RU的fast-ping报文统计信息：

  ```
  DSP SFEFASTPINGPKTSTC:;
  ```

  ```
  RETCODE = 0  操作成功。                                          
                                                                                  
  结果如下                                                       
  -------------------------                                                       
  RU名称                      报文类型         报文数量
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv4 ping快回应答     15   
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0064    IPv6 ping快回应答     15                           
  VNODE_VNRS_VNFC_IPU_0065    IPv4 ping快回请求     0                           
  VNODE_VNRS_VNFC_IPU_0065    IPv4 ping快回应答     0   
  VNODE_VNRS_VNFC_IPU_0065    IPv6 ping快回请求     15                          
  VNODE_VNRS_VNFC_IPU_0065    IPv6 ping快回应答     15                            
  (结果个数 = 8)                                                         
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                           |
|:--------|:----------------------------------------------------------------|
| RU名称    | 资源单元名称。                                                         |
| 报文类型    | 报文类型，如：ipv4 ping快回请求、ipv4 ping快回应答、ipv6 ping快回请求、ipv6 ping快回应答。 |
| 报文数量    | 报文统计计数。                                                         |