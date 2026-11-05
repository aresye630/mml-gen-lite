# 查询临时表信息（LST TMPTBL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查看数据库的临时表信息。

- 如果要查询所有网元的临时表信息，请不要输入任何的参数。
- 如果要查询某个网元的临时表信息，请输入该网元的网元ID。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                         |
|:-------|:-------|:---------------------------------------------------------------------------------------------|
| MEID   | 网元ID   | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个网元ID来查询该网元所有的临时表；如果不输入，则表示查询所有网元的临时表。 取值范围：0～1023 默认值:无。 配置原则：无。 |

## 使用实例

1. 查询数据库的所有临时表信息。

   `LST TMPTBL:;`

   ```
   %%LST TMPTBL:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    网元ID  网元名称  临时表名称                   

    0       CGP_1    RST_FM_ADDSUBSCRIPTION      
    0       CGP_1    RST_FM_ALARMCLEAR           
    0       CGP_1    TBL_TMP_DSPLICENSE_FLAG    
    0       CGP_1    TBL_TMP_DSPPATCH_FIRSTRPT  
    0       CGP_1    TBL_TMP_DSPPATCH_STATS     
    0       CGP_1    TBL_TMP_PATCH_OPER_LODPATCH
    0       CGP_1    TMP_FM_EVENT_LOG           
    0       CGP_1    TMP_TBL_ALAMR_ACTIVE       
    0       CGP_1    TMP_TBL_ALAMR_LOG          
    0       CGP_1    TMP_TBL_ALAMR_MSK_LOG      
    0       CGP_1    TMP_TBL_NBIALAMR_ACTIVE    
    0       CGP_1    TMP_TBL_NBIALAMR_LOG       
    5       NE5_1    TMP_TBL_GETCDBMIDBYSRV_BC     
    5       NE5_1    TMP_TBL_GETMODNOBYMGW_BC      
    5       NE5_1    TMP_TBL_SIPDISTTBLNM_0        
   (结果个数 = 15)

   ---    END
   ```
2. 查询指定网元下的临时表信息：

   `LST TMPTBL: MEID=5;`

   ```
   %%LST TMPTBL: MEID=5;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    网元ID  网元名称  临时表名称                    

    5       NE5_1     TMP_TBL_GETCDBMIDBYSRV_BC     
    5       NE5_1     TMP_TBL_GETMODNOBYMGW_BC      
    5       NE5_1     TMP_TBL_SIPDISTTBLNM_0        
   (结果个数 = 3)

   ---    END
   ```

## 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 网元ID    | 用于标识网元的ID。  |
| 网元名称    | 用于标识网元的名称。  |
| 临时表名称   | 用于标识临时表的名称。 |