# 增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN**

在MOCN、GWCN下，当一个运营商有多个HPLMN时，可以通过此命令为当前运营商的Non-supporting UE提供一个或多个Serving PLMN。

在MOCN、GWCN下，当一个运营商有多个HPLMN时，运营商通常对外只使用一个PLMN ID，这样使在用户呈现上和网间计费结算上更为简洁，因此一般只为一个运营商配置一个Serving PLMN。

#### 注意事项

- 此命令的最大记录数为256。
- 此命令执行后立即生效。
- 若MCC相同，有效长度为2的MNC和3位的MNC前两位不允许相同。
- 在MOCN、GWCN下，当在一个运营商中为Non-supporting UE配置多个Serving PLMN时，则优先基于UE的IMSI匹配Serving PLMN，如果匹配上，选择此Serving PLMN；如果没有匹配上，将随机选择此运营商下的Serving PLMN。
- 在MOCN、GWCN下，当一个运营商有多个HPLMN时，如果没有通过此配置命令为Non-supporting UE指定一个Serving PLMN，则系统随机的从多个HPLMN中为此用户选择一个作为Serving PLMN。
- 对于MOCN，需要先将**SET CHGCDR**中的“Non-supporting UE的PLMN获取策略”设置为“SRV\_PLMN(SERVING PLMN)”后，此配置的数据才会生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                       |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------|
| NOID   | 运营商标识  | 可选必选说明：必选参数 参数含义：该参数用于指定运营商标识。 数据来源：整网规划 取值范围：0～64，128～254 默认值：无 配置原则：此参数需要先在ADD HPLMN或ADD MVNONET中先配置好。                   |
| MCC    | 移动国家码  | 可选必选说明：必选参数 参数含义：该参数用于指定该运营商的Serving PLMN的移动国家号码。 数据来源：整网规划 取值范围：3位十进制数字 默认值：无 配置原则：此参数需要先在ADD HPLMN或ADD MVNONET中先配置好。     |
| MNC    | 移动网号   | 可选必选说明：必选参数 参数含义：该参数用于指定该运营商的Serving PLMN的移动网号码。 数据来源：整网规划 取值范围：位数为2或3的十进制数字 默认值：无 配置原则：此参数需要先在ADD HPLMN或ADD MVNONET中先配置好。 |
| PLMNN  | 运营商名称  | 可选必选说明：可选参数 参数含义：该参数用于指定运营商名称。 数据来源：整网规划 取值范围：0~50位字符串 默认值：noname                                                          |

#### 使用实例

增加一个HNPSRVPLMN配置：运营商标识为0，移动国家码为123，移动网号为03，运营商名称为AAA

ADD HNOSRVPLMN: NOID=0, MCC="123", MNC="03", PLMNN="AAA";