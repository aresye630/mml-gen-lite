# 增加分层互联信元字符串通配属性路由（ADD NRFWILDCARDSTRRT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

通配字符串配置错误，可能会导致业务路由到其他大区或者省份，引起业务不可用。

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于配置新增分层互联信元字符串通配属性路由。当需要对某个NF进行跨NRF寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。
- 当通过此命令与ADD NRFROUTINGINDRT命令同时配置了某个ROUTINGINDICATOR的下一跳NRF实例组时，优先使用ADD NRFROUTINGINDRT配置的NRF实例组信息。

- 最多可输入100000条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                              |
|:---------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATTRIBUTE      | 属性       | 可选必选说明：必选参数  参数含义：该参数用于表示分层互联属性类型。  数据来源：全网规划 取值范围： TAC（TAC）NRFNFGROUP（NFGROUP）SERVINGSCOPE（SERVINGSCOPE）REGIONIDSETID（区域标识和集合标识）ROUTINGINDICATOR（选路指示器）  默认值：无  配置原则：无           |
| MATCHSTR       | 通配字符串    | 可选必选说明：必选参数  参数含义：该参数用于表示分层互联信元字符串通配值。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~128。  默认值：无  配置原则：  通配字符串的长度应该与ADD NRFWILDCARDATTR命令中对应属性配置的通配长度相同。                                        |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数  参数含义：该参数用于表示NRF基于通配字符串寻址NF时的下一跳NRF实例组名称，该参数需要输入时，必须通过LST NRFGROUP命令获取。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，通过LST NRFGROUP命令查询获取。 |

## 使用实例

支持通配规则为按AMF RegionId, AMF SetId的1~12比特位设置16进制字符串通配值为“042”所对应的下一跳路由为nrfgroup001，则请求信息中携带用户信息AMFID只要满足通配000001000010XXXXXXXXXXXX（按AMFID实际的位数写），NRF判断对应下一跳路由即为nrfgroup001。

```
ADD NRFWILDCARDATTR: ATTRIBUTE= REGIONIDSETID, MATCHSTART=0, MATCHLEN=12;
ADD NRFWILDCARDSTRRT: ATTRIBUTE=REGIONIDSETID, MATCHSTR="042", NEXTNRFGRPNAME="nrfgroup001";
```