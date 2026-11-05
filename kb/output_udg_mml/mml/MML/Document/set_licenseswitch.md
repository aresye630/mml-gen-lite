# 设置License项的开关（SET LICENSESWITCH）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于设置License项的配置开关。当License文件中含有某功能的许可时，通过此命令可以设置该功能是否开通。

## 注意事项

- 该命令执行后立即生效。

- 当License文件未激活时，无法设置任何License项，激活后只能设置已购买且支持配置开关的License项。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| LICITEM        | SWITCH   |
|:---------------|:---------|
| LKV2MSCMG02    | ENABLE   |
| LKV2C2AF01     | ENABLE   |
| LKV2C6AF01     | ENABLE   |
| LKV2C9AF01     | ENABLE   |
| LKV2C11AF01    | ENABLE   |
| LKV2E2ETRACE02 | ENABLE   |
| LKV2BFD02      | ENABLE   |
| LKV2C15AF01    | ENABLE   |
| LKV2PPTF01     | ENABLE   |
| LKV2V6IF01     | ENABLE   |
| LKV3W9CAT411   | ENABLE   |
| LKV3W9CAT611   | ENABLE   |
| LKV3W9CT9A11   | ENABLE   |
| LKV3W9CTBC11   | DISABLE  |
| LKV3W9CA1611   | ENABLE   |
| LKV2C17AF01    | ENABLE   |
| LKV2C19AF01    | ENABLE   |
| LKV2NFBAM01    | ENABLE   |
| LKV2NFBSM01    | ENABLE   |
| LKV2NFAAM01    | ENABLE   |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                                             |
|:--------|:---------|:---------------------------------------------------------------------------------------------------------------------------------|
| LICITEM | License项 | 可选必选说明：必选参数  参数含义：该参数用于指定需要开通的License项。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无。  配置原则：无                                     |
| SWITCH  | 开关       | 可选必选说明：必选参数  参数含义：该参数用于表示License项的配置开关是否已经打开。  数据来源：本端规划 取值范围： “ENABLE（开）”：开启License控制项“DISABLE（关）”：关闭License控制项  默认值：无。  配置原则：无 |

## 使用实例

开通License项为“LKV2INLINR01”的功能的License开关：

```
%%SET LICENSESWITCH: LICITEM="LKV2INLINR01", SWITCH=ENABLE;%%
RETCODE = 0  操作成功

---    END
```