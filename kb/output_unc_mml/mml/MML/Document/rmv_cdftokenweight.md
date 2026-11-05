# 删除cdf token权重（RMV CDFTOKENWEIGHT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

当CDFTOKENPOLICY开关配置为使能且删除cdf token权重配置时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于删除cdf token权重配置。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                |
|:--------|:-------|:------------------------------------------------------------------------------------|
| PODNAME | pod 名称 | 可选必选说明：必选参数  参数含义：该参数用于描述pod名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无 |

## 使用实例

当删除pod名称为cgfb-pod-0上的cdf token权重配置：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-06-11 15:20:20+8:00
O&M    #3546
%%RMV CDFTOKENWEIGHT: PODNAME="cgfb-pod-0", CONFIRM=Y;%%
RETCODE = 0  操作成功

---    END
```