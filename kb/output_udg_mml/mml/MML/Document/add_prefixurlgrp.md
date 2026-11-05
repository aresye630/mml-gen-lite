# 增加前缀URL组（ADD PREFIXURLGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于增加前缀URL组或添加前缀URL到前缀URL组。前缀URL组配置的URL是代理服务器对应的域名。

#### 注意事项

- 如果只指定了前缀URL组名字，该命令执行后立即生效；如果指定了前缀URL，该命令执行后60s或配置恢复后60s生效。
- 系统支持配置100个前缀URL组。
- 单个前缀URL组中可以配置10个前缀URL。
- URL参数输入要求：

  - 不支持通配符，不允许配置Path，不能以“/”开头，可携带“http://”，“https://”，“rtsp://”，“ftp://”，“tftp://”头。
  - 对于？可以使用%3f代替；例如：www.hua?wei.com 输入可以是：www.hua%3fwei.com。
  - 对于空格可以使用％20代替；例如：www.hua wei.com 输入可以是：www.hua%20wei.com。
  - 对于逗号可以使用％2c代替；例如：www.hua,wei.com 输入可以是：www.hua%2cwei.com。
  - 对于加号可以使用％2b代替，例如：www.hua+++wei.com 输入可以是：www.hua%2b%2b%2bwei.com。
  - 当url字段中出现%3f、%20、%20、%2b或者%25这样的特殊字符时，对于%可以使用%25代替；例如www.hua%3fwei.com 输入可以是www.hua%253fwei.com。
  - 其他情况的％就认为是％本身，保持原有实现即可；例如：www.hua%wei.com 输入应该是：www.hua%wei.com或者是www.hua%25wei.com。
  - 对于' '、'<'、'>'、'"'、'#'、'`'、'{'、'}'、'|'、'\\'、'^'、'~'、'['、']'等特殊字符，会被转义成 3个字符来处理，URL长度是指转义后的字符数，URL中每出现一个特殊字符，其长度将比真实长度多两个字符，例如：www.hua<wei.com的URL长度为15个字符。
  - 字符串不能包含非法字符0x00~0x1F和0x7F。
  - 配置的URL中允许出现文本 IPv6 地址。由于文本 IPv6 地址可能需要对网段进行通配，因此需要通过在其中添加掩码长度来表述。配置时必须严格按照[ipv6-addrdess/prefix-length]格式配置，如[2001:db8:0:0:1:0:0:1/63]，其中63是掩码长度，通过“/”和IP地址分隔开。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                    |
|:--------------|:---------|:----------------------------------------------------------------------------------------|
| PREURLGRPNAME | 前缀URL组名字 | 可选必选说明：必选参数 参数含义：该参数用于指定前缀URL组名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写。 默认值：无 配置原则：无 |
| PREFIXURL     | 前缀URL    | 可选必选说明：可选参数 参数含义：该参数用于指定前缀URL。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写。 默认值：无 配置原则：无    |
| CFGDOMAINNAME | 配置域名称    | 可选必选说明：可选参数 参数含义：该参数表示命令所属公共配置域的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无      |

#### 使用实例

- 增加前缀URL组，PREURLGRPNAME为“testurlgroup”：

  ```
  ADD PREFIXURLGRP:PREURLGRPNAME="testurlgroup";
  ```
- 增加前缀URL组，并添加前缀URL到前缀URL组中：PREURLGRPNAME为“testurlgroup”,PREFIXURL为"www.huawei.com"：

  ```
  ADD PREFIXURLGRP:PREURLGRPNAME="testurlgroup",PREFIXURL="www.huawei.com";
  ```