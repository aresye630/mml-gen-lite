# 输出数据库系统信息(EXP DBINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于输出数据库的系统信息，包括数据库的链接信息和数据库的当前的锁的状态信息。

本命令的使用场景：当需要使用“信息收集工具”收集数据库系统信息时，工具会使用此命令输出数据库系统信息。

## 注意事项

“显示所有记录”为“YES(显示所有记录)”时，若返回记录过多，可能出现命令执行超时或输出报文显示不完整。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                   |
|:------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------|
| TABLETYPE   | 系统表名称  | 可选必选说明：必选参数。 参数含义：该参数用于指定输出哪张表的数据信息。 取值范围： “PG_STAT_ACTIVITY(链接信息表)”“PG_LOCKS(锁信息表)” 默认值：无。 配置原则：无。                                    |
| RECORDSTART | 开始记录号  | 可选必选说明：必选参数。 参数含义：该参数用于指定返回的记录数开始的位置。 取值范围：1～65535 默认值：无。 配置原则：无。                                                                      |
| RECORDNUM   | 返回记录数  | 可选必选说明：必选参数。 参数含义：该参数用于指定返回的记录个数。 取值范围：1～200 默认值：120。 配置原则：无。                                                                          |
| DISPLAYALL  | 显示所有记录 | 可选必选说明：必选参数。 参数含义：该参数用于指定是否显示所有记录。若该参数为“YES(显示所有记录)”，则“开始记录号”和“返回记录数”的值忽略。 取值范围： “NO(不显示所有记录)”“YES(显示所有记录)” 默认值：“NO(不显示所有记录)”。 配置原则：无。 |

## 使用实例

1. 输出数据库链接信息，“系统表名称”为“PG\_STAT\_ACTIVITY(链接信息表)”,“开始记录号”为“1”，“返回记录数”为“5”。

   `EXP DBINFO: TABLETYPE=PG_STAT_ACTIVITY, RECORDSTART=1, RECORDNUM=5;`

   ```
   %%EXP DBINFO: TABLETYPE=PG_STAT_ACTIVITY, RECORDSTART=1, RECORDNUM=5;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    数据库ID  进程ID  用户名  等待状态  客户端ID  客户端名

    16384     580     cgp     false     325       MOD_18  
    16384     15559   cgp     false     15004     MOD_15  
    16384     15574   cgp     false     15004     MOD_15  
    16384     15583   cgp     false     15004     MOD_15  
    16384     15596   cgp     false     15004     MOD_15  
   (结果个数 = 5)

   ---    END
   ```
2. 输出数据库的锁的状态信息，“系统表名称”为“PG\_LOCKS(锁信息表)”,“开始记录号”为“1”，“返回记录数”为“5”。

   `EXP DBINFO: TABLETYPE=PG_LOCKS, RECORDSTART=1, RECORDNUM=5;`

   ```
   %%EXP DBINFO: TABLETYPE=PG_LOCKS, RECORDSTART=1, RECORDNUM=5;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    锁的类型  数据库ID  关系ID  页面编号  行编号  虚拟事务ID  事务ID  系统表的ID  对象的ID  子对象的ID  等待或者持有该锁的事务ID  等待或者持有该锁的进程ID  锁的模式         是否持有锁

    relation  16384     2965    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  0         1213    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     2684    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     2658    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1247    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
   (结果个数 = 5)

   ---    END
   ```
3. 输出数据库的锁的所有状态信息，“系统表名称”为“PG\_LOCKS(锁信息表)”,“显示所有记录”为“YES(显示所有记录)”。

   `EXP DBINFO: TABLETYPE=PG_LOCKS, DISPLAYALL=YES;`

   ```
   %%EXP DBINFO: TABLETYPE=PG_LOCKS, DISPLAYALL=YES;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    锁的类型  数据库ID  关系ID  页面编号  行编号  虚拟事务ID  事务ID  系统表的ID  对象的ID  子对象的ID  等待或者持有该锁的事务ID  等待或者持有该锁的进程ID  锁的模式         是否持有锁

    relation  16384     2965    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  0         1213    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     2684    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     2658    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1247    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1533    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1537    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1284    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1290    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1656    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1623    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1225    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1435    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1678    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
    relation  16384     1589    0         0       NULL        NULL    0           0         0           89/206                    27011                     AccessShareLock  true      
   (结果个数 = 15)

   ---    END
   ```

## 输出结果说明

| 输出项名称         | 输出项解释              |
|:--------------|:-------------------|
| 数据库ID         | 用于唯一标识一个数据库的进程。    |
| 进程ID          | 用于唯一标识一个数据库链接的进程。  |
| 用户名           | 用于标识申请数据库链接的用户名。   |
| 等待状态          | 用于标识数据库链接是否处于等待状态。 |
| 客户端ID         | 用于标识申请数据库链接的进程。    |
| 客户端名          | 用于标识申请数据库链接的进程的名字。 |
| 锁的类型          | 用于标识数据库的锁的类型。      |
| 关系ID          | 用于标示和该锁有关系的表的ID。   |
| 页面编号          | 用于标识和该锁相关的表的页面编号。  |
| 行编号           | 用于标识和该锁相关的表的行编号。   |
| 虚拟事务ID        | 用于标识一个虚拟事务。        |
| 事务ID          | 用于标识一个事务。          |
| 系统表的ID        | 用于标识一个和该锁相关的系统表。   |
| 对象的ID         | 用于标识一个对象的ID。       |
| 子对象的ID        | 用于标识一个子对象的ID。      |
| 等待或者持有该锁的事务ID | 用于标识等待或者持有该锁的事务。   |
| 等待或者持有该锁的进程ID | 用于标识等待或者持有该锁的进程。   |
| 锁的模式          | 用于标识锁的模式。          |
| 是否持有锁         | 用于相关的事务或者进程是否持有该锁。 |