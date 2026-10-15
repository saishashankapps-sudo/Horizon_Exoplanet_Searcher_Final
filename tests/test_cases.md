# Horizon Test Cases

| ID | Test | Input | Expected Result |
|---|---|---|---|
| TC01 | Open application | `/` | Homepage loads |
| TC02 | Database records | Open homepage | Up to 100 records appear |
| TC03 | Search | `Kepler` | Matching planets appear |
| TC04 | Empty search | `XYZ123` | No matching records |
| TC05 | Discovery method | `Transit` | Only Transit records appear |
| TC06 | Year range | `2010` to `2020` | Results fall in the range |
| TC07 | Sorting | `Distance` | Results sorted by distance |
| TC08 | Add | Valid record | Record is inserted |
| TC09 | Duplicate add | Existing planet name | Insert is rejected |
| TC10 | Update | Valid planet ID | Record is updated |
| TC11 | Invalid update | Invalid ID | Error handled |
| TC12 | Delete | Valid planet ID | Record is deleted |
| TC13 | Invalid delete | Invalid ID | Error handled |
| TC14 | Statistics | Homepage | Summary values display |
| TC15 | Blank required field | Empty planet name | Validation message |
| TC16 | Invalid numeric value | Letters in numeric field | Validation message |
| TC17 | Logging | Search/add/update/delete | Events recorded in `logs/app.log` |
