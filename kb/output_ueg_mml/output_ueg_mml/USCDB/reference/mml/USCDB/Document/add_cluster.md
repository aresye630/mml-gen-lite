# 增加Cluster信息(ADD CLUSTER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于为USCDB网元下的DRU和DSU模块添加对应类型的Cluster信息，只有添加Cluster后才能进行节点的添加。

该命令的使用场景：在开局或扩容场景下，完成模块的添加后，需要为DRU、DSU模块添加对应Cluster类型的Cluster信息。

该命令的参数索引关系如图1所示：

**图1** 命令参数的索引关系图

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                      |
|:------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CID         | Cluster标识 | 用于定义一个待增加Cluster的Cluster标识。 该参数的配置原则：“1”固定预留给存储USCDB公共数据的DRU Cluster，系统自动配置。从“2”到“30”，从“1025”到“4078”分配给存储全局数据的DRU Cluster。从“31”到“100”，从“513”到“612”，从“1025”到“4078”分配给存储路由数据的DRU Cluster。从“101”到“512”，从“613”到“1024”，从“1025”到“4078”分配给存储用户数据的DSU Cluster。 取值范围：2～4096 默认值：无。 |
| CT          | Cluster类型 | 用于定义一个待增加Cluster的Cluster类型。 取值范围： DRU(DRU)DSU(DSU) 默认值：无。                                                                                                                                                                                                                 |
| DATATYPE    | 数据类型      | 用于定义一个待增加Cluster的数据类型。仅当本命令中的“Cluster类型”参数为“DRU(DRU)”时，该参数有效。 该参数的配置原则：根据对接的FE不同，待添加各数据类型的Cluster个数会存在差异。 取值范围：GLOBAL_DATA(全局数据)ROUTE_DATA(路由数据) 默认值：无。                                                                                                                   |
| ROLE        | 主备标识      | 用于定义一个待增加Cluster的主备标识。 该参数配置原则：容灾组网场景下，如果为主用局的Cluster，则“主备标识”需要配置为“ACTIVE(主用)”；如果为容灾局的Cluster，则“主备标识”需要配置为“REDUNDANCY(容灾)”。单局点场景下，本局的“主备标识”直接配置成“ACTIVE(主用)”。 取值范围： ACTIVE(主用)REDUNDANCY(容灾) 默认值：无。                                                                       |
| SERVICETYPE | 业务类型      | 用于定义一个待增加Cluster的业务类型。此参数在USCDB下唯一，通过LOD FEPLUG命令加载FE插件后在此引用。 取值范围：长度不超过128的字符串。 默认值：无。                                                                                                                                                                                   |

## 使用实例

1. 在开局场景下，需要为新增Pod配置对应的Cluster信息，此时需要进行如下配置。
   1. 根据图1中的参数索引关系，确认FE插件包是否已加载。

      执行**LST FEPLUG**命令查询待增加模块对应的插件包类型是否已添加。若未添加，需执行**LOD FEPLUG**命令加载FE插件包，加载的插件包类型为SUP-FE。

      **说明** 

      SUP-FE为一个举例的名称，请根据局点的实际情况加载对应的FE插件包。
   2. 新增Pod内待增加的模块、Cluster的配置信息为：
      - 每个Pod需要配置以下模块：1\*DSG+4\*DRU+8\*DSU。
      - 总共需要增加11个Cluster，3个“Cluster类型”为“DRU(DRU)”的Cluster和8个“Cluster类型”为“DSU(DSU)”的Cluster。

        **说明** 

        因为有1个“Cluster类型”为“DRU(DRU)”的Cluster用于存储USCDB网元的全局数据。该Cluster已由系统自动配置，因此无需手动添加。
      - 2个“Cluster类型”为“DRU(DRU)”的Cluster的“数据类型”为“ROUTE\_DATA(路由数据)”，1个“Cluster类型”为“DRU(DRU)”的Cluster的“数据类型”为“GLOBAL\_DATA(全局数据)”。
   3. 根据新增Pod内待增加的模块配置信息，执行**ADD MODULE**命令添加模块。
   4. 根据新增Pod内待增加的Cluster的配置信息，执行**ADD CLUSTER**命令添加对应Cluster。
      - “Cluster类型”为“DRU(DRU)”的Cluster的命令为：

        ```
        ADD CLUSTER: CID=2, CT=DRU, DATATYPE=GLOBAL_DATA, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=31, CT=DRU, DATATYPE=ROUTE_DATA, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=32, CT=DRU, DATATYPE=ROUTE_DATA, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ```
      - “Cluster类型”为“DSU(DSU)”的Cluster的命令为：

        ```
        ADD CLUSTER: CID=101, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=102, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=103, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=104, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=105, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=106, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=107, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ADD CLUSTER: CID=108, CT=DSU, ROLE=ACTIVE, SERVICETYPE="SUP-FE";
        ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                       | 原因分析                                      | 处理建议                                                                                                                         |
|-------:|:--------------------------------------------|:------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| 250098 | 参数取值无效：参数SERVICETYPE的取值不存在，请确认已经成功加载了该FE插件。 | 输入的“业务类型”在系统中未配置。                         | 通过LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即“业务类型”。 若“业务类型”加载成功，请在执行该命令时输入正确的业务类型名称。若“业务类型”加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。 |
| 250100 | 一个业务类型只能有一个数据类型是全局数据的DRU。                   | 一种“业务类型”只能设置一个“数据类型”为“GLOBAL_DATA”的DRU模块。 | 请确认是否需要添加“数据类型”为“ROUTE_DATA”的DRU，然后重新执行本命令。                                                                                  |
| 260103 | 该cluster已存在。                                | 输入的“Cluster标识”在系统中已配置。                    | 通过LST CLUSTER命令查询配置的cluster，按照“Cluster标识”的分配原则选择一个没有被使用的ID重新进行配置。                                                            |