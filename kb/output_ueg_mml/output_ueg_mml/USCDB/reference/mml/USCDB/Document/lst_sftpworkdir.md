# 查询SFTP工作目录(LST SFTPWORKDIR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于SFTP客户端从系统中查询SFTP本地工作目录的联想参数列表。

该命令的使用场景为：在SFTP客户端输入命令参数时，支持参数联想的输入参数可以通过单击下拉框显示出“配置名称”参数已经配置过的数据。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                           |
|:------------|:-------|:---------------------------------------------------------------------------------------------------------------|
| SERVICETYPE | 业务类型   | 用于指示系统按照哪个业务类型查询SFTP工作目录列表。 取值范围：长度不超过128的字符串。 默认值：无。                                                          |
| NAME        | 配置名称   | 用于指示系统按照哪个配置名称查询SFTP工作目录列表。 取值范围：长度不超过31的字符串。 默认值：无。                                                           |
| PATH        | 配置路径   | 用于指示系统按照哪个配置路径查询SFTP工作目录列表。 取值范围：长度不超过127的字符串。 默认值：无。                                                          |
| USERTYPE    | 用户类型   | 用于指示系统按照哪个用户类型查询SFTP工作目录列表。 取值范围： PROV(业务)：表示查询客户端为营帐功能的SFTP工作目录列表。DATAMTN(维护)：表示查询客户端为导出功能的SFTP工作目录列表。 默认值：无。 |

## 使用实例

查询SFTP工作目录信息：

```
LST SFTPWORKDIR:;
```

```
%%LST SFTPWORKDIR:;%%
RETCODE = 0 操作成功

操作结果如下
------------------------
业务类型      配置名称             配置路径                             用户类型
GU-HLR        UPALACCIMA           redundance/download/upalaccima       Prov 
GU-HLR        UPALACCIMA1          redundance/download/upalaccima1      Prov 
GU-HLR        UPALACCIMA2          redundance/download/upalaccima2      Prov 
USCDB         UPLOADEXPORTFILE     upload                               DataMtn
SUP-FE        0                    clientdownload/_                     Prov 
SUP-FE        0123456789ABCDEF     clientdownload/123456789abcdefg      Prov 
USCDB         BACKUPNODE           backupnode                           DataMtn 
USCDB         CLIENTDOWNLOAD       clientdownload                       Prov 
SUP-FE        FILENOTIFY_SUP_FE    redundance/download/SUP-FE           Prov 
SUP-FE        NOPQRSTUVWXYZ_       clientdownload/TRUEPATH              Prov 
USCDB         NOTIFYFAILLIST       redundance/download/USCDB            Prov 
USCDB         REDUNDANCE           redundance/syn                       Prov 
SUP-FE        SUP_EXP              sup_exp                              DataMtn 
SUP-FE        SUP_PROV             sup_prov                             Prov 
USCDB         TIMDOWNLOAD          clientdownload/timingftp             Prov 
USCDB         UPLOADEXPORTFILE     upload                               DataMtn 
USCDB         UPLOADEXPLOGFILE     upload                               DataMtn 
(结果个数 = 17) 

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1的参数说明。

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 业务类型    | 用于返回SFTP客户端对应的业务类型。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 配置名称    | 用于返回SFTP本地工作目录： REDUNDANCE：用于下载容灾文件的本地目录。 容灾局SFTP客户端从主用局SFTP服务器的realtime目录下载容灾文件到本地的“/opt/dpu/redundance/syn”目录。容灾局的主PGW从“/opt/dpu/redundance/syn”目录下载容灾文件到“/opt/pgw/redundance/syn”目录。 CLIENTDOWNLOAD：用于从远端目录下载文件存放的本地目录。 从指定的远端目录按过滤条件下载文件到本端的“/opt/dpu/clientdownload”目录。主PGW模块同步该目录下的文件到“/opt/pgw/clientdownload/”目录。 TIMDOWNLOAD：用于定时下载文件的本地目录。 每天在配置指定的时间范围内启动并从指定的远端目录按过滤条件下载文件到本端的“/opt/dpu/clientdownload/timingftp”目录。主PGW模块同步该目录下的文件到“/opt/pgw/clientdownload/timingftp”目录。 UPLOADEXPORTFILE：用于上传导出文件的本地目录。 DMA模块完成导出后，将本地导出的文件上传到网关类型为DMA的DPU模块所在Pod的“/opt/dpu/export/upload/taskid”目录。PGW通知DPU上传导出结果文件，DPU将该目录下的文件上传到对端SFTP服务器。 UPLOADEXPLOGFILE：用于上传导出日志文件的本地目录。DMA模块完成导出后，将本地导出日志文件上传到网关类型为DMA的DPU模块所在Pod的“/opt/dpu/export/uploadexplog/taskid”目录。PGW通知DPU上传导出结果文件，DPU将该目录下的文件上传到对端SFTP服务器。 NOTIFYFAILLIST：用于上传订阅通知的失败列表文件。 PGW将生成在“/opt/pgw/redundance/pgw/download/USCDB”和“/opt/pgw/redundance/tmp/download/USCDB”目录下的文件上传到DPU的目录“/opt/dpu/redundance/download/USCDB”。由DPU上传到对端的SFTP服务器。 FILENOTIFY_插件包名称：用于上传订阅通知成功的列表文件。 PGW将生成在“/opt/pgw/redundance/pgw/download/FETYPE”和“/opt/pgw/redundance/tmp/download/FETYPE”目录下的文件上传到DPU的目录“/opt/dpu/redundance/download/FETYPE”。由DPU上传到对端的SFTP服务器。 BACKUPNODE：用于上传备份文件的本地目录。 DRU/DSU节点备份完成后，DMA会将与其对应的DRU/DSU模块的备份的上传到网关类型为DMA的DPU的“/opt/dpu/export/backupnode”目录。上传完成后，由DPU上传到对端SFTP服务器。 FE插件包中配置的指定目录：例如，UPALACCIMA。 指定的远端目录按过滤条件下载文件到本端的“/opt/dpu/clientdownload/upalaccima”目录。主PGW模块同步该目录下的文件到“/opt/pgw/clientdownload/upalaccima”目录。文件同步后，需由lib扫描该目录并对文件内容做规整，规整后由lib决定后继的操作。 |
| 配置路径    | 用于返回配置的SFTP工作目录。 当“用户类型”为“Prov”时，其根目录为“/opt/dpu/”。当“用户类型”为“DataMtn”时，其根目录为“/opt/dpu/export/”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 用户类型    | 用于返回SFTP用户的服务类型。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |