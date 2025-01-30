Feature: URL Shortener
  Scenario: Shorten a URL
    Given the user is on the URL shortener page
    When the user enters a URL "https://example.com"
    And clicks the "Make it short" button
    Then a shortened URL should be displayed

  Scenario: Shorten a URL Invalid
    Given the user is on the URL shortener page
    When the user enters a URL "invalidurlcom"
    And clicks the "Make it short" button
    Then error message "invalid url" should be displayed 

  Scenario: Retrieve original URL
    Given the user is on the URL shortener page
    When the user enters a shortened URL "c984d0"
    And clicks the "Get original" button
    Then the original URL should be displayed

  Scenario: Retrieve original invalid URL
    Given the user is on the URL shortener page
    When the user enters a shortened URL "zzzz"
    And clicks the "Get original" button
    Then error message "invalid short url" should be displayed