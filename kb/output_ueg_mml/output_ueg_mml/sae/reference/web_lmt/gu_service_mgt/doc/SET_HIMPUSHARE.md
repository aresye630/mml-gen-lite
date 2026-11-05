# 设置IMPU的共享属性(SET HIMPUSHARE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中设置一个IMPU的共享属性：可以设置为共享，也可以设置为非共享。当IMPU被设置为共享时，此IMPU将与归属Subscription中的所有IMPI建立关联关系。当IMPU被设置为非共享时，此IMPU仅和其归属IMPI存在关联关系。

## 注意事项

- **SET HSYSTEMPARA**命令中“IMPU共享属性和隐式注册集签约优化”设置为“FALSE”时，检查针对别名组和隐式注册集的约束，**SET HIMPUSHARE**注意事项如下：
  - 当Subscription中存在且仅存在一个IMPI时，不能将IMPU的共享属性设置为共享。
  - 如果该IMPU属于某隐式注册集的Default IMPU，则不允许设置共享属性。
  - 如果该IMPU属于某隐式注册集但不是该隐式注册集的Default IMPU，则在改变共享属性之后，该IMPU自动的脱离了该隐式注册集。如果除去该IMPU后，隐式注册集中的IMPU只有一个，则HSS系统自动删除该隐式注册集。
- **SET HSYSTEMPARA**命令中的“IMPU共享属性和隐式注册集签约优化”设置为“TRUE”时，不检查针对别名组和隐式注册集的约束，**SET HIMPUSHARE**注意事项如下：
  - 已签约别名组的IMPU可以设置共享属性。
  - 隐式注册集的Default IMPU可以设置共享属性。
  - 不将隐式注册集中的非Default IMPU从隐式注册集中删除。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                          |
|:-------|:-------|:----------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要设置IMPU共享的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无        |
| SHARED | 共享属性   | 用于指定IMPU的共享属性，TRUE表示要把指定的IMPU设置为共享，FALSE标识要把指定的IMPU设置为非共享。 取值范围：FALSE(False)TRUE(True) 缺省值： 无 |

## 使用实例

设置IMPU的共享属性。IMPU：sip:impuinfo@huawei.com，共享属性：TRUE。

```
SET HIMPUSHARE: IMPU="sip:impuinfo@huawei.com", SHARED=TRUE;
```