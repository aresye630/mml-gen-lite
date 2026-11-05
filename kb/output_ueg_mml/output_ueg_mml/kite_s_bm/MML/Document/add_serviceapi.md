# 添加服务API（ADD SERVICEAPI）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF、MPF**

该命令用于添加指定服务的API信息。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5000。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVICENAME   | 服务名称        | 可选必选说明：必选参数 参数含义：API所属服务名称。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～127。取值1-127字节的字符串。该服务名称由服务提供商提供，且该服务已经通过MP1口注册至MEP，可通过DSP MECSERVICE命令查询到。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| APINAME       | API名称       | 可选必选说明：必选参数 参数含义：API名称。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～127。取值1-127字节的字符串。服务内不允许重复。由大小写字母，数字，“_”，“-”组成，且只能以字母开头。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BASEURL       | API 对外的基础路径 | 可选必选说明：必选参数 参数含义：API 对外的基础路径，如/photoservice。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～127。相同服务的BaseURL必须一致；字符串类型，输入长度范围为1～127。由大小写字母，数字，“-”，“_”,"~",".",“/”,"%"组成，不区分大小写，且必须以"/"开头。 默认值：无 配置原则：API 对外的基础路径，如/photoservice。                                                                                                                                                                                                                                                                                                                                                                                                                             |
| RESOURCEPATH  | API 共有资源路径  | 可选必选说明：可选参数 参数含义：API 共有资源路径。网关后端目标服务API的共有资源路径，如果没有公共路径，则不填。 例如网关后端目标服务提供3个API: GET /photoservice/api/v1/animal/tiger; POST /photoservice/api/v1/animal/tiger?photo={name}; POST /photoservice/api/v1/animal/lion;那么API的共有资源路径ResourcePath为：/api/v1/animal。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～255。相同服务的ResourcePath必须一致；字符串类型，输入长度范围为1～255。由大小写字母，数字，“-”，“_”,"~",".",“/”,"%"组成，且必须以"/"开头。 默认值：无 配置原则：API 共有资源路径。网关后端目标服务API的共有资源路径，如果没有公共路径，则不填。 例如网关后端目标服务提供3个API: GET /photoservice/api/v1/animal/tiger; POST /photoservice/api/v1/animal/tiger?photo={name}; POST /photoservice/api/v1/animal/lion;那么API的共有资源路径ResourcePath为：/api/v1/animal。 |
| REQUESTMETHOD | API 请求方法    | 可选必选说明：必选参数 参数含义：API 请求方法。 数据来源：对端协商 取值范围：枚举类型。 HTTP_GET：HTTP GET 方法。HTTP_POST：HTTP POST 方法。HTTP_DELETE：HTTP DELETE 方法。HTTP_PUT：HTTP PUT 方法。HTTP_HEADER：HTTP HEADER 方法。HTTP_TRACE：HTTP TRACE 方法。HTTP_PATCH：HTTP PATCH 方法。HTTP_CONNECT：HTTP CONNECT 方法。HTTP_OPTIONS：HTTP OPTIONS 方法。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                            |
| REQUESTPATH   | API 请求路径    | 可选必选说明：必选参数 参数含义：API 请求路径。比如API对外部的完整地址为http://api.a.com:8080/photoservice/api/v1/animal/tiger?photo={name}，/photoservice为API的baseURL，/api/v1/animal为API的ResourcePath，API RequestPath是指/tiger这一部分。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～2047。由大小写字母，数字，“-”，“_”,"~",".",“/”,"%"组成，不区分大小写，且必须以"/"开头。 默认值：无 配置原则：API 请求路径。比如API对外部的完整地址为http://api.a.com:8080/photoservice/api/v1/animal/tiger?photo={name}，/photoservice为API的baseURL，/api/v1/animal为API的ResourcePath，RequestPath是指/tiger这一部分。                                                                                                                                                        |

#### 使用实例

添加ServiceAPI对象，服务名称为"photo"，API名称为"getphoto"，API对外的基础路径为"/photoservice"，API共有资源路径为"/api/v1/animal"，API请求方法为HTTP\_GET，API 请求路径为"/tiger"：

```
ADD SERVICEAPI: SERVICENAME="photo", APINAME="getphoto", BASEURL="/photoservice", RESOURCEPATH="/api/v1/animal", REQUESTMETHOD=HTTP_GET, REQUESTPATH="/tiger";
```