# 创建数据同步服务器公钥（ADD RSFTPPUBLICKEY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UDM**

该命令用于创建数据同步服务器公钥。客户端需要对服务端进行公钥认证时，使用该命令配置绑定服务端对端公钥。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10。
- 密钥需定期修改否则会有安全风险。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                           |
|:-----------|:-------|:-----------------------------------------------------------------------------------------------|
| KEYNAME    | 密钥名称   | 可选必选说明：必选参数 参数含义：密钥名称。 数据来源：本端规划 取值范围：由数字、字母和下划线组成的不超过63位的字符串。 默认值：无 配置原则：无                    |
| PUBKEYTYPE | 密钥类型   | 可选必选说明：必选参数 参数含义：密钥类型。 数据来源：本端规划 取值范围： RSA：RSA公钥。ECDSA：ECDSA公钥。 默认值：无 配置原则：无                   |
| KEYCODE    | 密钥     | 可选必选说明：必选参数 参数含义：密钥。 数据来源：对端协商 取值范围：输入长度范围为1～1024。 默认值：无 配置原则：当密钥类型为RSA时，输入密钥值时需去掉“ssh-rsa”开头。 |
| ENCODETYPE | 编码类型   | 可选必选说明：可选参数 参数含义：编码类型。 数据来源：本端规划 取值范围： PEM：PEM编码。OPENSSH：OPENSSH编码。 默认值：PEM 配置原则：无             |

#### 使用实例

创建类型为RSA、名称为rsa2的对端公钥：

```
ADD RSFTPPUBLICKEY:KEYNAME="rsa2",PUBKEYTYPE=RSA,KEYCODE="MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAybi/3guc70NLoGecAdyAo0dJYLRXCYFdx7Iaq20REXb5SsyqSjGV/KEr8sdyFhr/PasKb1XbV7G8/gdtxU+Sl5dGI9h8mymIQ7VzbyEhwQqjzdyCKoz2levKPgjsTDN93IQiNfSOfc4qUux5viWQaPWt3bzpvOZXHcMUbzEz/jahKZPU/hMq/N3DroE6xFYB91fb74qHOC5RGMPjskUYKOjCtj+v+sZqznuckf2x0a2r5X++gsqGZT8dHaX9smyrpBbV9Y/g1VZ+CO8XFdRiHWth98FnlbEeHsrXbho9CE2GEACWvRRApMn1uSpghpENbkefpbYCIN7tq6X4lKvSYQZARiLkD1ELHcmWCX+cpIlfxihrKpVnRR4iLJNl33VtOBIPaMvtifojkLxsi3dtyJkcEFQI/kXbKW8Kdw5Fd+UOcsQf8PKk7k9LgFaH8GZRFhbwT0bLjjy0UIV5NDHcSozydV2uQh+ON6BsygCSvME8V4lu9z74Rq3T7eP25pC+Q0mN+1n7QGQL4zKshkKNh6Rx+QCP0hVGNosL6MoLzseluapTqnHrQEHTbG1Jm+WL/ces3thH7PySyWKJcUQ/iWBD0FFkya0KTvTfWvBg/WPdqBHLIQh6ie/7lOFyE56FbRYuRU0cF8+NykA/6HN247pFtw1PSgQ68Dqtv9bZMFUCAwEAAQ==";
```