# 查询数据库表信息（DSP TBL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询数据库的表信息、字段信息、索引信息和记录内容。

## 注意事项

- 查询CSP网元中的表信息时，表ID要加上10000，如查询网元0中的95号表信息，表ID要输入10095。
- 查询业务网元中的表信息，直接输入表ID即可，如查询网元5的10号表信息，表ID要输入10。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                  |
|:--------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| MEID    | 网元ID   | 可选必选说明：必选参数。 参数含义：用于请求系统根据网元ID来显示数据库中的表信息。 取值范围:0～1023 默认值：无。 配置原则：无。                                                                                 |
| MN      | 模块标识   | 可选必选说明：必选参数。 参数含义：用于请求系统显示哪个模块的表信息。 取值范围：0～4294967294 默认值：无。 配置原则：无。                                                                                  |
| STATUS  | 进程主备状态 | 可选必选说明：必选参数。 参数含义：用于请求系统显示主模块或者备模块数据库中的表信息。 取值范围： “Active(主模块)”：查询主模块数据库中的表信息。“Standby(备模块)”：查询备模块数据库中的表信息。 默认值：“Active(主模块)”。 配置原则：无。                |
| TABLEID | 表标识符   | 可选必选说明：必选参数。 参数含义：用于请求系统显示哪个表的信息。 取值范围：0～4294967294 默认值：无。 配置原则：无。                                                                                    |
| SUBCMD  | 对应的子命令 | 可选必选说明：必选参数。 参数含义：用于请求系统显示表信息、字段信息、索引信息或记录内容。 取值范围： “Table(表信息)”：查询表信息。“Field(字段信息)”：查询字段信息。“Index(索引信息)”：查询索引信息。“Tuple(元组内容)”：查询记录内容。 默认值：无。 配置原则：无。 |
| TPLID   | 记录标识符  | 可选必选说明：必选参数。 参数含义：用于指定待查询的记录ID，该参数只有SUBCMD为“Tuple(元组内容)”时才会显示。 取值范围：0～4294967294 默认值：无。 配置原则：无。                                                       |

## 使用实例

1. 查询CSP网元下模块号为500模块的7号表信息。

   `DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Table;`

   ```
   %%DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Table;%%
   RETCODE = 0  操作成功

   命令执行结果如下:
   -----------------
           表名称  =  TBL_PLANETPORT
         索引类型  =  直接索引
         元组长度  =  213
       最大元组数  =  4000
       实际元组数  =  113
           字段数  =  29
       域描述序号  =  NULL
       索引字段数  =  NULL
           表地址  =  NULL
   哈希描述表序号  =  NULL
   哈希索引字段数  =  NULL
   (结果个数 = 1)

   ---    END
   ```
2. 查询CSP网元下模块号为500模块的7号表字段信息。

   `DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Field;`

   ```
   DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Field;%%
   RETCODE = 0  操作成功

   命令执行结果如下:
   -----------------
    字段名称       字段ID  数据类型  偏移量  长度    索引属性

    I_INDEX        0       UINT32    0       4       NULL    
    I_NETPORTIDX   1       UINT32    4       4       NULL    
    SV_NETPORTMAC  2       STRING    8       20      NULL    
    I_IP1ADDRTYPE  3       UINT8     28      1       NULL    
    SV_IP1IPV6     4       STRING    29      40      NULL    
    I_NETPORTIP1   5       UINT32    69      4       NULL    
    I_IP2ADDRTYPE  6       UINT8     73      1       NULL    
    SV_IP2IPV6     7       STRING    74      40      NULL    
    I_NETPORTIP2   8       UINT32    114     4       NULL    
    I_IP3ADDRTYPE  9       UINT8     118     1       NULL    
    SV_IP3IPV6     10      STRING    119     40      NULL    
    I_NETPORTIP3   11      UINT32    159     4       NULL    
    I_BRDINSTID    12      UINT32    163     4       NULL    
    I_OAMSTAT      13      UINT8     167     1       NULL    
    I_OAMMODE      14      UINT8     168     1       NULL    
    I_OAMTHRD      15      UINT8     169     1       NULL    
    I_WORKMODE     16      UINT8     170     1       NULL    
    I_AVAILABLE    17      UINT8     171     1       NULL    
    I_PORTTYPE     18      UINT32    172     4       NULL    
    I_PORTMTU      19      UINT32    176     4       NULL    
    I_PORTCONFIG   20      UINT32    180     4       NULL    
    I_LOGICPORTID  21      UINT32    184     4       NULL    
    I_RESERVE5     22      UINT32    188     4       NULL    
    I_SWAPATTR     23      UINT32    192     4       NULL    
    I_PORTNAME     24      UINT32    196     4       NULL    
    I_RESERVE8     25      UINT32    200     4       NULL    
    I_RESERVE9     26      UINT32    204     4       NULL    
    I_RESERVE10    27      UINT32    208     4       NULL    
    I_STATUS       28      UINT8     212     1       NULL    
   (结果个数 = 29)

   ---    END
   ```
3. 查询CSP网元下模块号为500模块的7号表索引信息。

   `DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Index;`

   ```
   %%DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Index;%%
   RETCODE = 0  操作成功

   命令执行结果如下:
   -----------------
    索引名称     索引类型  唯一性索引  索引号  域号  

    I_INDEX      排序索引  TRUE        0       0     
    I_PORTINDEX  排序索引  FALSE       1       1     
    I_BRDINSTID  排序索引  FALSE       2       3     
   (结果个数 = 3)

   ---    END
   ```
4. 查询CSP网元下模块号为500模块的7号表第0条记录的内容。

   `DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Tuple,TPLID=0;`

   ```
   %%DSP TBL: MEID=0, MN=500, TABLEID=10007, SUBCMD=Tuple,TPLID=0;%%
   RETCODE = 0  操作成功

   命令执行结果如下:
   -----------------
    字段名称       主机返回的数据  数据文件返回的数据: /opt/HUAWEI/cgp/workshop/omu/workspace1/conf_data/db_c2.dat

    I_INDEX        0               0                                                                              
    I_NETPORTIDX   0               0                                                                              
    SV_NETPORTMAC  NULL            NULL                                                                           
    I_IP1ADDRTYPE  0               0                                                                              
    SV_IP1IPV6     NULL            NULL                                                                           
    I_NETPORTIP1   2886762608      2886762608                                                                     
    I_IP2ADDRTYPE  255             255                                                                            
    SV_IP2IPV6     NULL            NULL                                                                           
    I_NETPORTIP2   4294967295      4294967295                                                                     
    I_IP3ADDRTYPE  255             255                                                                            
    SV_IP3IPV6     NULL            NULL                                                                           
    I_NETPORTIP3   4294967295      4294967295                                                                     
    I_BRDINSTID    2151170047      2151170047                                                                     
    I_OAMSTAT      0               0                                                                              
    I_OAMMODE      0               0                                                                              
    I_OAMTHRD      1               1                                                                              
    I_WORKMODE     6               6                                                                              
    I_AVAILABLE    1               1                                                                              
    I_PORTTYPE     0               0                                                                              
    I_PORTMTU      4294967295      4294967295                                                                     
    I_PORTCONFIG   16777215        16777215                                                                       
    I_LOGICPORTID  4294967295      4294967295                                                                     
    I_RESERVE5     4294967295      4294967295                                                                     
    I_SWAPATTR     4294967295      4294967295                                                                     
    I_PORTNAME     160             160                                                                            
    I_RESERVE8     4294967295      4294967295                                                                     
    I_RESERVE9     4294967295      4294967295                                                                     
    I_RESERVE10    4294967295      4294967295                                                                     
    I_STATUS       1               1                                                                              
   (结果个数 = 29)

   ---    END
   ```

## 输出结果说明

| 输出项名称            | 输出项解释              |
|:-----------------|:-------------------|
| 表名称              | 标识查询的表名称。          |
| 索引类型             | 标识表上索引的类型。         |
| 元组长度             | 标识表中一条记录的长度。       |
| 最大元组数            | 表的最大记录数。           |
| 实际元组数            | 表的实际记录数。           |
| 字段数              | 表的字段数。             |
| 域描述序号            | 表的第一个字段在字段描述表中的位置。 |
| 索引字段数            | 表中索引的字段数。          |
| 表地址              | 表在内存中的地址。          |
| 哈希描述表序号          | 哈希索引的表序号。          |
| 哈希索引字段数          | 哈希索引表的字段数。         |
| 字段名称             | 标识字段的名称。           |
| 字段ID             | 标识字段的序号。           |
| 数据类型             | 字段的数据类型。           |
| 偏移量              | 字段在表中的偏移。          |
| 长度               | 字段的长度。             |
| 索引属性             | 描述索引的信息，只对部分网元有效。  |
| 索引名称             | 标识索引的名称。           |
| 唯一性索引            | 标识是否是唯一性索引。        |
| 索引号              | 标识索引的序号。           |
| 域号               | 标识字段的序号。           |
| 主机返回的数据          | 查询得到的主机侧的数据。       |
| 数据文件返回的数据:数据文件路径 | omu侧数据文件的位置。       |