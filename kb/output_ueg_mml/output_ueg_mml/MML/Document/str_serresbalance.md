# 启动业务资源均衡操作(STR SERRESBALANCE)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

资源均衡过程中可能会影响现有业务，建议在业务低峰时执行此命令。

**适用网元：SGSN、MME**

1. 此命令用于手动启动系统内资源均衡。
2. 系统扩容、减容或出现进程或节点故障场景时，可能出现系统资源在进程或节点之间部署不均。
3. RM\_TYPE\_USER、RM\_TYPE\_S1ECMCONN、RM\_TYPE\_S1UCMCONN、RM\_TYPE\_GTPUPDP、RM\_TYPE\_GBCELL、RM\_TYPE\_GBUSER、RM\_TYPE\_IUUSRCONN、RM\_TYPE\_NGAPLNK这几类资源在执行此命令后，不能保证进程间完全均衡，各个进程间上下文差值占进程上下文规格的比例小于10%。其他资源在执行此命令后，能保证各个进程间上下文分布均衡。
4. 资源部署不均衡对进程的影响:
   - RM\_TYPE\_DMLNK(Diameter链路)、RM\_TYPE\_M3UALNK(M3UA链路)、RM\_TYPE\_SGSVLRLNK(SGS链路)、RM\_TYPE\_DNSCONN(DNS本端端点)、RM\_TYPE\_S1ECMCONN（S1链路）、RM\_TYPE\_S1UCMCONN（S1连接）、RM\_TYPE\_IUUSRCONN(IU连接)、RM\_TYPE\_NGAPLNK（N2链路）这些资源部署在SGP进程上，这些资源部署不均衡可能导致SGP CPU开销不均。
   - RM\_TYPE\_GBCELL(2G小区)、RM\_TYPE\_NSE(NSE)、RM\_TYPE\_GBUSER(GB用户上下文)这些资源部署在GBP进程上，这些资源部署不均衡可能导致GBP CPU开销不均。
   - RM\_TYPE\_GTPCPATH(GTPC本端端点)、RM\_TYPE\_GTPUPATH(GTPU本端端点)、RM\_TYPE\_GTPUPDP(用户面PDP上下文)这些资源部署在UPP进程上，这些资源不均衡可能导致UPP CPU开销不均。
   - RM\_TYPE\_USER(用户和承载上下文)这个资源部署在SPP进程上，这个资源不均衡可能导致SPP CPU开销不均。

#### 注意事项

- 该命令执行后立刻生效。
- 资源均衡过程中，现有业务会有影响。建议在业务低峰时段进行资源迁移。
- 迁移过程中出现进程或节点复位，则停止均衡。通过**DSP SERRESLOC**命令可以查询各种资源在系统中的部署情况。
- 该命令生效以后，需要等待4分钟左右才能实现资源的均衡，此过程中如果节点或者进程复位，则停止均衡。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERRESTYPE  | 业务资源类型 | 可选必选说明：必选参数 参数含义：需要重新进行负载均衡的业务资源。 MNT_RM_TYPE_USER：用户和承载上下文资源。 MNT_RM_TYPE_DMLNK：Diameter链路资源。 MNT_RM_TYPE_S1ECMCONN：S1链路资源。 MNT_RM_TYPE_S1UCMCONN：S1连接资源。 MNT_RM_TYPE_GTPCPATH：GTPC本端端点资源。 MNT_RM_TYPE_GTPUPATH：GTPU本端端点资源。 MNT_RM_TYPE_DNSCONN：DNS本端端点资源。 MNT_RM_TYPE_M3UALNK：M3UA链路资源。 MNT_RM_TYPE_GTPUPDP：用户面PDP上下文资源。MNT_RM_TYPE_SGSVLRLNK：SGS链路资源。 MNT_RM_TYPE_IUUSRCONN：IU连接资源。 MNT_RM_TYPE_GBCELL：2G小区资源。 MNT_RM_TYPE_GBUSER：GB用户上下文资源。 MNT_RM_TYPE_NSE：GB NSE资源。 MNT_RM_TYPE_NGAPLNK：N2链路资源。 取值范围: “MNT_RM_TYPE_USER(USER)”“MNT_RM_TYPE_DMLNK(DMLNK)”“MNT_RM_TYPE_S1ECMCONN(S1ECMCONN)”“MNT_RM_TYPE_S1UCMCONN(S1UCMCONN)”“MNT_RM_TYPE_GTPCPATH(GTPCPATH)”“MNT_RM_TYPE_GTPUPATH(GTPUPATH)”“MNT_RM_TYPE_DNSCONN(DNSCONN)”“MNT_RM_TYPE_M3UALNK(M3UALNK)”“MNT_RM_TYPE_GTPUPDP(GTPUPDP)”“MNT_RM_TYPE_SGSVLRLNK(SGSVLRLNK)”“MNT_RM_TYPE_IUUSRCONN(IUUSRCONN)”“MNT_RM_TYPE_GBCELL(GBCELL)”“MNT_RM_TYPE_GBUSER(GBUSER)”“MNT_RM_TYPE_NSE(NSE)”“MNT_RM_TYPE_NGAPLNK(NGAPLNK)” 默认值：无 |
| SERVICETYPE | 服务名称   | 可选必选说明：必选参数 参数含义：本参数用于指定服务名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。 默认值：无  说明： 该参数可以通过VNFP上的LST VNFC命令查询得到。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

#### 使用实例

启动业务资源均衡操作，选择MNT\_RM\_TYPE\_USER(用户和承载上下文资源)的业务资源：

STR SERRESBALANCE: SERRESTYPE=MNT\_RM\_TYPE\_USER, SERVICETYPE="USN\_VNFC";

```
%%STR SERRESBALANCE: SERRESTYPE=MNT_RM_TYPE_USER, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

---    END
```