# 算法图解

## 目录
### 01 算法简介
#### 算法：
- [二分查找](https://github.com/chenyang929/grokking_algorithms/blob/master/01%20%E7%AE%97%E6%B3%95%E7%AE%80%E4%BB%8B/01_binary_search.py)
#### 总结：
+ 二分查找的速度比简单查找快得多,其运行时间是O(log n)
+ O(log n)比O(n)快，需要搜索的元素越多，前者比后者就快的越多
+ 算法运行时间并不是以秒为单位
+ 算法运行时间是从其增速的角度衡量的
### 02 选择排序
#### 算法：
- [选择排序](https://github.com/chenyang929/grokking_algorithms/blob/master/02%20%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F/02_selection_sort.py)
#### 总结：
+ 数组的元素都在一起
+ 链表的元素是分开的，其中每个元素都存储了下一个元素的地址
+ 数组的读取速度很快
+ 链表的插入和删除速度很快
+ 在同一数组中，所有元素的类型都必须相同（都为int、double等）
+ 排序算法是一种较慢的算法，其运行时间是O(n<sup>2</sup>)
### 03 递归
#### 总结：
+ 递归指的是调用自己的函数
+ 每个递归函数都有两个条件：基线条件（停止递归）和递归条件
+ 栈有两种操作：压入和弹出
+ 所有函数调用都进入调用栈
+ 调用栈可能很长，这将占用大量内存
### 04 快速排序
#### 算法：
- [快速排序](https://github.com/chenyang929/grokking_algorithms/blob/master/04%20%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F/04_quick_sort.py)
- [合并（归并）排序](https://github.com/chenyang929/grokking_algorithms/blob/master/04%20%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F/04_merge_sort.py)
#### 总结
+ D&C(分而治之)将问题逐步分解。使用D&C处理列表时，基线条件很可能是空数组或只包含一个元素的数组
+ 实现快速排序时，请随机选择作为基准值的元素。快速排序的平均运行时间为O(nlogn)
### 05 散列表（hash table）
#### 总结：
+ 可以结合散列函数和数组来创建散列表
+ 散列表的查找、插入和删除速度都非常快，O(1)
+ 散列表应用场景：web服务器缓存数据，防止重复
+ python中散列表实现的形式是字典
### 06 广度优先搜索
#### 算法：
- [广度优先搜索](https://github.com/chenyang929/grokking_algorithms/blob/master/06%20%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E7%AE%97%E6%B3%95/06_breadth-first_search.py)
#### 总结：
+ 广度优先搜索支出是否有从A到B的路径，如果有，给出最短路径
+ 有向图中的边带箭头，箭头方向指定了关系的方向
+ 无向图中的边没有箭头，关系是双向的
+ 队列是先进先出（FIFO）的
+ 栈是先进后出（LIFO）的
### 07 狄克斯特拉算法
### 算法：
- [狄克斯特拉算法](https://github.com/chenyang929/grokking_algorithms/blob/master/07%20%E7%8B%84%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95/07_dijkstras_algorithm.py)
#### 总结：
+ 广度优先搜索用于在非加权图中查找最短路径
+ 狄克斯特拉算法用于在加权图中查找最短路径
+ 仅当权重为正时狄克斯特拉算法才管用，权重为负可使用贝尔曼-福德算法







