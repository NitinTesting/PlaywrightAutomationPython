Feature: Order Transaction
  Test related to end to end transaction

  Scenario Outline: Verify View Page
    Given user on login page
    When user successfully login with <username> and <password>
    And user select a product <product_name> to view
    Then view page is showing correct product <product_name>
    Examples:
     | username | password | product_name |
     | Nqatest@gmail.com | testQA@1111 | ZARA COAT 3 |

  @smoke
  Scenario Outline: Verify End to End transaction
    Given user on login page
    When user successfully login with <username> and <password>
    And user select a product <product_name> to add to cart
    Then user should see product <product_name> in the cart
    When from MyCart page proceed to checkout
    And place order
    Then verify product in the <product_name> Thanks page
#    When navigate to Orders page
#    Then verify product <product_name> in the order page
    Examples:
      | username | password | product_name |
      | Nqatest@gmail.com | testQA@1111 | ZARA COAT 3 |


