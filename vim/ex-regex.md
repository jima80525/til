# Using regex matches in EX mode

If you want to use the s/// command in ex mode but you need to use a capture, you need to escape the capture characters `()`.

To replace `{1, ...` with `{ 1, ...`, you would use the following ex command:

```
:% s/{\([^ ]\)/{ \1/g
```
