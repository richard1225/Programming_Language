# 叶志杰 
# 2015300091
## 在状态{n->3}下的操作语义
`count = n`, {n->3} => {n->3, count->3}

`sum = 0`, {n->3, count->3} => {n->3, count->3, sum->0}

在状态{n->3, count->3, sum->0}下, count > 0 成立， 执行`sum=sum+count; count=count-1`, 得{n->3, count->2, sum->3}

在状态{n->3, count->2, sum->3}下, count > 0 成立， 执行`sum=sum+count; count=count-1`, 得{n->3, count->1, sum->5}

在状态{n->3, count->1, sum->5}下, count > 0 成立， 执行`sum=sum+count; count=count-1`, 得{n->3, count->0, sum->6}

在状态{n->3, count->0, sum->6}下, count > 0 不成立， 那么`WHILE END`, {n->3, count->3, sum->0} => {n->3, count->0, sum->6}

## 在状态{n->3}下的指称语义
M(count=n;sum=0)({n->3})

 = M(sum=0)(M(count=n)({n->3}))

 = M(sun=0)({n->3, count->3})
 
 = {n->3, count->3, sum=0}

令P=`WHILE count > 0 DO sum=sum+count;count=count-1`

M(P)({n->3, count->3, sum=0})

 = M(P)({n->3, sum->3, count->2})

 = M(P)({n->3, sum->5, count->1})

 = M(P)({n->3, sum->6, count->0})

 = {n->3, sum->6, count->0}




## 在状态{n->-1}的操作语义

`count = n`, {n->-1} => {n->-1, count->-1}

`sum = 0`, {n->-1, count->-1} => {{n->-1, count->-1, sum->0}

在状态{{{n->-1, count->-1, sum->0}下, count > 0 不成立， 那么`WHILE END`, {n->-1, count->-1, sum->0} => {n->-1, count->-1, sum->0}

## 在状态{n->-1}下的指称语义

令P=`WHILE count > 0 DO sum=sum+count;count=count-1`

 M(P)({n->3, count->3, sum=0})

 = {n->3, count->3, sum=0}
