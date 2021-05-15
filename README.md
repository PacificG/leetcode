# leetcode

run scripts using command
> python -m doctest file.py -v


## things to consider

* this does not work
  ```python
  >>> A = [2,3,1,0,2,5]
  >>> A[0], A[A[0]] = A[A[0]], A[0]  #error
  >>> A
  [1, 2, 1, 0, 2, 5]
  >>> A[0], A[1] = A[1], A[0] #This works
  ```
