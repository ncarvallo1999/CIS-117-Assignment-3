# Assignment 3: Interstate Highway Numbers

Due Sep 7, 5 points. Locked Sep 14.

Asks the user for a highway number (1 to 999).

- 1 to 99: primary highway. Even runs east/west, odd runs north/south.
- 100 to 999: auxiliary highway. The last two digits are the primary it
  serves, and its direction is printed too.
- 0, above 999, or a multiple of 100 (200, 300, ... would serve "I-0"): `Invalid highway number.`

## Sample output

```
Enter a highway number: 80
Interstate 80 runs east/west.

Enter a highway number: 5
Interstate 5 runs north/south.

Enter a highway number: 405
Interstate 405 is an auxiliary highway serving I-5, which runs north/south.

Enter a highway number: 0
Invalid highway number.
```
