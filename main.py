def bubble_sort(ro'yhat):
    n = len(ro'yhat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ro'yhat[j] > ro'yhat[j + 1]:
                ro'yhat[j], ro'yhat[j + 1] = ro'yhat[j + 1], ro'yhat[j]
    return ro'yhat

ro'yhat = [64, 34, 25, 12, 22, 11, 90]
print("Asl ro'yxat:", ro'yhat)
print("Tartiblangan ro'yxat:", bubble_sort(ro'yhat))
```

```python
def bubble_sort(ro'yhat):
    n = len(ro'yhat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ro'yhat[j] > ro'yhat[j + 1]:
                ro'yhat[j], ro'yhat[j + 1] = ro'yhat[j + 1], ro'yhat[j]
    return ro'yhat

ro'yhat = [64, 34, 25, 12, 22, 11, 90]
print("Asl ro'yxat:", ro'yhat)
print("Tartiblangan ro'yxat:", bubble_sort(ro'yhat))
