# 增加POD模块配置(ADD PODMDU)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于添加Pod模块配置，是提供给CSM自动部署时添加业务网元下Pod模块配置的内部命令接口。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                                                                                                                                                    |
|:---------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PODNAME1 | Pod名称   | 用于指定需要增加的Pod名称，唯一标识一个Pod。操作员可以使用LST PODINFO查询获取。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：该参数的值域范围为：大写字母“A～Z”、小写字母“a～z”、数字“0～9”、特殊字符“-”、“_”。该参数必须以字母开头。该参数区分大小写。                                                                                                  |
| PODNAME2 | 互助Pod名称 | 用于指定需要增加的互助Pod名称，唯一标识一个Pod，与“Pod名称”所指定的Pod构成双平面，部署主备模块时使用。操作员可以使用LST PODINFO查询获取。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：该参数的值域范围为：大写字母“A～Z”、小写字母“a～z”、数字“0～9”、特殊字符“-”、“_”。该参数必须以字母开头。该参数区分大小写。                                                                 |
| PODTYPE  | Pod类型   | 用于指定需要增加的Pod的类型。 取值范围： UCCU(UCCU)UISU(UISU)UFEUS(UFEUS)UCCU_A(UCCU_A)UCCU_I(UCCU_I)UCCU_L1(UCCU_L1)UISU_L1(UISU_L1)UFUNC(UFUNC)UERU(UERU)UFEUE(UFEUE)UENS-NP(UENS-NP)UISU_B(UISU_B)UAAA-E(UAAA-E)UAAA(UAAA)UGBA(UGBA)UBSF(UBSF)UAP(UAP) 默认值：无。          |
| NETYPE   | 网元类型    | 用于指定需要增加的Pod的网元类型。 取值范围： “HSS9860（HSS9860）”：表示当前网元类型是HSS9860。“ENS（ENS）”：表示当前网元类型是UDM-ENS。“UEIR（UEIR）”：表示当前网元类型是UDM-EIR。“AAA（AAA）”：表示当前网元类型是UDM-UIM，做AAA认证功能。“GBA(GBA) ”：表示当前网元类型是UDM-UIM，做GBA认证功能。“BSF(BSF) ”：表示当前网元类型是BSF。“AP(AP)”：表示当前网元类型是AP。 默认值：无。 |
| VDUTYPE  | VDU平面   | 用于指定需要增加的Pod的VDU平面。 取值范围： VDU_1(VDU_1)：表示Pod所在VDU平面是VDU_1。VDU_2(VDU_2)：表示Pod所在VDU平面是VDU_2。VDU_1&VDU_2(VDU_1&VDU_2)：表示添加的两个Pod分别从属于两个VDU平面，部署主备模块时使用。 默认值：无。                                                                                             |

## 使用实例

增加“Pod名称”为“UDM\_01”，“Pod类型”为“UCCU(UCCU)”，“网元类型”为“HSS9860(HSS9860)”，“VDU平面”为“VDU\_1”的Pod模块配置：

```
ADD PODMDU: PODNAME1="UDM_01", PODTYPE=UCCU, NETYPE=HSS9860, VDUTYPE=VDU_1;
```