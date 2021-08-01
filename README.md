# sms_parts
This is just a py file that have a sample text and the fucntion that needs to be changed.

```
sendSmsMessage(text, to, from_)
```
is the function that needs to be updated.
Assuming the max len of suffix text to be 16 char. length of "\n- Part 99 of 99" is 16 chars.
The remaining char will be 144 (160 - 16).

This function will send messages till all parts ends.
