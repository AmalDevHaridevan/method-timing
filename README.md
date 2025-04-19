# method-timing
A class that wraps arbitrary python classes to provide timing functionality. Allows to record the execution time of every function calls individually with no hassle. 
Can recursively time every indivudial methods.
# Example
```python
class A:
  def fnc1(...):...

  def fnc2(...):
    fnc1(...)

  def fnc3(...):...
    fnc2(...)
```
Using ```MethodTimer``` to call ```fnc3(...)``` will implicitly time the calls to ```fnc2``` and ```fnc1```.
# Visualization
```python
raw_obj = A(...)
wrapped_obj = MethodTimer(raw_obj)
for i in range(1000):
  wrapped_obj.fnc3(...)
timing_data = wrapped_obj.data_
wrapped_obj.plot(('fnc3','fnc2','fnc1'))
wrapped_obj.plot_histograms(('fnc_3','fnc2','fnc1'))
```
## Alternatively
```python
# MethodTimer will construct class A using args and kwargs, the 2nd arg specifies what methods to time track
# by default, we track all (if empty)
wrapped_obj = MethodTimer(A, (), *args, **kwargs)
for i in range(1000):
  wrapped_obj.fnc3(...)
timing_data = wrapped_obj.data_
wrapped_obj.plot(('fnc3','fnc2','fnc1'))
wrapped_obj.plot_histograms(('fnc_3','fnc2','fnc1'))
```
