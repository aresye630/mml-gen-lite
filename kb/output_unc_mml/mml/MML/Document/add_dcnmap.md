# 增加DCN映射关系(ADD DCNMAP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

当部署DCN时，此命令用于根据用户的签约数据UE Usage Type配置指定DCN所服务的用户范围。UE Usage Type表示UE的使用特征，根据UE Usage Type可以选择特定的专用核心网。执行此命令前需要通过**ADD DCN**增加专用核心网。

#### 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为512。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称            | 参数说明                                                                                                                                                                            |
|:---------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DCNID          | DCN ID          | 可选必选说明：必选参数 参数含义：该参数用于指定DCN ID。 数据来源：全网规划 取值范围：0~255 默认值：无 配置原则：“DCN ID”必须已通过ADD DCN配置。一个DCN ID可配置多条记录。                                                                         |
| BGNUEUSAGETYPE | 起始UE USAGE TYPE | 可选必选说明：必选参数 参数含义：该参数用于指定起始UE USAGE TYPE。 数据来源：全网规划 取值范围：0~255 默认值：无 配置原则：相同PLMN下的UE Usage Type范围不可以重叠。                                                                          |
| ENDUEUSAGETYPE | 终止UE USAGE TYPE | 可选必选说明：可选参数 参数含义：该参数用于指定终止UE USAGE TYPE。 数据来源：全网规划 取值范围：0~255 默认值：无 配置原则：相同PLMN下的UE Usage Type范围不可以重叠。“终止UE Usage Type”必须大于等于“起始UE Usage Type”。如果该参数未输入，取值与“起始UE Usage Type”相同。 |

#### 使用实例

运营商按照如下方式规划DCN：

1. 增加一个“DCN ID”为“0”的普通专用核心网：

   ADD DCN: DCNID=0, MCC="123", MNC="01", DCNTYPE=COMMON, DESC="eMtc";
2. 将“MMEGI”为“A1B3”的MME组划分到“DCN ID”为“0”的网络中：

   ADD DCNMEMBER: DCNID=0, MMEGI="A1B3";
3. 增加DCN映射关系，使在专用核心网重选中范围在“150”至“180”的UE USAGE TYPE映射到“DCN ID”为“0”的DCN网络中：

   ADD DCNMAP: DCNID=0, BGNUEUSAGETYPE=150, ENDUEUSAGETYPE=180;