# 删除软件包（RMV PACKAGE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于删除指定版本的基础包、风险排查包、补丁包以及DB翻译包等软件包。

#### 注意事项

- 该命令执行后立即生效。
- 不能删除现在正在使用版本以及回退版本的基础包、补丁包。
- “ISFORCE”字段为“TRUE”，可以强制删除处于running状态的异构软件包，但如果异构类型已经扩容对应接口板，则不能删除。

  **说明** 

  该功能仅在Full-stack虚机场景下支持。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称    | 参数说明                                                                                                                                                                                                 |
|:----------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PACKAGETYPE     | 包类型     | 可选必选说明：必选参数 参数含义：该参数用于表示包类型。 数据来源：本端规划 取值范围：枚举类型。 Version：软件版本包，包括基础版本包、冷补丁、热补丁等几种。RiskCheckPackage：风险排查包。AppPackage：App软件包。 默认值：无                                                                   |
| VERSIONTYPE     | 版本类型    | 可选必选说明：必选参数 参数含义：该参数用于表示版本类型。 数据来源：本端规划 取值范围：枚举类型。 BaseSoftware：包含网元或APP运行所需所有软件的全版本。ColdPatch：为网元或APP运行所需的部分软件，为对基础版本的补充，冷补丁不能独立运行，冷补丁升级往往会中断业务。HotPatch：为对基础版本或冷补丁的热补充，热补丁不能独立运行，热补丁升级不中断业务。 默认值：无 |
| VERSIONID       | 版本号     | 可选必选说明：必选参数 参数含义：该参数用于表示版本号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无                                                                                                                                 |
| APPTYPE         | 版本应用类型  | 可选必选说明：必选参数 参数含义：该参数用于表示版本应用类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无                                                                                                                              |
| CPUARCHTYPE     | CPU架构类型 | 可选必选说明：可选参数 参数含义：CPU架构类型。 数据来源：本端规划 取值范围：枚举类型。 X86：CPU架构类型是X86。ARM：CPU架构类型是ARM。Any：不区分CPU架构类型。 默认值：Any                                                                                               |
| ISFORCE         | 是否强制删除  | 可选必选说明：可选参数 参数含义：是否强制删除。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE                                                                                                                         |
| ONLYREMOVEPOOL  | 只删除补丁池  | 可选必选说明：可选参数 参数含义：是否只删除补丁池。 数据来源：本端规划 取值范围：布尔类型。 FALSE：同时删除对应版本号的补丁包和内部补丁池目录。TRUE：只删除对应版本号的内部补丁池目录。 默认值：FALSE 配置原则：只在灰度升级结束后清理低版本残留内部补丁池目录时参数选为“TRUE”。                                                |
| SERVICEINSTANCE | 服务实例    | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                                         |

#### 使用实例

- 删除风险排查包：

  ```
  RMV PACKAGE:PACKAGETYPE=RiskCheckPackage,VERSIONTYPE=BaseSoftware,VERSIONID="ck0820S4",APPTYPE="BaseApp",SERVICEINSTANCE="vnfc";
  ```
- 只删除补丁池：

  ```
  RMV PACKAGE:PACKAGETYPE=Version,VERSIONTYPE=HotPatch,APPTYPE="BaseApp",VERSIONID="FENIXSPH255H",CPUARCHTYPE=Any,ISFORCE=FALSE,ONLYREMOVEPOOL=TRUE,SERVICEINSTANCE="vnfc";
  ```
- 删除异构CPU类型的软件包：

  ```
  RMV PACKAGE:PACKAGETYPE=Version,VERSIONTYPE=BaseSoftware,APPTYPE="BaseApp",VERSIONID="V100R020C20SPC200B010",CPUARCHTYPE=ARM,ISFORCE=TRUE,SERVICEINSTANCE="vnfc";
  ```