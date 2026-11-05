# 查询外部S-CSCF设备链路的配置信息(LST HSCSCFL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HSS与S-CSCF设备之间的Diameter链路的配置信息：

- 若需要查询全部S-CSCF数据记录的信息，请不要输入任何参数。
- 若需要查询某条HSS与S-CSCF设备之间的Diameter链路数据记录的详细信息，请输入“链路标识”或其他参数或这些参数的组合。

## 注意事项

当HSS的“工作模式”被指定为“SERVER(服务器)”时，返回结果中参数“分发端口号”表示内部分发端口号，HSS整体对外端口号为3868，在进行对端配置的时候需配置HSS的对外端口号为3868。

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                              |
|:--------|:-----------|:----------------------------------------------------------------------------------|
| HSSN    | HSS名称      | 用于指示系统需要按照哪个“HSS名称”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的HSS实体名称。           |
| CSCFN   | S-CSCF名称   | 用于指示系统需要按照哪个“S-CSCF名称”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“S-CSCF名称”。     |
| LNKN    | 链路名称       | 用于指示系统需要按照哪个“链路名称”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“链路名称”。             |
| PTYPE   | 传输协议类型     | 用于指示系统需要按照哪个“传输协议类型”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“传输协议类型”。         |
| WMODE   | 工作模式       | 用于指示系统需要按照哪个“工作模式”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“工作模式”。             |
| HSFMID  | HSF模块号     | 用于指示系统需要按照哪个“HSF模块号”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“HSF模块号”。         |
| ADDRN   | HSS地址名称    | 用于指示系统需要按照哪个“HSS地址名称”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“HSS地址名称”。       |
| SADDRN  | HSS备用地址名称  | 用于指示系统需要按照哪个“HSS备用地址名称”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“HSS备用地址名称”。   |
| LPT     | 分发端口号      | 用于指示系统需要按照哪个“分发端口号”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“分发端口号”。           |
| PIPVER  | 对端IP地址版本   | 用于指示系统需要按照哪个“对端IP地址版本”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端IP地址版本”。     |
| PIPV4   | 对端IPV4地址   | 用于指示系统需要按照哪个“对端IPV4地址”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端IPV4地址”。     |
| PIPV6   | 对端IPV6地址   | 用于指示系统需要按照哪个“对端IPV6地址”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端IPV6地址”。     |
| SPIPVER | 对端备用IP地址版本 | 用于指示系统需要按照哪个“对端备用IP地址版本”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端备用IP地址版本”。 |
| SPIPV4  | 对端备用IPV4地址 | 用于指示系统需要按照哪个“对端备用IPV4地址”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端备用IPV4地址”。 |
| SPIPV6  | 对端备用IPV6地址 | 用于指示系统需要按照哪个“对端备用IPV6地址”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端备用IPV6地址”。 |
| PPT     | 对端端口号      | 用于指示系统需要按照哪个“对端端口号”来查询HSS与S-CSCF设备之间的Diameter链路数据记录；若不输入，则表示所有的“对端端口号”。           |

## 使用实例

1. 查询所有链路的配置信息：

   ```
   LST HSCSCFL:;
   ```

   ```
   %%LST HSCSCFL:;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    HSS名称  S-CSCF名称        链路名称          传输协议类型  工作模式  HSF模块号  HSS地址名称  HSS备用地址名称  分发端口号  对端IP地址版本  对端IPV4地址  对端IPV6地址  对端备用IP地址版本  对端备用IPV4地址  对端备用IPV6地址  对端端口号  HSS索引  S-CSCF索引  链路索引

   IMSHSS   SCSCF10           SCSCF10           SCTP协议类型  服务器    3          DIAM         NULL             3883        IPV4            10.100.2.47  NULL          IPV4                NULL              NULL              3858        0        14          15      
    IMSHSS   SCSCF11           SCSCF11           SCTP协议类型  服务器    3          DIAM         NULL             3882        IPV4            10.100.2.47  NULL          IPV4                NULL              NULL              3859        0        13          14      
    IMSHSS   SCSCF12           SCSCF12           SCTP协议类型  服务器    3          DIAM         NULL             3881        IPV4            10.100.2.47  NULL          IPV4                NULL              NULL              3860        0        12          13      
    IMSHSS   SCSCF9            SCSCF9            SCTP协议类型  服务器    3          DIAM         NULL             3884        IPV4            10.100.2.47  NULL          IPV4                NULL              NULL              3857        0        15          16      
    IMSHSS   SCSCF             IMSHSS-SCSCF      SCTP协议类型  服务器    3          DIAM         NULL             3894        IPV4            10.100.2.53  NULL          IPV4                NULL              NULL              6002        0        27          26      
   (结果个数 = 5)

   ---    END
   ```
2. 查询某条链路的配置信息，“链路名称”为“SCSCF10”：

   ```
   LST HSCSCFL: LNKN="SCSCF10";
   ```

   ```
   %%LST HSCSCFL: LNKN="SCSCF10";%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
              HSS名称  =  IMSHSS
           S-CSCF名称  =  SCSCF10
             链路名称  =  SCSCF10
         传输协议类型  =  SCTP协议类型
             工作模式  =  服务器
            HSF模块号  =  3
          HSS地址名称  =  DIAM
      HSS备用地址名称  =  NULL
           分发端口号  =  3883
       对端IP地址版本  =  IPV4
         对端IPV4地址  =  10.100.2.47
         对端IPV6地址  =  NULL
   对端备用IP地址版本  =  IPV4
     对端备用IPV4地址  =  NULL
     对端备用IPV6地址  =  NULL
           对端端口号  =  3858
              HSS索引  =  0
           S-CSCF索引  =  14
             链路索引  =  15
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

以下列出的是未包含在本命令参数说明中的输出项，其他输出项的详细说明请参见本命令的参数说明。

| 输出项名称    | 输出项解释                                          |
|:---------|:-----------------------------------------------|
| SLF索引    | 用于在配置数据库中定义一条SLF设备数据记录索引，该索引仅供内部使用，无实际含义。      |
| S-CSCF索引 | 用于在配置数据库中定义一条S-CSCF设备数据记录索引，该索引仅供内部使用，无实际含义。   |
| 链路索引     | 用于在配置数据库中定义一条S-CSCF设备链路数据记录索引，该索引仅供内部使用，无实际含义。 |