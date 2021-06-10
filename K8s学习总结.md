# 云服务类型

- iaas
- paas
- saas

# Kubernetes特点

- 轻量级：消耗资源小
- 开源
- 弹性伸缩
- 负载君和：IPVS

*高可用集群副本数据最好是 >= 3 奇数个*

# 基础概念

## Pod

管理的最小单位

## 控制器类型

## 网络通讯模式

# 构建一个K8s集群

# 资源清单

# Pob控制器

# 服务发现

# 存储

# 调度器

# 集群安全机制

# HELM（yum）

# K8s运维

## 源码修改

## 高可用构建

# 组件

## APISERVER

所有服务访问统一入口

## CrontrollerManager

维持副本期望数目

## Scheduler

负责介绍任务，选择合适的节点进行分配任务

## ETCD

键值对数据库
存储K8S集群所有重要信息（持久化）

## Kubelet

直接跟容器引擎交互实现容器的生命周期管理

## Kube-proxy

负责写入规则至IPTABLES、IPVS实现服务映射访问

## COREDNS

可以为集群钟的SVC创建一个域名IP的对应关系杰解析

## DASHBOARD

给K8S集群提供一个B/S的结构访问体系

## INGRESS CONTROLLER

官方只能实现四层代理 INGRESS能实现七层代理

## FEDREATION

提供一个可以跨集群中心多K8S统一管理功能

## PROMETHEUS

提供K8S集群的监控能力

## ELK

提供K8S集群日志统一分析介入平台

