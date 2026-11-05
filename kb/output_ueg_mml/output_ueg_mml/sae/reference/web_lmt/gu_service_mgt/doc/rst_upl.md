# 发送模拟Reset Update Location消息（RST UPL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用来发送模拟重置位置更新消息给用户原归属HLR。

NPMSC模拟VLR向用户原归属HLR发起位置更新请求消息，原归属HLR出现异常时，网络维护人员可执行该命令发送模拟Reset Update Location消息。NPMSC能根据请求消息中的HLR Number，找到该HLR的所有携出用户，重新发起位置更新，原归属HLR记录NPMSC的MSCID，NPMSC记录原归属HLR的HLR Number。

## 注意事项

该操作对性能的影响较大，测试的时候不能在大话务量下测试该功能。

## 参数说明

无。

## 使用实例

RST UPL:;