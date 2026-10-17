# Inventory Manager Testing

| #   | Feature                                           | Input or Action                    | Expected Result        | Actual Result | Pass/Fail |
| --- | ------------------------------------------------- | ---------------------------------- | ---------------------- | ------------- | --------- |
| 1   | Missing inventory                                 | No inventory file                  | Program doesnt start   | Didnt start   | [Pass]    |
| 2   | Inventory                                         | Nothing in invetory file           | Says theres nothing    | Expected      | [Pass]    |
| 3   | Adding a valid item                               | Give item information              | Adds item              | Expected      | [Pass]    |
| 4   | Rejecting an empty item name                      | input empty item name              | Doesnt add item        | Expected      | [Pass]    |
| 5   | Rejecting a duplicate item name                   | Duplicate name                     | Doesnt add item        | Expected      | [Pass]    |
| 6   | Rejecting a nonnumeric quantity                   | Input nonnumeric number            | Doesnt add item        | Expected      | [Pass]    |
| 7   | Rejecting a negative quantity                     | INput negative number              | Doesnt add item        | Expected      | [Pass]    |
| 8   | Updating a valid item                             | new quanityt of item               | Doesnt add item        | Expected      | [Pass]    |
| 9   | Rejecting an invalid item number                  | Give a number that isnt in it      | Doesnt work            | Expected      | [Pass]    |
| 10  | Removing an item                                  | number for itme you want to remove | Removes item           | Expected      | [Pass]    |
| 11  | Performing a case-insensitive partial search      | Input case sensitve search         | pops up with all items | Expected      | [Pass]    |
| 12  | Searching when no matches exist                   | Nothing                            | Shows no items         | Expected      | [Pass]    |
| 13  | Verifying the inventory summary                   | Nothing                            | Shows all we want      | Expected      | [Pass]    |
| 14  | Restarting the program and confirming persistence | exit program and restart           | Persists items         | Expected      | [Pass]    |
