# 修改承载业务(MOD BS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改用户的承载业务数据。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果要提供BS20业务，PROV＝TRUE；如果要撤销BS20业务，PROV＝FALSE。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                       |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。 ISDNFILE包含多个不连续的MSISDN号码。                                    |
| BS20        | 是否提供BS20  | 提供还是撤销BS20业务。 TRUE：提供 FALSE：撤销                                                      |
| BS21        | 是否提供BS21  | 提供还是撤销BS21业务。 TRUE：提供 FALSE：撤销                                                      |
| BS22        | 是否提供BS22  | 提供还是撤销BS22业务。 TRUE：提供 FALSE：撤销                                                      |
| BS23        | 是否提供BS23  | 提供还是撤销BS23业务。 TRUE：提供 FALSE：撤销                                                      |
| BS24        | 是否提供BS24  | 提供还是撤销BS24业务。 TRUE：提供 FALSE：撤销                                                      |
| BS25        | 是否提供BS25  | 提供还是撤销BS25业务。 TRUE：提供 FALSE：撤销                                                      |
| BS26        | 是否提供BS26  | 提供还是撤销BS26业务。 TRUE：提供 FALSE：撤销                                                      |
| BS30        | 是否提供BS30  | 提供还是撤销BS30业务。 TRUE：提供 FALSE：撤销                                                      |
| BS31        | 是否提供BS31  | 提供还是撤销BS31业务。 TRUE：提供 FALSE：撤销                                                      |
| BS32        | 是否提供BS32  | 提供还是撤销BS32业务。 TRUE：提供 FALSE：撤销                                                      |
| BS33        | 是否提供BS33  | 提供还是撤销BS33业务。 TRUE：提供 FALSE：撤销                                                      |
| BS34        | 是否提供BS34  | 提供还是撤销BS34业务。 TRUE：提供 FALSE：撤销                                                      |
| BS41        | 是否提供BS41  | 提供还是撤销BS41业务。 TRUE：提供 FALSE：撤销                                                      |
| BS42        | 是否提供BS42  | 提供还是撤销BS42业务。 TRUE：提供 FALSE：撤销                                                      |
| BS43        | 是否提供BS43  | 提供还是撤销BS43业务。 TRUE：提供 FALSE：撤销                                                      |
| BS44        | 是否提供BS44  | 提供还是撤销BS44业务。 TRUE：提供 FALSE：撤销                                                      |
| BS45        | 是否提供BS45  | 提供还是撤销BS45 TRUE：提供 FALSE：撤销                                                         |
| BS46        | 是否提供BS46  | 提供还是撤销BS46业务。 TRUE：提供 FALSE：撤销                                                      |
| BS51        | 是否提供BS51  | 提供还是撤销BS51业务。 TRUE：提供 FALSE：撤销                                                      |
| BS52        | 是否提供BS52  | 提供还是撤销BS52业务。 TRUE：提供 FALSE：撤销                                                      |
| BS53        | 是否提供BS53  | 提供还是撤销BS53业务。 TRUE：提供 FALSE：撤销                                                      |
| BS61        | 是否提供BS61  | 提供还是撤销BS61业务。 TRUE：提供 FALSE：撤销                                                      |
| BS81        | 是否提供BS81  | 提供还是撤销BS81业务。 TRUE：提供 FALSE：撤销                                                      |

## 使用实例

1. 运营商为IMSI号码是460000009012345的用户签约BS20, BS24, BS33, BS43业务。命令如下：

   MOD BS: IMSI="460000009012345", BS20=TRUE, BS24=TRUE, BS33=TRUE, BS43 = TRUE;
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477的用户签约BS20、BS24、BS33、 BS43业务。

   1. 编写IMSIFILE，文件名称为IMSIBAT，内容如下：

      460000009123455

      460000009123466

      460000009123477
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行MOD BS命令提供BS20、BS24、BS33、BS43业务。

      MOD BS: IMSIFILE="IMSIBAT", BS20=TRUE, BS24=TRUE, BS33=TRUE, BS43 =TRUE;