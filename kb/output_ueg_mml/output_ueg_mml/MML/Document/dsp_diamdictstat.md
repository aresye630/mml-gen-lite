# 显示Diameter字典加载状态（DSP DIAMDICTSTAT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter字典的加载状态。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                         |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ITEM   | 选项     | 可选必选说明：必选参数 参数含义：该参数用于指定状态输出类型。 数据来源：本端规划 取值范围：枚举类型。 LOAD_STAT：字典加载状态。PATH_STAT：字典加载路径状态。 默认值：无 配置原则：指定参数类型为LOAD_STAT时，输出参数中进程ID显示为“ALL”表示某个POD上需要加载字典的所有进程。 |

#### 使用实例

- 查询当前UNC Diameter字典加载状态：

  ```
  DSP DIAMDICTSTAT:ITEM=LOAD_STAT;
  ```

  ```
  RETCODE = 0  操作成功

  Diamter字典加载状态
  -------------------
                       POD名称  =  uncpod-0
                       进程 ID  =  ALL
              数据字典加载状态  =  失败
  第一套字典gy-ccr.xml加载状态  =  成功
  第二套字典gy-ccr.xml加载状态  =  不可用
           cer-cea.xml加载状态  =  成功
  (结果个数 = 1)

  ---    END
  ```
- 查询当前UNC Diameter字典加载路径状态：

  ```
  DSP DIAMDICTSTAT:ITEM=PATH_STAT;
  ```

  ```
  RETCODE = 0  操作成功

  Diamter字典加载路径状态
  -----------------------
  结果  =  
  Configured Dict Path:
  Status = Loaded
  Application   DictNo    Path  
  GY            1       CUSTOM1
  GX            1       CUSTOM1
  S6B           1       EPC_STANDARD
  GY            2       CUSTOM2

  Loaded Dict Path:
  Status = Loaded
  Application   DictNo    Path  
  GY            1       CUSTOM1
  GX            1       CUSTOM1
  S6B           1       EPC_STANDARD
  GY            2       CUSTOM2

  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称               | 输出项解释                   |
|:--------------------|:------------------------|
| 结果                  | 路径状态查询结果。               |
| POD名称               | POD单元名称。                |
| 进程ID                | 表示微服务进程ID。              |
| 数据字典加载状态            | Diameter字典文件的加载状态。      |
| 第一套字典gy-ccr.xml加载状态 | gy-ccr.xml信元控制文件1的加载状态。 |
| 第二套字典gy-ccr.xml加载状态 | gy-ccr.xml信元控制文件2的加载状态。 |
| cer-cea.xml加载状态     | cer-cea.xml信元控制文件的加载状态。 |